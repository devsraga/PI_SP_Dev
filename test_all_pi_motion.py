from pipython import GCSDevice, pitools
from collections import OrderedDict

CONTROLLERNAME = 'E-887'  # 'C-884' will also work
STAGES = None
REFMODES = ['FRF', 'FRF']
pidevice = GCSDevice('C-887')
pidevice.InterfaceSetupDlg()
print(pidevice.qIDN())
print(pidevice.qPOS())
# Choose the interface which is appropriate to your cabling.

# pidevice.ConnectTCPIP(ipaddress='192.168.178.42')
# pidevice.ConnectUSB(serialnum='104237344')
# pidevice.ConnectRS232(comport=1, baudrate=115200)

# Each PI controller supports the qIDN() command which returns an
# identification string with a trailing line feed character which
# we "strip" away.

print('connected: {}'.format(pidevice.qIDN().strip()))

# Show the version info which is helpful for PI support when there
# are any issues.

if pidevice.HasqVER():
    print('version info: {}'.format(pidevice.qVER().strip()))

print('done - you may now continue with the simplemove.py example...')


# pidevice.MOV([1, 2, 3, 4, 5, 6], [0, 0, 0, 0, 0, 0])
# pidevice.MOV(['X', 'Y'], [0, 0])
def readparametervalue(device, memtype, cont_unit, func_unit, parameter_id):
    return device.qSPV(memtype, cont_unit, func_unit, parameter_id)[memtype][cont_unit][func_unit][parameter_id]


def getminpos(device):
    minpos = OrderedDict()
    for axis in device.axes:
        minpos[axis] = readparametervalue(device, "RAM", axis, "-", "0x1 21")
    return minpos



def getmaxpos(device):
    maxpos = OrderedDict()
    for axis in device.axes:
        maxpos[axis] = readparametervalue(device, "RAM", axis, "-", "0x122")
    return maxpos


print('initialize connected stages...')
pitools.startup(pidevice, stages=STAGES, refmodes=REFMODES)


# min and max range of stage
print("\nMinimum and Maximum ranges of the axes------------------------------------------")
rangemin = pidevice.qTMN()
print(f" The minimum range of each axis is:  {rangemin}")
rangemax = pidevice.qTMX()
print(f" The maximum range of each axis is:  {rangemax}")
curpos = pidevice.qPOS()
print(curpos)


# Setting upper plate velocity
print("\nThe overall velocity has been set----------------------------------------------------------------")
cur_vel = 15.0
pidevice.VLS(cur_vel)
pitools.waitontarget(pidevice, pidevice.axes)                                            # Wait till motion using PITool
print(f"The overall velocity of upper plate is {cur_vel} mm/sec and deg/sec ")
print(pidevice.qPOS())

for axis in pidevice.axes:
    for target in (rangemin[axis], rangemax[axis], curpos[axis]):
        print('move axis {} to {:.2f}'.format(axis, target))
        pidevice.MOV(axis, target)


        # To check the "on target state" of an axis there is the GCS command
        # qONT(). But it is more convenient to just call "waitontarget".

        pitools.waitontarget(pidevice, axes=axis)

        # GCS commands usually can be called with single arguments, with
        # lists as arguments or with a dictionary.
        # If a query command is called with an argument the keys in the
        # returned dictionary resemble the arguments. If it is called
        # without an argument the keys are always strings.

        position = pidevice.qPOS(axis)[axis]  # query single axis
        print('current position of axis {} is {:.2f}'.format(axis, position))

print('done')
pidevice.CloseConnection()
