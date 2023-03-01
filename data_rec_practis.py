from pipython import GCSDevice, datarectools, pitools
import time
import matplotlib
from matplotlib import pyplot
import numpy as np
axes = ['X', 'Y', 'Z', 'U', 'V', 'W']

pidevice = GCSDevice()




#pidevice.InterfaceSetupDlg()
pidevice.ConnectRS232(comport=1, baudrate=115200)                               # If wanted to connect directly without user setup interface
...
drec = datarectools.Datarecorder(pidevice)
drec.samplerate = 1  # servo cycles
drec.sampletime = 1E-4  # seconds
drec.samplefrequ = 6000  # Hertz
pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)
# Setting upper plate velocity
print("\nThe overall velocity has been set----------------------------------------------------------------")
cur_vel = 10.0
pidevice.VLS(cur_vel)
pitools.waitontarget(pidevice, axes)                                            # Wait till motion using PITool
print(f"The overall velocity of upper plate is {cur_vel} mm/sec and deg/sec ")
print(pidevice.qPOS())

print('data recorder rate: {:d} servo cycles'.format(drec.samplerate))
print('data recorder rate: {:.1g} seconds'.format(drec.sampletime))
print('data recorder rate: {:.2f} Hertz'.format(drec.samplefrequ))

drec.options = (datarectools.RecordOptions.ACTUAL_POSITION_2,
                datarectools.RecordOptions.COMMANDED_POSITION_1)
drec.sources = pidevice.axes[0]
drec.trigsources = datarectools.TriggerSources.POSITION_CHANGING_COMMAND_1
drec.arm()

readout = 'pos_chg_cmd'  # e.g. from an INI file
drec.trigsources = datarectools.gettrigsources(readout)
pidevice.MOV(axes, [-15, 0, 0, 0, 0, 0])   # To move at an axes
pitools.waitontarget(pidevice, axes)
#header = pidevice.qDRR(rectables, offset, numvalues)
header = pidevice.qDRR()
print(header)
while pidevice.bufstate is not True:
    print('read data {:.1f}%...'.format(pidevice.bufstate * 100))
    time.sleep(0.1)
header, data = drec.getdata()
# timescale = [header['SAMPLE_TIME'] * i for i in range(len(data[0]))]
print(len(data[0]))


timescale = range(0, 1024)
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
drec.arm()
drec.wait()
# recording is now finished
header, data = drec.read()


# Close the connections
print("\nClose the connections----------------------------------------------------------------")
pidevice.CloseConnection()
print("Connection closed")
