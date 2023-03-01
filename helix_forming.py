import matplotlib.pyplot as plt
import numpy as np
import math
def helix_para(R, height, intencity):
    max_theta = 2 * np.pi
    list_t = list(np.arange(0, max_theta + intencity, intencity))
    print((np.arange(0, max_theta, 0.0001)).shape)
    x_circle = [(R*math.cos(x_y)) for x_y in list_t]
    y_circle = [(R*math.sin(x_y)) for x_y in list_t]
    Z_circle = [(R*math.sin(x_y)) for x_y in list_t]
    # Plot
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_axes([0.15, 0.2, 0.7, 0.7])
    ax.plot(x_circle, y_circle, linestyle='solid', color='black')
    plt.show()

    # points generation
    list_zero = [0] * len(x_circle)
    list_pos = [x_circle, y_circle, list_zero, list_zero, list_zero, list_zero]
    print(len(list_pos))
    print(list_pos[2][0])
    a = list_pos
    print(len(a))
    data_size = len(x_circle)
    j = 0
    for i in range(0, len(x_circle)):
        pos = [a[j][i], a[j+1][i], a[j+2][i], a[j+3][i], a[j+4][i], a[j+5][i]]
        print(pos)
    return data_size, a
