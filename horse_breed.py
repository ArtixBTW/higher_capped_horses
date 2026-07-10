#!/usr/bin/env python3

from horse_testing import MOVEMENT_SPEED, next_float


# https://minecraft.wiki/w/Horse#Bred_values
def breed_attributes(attr1: float, attr2: float, min: float, max: float) -> float:
    base = (abs(attr1 - attr2) + (max - min) * 0.3) * (
        (next_float() + next_float() + next_float()) / 3 - 0.5
    ) + (attr1 + attr2) / 2
    if base > max:
        base = 2 * max - base
    if base < min:
        base = 2 * min - base
    return base


print(breed_attributes(13.46, 14.29, MOVEMENT_SPEED.min, MOVEMENT_SPEED.max))
