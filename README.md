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

---
*For `CLIENT_ID`,`CLIENT_SECRET` and `PROJECT_ID` you can follow the steps mentioned in [Google API Documentation](https://developers.google.com/workspace/guides/get-started)*
