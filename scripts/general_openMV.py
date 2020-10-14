'''
Author: Khai Fahmi
Description: General Script to run the custom model, printing the prediction and FPS in the console,
writing the predicted label on openMV camera view
'''

import sensor, image, time, os, tf, pyb

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

# initialise the LED on openMV board
red_led = pyb.LED(1)
green_led = pyb.LED(2)
blue_led = pyb.LED(3)

# Load the custom trained tflite model
net = "trained.tflite"
labels = [line.rstrip('\n') for line in open("labels.txt")]

clock = time.clock()
while(True):
    clock.tick()

    img = sensor.snapshot()

    # default settings just do one detection... change them to search the image...
    for obj in tf.classify(net, img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions Cough at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        predictions_list = list(zip(labels, obj.output()))

        for i in range(len(predictions_list)):
            print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

            # draw a rectangle and the predicted label on screen
            img.draw_rectangle(obj.rect())
            img.draw_string(obj.x()+3, obj.y()-1, labels[obj.output().index(max(obj.output()))], mono_space = False)

    print(clock.fps(), "fps")
