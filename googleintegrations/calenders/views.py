import os
import json
from dotenv import load_dotenv
from django.http import HttpResponseRedirect
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build


load_dotenv()

"""As we are using http for testing purposes only,
 and google_auth_oauthlib needs a https connection,
 so we are setting the environment variable to 1
 """
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

CLIENT_CONFIG = {
    "web": {
        "project_id": os.getenv('PROJECT_ID'),
        "client_id": os.getenv('CLIENT_ID'),
        "client_secret": os.getenv('CLIENT_SECRET'),
        "redirect_uris": [os.getenv('REDIRECT_URI')],
        "javascript_origins": [os.getenv('JS_ORIGIN')],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    }
}

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class GoogleCalendarInitView(APIView):
    def get(self, request):
        try:
            flow = Flow.from_client_config(CLIENT_CONFIG, SCOPES, redirect_uri=os.getenv('REDIRECT_URI'))
            authorization_url, state = flow.authorization_url(access_type='offline', include_granted_scopes='true')
            request.session['state'] = state
            return HttpResponseRedirect(authorization_url)
        except Exception as e:
            raise exceptions.ValidationError(str(e))

class GoogleCalendarRedirectView(APIView):
    def process_events(self, credentials):
            service = build('calendar', 'v3', credentials=credentials)
            events_result = service.events().list(calendarId='primary', maxResults=10, singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])
            if not events:
                return Response({'error': 'No upcoming events found.'}, status=404)
            response = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                response.append({'start': start, 'summary': event['summary']})
            return response

    def set_session(self, request, credentials):
        request.session['credentials'] = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes,
        }

    def get(self, request):
        try:
            state = request.session.get('state')
            if not state:
                return Response({'error': 'Invalid state parameter'}, status=400)
            flow = Flow.from_client_config(CLIENT_CONFIG, SCOPES, state=state, redirect_uri=os.getenv('REDIRECT_URI'))
            flow.fetch_token(authorization_response=request.build_absolute_uri())
            credentials = flow.credentials
            self.set_session(request, credentials)
            return Response(self.process_events(credentials))
        except Exception as e:
            raise exceptions.ValidationError(str(e))

class HomeView(APIView):
    def get(self, request):
        return Response({'Google Calendar Integration, click on the link to authorize your google account: http://localhost:8000/rest/v1/calendar/init/'})
