import initial_setup as ins
from pipython import GCSDevice, datarectools, pitools
import sys
import signal
import time
import cv2 as cv

# Setting stage with initial things: velocity
ret_back = ins.initial_set(stage_vel=3)
pidevice = ret_back[0]
axes = ret_back[1]


def sigint_handler(signal, frame):
    print("Interrupted")
    pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
    pitools.waitontarget(pidevice, axes)
    sys.exit(0)


while True:  # for 'q' key:
    # Move on Target
    signal.signal(signal.SIGINT, sigint_handler)
    pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
    pitools.waitontarget(pidevice, axes)
    signal.signal(signal.SIGINT, sigint_handler)
    pidevice.MOV(axes, [0, 0, 0, 10, 0, 0])
    pitools.waitontarget(pidevice, axes)
    signal.signal(signal.SIGINT, sigint_handler)
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
pitools.waitontarget(pidevice, axes)
# Close the connections
print("\nClose the connections----------------------------------------------------------------")
pidevice.CloseConnection()
print("Connection closed")


# def hit():
#     try:
#         x = input()
#         print('Try using KeyboardInterrupt')
#     except KeyboardInterrupt:
#         print('KeyboardInterrupt exception is caught')
#         pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
#         pitools.waitontarget(pidevice, axes)
#     else:
#         print('No exceptions are caught')
#
#
#
# while True:  # for 'q' key:
#     # Move on Target
#     hit()
#     pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
#     pitools.waitontarget(pidevice, axes)
#     hit()
#     pidevice.MOV(axes, [0, 0, 0, 10, 0, 0])
#     pitools.waitontarget(pidevice, axes)
#     hit()
# pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
# pitools.waitontarget(pidevice, axes)