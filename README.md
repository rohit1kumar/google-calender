### Basic Setup
1. Install dependencies: `pip install -r requirements.txt`.
2. Add `CLIENT_ID, CLIENT_SECRET, PROJECT_ID` in `.env` file. You can copy the `.env.example` file and update the values accordingly.
```
    cp .env.example .env
```
3. Move to `googleintegration` directory using & migrate the database.
```
    cd googleintegration && python manage.py migrate
```
4. Run the server
```
    python manage.py runserver
```
5. Open the browser and go to `http://127.0.0.1:8000/` to see the application running.

### How to use?
1. Go to  [http://127.0.0.1:8000/rest/v1/calendar/init](http://127.0.0.1:8000/rest/v1/calendar/init), it will redirect you to google login page.
2. Login with your google account and allow the application to access your calendar.
3. After allowing the application to access your calendar, you will be redirected to a [http://127.0.0.1:8000/rest/v1/calendar/redirect](http://127.0.0.1:8000/rest/v1/calendar/redirect) and shows the Top 10 Calendar Events.
4. You can watch this video to see the application in action: [https://youtu.be/AePSGDiVGtY](https://youtu.be/AePSGDiVGtY)

---
*For `CLIENT_ID`,`CLIENT_SECRET` and `PROJECT_ID` you can follow the steps mentioned in [Google API Documentation](https://developers.google.com/workspace/guides/get-started)*
