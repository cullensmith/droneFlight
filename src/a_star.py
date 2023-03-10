import math
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

# credit source
# https://www.linkedin.com/pulse/least-cost-path-analysis-algorithm-chonghua-yin/

def e_dist(p1, p2):
    """
    Takes two points and returns the euclidian distance
    """
    x1, y1 = p1
    x2, y2 = p2
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return int(distance)


def weighted_score(cur, node, h, start, end):
    """
    Provides a weighted score by comparing the current node with a neighboring node. 
    Loosely based on on the Nisson score concept: f=g+h
    In this case, the "h" value, or "heuristic", is the elevation value of each node.
    """
    score = 0
    # current node elevation
    cur_h = h[cur]
    # current node distance from end
    cur_g = e_dist(cur, end)
    # current node distance from start
    cur_d = e_dist(cur, start)
    # neighbor node elevation
    node_h = h[node]
    # neighbor node distance from end
    node_g = e_dist(node, end)
    # neighbor node distance from start
    node_d = e_dist(node, start)
    # Compare values with the heighest
    # weight given to terrain followed by progress towards the goal.
    if node_h < cur_h:
        score += cur_h-node_h
    if node_g < cur_g:
        score += 10
    if node_d > cur_d:
        score += 8
    return score


def astar(start, end, h):
    """
    A-Star (or A*) search algorithm.
    Moves through nodes in a network
    (or grid), scores each node's
    neighbors, and goes to the node
    with the best score until it finds
    the end.  A* is an evolved Dijkstra
    algorithm.
    """
    # Closed set of nodes to avoid
    closed_set = set()
    # Open set of nodes to evaluate
    open_set = set()
    # Output set of path nodes
    path = []
    # Add the starting point to to begin processing
    open_set.add(start)
    while open_set:
        # Grab the next node
        cur = open_set.pop()
        # Return if we're at the end
        if cur == end:
            return path
        # Close off this node to future processing
        closed_set.add(cur)
        # The current node is always a path node by definition
        path.append(cur)
        # List to hold neighboring nodes for processing
        options = []
        # Grab all of the neighbors
        y1 = cur[0]
        x1 = cur[1]
        if y1 > 0:
            options.append((y1-1, x1))
        if y1 < h.shape[0]-1:
            options.append((y1+1, x1))
        if x1 > 0:
            options.append((y1, x1-1))
        if x1 < h.shape[1]-1:
            options.append((y1, x1+1))
        if x1 > 0 and y1 > 0:
            options.append((y1-1, x1-1))
        if y1 < h.shape[0]-1 and x1 < h.shape[1]-1:
            options.append((y1+1, x1+1))
        if y1 < h.shape[0]-1 and x1 > 0:
            options.append((y1+1, x1-1))
        if y1 > 0 and x1 < h.shape[1]-1:
            options.append((y1-1, x1+1))
        # If the end is a neighbor, return
        if end in options:
            return path
        # Store the best known node
        best = options[0]
        # Begin scoring neighbors
        best_score = weighted_score(cur, best, h, start, end)
        # process the other 7 neighbors
        for i in range(1, len(options)):
            option = options[i]
            # Make sure the node is new
            if option in closed_set:
                continue
            else:
                # Score the option and compare it to the best known
                option_score = weighted_score(cur, option, h, start, end)
                if option_score > best_score:
                    best = option
                    best_score = option_score
                else:
                    # If the node isn't better seal it off
                    closed_set.add(option)
                # Uncomment this print statement to watch the path develop in real time:
                # print(best, e_dist(best, end))
        # Add the best node to the open set
        open_set.add(best)
    return []

def run_astar():
    infile = "../data/cost.tif"

    da_dem = xr.open_rasterio(infile).drop('band')[0]
    nodata = da_dem.nodatavals[0]
    da_dem = da_dem.where(da_dem>nodata, np.nan)

    cost   = da_dem.data

    # Starting column, row
    sx = 320
    sy = 330

    # Ending column, row
    dx = 1670
    dy = 2870

    path = astar((sy, sx), (dy, dx), cost)



