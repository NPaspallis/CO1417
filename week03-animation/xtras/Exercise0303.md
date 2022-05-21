# Exercise 0303

The code of [Collisions](../step0306/Collisions.py) in [step0306](../step0306) has a glitch:
As the speed of each ball over the horizontal and vertical axis is decided in _random_, it is possible that
some of the balls are stationary (i.e., not moving). 

You are asked to:
1. Make sure that speed over X and speed over Y are checked, so they are never 0
2. Relax the previous constraint so that you check that the speed over X can be 0, as long as speed over Y is not. and vice versa. In other words make sure that at least one of speed over X and speed over Y is not 0 (but leave the possibility for one of the two to be 0).
