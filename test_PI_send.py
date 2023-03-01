from pipython import GCSDevice, datarectools, pitools

pidevice = GCSDevice('C-887')
STAGES = None
REFMODES = 'FRF'
pidevice.ConnectRS232(comport=1, baudrate=115200)
axes = pidevice.axes

print('Referencing..........................................................................')
pitools.startup(pidevice, stages=STAGES, refmodes=REFMODES)                     # For referencing and startup
print(pidevice.qFRF)                                                            # qurry for referencing **
pidevice.qFRF(axes=axes)                                                        # qurry for referencing **

print(pidevice.qSVO(axes))
cur_vel = 3.0
pidevice.VLS(cur_vel)
pidevice.ACC(axes, [1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
pidevice.MOV(axes, [0, 0, 0, 0, 0, 10])
pitools.waitontarget(pidevice, axes)
pidevice.CloseConnection()





















