"""FastAPI application entry point."""

from fastapi import FastAPI

from app.random_service import generate_random_letter, generate_random_number
from app.schemas import GeneratedLetter, GeneratedNumber

app = FastAPI()


@app.post("/generate", response_model=GeneratedNumber)
def generate() -> GeneratedNumber:
    """Generate and return a random number in the interval [0.0, 1.0)."""
    return GeneratedNumber(number=generate_random_number())


@app.get("/generate-letter", response_model=GeneratedLetter)
def generate_letter() -> GeneratedLetter:
    """Generate and return one random uppercase English alphabet letter."""
    return GeneratedLetter(letter=generate_random_letter())
