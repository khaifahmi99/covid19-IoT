'''
Author: Khai Fahmi
Description: Temporal wrapper so that any model can make inference based on timstamp rolling average.
Please change the value of the parameter to suit the model and use case
'''
import sensor, image, time, os, tf, pyb

class TemporalWrapper():

    def __init__(self, net, labels, window_size, name="Topic"):
        self.net = net
        self.labels = labels
        self.window_size = window_size
        self.red_led = pyb.LED(1)
        self.green_led = pyb.LED(2)
        self.blue_led = pyb.LED(3)
        self.clock = time.clock()
        self.name = name

    def predict(self, img, name):
        for obj in tf.classify(self.net, img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
            print("**********\nPredictions () at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
            img.draw_rectangle(obj.rect())

            # This combines the labels and confidence values into a list of tuples
            predictions_list = list(zip(self.labels, obj.output()))

            for i in range(len(predictions_list)):
                print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

                # draw a rectangle and the predicted label on screen
                img.draw_rectangle(obj.rect())
                img.draw_string(obj.x()+3, obj.y()-1, self.labels[obj.output().index(max(obj.output()))], mono_space = False)

    def run(self):
        while(True):
            self.clock.tick()

            img = sensor.snapshot()
            self.predict(img, self.name)

            print(self.clock.fps(), "fps")

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

# Load the custom trained tflite model
net = "trained.tflite"
labels = [line.rstrip('\n') for line in open("labels.txt")]

runner = TemporalWrapper(net, labels, 4)
runner.run()