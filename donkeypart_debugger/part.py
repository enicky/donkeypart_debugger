class DonkeypartDebugger:
    def __init__(self):
        print("init debugger")

    def run_threaded(self, image_array=None, steering=0, throttle=0, recording=False):
        if image_array is not None:
            print("Sizeof ImageArryay : " + len(image_array))
        else:
            print("Imagearray None")
        print("Steering : " + str(steering))
        print("Throttle : " + str(throttle))
        print("Recording: " + str(recording))
        return image_array, steering, throttle, recording


if __name__ == "__main__":
    p = DonkeypartDebugger()
    p.run_threaded()
