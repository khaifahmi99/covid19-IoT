# Test Portenta - By: khairunnasulfahmi - Sun Nov 1 2020

import image, tf, os

def transfer(trigger, conf):
    time_current = time.localtime()
    time_s = '{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}'.format(time_current[0],time_current[1],time_current[2],time_current[3], time_current[4], time_current[5])

    data = {'data': str(time_s) + ", " + trigger + ", " + str(conf)}
    print(data['data'])

# Load the custom trained tflite model
net = "trained.tflite"
labels = [line.rstrip('\n') for line in open("labels.txt")]

print("starting...")
img = image.Image("test_img.PPM", copy_to_fb=True)

obj = tf.classify(net, img)
predictions_list = list(zip(labels, obj[0].output()))

for i in range(len(predictions_list)):
     print("%s = %f" % (predictions_list[i][0], predictions_list[i][1]))

