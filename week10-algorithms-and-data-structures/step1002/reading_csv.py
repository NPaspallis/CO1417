import itertools

file = open('distances.csv', 'r')
lines = file.readlines()
cities = lines.pop(0).strip().split(',')
cities.pop(0)  # remove first entry ('Cities' label)
print("Cities: ", cities)
distances = {}
for line in lines:
    # print("line: ", line)
    values = line.strip().split(',')
    city_from = values.pop(0)
    distances[city_from] = {}

    # for i in range(0, len(cities)):
    for i in range(0, len(cities)):
        city_to = cities[i]
        distance = values[i]
        distances[city_from][city_to] = int(distance)

    # print(city_from, " -> ", distances[city_from])

print('Distances: ', distances)

print('Permutations')
routes = [route for route in itertools.permutations(cities)]
print('Number of possible routes: ', len(routes))


def compute_distance(route):
    """For given route: [a, b, c], compute distance as the sum of distances: a->b + b->c + c->a"""
    d = 0
    for i in range(len(route)):
        from_city = route[i]
        to_city = route[i + 1] if i < len(route) - 1 else route[0]  # destination is next city - if last one, then back to first
        d = d + distances[from_city][to_city]
    return d


shortest_route = None
shortest_distance = float('inf')  # Python's way of setting a value to 'infinity'

for route in routes:
    d = compute_distance(route)
    if d < shortest_distance:
        shortest_distance = d
        shortest_route = route

print('Shortest route: ', shortest_route)
print('Shortest distance: ', shortest_distance)

longest_route = None
longest_distance = 0

for route in routes:
    d = compute_distance(route)
    if d > longest_distance:
        longest_distance = d
        longest_route = route

print('Longest route: ', longest_route)
print('Longest distance: ', longest_distance)