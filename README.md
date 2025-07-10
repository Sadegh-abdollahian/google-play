# Google Play Clone API

This project is a Django-based backend API for an application marketplace, inspired by the functionality of Google Play. It enables users to browse, download, and purchase applications, while providing developers with tools to upload and manage their apps.

## Table of Contents

- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [API Endpoints Overview](#api-endpoints-overview)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Key Features

- **User Authentication:** Secure registration and login via phone number and OTP verification.
- **User Roles:** Separate roles for users and developers, with appropriate permissions.
- **App Management:** Developers can upload, update, and manage APK files, icons, and preview images.
- **Categorization and Tagging:** Applications can be categorized and tagged for easier discovery.
- **Reviews and Ratings:** Users can leave reviews and rate applications they’ve used.
- **Wishlist/Bookmarks:** Users can bookmark applications to their personal wishlist.
- **Order Processing:** Basic system for managing application purchases.
- **RESTful API:** Full-featured API built using Django REST Framework.

## Technologies Used

- **Backend:** Python, Django, Django REST Framework
- **Database:** SQLite (for development)
- **Libraries:**
  - `django-filter`: For advanced filtering on API endpoints
  - `django-taggit`: For tagging functionality
  - `Pillow`: For image handling and resizing

## Installation and Setup

To run the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sadegh-abdollahian/google-play.git
   cd google-play
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   The API will be available at: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API Endpoints Overview

All main API routes are prefixed with `/api/v1/`.

- `POST /api/v1/accounts/`: Registration and login
- `GET /api/v1/apps/`: Browse and search for applications
- `GET /api/v1/apps/<id>/`: View application details
- `POST /api/v1/orders/`: Create and manage orders
- `GET /api/v1/orders/history/`: View purchase history

## Project Structure

This Django project is divided into three core apps:

- `accounts`: User accounts, authentication, and profiles
- `applications`: App upload, management, categories, tags, reviews, and media
- `orders`: Order and purchase handling logic

## Running Tests

To run the automated tests:

```bash
python manage.py test
```

## Contributing

Contributions are welcome! Please feel free to fork the repository, open issues, or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).