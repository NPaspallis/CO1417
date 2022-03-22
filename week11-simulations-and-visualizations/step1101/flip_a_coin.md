# Flip a coin

Imagine you flip a coin. Better yet, flip an actual coin. Or try asking [Google to flip a coin](https://www.google.com/search?q=flip+a+coin).
You will notice the outcome is either ``heads`` or ``tails``.

![Heads](heads.png)
![Tails](tails.png)

The ``heads`` and ``tails`` graphics from Google Search

A **fair flip** should give ``heads`` and ``tails`` with an equal, 50-50 chance. Let's assume that we have a way to flip coins fairly.

## Flipping a coin many times

If the _flip_ is fair, and you try it a couple of times, then you would expect to get an equal number of ``heads`` and ``tails``.
But of course, as randomness is _unpredictable_, you would also get a few consecutive turns of the same side.

> How many times do you think you need to flip a coin for, in order to get 3 consecutive times ``heads``?

The minimum is of course 3. How about the maximum?

In theory, the maximum is infinity: there is no guarantee of when you will get 3 consecutive times the same side.

In practice, you would _expect_ this to happen in a finite number of tries though.
Mathematically, you could compute that the _expected_ number of tries is 2^3 = 8 times.

> The ``x^y`` is another way of expressing the mathematical operation of exponent, i.e., in this case ``x to the power of y``.
 
But practically, we could also prove that the formula is indeed ``2^3`` using **simulations**.

## Simulating a flip coin (Exercise1101)

The goal of the first exercise, is to create a program to experimentally check how many times it takes to get
``K`` consecutive times ''heads''.

You can use the following function to _flip a coin_:

```python
import random


def flip_coin() -> str:  # this is a simple function that returns a 'str'
    """Returns 'heads' or 'tails' with equal probability."""
    return random.choice(['heads', 'tails'])  # simply choose one of the 2 values in the list and return it
```

To increase the accuracy of the simulation, add code that repeats the experiment ``N`` times (e.g. ``N=100``),
and compute the _average_ number of tries it takes to get ``K`` consecutive times ``heads``.

Mathematically, we expect tries to be ~8 for ``K=3``, and ~16 for ``K=4``, and generally ``2^K`` for any ``K``.
Does your simulation confirm this formula?
