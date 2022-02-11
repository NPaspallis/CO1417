# Exercise 0603 - Smooth animations

Revisit the code of the [interactive_flappy_wings.py](../step0604/interactive_flappy_wings.py) in step0604.

Study the code. Then run it. You will notice that the jump is a bit 'slow'.
Specifically, it takes 12 (# of offsets) X 100ms (delay) = 1.2 seconds to complete. How can you speed this up?

There are at least 2 approaches:

## Approach #1 - Speeding up by cutting down the frames

This is the original list of 12 offsets:

```python
jump_offsets = [0, -60, -45, -30, -20, 0, 20, 30, 45, 50, 25, -15, ]
```

Edit the code so that there is a smaller number of offsets (aim for 6). How long does the jump animation last now?
Run the code and study the result. Is the animation as smooth as before?

> Hint: remember that the ``jump_offsets`` must add up to zero.

## Approach #2 - Speeding up by halving the delay

The ``DELAY`` value controls the waiting time between frames.

```python
DELAY = 100  # 100 ms = 0.1 sec
```

Edit the code to cut down the delay to half (50ms). How long does the jump animation last now?
Run the code and study the result. Is the animation as smooth as before?
But there is still a downside: *flappy bird* seems to flap its wings unnaturally fast. Can you do better?

> Hint: remember to restore the ``jump_offsets`` to its original 12 values first.

## Approach #3 - Processing separate animations at different paces

Ideally, we would like to keep the ``DELAY`` small (so that we have many frames per second) but at the
same time we would like individual animations to progress at their own pace.

For instance, assuming the delay is 50 ms (i.e., animation updates 20 times per second), we would like the
*jump* part of the animation to progress in each update so that it completes in 0.6 seconds.
But, at the same time, we would like the *wing flapping* part of the animation to only update every two
updates, so that a full cycle of the animation completes in 9 X 2 X 50ms = 0.9 seconds.

Your challenge here is to edit the code of the [interactive_flappy_wings.py](../step0604/interactive_flappy_wings.py)
to achieve this.
