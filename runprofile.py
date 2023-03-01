from math import pi, cos, sin
from pipython import GCSDevice, pitools
from pipython.datarectools import getservotime
import initial_setup as ins
import cir as c

# Setting stage with initial things: velocity
ret_back = ins.initial_set(stage_vel=5)
pidevice = ret_back[0]

PERIOD = 5.0  # duration of one sine period in seconds as float
CENTERPOS = (0.0, 0.0)  # center position of the circular motion as float for both axes
AMPLITUDE = (10.0, 10.0)  # amplitude (i.e. diameter) of the circular motion as float for both axes
BUFFERMIN = 200  # minimum number of points in buffer until motion is started



def runprofile(pidevice):
    """Move to start position, set up and run trajectories and wait until they are finished.
    @type pidevice : pipython.gcscommands.GCSCommands
    """
    assert 2 == len(pidevice.axes[:2]), 'this sample requires two connected axes'
    trajectories = (1, 2)
    print('maximum buffer size: {}'.format(pidevice.qSPA(1, 0x22000020)[1][0x22000020]))
    numpoints = pidevice.qSPA(1, 0x22000020)[1][0x22000020]  # maximum buffer size

    xvals = [2 * pi * float(i) / float(numpoints) for i in range(numpoints)]
    xtrajectory = [CENTERPOS[0] + AMPLITUDE[0] / 2.0 * sin(xval) for xval in xvals]
    ytrajectory = [CENTERPOS[1] + AMPLITUDE[1] / 2.0 * cos(xval) for xval in xvals]
    print('move axes {} to their start positions {}'.format(pidevice.axes[:2], (xtrajectory[0], ytrajectory[0])))
    pidevice.MOV(pidevice.axes[:2], (xtrajectory[0], ytrajectory[0]))
    pitools.waitontarget(pidevice, pidevice.axes[:2])
    servotime = getservotime(pidevice)
    tgtvalue = int(float(PERIOD) / float(numpoints) / servotime)
    print('set %d servo cycles per point -> period of %.2f seconds' % (tgtvalue, tgtvalue * servotime * numpoints))
    pidevice.TGT(tgtvalue)
    print('trajectory timing: {}'.format(pidevice.qTGT()))
    print('clear existing trajectories')
    pidevice.TGC(trajectories)
    pointnum = 0
    print('\r%s' % (' ' * 40)),
    while pointnum < numpoints:
        if pidevice.qTGL(1)[1] < BUFFERMIN:
            pidevice.TGA(trajectories, (xtrajectory[pointnum], ytrajectory[pointnum]))
            pointnum += 1
            print('\rappend point {}/{}'.format(pointnum, numpoints)),
        if BUFFERMIN == pointnum:
            print('\nstarting trajectories')
            pidevice.TGS(trajectories)
        if numpoints == pointnum:
            print('\nfinishing trajectories')
            pidevice.TGF(trajectories)
    pitools.waitontrajectory(pidevice, trajectories)
    print('done')
runprofile(pidevice)