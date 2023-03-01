import initial_setup as ins
import cir as c
from pipython import GCSDevice, datarectools, pitools
import time
# Setting stage with initial things: velocity
ret_back = ins.initial_set(stage_vel=5)
pidevice = ret_back[0]
axes = ret_back[1]
RELAXTIME = 0.25/1000  # time in ms to wait after each motion command or 0 to wait for on target state


# motion in X Y plane
j = 0
x = c.cir_para(25, 0.01)
x_circle_len = x[0]
a = x[1]
print(x_circle_len)

pidevice.MOV(axes, [25, 0, 0, 0, 0, 0])
time.sleep(5)
for i in range(0, x_circle_len):
    pidevice.MOV(axes, [a[j][i], a[j + 1][i], a[j + 2][i], a[j + 3][i], a[j + 4][i], a[j + 5][i]])
    time.sleep(RELAXTIME / 1000.)
    if not RELAXTIME:
        pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(pidevice.qPOS())
time.sleep(5)
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
time.sleep(5)
pidevice.MOV(axes, [0, 15, 0, 0, 0, 0])
time.sleep(5)
for i in range(0, x_circle_len):
    pidevice.MOV(axes, [a[j + 2][i], a[j][i], a[j + 1][i], a[j + 3][i], a[j + 4][i], a[j + 5][i]])
    #pidevice.MOV(axes, [a[j][i], a[j + 1][i], a[j + 2][i], a[j + 3][i], a[j + 4][i], a[j + 5][i]])
    time.sleep(RELAXTIME / 1000.)
    if not RELAXTIME:
        pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(pidevice.qPOS())

time.sleep(5)
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
time.sleep(5)



pidevice.MOV(axes, [15, 0, 0, 0, 0, 0])
time.sleep(5)
for i in range(0, x_circle_len):
    pidevice.MOV(axes, [a[j][i], a[j + 2][i], a[j + 1][i], a[j + 3][i], a[j + 4][i], a[j + 5][i]])
    #pidevice.MOV(axes, [a[j][i], a[j + 1][i], a[j + 2][i], a[j + 3][i], a[j + 4][i], a[j + 5][i]])
    time.sleep(RELAXTIME / 1000.)
    if not RELAXTIME:
        pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(pidevice.qPOS())

time.sleep(5)
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
time.sleep(5)

# Close the connections
print("\nClose the connections----------------------------------------------------------------")
pidevice.CloseConnection()
print("Connection closed")