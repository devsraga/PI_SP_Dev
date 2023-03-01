import initial_setup as ins
import cir as c
from pipython import GCSDevice, datarectools, pitools
import time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
import csv

# Setting stage with initial things: velocity
ret_back = ins.initial_set(stage_vel=5)
pidevice = ret_back[0]
axes = ret_back[1]
RELAXTIME = 0.25/1000000  # time in ms to wait after each motion command or 0 to wait for on target state

# field names for csv file
fields = ['X', 'Y', 'Z', 'alpha', 'bita', 'gama']

print(pidevice.qPOS())
print("dev")
# motion in X Y plane
j = 0
x = c.cir_para(25, 0.01)
x_circle_len = x[0]
a = x[1]
print(x_circle_len)
print(a)
print(len(a[0]))
print(len(a[1]))
print(len(a[2]))
print(len(a[3]))
print(len(a[4]))
print(len(a[5]))


pidevice.MOV(axes, [25, 0, 0, 0, 0, 0])
print(pidevice.qPOS())

time.sleep(5)
pos_cir_1 = []
total_actual_pos = []
print("###############################")
for i in range(0, x_circle_len):
    pidevice.MOV(axes, [a[j][i], a[j + 1][i], a[j + 2][i], a[j + 3][i], a[j + 4][i], a[j + 5][i]])
    pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
    pos_cir_1 = pidevice.qPOS()
    actual_pos = [pos_cir_1['X'], pos_cir_1['Y'], pos_cir_1['Z'], pos_cir_1['U'], pos_cir_1['V'], pos_cir_1['W']]
    total_actual_pos += [actual_pos]
    print(actual_pos)
    time.sleep(RELAXTIME / 1000.)
    if not RELAXTIME:
        pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(pos_cir_1)
print(total_actual_pos)
data_0 = pd.DataFrame(total_actual_pos)
data_1 = data_0.T
print(data_0)
print(data_1)
data_0.to_csv('data_1.csv', index=False)
print(total_actual_pos[0][0])
print(total_actual_pos[1][1])
print(total_actual_pos[1][2])
print(total_actual_pos[2][1])
print(total_actual_pos[2][2])
# Plot
fig_2 = plt.figure()
fig_2.set_size_inches(8, 8)
ax = fig_2.add_axes([0.15, 0.2, 0.7, 0.7])
print(x_circle_len)
x_circle = [total_actual_pos[i][0] for i in range(0, x_circle_len-1)]
y_circle = [total_actual_pos[i][1] for i in range(0, x_circle_len-1)]
ax.plot(x_circle, y_circle, linestyle='solid', color='black')

x_circle_given = [a[0][i] for i in range(0, x_circle_len)]
y_circle_given = [a[1][i] for i in range(0, x_circle_len)]
ax.plot(x_circle_given, y_circle_given, linestyle='solid', color='red')
plt.show()
print(pidevice.qPOS())


pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
print(pidevice.qPOS())

# Close the connections
print("\nClose the connections----------------------------------------------------------------")
pidevice.CloseConnection()
print("Connection closed")
