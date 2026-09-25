"""API response schemas."""

from pydantic import BaseModel


class GeneratedNumber(BaseModel):
    """A random number generated for one request."""

    number: float


class GeneratedLetter(BaseModel):
    """A random letter generated for one request."""

    letter: str
