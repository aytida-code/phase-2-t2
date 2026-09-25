# Random Number Generator API

A minimal public FastAPI backend that generates random floating-point numbers.

## Install

```sh
python -m pip install -r requirements.txt
```

## Run

```sh
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

## Generate a number

```sh
curl -X POST http://127.0.0.1:8000/generate
```

The endpoint returns JSON in the form `{"number": 0.5}`. The number is a float in `[0.0, 1.0)`.

## Test

```sh
python -m unittest discover -s tests
```
