
# Imported Lib Information................................................................

from pipython import GCSDevice, datarectools, pitools
import time





# Device info and ref mode..................

pidevice = GCSDevice('C-887')
STAGES = None                                                                   # Not require for C-887
REFMODES = 'FRF'                                                                # reference the connected stages also ['FRF', 'FNL', 'FPL']
print("Device info and ref mode---------------------------------------------------------")
print(f"PI controller {pidevice}")
print(f"Stage(Not require) = 'None', Hexapod = 'H-820.D1', Refmode = 'FRF'")



# Device Setup....................

pidevice.ConnectRS232(comport=1, baudrate=115200)                               # If wanted to connect directly without user setup interface
# pidevice.InterfaceSetupDlg()                                                  # For set up a user interface dialog has shown
print("\nDevice ID number---------------------------------------------------------------")
print('connected: {}'.format(pidevice.qIDN().strip()))                          # For ID number
print(f"         {pidevice.qIDN()}")                                            # For ID number
print("\nVariable details---------------------------------------------------------------")
print(pidevice.qVER())                                                          # Ver



pitch = 0
roll = -25
yaw = 0



# Stage Axes setup ['X', 'Y', 'Z', 'U', 'V', 'W']

print("\nStage axes setup---------------------------------------------------------------")
axes = pidevice.axes
print(f"PI device can move 6 DOF means 6 axis as {axes} ")
print(axes[0], axes)
print(axes)



# Stage Axes Referencing about all axes ['X', 'Y', 'Z', 'U', 'V', 'W']
print('\nInitialize the connected stages....................................................')
print('Referencing..........................................................................')
pitools.startup(pidevice, stages=STAGES, refmodes=REFMODES)                     # For referencing and startup
print(pidevice.qFRF)                                                            # qurry for referencing **
pidevice.qFRF(axes=axes)                                                        # qurry for referencing **




# min and max range of stage
print("\nMinimum and Maximum ranges of the axes------------------------------------------")
rangemin = pidevice.qTMN()
print(f" The minimum range of each axis is:  {rangemin}")
rangemax = pidevice.qTMX()
print(f" The maximum range of each axis is:  {rangemax}")



# current position
print("\nCurrent Position----------------------------------------------------------------")
curpos = pidevice.qPOS()
print(curpos['Z'])
# print(curpos['1'])                                                            # will not work
print(curpos)



# current position with for loop
for axis in pidevice.axes:
    print(axis)
    #print(curpos[axis])
    #print(curpos['X'])

position = pidevice.qPOS(axis)[axis]                                            # query single axis
# position = pidevice.qPOS()[str(axis)]                                         # query all axes
print('current position of axis {} is {:.2f}'.format(axis, position))




# Motion details 'Target'
print("\nMotion details 'Target'----------------------------------------------------------------")
#print(pidevice.gcscommands()) # showing error not callable

print(pidevice.qPOS())    # To see the all axes position
#pidevice.MOV(axes, [0, 0, 0, yaw, pitch, roll])   # To move at an axes
#pidevice.MOV(axes, [0, 0, 0, 15, 0, -20])   # To move at an axes

pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
print(pidevice.qPOS())    # To see the all axes position
# pidevice.MVR('1', 5.0)
#pitools.waitontarget(pidevice, axes)

print(pidevice.qPOS())
#pidevice.GOH  # not working
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [-10, 0, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [10, 0, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 10, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, -10, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 10, 15, 0, -20])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 10, 15, 0, -20])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 0, 15, 0, -20])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 0, -15, 0, -20])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 0, 0, -15, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 0, 0, 15, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 0, 0, 0, -20])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
#pidevice.MOV(axes, [0, 0, 0, 15, 0, 20])   # To move at an axes
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
pitools.waitontarget(pidevice, axes)  # Wait till motion using PITool
print(pidevice.qPOS())
print(pidevice.qSPA())
print(len(pidevice.qSPA()))
dev = pidevice.qSPA()
print(type(dev))
# print(dev([0]))
# print(dev([1]))
# print(dev([2]))



#Closeing the connection .....................................
pidevice.CloseConnection()
