import matplotlib.pyplot as plt
import math
import time
import numpy as np
import functions as f

def plot_convex_hull(cords,result):
    for c in cords:
        plt.scatter(c[0], c[1], marker='o', c='b', s=10)
    length = len(result)
    for i in range(0, length - 1):
        plt.plot([result[i][0], result[i + 1][0]], [result[i][1], result[i + 1][1]], c='r')
    plt.plot([result[0][0], result[length - 1][0]], [result[0][1], result[length - 1][1]], c='r')
    plt.show()

def graham_scan(points):
    minY = f.minimum_y_coordinate(points)
    bp = points.pop(minY)
    sorted_points = f.sort_polar_angle(points, bp)
    m = len(sorted_points)
    if m < 2:
        print("Not enough coordinate pairs to form convex hull!!!!")
        return

    stack = []
    stack.append(bp)
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])

    for i in range(2, m):
        length = len(stack)
        top = stack[length - 1]
        next_top = stack[length - 2]
        v1 = [sorted_points[i][0] - next_top[0], sorted_points[i][1] - next_top[1]]
        v2 = [top[0] - next_top[0], top[1] - next_top[1]]

        while f.coss_multi(v1, v2) >= 0:
            if length < 3:     # After adding these two lines of code, no error will be reported when the amount of data is large
                break          # After adding these two lines of code, no errors will be reported when the amount of data is large
            stack.pop()
            length = len(stack)
            top = stack[length - 1]
            next_top = stack[length - 2]
            v1 = [sorted_points[i][0] - next_top[0], sorted_points[i][1] - next_top[1]]
            v2 = [top[0] - next_top[0], top[1] - next_top[1]]
        stack.append(sorted_points[i])

    return stack

################################################################################################################################
##  SINCE PLOTTING TAKES ALOT OF TIME IM ONLY PLOTTING THE FIRST 4 GRAPHS, REMOVE COUNT CHECKER TO PLOT ALL
################################################################################################################################
sizes = [50, 100, 1000, 2500, 5000, 10000, 50000, 100000]
time_r = []
count_checker = 0 #counter for plotting first 4 graphs
for i in range(len(sizes)):
    coordinates = []
    for j in range(sizes[i]):
        x = np.random.randint(1, 10000)
        y = np.random.randint(1, 10000)
        coordinates.append((x,y))
    start_t = time.time()
    res = graham_scan(coordinates)
    end_t = time.time()
    total_time = end_t - start_t
    print(f"Running time for n={sizes[i]} : {total_time}")
    time_r.append(total_time)
    if count_checker < 4: #increase val to plot more of bigger size tests
        plot_convex_hull(coordinates,res)
    count_checker += 1

plt.plot(sizes, time_r)
plt.show()

