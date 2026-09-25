"""Pure random-number generation logic."""

import random


def generate_random_number() -> float:
    """Return a random floating-point number in the interval [0.0, 1.0)."""
    return random.random()


def generate_random_letter() -> str:
    """Return one randomly selected uppercase English alphabet letter."""
    return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
