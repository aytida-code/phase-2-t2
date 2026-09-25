# Project Summary

This repository contains a minimal FastAPI random-number API.

- `app/main.py` exposes `POST /generate` and returns a `GeneratedNumber` response.
- `app/random_service.py` provides `generate_random_number()`, using `random.random()` to produce a float in the half-open interval `[0.0, 1.0)`.
- `app/schemas.py` defines the `GeneratedNumber` response model with a `number: float` field.
- `tests/test_api.py` and `tests/test_random_service.py` use Python `unittest` to cover the endpoint and random-number contract.

## Commands

Install dependencies:

```sh
python -m pip install -r requirements.txt
```

Run the API:

```sh
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Run tests:

```sh
python -m unittest discover -s tests
```

The project intentionally has no database, authentication, messaging, pagination, frontend, or infrastructure components.
