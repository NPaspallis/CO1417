# Intractable problems

In computing, sometimes problems which seem very simple can be very hard.

## The Traveling Salesman Problem

One of the most popular examples of intractable problems is the _Traveling Salesman Problem_ (TSP):
- Given a list of cities,
- And given the distance between each pair of cities,
- Find the shortest route to visit each city once

For example, consider this setup:

```python
cities = ['Nicosia', 'Athens', 'London']  # a simple list containing 3 cities
distances = {  # distances is a dict with one entry for each of the 3 cities...
    'Nicosia': {'Athens': 913, 'London': 3216},  # each entry has as value another dict with the name and distance to each other city
    'Athens': {'Nicosia': 913, 'London': 2392},
    'London': {'Nicosia': 3216, 'Athens': 2392}
}
```

Assuming you start at ``Nicosia``, there are just 2 possible routes:
1. ``Nicosia, Athens, London`` with a covered distances of ``913+2392`` => ``3305``
2. ``Nicosia, London, Athens`` with a covered distances of ``3216+2392`` => ``5608``

In this case, the second route is obviously the shortest option.

But how do you generalize for a number of N cities: ``[city_1, city_2, ..., city_N]``?

The most straightforward solution is to simply go ahead and try every possible solution. This is sometimes also called
a _brute force_ solution.

In this problem, the brute force approach is to try out every possible combination of city orderings:
1. ``1, 2, 3, ..., N-2, N-1, N`` 
2. ``1, 2, 3, ..., N-2, N, N-1`` 
3. ``1, 2, 3, ..., N-1, N-2, N`` 
4. ``1, 2, 3, ..., N-1, N, N-2``
5. ``...``

Using results from [Combinatorics](https://en.wikipedia.org/wiki/Combinatorics), we can compute the number of
unique orderings (aka _permutations_) as ``N!`` (i.e., N [factorial](https://en.wikipedia.org/wiki/Factorial)). 

Unfortunately, this is a number which increases very _fast_ with ``N``. Even though the first 10 values of
``N!`` are more approachable, values for ``20!`` already become _intractable_:
- ``1! = 1``
- ``2! = 2``
- ``3! = 6``
- ``4! = 24``
- ``5! = 120``
- ``6! = 720``
- ``7! = 5040``
- ``8! = 40320``
- ``9! = 362880``
- ``10! = 3628800``
- ``...``
- ``20! = 2432902008176640000``
- ``...``

For instance, if you had a list of 20 cities, and you wanted to find the shortest path connecting them, then using
the brute force approach, you would need to check 3628800 (almost 4 million) different combinations.
A decent computer can do this in a reasonable amount of time, say 1 minute.

The problem is that adding just 1 more city to the list, makes the problem orders of time harder. In this case,
moving from 20 to 21 cities means 21x more time, i.e. the same computer requires 21 minutes to solve.
Then adding 1 more city, the same computer takes 22x more time, i.e., 462 minutes or almost 8 hours.
- 20 cities: 1 minute
- 21 cities: 21 minutes
- 22 cities: 462 minutes = ~8 hours
- 23 cities: 10626 minutes = ~177 hours = ~7.5 days
- 24 cities: 255024 minutes = ~4250 hours = ~177 days = ~6 months
- etc.

It is important to note how fast the complexity increases with each step! While it is very easy to solve a problem with
size N=20 (in just 1 minute) it becomes almost impossible to solve with N=24 (almost half a year!)

This kind of problems are often called **intractable**.

## Intractable problems

_Intractable problems_ are problems for which there exist no efficient algorithms to solve them.

In fact, most intractable problems are solved by brute-force search: Generate all possible solutions and check them one by one.

However, this _exhaustive_ algorithm is not efficient and therefor it is impossible to use it for _large_ inputs.

Examples of **Intractable Problems** include:
- The [Traveling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) discussed above
- The [Bin packing problem](https://en.wikipedia.org/wiki/Bin_packing_problem) concerns the finding of a distribution
of items of different sizes into a finite number of bins (i.e., containers), each with a fixed capacity, in a way that
minimizes the number of bins used.
- The [Graph Coloring Problem](https://en.wikipedia.org/wiki/Graph_coloring) concerns to the finding of the minimum
number of colors required to assign to the nodes of a graph so that no edge has the same color on both sides. For
example, in the following 10-node graph the minimum number of colors is 3: ``red``, ``blue``, ``green``.

![Graph](https://upload.wikimedia.org/wikipedia/commons/9/90/Petersen_graph_3-coloring.svg)

Source: [wikipedia](https://en.wikipedia.org/wiki/Graph_coloring#/media/File:Petersen_graph_3-coloring.svg)

## Complexity and the $1M Prize

The [P versus NP problem](https://en.wikipedia.org/wiki/P_versus_NP_problem) is a major unsolved problem in computer science.
It asks whether every problem whose solution can be quickly verified can also be solved quickly.

For instance, a solution of the TSP can be easily verified (by going through the route and summing the distance), but is
very hard to compute (because in its basic form it requires an exhaustive search of all ``N!`` possible solutions).

In year 2000, the Clay Mathematics Institute pledged a $1 million prize for the correct solution of each of the 7
[Millennium Prize Problems](https://en.wikipedia.org/wiki/Millennium_Prize_Problems). Only one of those problems has
already been proved. The remaining, including the _P versus NP_, remain unsolved.

## Exercises

1. Study the code in [cities.py](cities.py). Then add code to compute the name and the population of the most populous city.
2. Also in [cities.py](cities.py), add code to compute the name and the population of the least populous city.
3. Study and understand the code in [tsp.py](tsp.py) which solves the TSP for 3 cities.
4. Add code to the end of the [tsp.py](tsp.py) file to also compute the ``Longest route`` and the corresponding
``Longest distance``.
