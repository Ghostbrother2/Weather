# Weather Application

This is a Django-based web application that allows users to search for and view current weather information for cities worldwide. It uses the OpenWeather API to fetch real-time weather data and displays the information on a user-friendly interface.

---

## Features

- **Search for City Weather:**
  - Users can input a city name to retrieve its current weather, temperature, and local time.

- **Local Time Display:**
  - Converts the UTC time provided by the API to the city's local time.

- **Page Reload Counter:**
  - Tracks the number of times the page has been reloaded.

---

## Requirements

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Django 5.1.4
- SQLite (default database)

### Python Libraries

Install the required Python libraries using pip:
```bash
pip install django requests pytz python-decouple
```

---

## Setup

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd weather
   ```

2. **Environment Variables:**
   Create a `.env` file in the project root and add your OpenWeather API key:
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```

3. **Database Migrations:**
   Run the following commands to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Server:**
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## File Structure

```
weather/
├── apiweather/
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   │   └── index.html     # Main template for the app
│   ├── static/            # Static files (CSS, JS, images)
│   ├── models.py          # Database models
│   ├── views.py           # Application views
│   ├── urls.py            # App-specific URL configuration
├── weather/
│   ├── settings.py        # Django project settings
│   ├── urls.py            # Project-wide URL configuration
│   ├── wsgi.py            # WSGI entry point
│   ├── asgi.py            # ASGI entry point
├── manage.py              # Django management script
├── .env                   # Environment variables
├── db.sqlite3             # SQLite database file
```

---

## Usage

1. **Search for Weather:**
   - Enter a city name in the input box and submit to retrieve its current weather.

2. **Error Handling:**
   - If the city is not found, an error message is displayed.

3. **Page Reload Counter:**
   - The counter increments every time the page reloads.

---

## Key Files and Code Highlights

1. **`models.py`**
   - Defines the `PageReloadCounter` model to track page reload counts.

2. **`views.py`**
   - Handles the logic for fetching weather data and rendering the results.

3. **`urls.py`**
   - Maps URLs to the appropriate views.

4. **Templates:**
   - `index.html` is used to display the weather information and error messages.

5. **Static Files:**
   - Includes CSS for styling.

---

## Troubleshooting

1. **API Key Error:**
   - Ensure the `.env` file contains a valid OpenWeather API key.

2. **Template Not Found:**
   - Verify that `index.html` is located in the `templates/` directory and correctly referenced in `views.py`.

3. **Database Issues:**
   - Ensure migrations are applied correctly using:
     ```bash
     python manage.py makemigrations
     python manage.py migrate
     ```

---

## Future Improvements

- Add user authentication for personalized features.
- Implement caching for API responses to reduce API usage.
- Enhance the UI with more interactive elements.
- Add support for multi-language interfaces.

---

## License

This project is licensed under the MIT License. Feel free to use and modify the code as needed.

---

## Contact

For any questions or suggestions, feel free to reach out:
- **Email:** ma7moud.said86@hotmail.com
- **GitHub:** [Ghostbrother2](https://github.com/Ghostbrother2)

