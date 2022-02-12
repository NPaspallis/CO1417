# Exercise 0704 - Randomize obstacles

Revisit the code from ``step0704``, [adding_obstacles.py](../step0704/adding_obstacles.py).

At the moment, the *obstacles* are quite predictable: They always come at the same time
(every exactly one cycle of the background) and always at the same height (-15  pixels from
the center).

1. Using the code of [adding_obstacles.py](../step0704/adding_obstacles.py) as a starting point,
add code so that the obstacles come at a more random pace: every ``0.75`` to ``1.25`` cycle.

2. Additionally, add code to randomize the height of the obstacle. It has to be any of
these heights, chosen randomly: ``(-5, -15, -25)``.
