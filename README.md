# FastAPI + PostgreSQL CRUD Example

This project demonstrates a simple CRUD (Create, Read, Update, Delete) API using [FastAPI](https://fastapi.tiangolo.com/) and [PostgreSQL](https://www.postgresql.org/).

## Features

- FastAPI for building RESTful APIs
- SQLAlchemy ORM for database interactions
- PostgreSQL as the database backend
- Pydantic models for data validation
- Docker support for easy setup

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL
- (Optional) Docker & Docker Compose

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/fastapi_postgresql_crud.git
    cd fastapi_postgresql_crud
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Copy `.env.example` to `.env` and update the database credentials.

4. **Run database migrations:**
    ```bash
    alembic upgrade head
    ```

5. **Start the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

### Using Docker

```bash
docker-compose up --build
```

## API Endpoints

| Method | Endpoint        | Description         |
|--------|----------------|---------------------|
| GET    | `/items/`      | List all items      |
| GET    | `/items/{id}`  | Get item by ID      |
| POST   | `/items/`      | Create new item     |
| PUT    | `/items/{id}`  | Update item by ID   |
| DELETE | `/items/{id}`  | Delete item by ID   |

