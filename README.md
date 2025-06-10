# ETL Project 📊

This is an ETL (Extract, Transform, Load) service that fetches bank exchange rates from external APIs and stores them in a local database with Redis caching.

## 🌐 Environment Configuration

Create a `.env` file in the root of the project with the following variables:

```env
API_VERSION=1.0.0
API_TITLE='ETL project'
API_DESCRIPTION='ETL to fetching bank rates'

DEBUG=true

FRANKFURTER_URL=https://api.frankfurter.app/latest
EXCHANGERATE_URL=https://api.exchangerate-api.com/v4/latest

DATABASE_URL=mysql://user:password@host:port/db

REDIS_URL=host
REDIS_PORT=port
REDIS_DB=db
```

⚠️ **Important**: Replace placeholders (`user`, `password`, `host`, `port`, etc.) with your actual environment values.

## 🚀 Running the Project

### 1. Install Dependencies

Install project dependencies using Poetry:

```bash
poetry install
```

### 2. Apply Database Migrations

If using Alembic, apply database migrations:

```bash
alembic upgrade head
```

### 3. Start the Application

```bash
poetry run uvicorn app.main:app --reload
```

The API will be available at:
- **Main API**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs

## 🧩 Features

- 📡 **Fetch exchange rates** from multiple sources:
  - Frankfurter API
  - ExchangeRate-API
- 🗃 **Store normalized data** in MySQL database
- ⚡ **Cache responses** using Redis for improved performance
- 🧪 **Fully testable architecture** with support for mocking

## 🧪 Testing

Run tests with coverage reporting:

```bash
pytest --cov=app --cov-report=term --cov-report=html
```

This will generate both terminal output and an HTML coverage report.