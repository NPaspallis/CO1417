# Exercise 0704 - Randomize obstacles

Revisit the code from ``step0704``, [adding_obstacles.py](../step0704/adding_obstacles.py).

At the moment, the *obstacles* are quite predictable: They always come at the same time
(every exactly one cycle of the background) and always at the same height (centered at
``HEIGHT - 150`` pixels).

1. Using the code of [adding_obstacles.py](../step0704/adding_obstacles.py) as a starting point,
add code so that the obstacles come at a more random pace: every ``0.5`` to ``0.75`` cycles.

2. Additionally, add code to randomize the height of the obstacle. It has to be any of
these heights, chosen randomly: ``(HEIGHT - 150, HEIGHT - 160, HEIGHT - 170, HEIGHT - 180,
HEIGHT - 190, HEIGHT - 200)``.
