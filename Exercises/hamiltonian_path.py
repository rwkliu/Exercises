from itertools import permutations


# TODO: Write a function to generate all possible orders of nodes
def generate_permutations(n: list) -> list:
    paths = permutations(n)

    # print for debug
    # for p in list(paths):
    #     print(p)

    return paths


# TODO: Write a function that checks if a given order is a valid Hamiltonian Path
def is_valid_path(graph, path):
    """
    To check if a given path is a valid Hamiltonian Path, you need to ensure that each
    consecutive pair of nodes in the path has an edge between them in the graph.
    """
    print(path)
    for i in range(len(path) - 1):
        if graph[path[i]][path[i + 1]] == 0:
            return False
    return True


# TODO: Implement the brute-force Hamiltonian Path function
def hamiltonian_path_brute_force(graph):
    paths = generate_permutations(graph)
    for path in paths:
        if is_valid_path(graph, path):
            return path
    return []


# Test Case
islands = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0],
]

print(hamiltonian_path_brute_force(islands))  # Expected: A valid Hamiltonian path or []
