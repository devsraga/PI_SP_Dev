
import initial_setup as ins
from pipython import GCSDevice, datarectools, pitools
import keyboard


# Setting stage with initial things: velocity
ret_back = ins.initial_set(stage_vel=3)
pidevice = ret_back[0]
axes = ret_back[1]
def main():
    key = ''
    while key != 'q':  # for 'q' key:
        key = keyboard.read_key()
        settings(key)

    pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
    pitools.waitontarget(pidevice, axes)
    # Close the connections
    print("\nClose the connections----------------------------------------------------------------")
    pidevice.CloseConnection()
    print("Connection closed")

def move_sp():
    for i in range(1,4):
        pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
        pitools.waitontarget(pidevice, axes)
        pidevice.MOV(axes, [0, 0, 0, 10, 0, 0])
        pitools.waitontarget(pidevice, axes)

def settings(key):
    if key == "s":  # for 's' key
        print("started")
        move_sp()
    elif key == "q":  # for 'q' key
        print("Quit")


if __name__ == '__main__':
    main()