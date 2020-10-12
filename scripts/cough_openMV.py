# Edge Impulse - OpenMV Image Classification Example

import sensor, image, time, os, tf, pyb

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.GRAYSCALE)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

red_led = pyb.LED(1)
green_led = pyb.LED(2)
blue_led = pyb.LED(3)

# Load the built-in person detection network (the network is in your OpenMV Cam's firmware).
person_net = tf.load('person_detection')
person_labels = ['unsure', 'person', 'no_person']

net = "trained.tflite"
labels = [line.rstrip('\n') for line in open("labels.txt")]

def predict_cough(img):
    # default settings just do one detection... change them to search the image...
    for obj in tf.classify(net, img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions Cough at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        # This combines the labels and confidence values into a list of tuples
        predictions_list = list(zip(labels, obj.output()))

        for i in range(len(predictions_list)):
            print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))
            img.draw_rectangle(obj.rect())
            img.draw_string(obj.x()+3, obj.y()-1, labels[obj.output().index(max(obj.output()))], mono_space = False)


clock = time.clock()
while(True):
    clock.tick()

    img = sensor.snapshot()

    # default settings just do one detection... change them to search the image...
    for obj in tf.classify(person_net, img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        # print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        # This combines the labels and confidence values into a list of tuples
        predictions_list = list(zip(person_labels, obj.output()))

        for i in range(len(predictions_list)):
            # print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

            if predictions_list[1][1] > 0.80:
                # person exists
                blue_led.off()
                predict_cough(img)
            else:
                # person not exist
                blue_led.on()

    print(clock.fps(), "fps")
