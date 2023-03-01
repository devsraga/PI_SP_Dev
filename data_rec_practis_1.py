import initial_setup as ins
from pipython import GCSDevice, datarectools, pitools
import time
from matplotlib import pyplot
import numpy as np


# 1. Setting stage with initial things: velocity
ret_back = ins.initial_set(stage_vel=5)
pidevice = ret_back[0]
axes = ret_back[1]

# 2. Making a Datarecorder object 'drec'..................
drec = datarectools.Datarecorder(pidevice)

# 3. Setting data recorder rate..................
drec.samplerate = 822                     # servo cycles  Dev: change the sero cycle for increase the duration
# drec.sampletime = 8E-5                  # seconds 1E-4
drec.samplefrequ = 900                    # Hertz

# 4. Moving at home..................
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)

# 5. printing data recorder rate..................
print('data recorder rate: {:d} servo cycles'.format(drec.samplerate))
print('data recorder rate: {:.1g} seconds'.format(drec.sampletime))
print('data recorder rate: {:.2f} Hertz'.format(drec.samplefrequ))

# 6. Selecting options from tools from total kind of data..................
print(datarectools.RecordOptions())
drec.options = (datarectools.RecordOptions.ACTUAL_POSITION_2,
                datarectools.RecordOptions.COMMANDED_POSITION_1)  # pipython.pidevice.gcs2.gcs2datarectools.RecordOptions   <check
print(drec.options)


drec.sources = pidevice.axes[0]
drec.trigsources = datarectools.TriggerSources.POSITION_CHANGING_COMMAND_1
drec.arm()

readout = 'pos_chg_cmd'  # e.g. from an INI file
drec.trigsources = datarectools.gettrigsources(readout)
pidevice.MOV(axes, [5, 0, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)
#header = pidevice.qDRR(rectables, offset, numvalues)
# header = pidevice.qDRR(rectable=[0,1], offset=[0, 1], numvalues=2048)
header = pidevice.qDRR()
print(header)
print(pidevice.bufstate)
while pidevice.bufstate is not True:
    print('read data {:.1f}%...'.format(pidevice.bufstate * 100))
    time.sleep(0.1)
header, data = drec.getdata()
print(header)
print(header['NDATA'])
print(header['NAME0'])
print(header['DISP_UNIT0'])
#timescale = [header['SAMPLE_TIME'] * i for i in range(len(data[0]))]
timescale = [header['NDATA'] * i for i in range(len(data[0]))]
print(timescale)
print(len(data[0]))
print(data)
print(data[0])
print(data[1])


#timescale = range(0, 1024)
pyplot.plot(timescale, data[0], color='red')
pyplot.plot(timescale, data[1], color='blue')
pyplot.xlabel('time (s)')
pyplot.ylabel(', '.join((header['NAME0'], header['NAME1'])))
pyplot.title('Datarecorder data over time')
pyplot.grid(True)
pyplot.show()
header, data = drec.getdata()
npdata = np.array(data)
print(npdata)
print(npdata.ndim)
drec.arm()
drec.wait()
# recording is now finished
header, data = drec.read()


# Close the connections
print("\nClose the connections----------------------------------------------------------------")
pidevice.CloseConnection()
print("Connection closed")
