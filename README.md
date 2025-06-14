# ALX Travel App - API (0x01)

This project provides API endpoints for managing listings and bookings for a travel application.

## Project Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url> alx_travel_app_0x01
    cd alx_travel_app_0x01
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    # (Ensure Django and djangorestframework are in requirements.txt)
    # Or: pip install Django djangorestframework
    ```

4.  **Apply migrations:**
    ```bash
    python manage.py makemigrations listings
    python manage.py migrate
    ```

5.  **Create a superuser (optional, for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
    The API will be accessible at `http://127.0.0.1:8000/api/`.

## API Endpoints

The following API endpoints are available, providing full CRUD (Create, Read, Update, Delete) operations.

### Listings

Base URL: `/api/listings/`

*   **`GET /api/listings/`**: List all listings.
*   **`POST /api/listings/`**: Create a new listing.
    *   **Request Body (JSON):**
        ```json
        {
            "name": "Cozy Beach House",
            "description": "A beautiful house by the sea.",
            "address": "123 Ocean Drive, Beach City",
            "price_per_night": "150.00"
        }
        ```
*   **`GET /api/listings/{id}/`**: Retrieve a specific listing.
*   **`PUT /api/listings/{id}/`**: Update a specific listing (replaces the entire resource).
*   **`PATCH /api/listings/{id}/`**: Partially update a specific listing.
*   **`DELETE /api/listings/{id}/`**: Delete a specific listing.

### Bookings

Base URL: `/api/bookings/`

*   **`GET /api/bookings/`**: List all bookings.
*   **`POST /api/bookings/`**: Create a new booking.
    *   **Request Body (JSON):**
        ```json
        {
            "listing": 1, // ID of the listing to book
            "guest_name": "John Doe",
            "check_in_date": "2024-08-15",
            "check_out_date": "2024-08-20",
            "number_of_guests": 2
        }
        ```
*   **`GET /api/bookings/{id}/`**: Retrieve a specific booking.
*   **`PUT /api/bookings/{id}/`**: Update a specific booking.
*   **`PATCH /api/bookings/{id}/`**: Partially update a specific booking.
*   **`DELETE /api/bookings/{id}/`**: Delete a specific booking.

## Testing Endpoints

You can use tools like [Postman](https://www.postman.com/) or `curl` to test these endpoints.

**Example with curl (Listings):**
```bash
# Get all listings
curl http://127.0.0.1:8000/api/listings/

# Create a new listing
curl -X POST -H "Content-Type: application/json" -d '{"name":"New Apartment","description":"Modern and new.","address":"456 Main St","price_per_night":"120.50"}' http://127.0.0.1:8000/api/listings/