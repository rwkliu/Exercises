import math
def graham_scan(points):
    """
    Finds the convex hull of a set of points using the Graham Scan algorithm.

    :param points: List of points represented as tuples (x, y).
    :type points: List[Tuple[int, int]]
    :return: Convex hull as a list of points.
    :rtype: List[Tuple[int, int]] or None
    """
    def orientation(p, q, r):
        """Return positive if p-q-r are clockwise, neg if ccw, zero if colinear."""
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

    def square_distance(p, q):
        """Return the squared distance between points p and q."""
        return (p[0] - q[0])**2 + (p[1] - q[1])**2

    # Step 1: Find the pivot with the lowest y-coordinate and, in case of tie, the lowest x-coordinate
    pivot = min(points, key=lambda p: (p[1], p[0]))

    # Step 2: Sort the points by polar angle with pivot, removing closer points with the same angle
    sorted_points = sorted(points, key=lambda p: (math.atan2(p[1] - pivot[1], p[0] - pivot[0]), -square_distance(p, pivot)))
    print("sorted points")
    print(sorted_points)

    # Step 3: Construct the convex hull
    hull = [sorted_points[0], sorted_points[1]]  # Start with the first two points
    for p in sorted_points[2:]:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], p) <= 0:
            hull.pop()  # Remove the point if it's a right turn or colinear
        hull.append(p)

    return hull

# Example usage:
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
graham_scan(points)
# print(graham_scan(points))  # Output might vary slightly based on orientation checks
