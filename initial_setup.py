# Imported Lib Information................................................................

from pipython import GCSDevice, datarectools, pitools
import time



def initial_set(stage_vel):

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
    cur_vel = stage_vel
    pidevice.VLS(cur_vel)
    pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
    print(f"The overall velocity of upper plate is {cur_vel} mm/sec and deg/sec ")
    print(pidevice.qPOS())
    return pidevice, axes
