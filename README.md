# Tutoring System

A Django-based application to manage tutoring sessions, including user authentication, session creation, booking, and listing.

## Features

- User Registration and Authentication
- Admin User Management
- Tutoring Session Creation and Booking
- Listing Available Sessions
- Secure Token-Based Authentication

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/tutoring_system.git
    cd tutoring_system
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser 
    ```for admin panel```
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```

## API Endpoints

### User Registration

- **Endpoint:** `/api/admin/create-user/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "username": "jack",
        "email": "jack@example.com",
        "password": "password123"
    }
    ```
![main](https://github.com/Prabhakaran-D/Python-Task/blob/871d1680ded8e484b9f00f1a25d9d9d7db1119a9/tutoring_system/img/Create_user.png)
### User Login and admin login . (for addmin login use superuser username and password) 

- **Endpoint:** `/api/login/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "username": "jack",
        "password": "password123"
    }
    ```

- **Response:**

    ```json
    {
        "token": "your-auth-token",
        "user_id": 1
    }
    ```
	**by using the token from response you can access api's accordingly** 	
![main](https://github.com/Prabhakaran-D/Python-Task/blob/871d1680ded8e484b9f00f1a25d9d9d7db1119a9/tutoring_system/img/Login_admin.png)
![main](https://github.com/Prabhakaran-D/Python-Task/blob/871d1680ded8e484b9f00f1a25d9d9d7db1119a9/tutoring_system/img/Login_user.png)

### Create Tutoring Session

- **Endpoint:** `/api/admin/create-session/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
    	"title": "java",
    	"date": "2024-05-13",
    	"created_by": "1"
    }
    ```
![main](https://github.com/Prabhakaran-D/Python-Task/blob/871d1680ded8e484b9f00f1a25d9d9d7db1119a9/tutoring_system/img/Create-session.png)
### List Tutoring Sessions admin

- **Endpoint:** `/api/admin/list-sessions/`
- **Method:** `GET`
- **Response:**

    ```json
    [
        {
    	    "title": "Chemistry",
   	       "date": "2024-05-05",
    	    "created_by": 1
        }
    ]
    ```
![main](https://github.com/Prabhakaran-D/Python-Task/blob/871d1680ded8e484b9f00f1a25d9d9d7db1119a9/tutoring_system/img/Admin_list_session.png)

### Book a Tutoring Session

- **Endpoint:** `/api/book-session/`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "session_id": 1
    }
    ```
![main](https://github.com/Prabhakaran-D/Python-Task/blob/871d1680ded8e484b9f00f1a25d9d9d7db1119a9/tutoring_system/img/User_book_session.png)

### List Tutoring Sessions user

- **Endpoint:** `/api/user-list-sessions`
- **Method:** `GET`
- **Response:**

    ```json
    [
        {
    	    "title": "Chemistry",
   	       "date": "2024-05-05",
    	    "created_by": 1
        }
    ]
    ```
![main](https://github.com/Prabhakaran-D/Python-Task/blob/871d1680ded8e484b9f00f1a25d9d9d7db1119a9/tutoring_system/img/User_list_session.png)


