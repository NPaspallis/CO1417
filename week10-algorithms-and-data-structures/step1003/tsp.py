import itertools

cities = ['Nicosia', 'Athens', 'London']  # a simple list containing 3 cities
city_distances = {  # distances is a dict with one entry for each of the 3 cities...
    'Nicosia': {'Athens': 913, 'London': 3216},  # each entry has as value another dict with the name and distance to each other city
    'Athens': {'Nicosia': 913, 'London': 2392},
    'London': {'Nicosia': 3216, 'Athens': 2392}
}

# the 'itertools' is used to generate all possible permutations of the given list - note it returns a 'generator', not a list
routes_iterator = itertools.permutations(cities)
# the 'generator' is a mechanism which allows you to produce each item as needed, saving processing and storing resources
# you can 'unroll' an iterator into a list, using the 'list' constructor
routes = list(routes_iterator)
print(routes)


# The following function is used to compute the 'distance' of the route as a sum of the cost of individual segments
def compute_distance(route, distances):
    """For the given route (e.g. a->b, b-c), and distances map, compute the 'cost' of route as the sum of distances: a->b + b->c"""
    distance = 0
    for i in range(len(route) - 1):
        from_city = route[i]
        to_city = route[i + 1]  # destination is next city - if last one, then back to first
        distance = distance + distances[from_city][to_city]
    return distance


# compute the shortest path by checking all possible routes - initially, no route is chosen
shortest_route = None
# the shortest distance is initially set to a 'very large' value so that it is immediately replaced after the first comparison
shortest_distance = float('inf')  # Python's way of setting a value to 'infinity'

for r in routes:
    d = compute_distance(r, city_distances)
    if d < shortest_distance:
        shortest_distance = d
        shortest_route = r

print('Shortest route: ', shortest_route)
print('Shortest distance: ', shortest_distance)
