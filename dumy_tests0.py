import pyzed.sl as sl
import require as drq

def main():
	print("dev")
	# pidevice.VLS(cur_vel)
	dev_zed = sl.Camera()

	# setting initial camera parameters
	init_params = drq.devcam_init_set()





if __name__ == '__main__':
	main()
