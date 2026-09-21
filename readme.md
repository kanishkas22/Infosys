# ExamGuard

ExamGuard is a Flask-based web application designed for an online examination environment. It provides candidate registration and login functionality along with pre-exam verification checks such as camera, microphone, and selfie checks, followed by a dashboard.

## Features

* Candidate registration
* Candidate login authentication
* MySQL database integration
* Camera verification check
* Microphone verification check
* Selfie verification check
* Candidate dashboard
* Flask-based routing and templates

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MySQL
* **Database Connector:** `mysql-connector-python`
* **Frontend:** HTML templates
* **Development Server:** Flask development server

## Project Structure

```text
ExamGuard/
│
├── app.py
├── db.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── camera_check.html
│   ├── mic_check.html
│   ├── selfie_check.html
│   └── dashboard.html
│
└── README.md
```

## Application Flow

```text
Home Page
    │
    ├── Register
    │
    └── Login
          │
          ▼
    Camera Check
          │
          ▼
    Microphone Check
          │
          ▼
    Selfie Check
          │
          ▼
       Dashboard
```

## Routes

| Route           | Method | Description                            |
| --------------- | ------ | -------------------------------------- |
| `/`             | GET    | Displays the home page                 |
| `/register`     | POST   | Registers a new candidate              |
| `/login`        | POST   | Authenticates a candidate              |
| `/camera-check` | GET    | Opens the camera verification page     |
| `/mic-check`    | GET    | Opens the microphone verification page |
| `/selfie-check` | GET    | Opens the selfie verification page     |
| `/dashboard`    | GET    | Displays the candidate dashboard       |

The Flask application defines separate routes for registration, login, camera checking, microphone checking, selfie checking, and the dashboard.

## Database

The application uses MySQL through `mysql.connector`. The configured database is named `examguard`, and the application connects to a MySQL server running locally.

The candidate registration functionality stores:

* Full name
* Email
* Password

in the `candidates` table.

The login functionality verifies the candidate's email and password against the `candidates` table.

### Database Setup

Create the database:

```sql
CREATE DATABASE examguard;
```

Create the candidates table:

```sql
CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

> Update the MySQL credentials in `db.py` according to your local MySQL configuration.

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd ExamGuard
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask mysql-connector-python
```

Or, if `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

### 4. Configure MySQL

Make sure MySQL is running and create the `examguard` database and `candidates` table.

Update `db.py` with your local MySQL credentials.

### 5. Run the application

```bash
python app.py
```

The Flask development server will start, and the application can be accessed through the local server address displayed in the terminal.

## Authentication Flow

During registration, the application receives the candidate's full name, email, and password and inserts the details into the `candidates` table.

During login, the application queries the database using the submitted candidate identifier and password. If a matching record is found, the user is redirected to the camera-check page.

## Verification Modules

### Camera Check

The `/camera-check` route renders `camera_check.html`, providing the camera verification stage of the application.

### Microphone Check

The `/mic-check` route renders `mic_check.html` for microphone verification.

### Selfie Check

The `/selfie-check` route renders `selfie_check.html` for selfie verification.

### Dashboard

The `/dashboard` route renders `dashboard.html` after the verification stages.

## Running in Development

The application currently runs Flask in debug mode:

```python
app.run(debug=True)
```

This configuration is intended for development and testing.

## Security Note

For production deployment, database credentials should not be stored directly in source code. Passwords should also be securely hashed rather than stored as plain text.

Use environment variables or a `.env` file for sensitive configuration.

## Future Enhancements

Possible improvements include:

* Secure password hashing
* Session-based authentication
* Camera-based face verification
* Automated selfie/identity verification
* Microphone availability and audio checks
* Exam monitoring and proctoring
* Candidate activity logging
* Exam timer
* Question management
* Result generation
* Admin dashboard
* Secure environment-variable configuration

## License

This project is intended for educational and development purposes.
