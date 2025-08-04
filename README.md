# RailOps API


This repository contains the backend API for the RailOps application. It is built with FastAPI and handles form submissions for railway maintenance and inspection, specifically for Wheel Specifications and Bogie Checksheets.
## Component Diagram

The following diagram illustrates the high-level structure and interaction between components in the RailOps API system.

![Component Diagram](component.png)
## Tech Stack

*   **Framework**: FastAPI
*   **ORM**: SQLAlchemy
*   **Database**: PostgreSQL (via `psycopg2`)
*   **Data Validation**: Pydantic
*   **Server**: Uvicorn

## Project Structure
The project is organized to separate concerns such as database configuration, data models, API schemas, and routing logic.

```
.
├── requirements.txt      # Project dependencies
└── project/
    ├── database.py       # Database connection setup and session management
    ├── main.py           # Main FastAPI application entrypoint
    ├── models.py         # SQLAlchemy database models
    ├── schemas.py        # Pydantic schemas for data validation
    └── routers/
        └── forms.py      # API routes for form submissions
```

## Setup and Installation

Follow these steps to get the application running locally.

### 1. Clone the Repository
```bash
git clone https://github.com/matrix-09/railops_be.git
cd railops_be
```

### 2. Create a Virtual Environment
It is recommended to use a virtual environment to manage project dependencies.
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the `project` directory. This file will store your database connection string.

`project/.env`:
```env
DATABASE_URL="postgresql://user:password@host:port/dbname"
```
Replace `user`, `password`, `host`, `port`, and `dbname` with your PostgreSQL database credentials.

### 5. Run the Application
From the root directory of the project, run the Uvicorn server:
```bash
uvicorn project.main:app --reload
```
The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

The API provides endpoints for managing wheel specifications and bogie checksheets. All endpoints are prefixed with `/api/forms`.

### Wheel Specifications

#### `POST /api/forms/wheel-specifications`
Submits a new wheel specification form.

*   **Request Body:**
    ```json
    {
      "formNumber": "WS-2023-001",
      "submittedBy": "John Doe",
      "submittedDate": "2023-10-27",
      "fields": {
        "wheel_diameter": "840",
        "flange_thickness": "29.4",
        "tread_width": "135"
      }
    }
    ```
*   **Success Response (200 OK):**
    ```json
    {
        "success": true,
        "message": "Wheel specification submitted successfully.",
        "data": {
            "formNumber": "WS-2023-001",
            "submittedBy": "John Doe",
            "submittedDate": "2023-10-27",
            "status": "Saved"
        }
    }
    ```

#### `GET /api/forms/wheel-specifications`
Retrieves a specific wheel specification form based on query parameters.

*   **Query Parameters:**
    * `formNumber` (string)
    * `submittedBy` (string)
    * `submittedDate` (string, format `YYYY-MM-DD`)
*   **Example Request:**
    `GET /api/forms/wheel-specifications?formNumber=WS-2023-001&submittedBy=John%20Doe&submittedDate=2023-10-27`
*   **Success Response (200 OK):**
    ```json
    {
      "success": true,
      "message": "Filtered wheel specification forms fetched successfully.",
      "data": [
        {
          "_sa_instance_state": "<...>",
          "formNumber": "WS-2023-001",
          "submittedBy": "John Doe",
          "submittedDate": "2023-10-27",
          "fields": {
            "wheel_diameter": "840",
            "flange_thickness": "29.4",
            "tread_width": "135"
          }
        }
      ]
    }
    ```
*   **Error Response (404 Not Found):**
    ```json
    {
        "detail": "Specification not found"
    }
    ```

### Bogie Checksheet

#### `POST /api/forms/bogie-checksheet`
Submits a new bogie checksheet form.

*   **Request Body:**
    ```json
    {
      "formNumber": "BC-2023-001",
      "inspectionBy": "Jane Smith",
      "inspectionDate": "2023-10-27",
      "bogieDetails": {
        "bogie_type": "ICF",
        "coach_number": "ER-12345"
      },
      "bogieChecksheet": {
        "check_1_status": "OK",
        "check_2_clearance": "5mm"
      },
      "bmbcChecksheet": {
        "piston_stroke": "Normal",
        "brake_pad_wear": "Minimal"
      }
    }
    ```
*   **Success Response (200 OK):**
    ```json
    {
      "success": true,
      "message": "Bogie checksheet submitted successfully.",
      "data": {
        "formNumber": "BC-2023-001",
        "inspectionBy": "Jane Smith",
        "inspectionDate": "2023-10-27",
        "status": "Saved"
      }
    }
