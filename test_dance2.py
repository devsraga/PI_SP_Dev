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
        # Move on Target
        if keyboard.is_pressed("space"):
            key = "q"
            print("q")
            break
        # move_sp()
        # if keyboard.is_pressed("space"):
        #     key = "q"
        #     print("q")
        #     break
        pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
        if keyboard.is_pressed("space"):
            key = "q"
            print("q")
            break
        pitools.waitontarget(pidevice, axes)
        if keyboard.is_pressed("space"):
            key = "q"
            print("q")
            break
        pidevice.MOV(axes, [0, 0, 0, 10, 0, 0])
        if keyboard.is_pressed("space"):
            key = "q"
            print("q")
            break
        pitools.waitontarget(pidevice, axes)
        if  keyboard.is_pressed("space"):
            key = "q"
            print("q")
            break


    pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
    pitools.waitontarget(pidevice, axes)
    # Close the connections
    print("\nClose the connections----------------------------------------------------------------")
    pidevice.CloseConnection()
    print("Connection closed")

def move_sp():
    pidevice.MOV(axes, [0, 0, 0, 0, 0, 0])
    pitools.waitontarget(pidevice, axes)
    pidevice.MOV(axes, [0, 0, 0, 10, 0, 0])
    pitools.waitontarget(pidevice, axes)

if __name__ == '__main__':
    main()