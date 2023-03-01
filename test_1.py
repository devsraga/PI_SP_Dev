
# Imported Lib Information................................................................

from pipython import GCSDevice, datarectools, pitools
# try:
#     from matplotlib import pyplot
# except ImportError:
#     pyplot = None
# import time
#
# NUMVALUES = 1024  # number of data sets to record as integer
# RECRATE = 2000  # number of recordings per second, i.e. in Hz



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


# query for servo mode or non servo mode
print("\nQuery for servo mode----------------------------------------------------------------")
print(pidevice.qSVO(axes))                                                   # querry for set close loop or open loop means servo True or False)

# current position
print("\nCurrent Position----------------------------------------------------------------")
curpos = pidevice.qPOS()
print(curpos)


# Setting upper plate velocity
print("\nThe overall velocity has been set----------------------------------------------------------------")
cur_vel = 10.0
pidevice.VLS(cur_vel)
pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(f"The overall velocity of upper plate is {cur_vel} mm/sec and deg/sec ")
print(pidevice.qPOS())


# motion in X Y plane
pidevice.MOV(axes, [0, 0, 0, 10, 0, 0])                                       # max it can go x- 47, y-47

pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(pidevice.qPOS())


# # motion relative to current axis
# pidevice.MVR(axes[3], -5)                                                    # moving relative
# pitools.waitontarget(pidevice, axes)                                         # Wait till motion using PITool
#
#
# # motion relative to current axes
# pidevice.MVR(axes, [5, 5, 5, -10, 5, 5])                                                    # moving relative
# pitools.waitontarget(pidevice, axes)                                         # Wait till motion using PITool

# for axis in pidevice.axes:                                                   # @ not working
#     print('move axis {} forward...'.format(axis))
#     pidevice.OSM(axis, 1000)
#     pidevice.waitonwalk(pidevice, axis)
#     print('move axis {} backward...'.format(axis))
#     pidevice.OSM(axis, -1000)
#     pidevice.waitonwalk(pidevice, axis)
# print('finished')


# pidevice.SVO(axes[0], True)                                                    # set close loop or open loop means servo True or False
#print(pidevice.qFRH())



"""Set velocity-control "on" or "off" for 'axes'.
When velocity-control is "on", the corresponding axes will move with the currently valid
velocity. That velocity can be set with VEL().
@param axes: Axis or list of axes or dictionary {axis : value}.
@param values : Bool or list of bools or None.
"""

# pidevice.VCO(axes, [True, True, True, True, True, True])
#pidevice.VCO(axes[0], True)
# print(pidevice.qVEL(axes[0]))                                          # Get the velocity value commanded with VEL() for 'axes'
# print(pidevice.qCOV())
# pidevice.VEL(axes, [2.0, 2.0, 2.0, 2.0, 2.0, 2.0])




# def DMOV(self, axes, values=None):

""" Move 'axes' to absolute positions.
    This command is very similar to the "MOV" command. During "MOV!"
    command motion, a new target position can be set by a new "MOV!" command.
    When this is done, the new targets will be programmed immediately.
    Motion will change in a smooth manner according to the acceleration
    limitation settings in the C842data.dat configuration file entry. By
    sending "MOV!" commands at periodic intervals, it is possible to avoid
    pauses in motion between moves. Furthermore, the "MOV!" command adjusts
    the velocity so as to reach the target at the end of the interval which
    is set using the "SCT" command.
    @param axes: Axis or list of axes or dictionary {axis : value}.
    @param values : Float or list of floats or None.
    """


# print(pidevice.ACC(axes, [1.0, 1.0, 1.0, 1.0, 1.0, 1.0]))
# print(pidevice.ACC({'X': 1.0, 'Y': 3.0, 'Z': 3.0, 'U': 2.0, 'V': 2.0, 'W': 2.0, }))
# motion in X Y plane
pidevice.MOV(axes, [0, 0, 0, 15, 0, 0])                                       # max it can go x- 47, y-47
print(pidevice.qACC('X'))
pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(pidevice.qPOS())


# get help for data recorder
print(pidevice.qHDR())

# Close the connections
print("\nClose the connections----------------------------------------------------------------")
pidevice.CloseConnection()
print("Connection closed")


# Check reached the target.
# pidevice.qONT()                       #Check if 'axes' have reached the target.


