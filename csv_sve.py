import matplotlib.pyplot as plt
import numpy as np
import math
import csv
import pandas as pd

filename = "cir_data.csv"
def cir_para(R, intencity):
    max_theta = 2 * np.pi
    list_t = list(np.arange(0, max_theta + intencity, intencity))
    print((np.arange(0, max_theta, 0.0001)).shape)
    print(len(list_t))
    x_circle = [(R*math.cos(x_y)) for x_y in list_t]
    y_circle = [(R*math.sin(x_y)) for x_y in list_t]
    # Plot
    fig = plt.figure()
    fig.set_size_inches(8, 8)
    ax = fig.add_axes([0.15, 0.2, 0.7, 0.7])
    ax.plot(x_circle, y_circle, linestyle='solid', color='black')
    plt.show()
    list_zero = [0] * len(x_circle)
    list_pos = [x_circle, y_circle, list_zero, list_zero, list_zero, list_zero]
    data_0 = pd.DataFrame(list_pos)
    data_1 = data_0.T
    data_1.to_csv('file_name.csv', index=False)
    print(data_1)
    print(len(list_pos))
    print(list_pos[2][0])
    a = list_pos
    print(len(a))
    print(a)
    data_size = len(x_circle)
    print(len(x_circle))
    # name of csv file


    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(data_1)
    j = 0
    for i in range(0, len(x_circle)):
        pos = [a[j][i], a[j+1][i], a[j+2][i], a[j+3][i], a[j+4][i], a[j+5][i]]
        print(pos)
    return data_size, a
cir_para(25, 0.01)