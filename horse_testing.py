#!/usr/bin/env python3

import random
from collections.abc import Callable
from dataclasses import dataclass

# math and logic is based off 1.21.11 Java source code


@dataclass
class Attribute:
    min: float
    max: float
    randomized: float


def generate_health(f: Callable[[int], int]) -> float:
    return 15 + f(8) + f(9)


def generate_jump_strength(supplier: Callable[[], float]) -> float:
    return 0.4 + supplier() * 0.2 + supplier() * 0.2 + supplier() * 0.2


def generate_movement_speed(supplier: Callable[[], float]) -> float:
    # https://minecraft.wiki/w/Horse#Statistics
    INTERNAL_TO_BLOCKS_PER_SEC = 43.17
    return INTERNAL_TO_BLOCKS_PER_SEC * (
        (0.45 + supplier() * 0.3 + supplier() * 0.3 + supplier() * 0.3) * 0.25
    )


def next_int(cap: int) -> int:
    return random.randint(0, cap)


def next_float() -> float:
    return random.uniform(0, 1)


MAX_HEALTH = Attribute(
    generate_health(lambda n: 0),
    generate_health(lambda n: n - 1),
    generate_health(next_int),
)
print(f"Max Health: {MAX_HEALTH}")

JUMP_STRENGTH = Attribute(
    generate_jump_strength(lambda: 0),
    generate_jump_strength(lambda: 1),
    generate_jump_strength(next_float),
)
print(f"Jump Strength: {JUMP_STRENGTH}")

MOVEMENT_SPEED = Attribute(
    generate_movement_speed(lambda: 0),
    generate_movement_speed(lambda: 1.0),
    generate_movement_speed(next_float),
)
print(f"Movement Speed: {MOVEMENT_SPEED}")
