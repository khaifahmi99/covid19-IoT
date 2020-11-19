# IoT Implementation for Covid-19

## Projects Planned

1. Cough Detection (Khai)
2. Fall Detection (Hananta)
3. Long Distance Elderly Support (Hananta)
3. Gloves Detection (Andres)
4. Security on Edge Device (Sam)
5. Temperature Detection (Vassu)

## Package included

1. OpenMV Real-time Image Classification (TF Lite Model)
2. Raspberry Pi Configuration (CPU Extensive Model)
3. Web Application for Data Visualisation
4. Web Application for Model Inference Endpoint
5. Cloud Database
6. Extended Security on Edge Device

## Stacks used

1. Heroku/AWS EC2/Sagemaker (ML Endpoint)
2. Flask App/React App (Visualisation)
3. Heroku/Firebase/EC2 (Deployment)
4. OpenMV
5. TF Lite
6. Edge Impulse
7. Raspberry Pi
8. Keras/Tensorflow
9. AWS DynamoDB

## Models

| Name | Version | Testing Accuracy | Dataset | Architecture | Status (on OpenMV H7) |
| --- | --- | --- | --- | --- | --- |
| cough_image | v1 | 78% | 10000 96x96 images | transfer learning MobileNetV2 0.35 | Insufficient RAM |
| cough_image | v2 | 66% | 10000 96x96 images | transfer learning MobileNetV2 0.1 | Insufficient RAM |
| cough_image | v3 | 74% | 10000 96x96 images | 32-16Conv2D -> NN Dense(10) | Insufficient RAM |
| cough_image | v4 | 69% | 10000 64x64 images | 16-16Conv2D -> NN Dense(10) | Works |
| cough_image_short_distance | v1 | 90% | 200 64x64 images | 16-16Conv2D -> Dense(10) | Works |
| cough_sound | v1 | 96% | 10 mins wav files | Conv1D without Data Augmentation | Not supported |
| cough_sound | v2 | 95% | 10 mins wav files | Conv1D with Data Augmentation | Not supported |
| glove_detection| v0 | 93% | 147 64x64 images | 32-16Conv2D -> NN Dense(10) | Insufficient RAM |
| glove_detection| v1 | 100% | 147 64x64 images | 32-16Conv2D -> NN Dense(10) | Works |
| glove_detection| v2 | 85% | 147 48x48 images | 32-16Conv2D -> NN Dense(10) | Works |
| glove_detection| v4 | 100% | 18000 48x48 images | 32-16Conv2D -> NN Dense(20) | Works |
| glove_detection| v5 | 100% | 18000 48x48 images | Transfer Learning(8) MobileNetV2 0.05  | Works |
| fall_detection | v1 | 88% | 300 64x64 images | 16-16Conv2D | Works |

## Datasets

1. Flu Like Symptoms BIISC (source: https://web.bii.a-star.edu.sg/~chengli/FluRecognition.htm)
2. Cough Sound (source: https://github.com/hernanmd/COVID-19-train-audio/tree/master/not-covid19-coughs)
3. Urban Sound 8K (source: https://www.kaggle.com/chrisfilo/urbansound8k)
4. Fall Dataset (source: http://falldataset.com)
5. Hand Dataset 11K (source: https://sites.google.com/view/11khands)
6. No Hand Dataset 7K (source: https://www1.cs.columbia.edu/CAVE/software/softlib/coil-100.php)

## Run Node App Locally

1. Make sure npm and nodejs is installed
2. Run `cd nodeApp`
3. Install all dependencies `npm install`
3. Run application `npm run start`
4. The application should open automatically, if it does not, paste `http://localhost:8080/` in your browser

## Run WebAssembly App Locally

Models can be deployed as a WebAssembly library. This allows us to run our model locally, without any compilation. These are the instructions to achieve it.
1. Open the file code_examples_wasm.txt and “Copy” any of the 10 examples there are.
2. Open a terminal or command prompt in the folder WebAssembly\gloves_detection_v6-wasm-v1 and “paste” the code.
3. This will run the signal processing pipeline, and then classify the output (example):
{
  anomaly: 0,
  results: [
    { label: 'gloves', value: 0.05859375 },
    { label: 'no_gloves', value: 0.9375 },
    { label: 'no_hand', value: 0.0078125 }
  ]
}
Which matches the values we just saw in the edgeimpulse studio. We now have our model running locally!

## Run Models RaspberryPI

These models were tested in an environment with OpenCV 4.4.0, Python 3.7.3, protobuf 3.5.1, numpy 1.19.4 and the mobilenet_v1_1.0_224_quant.tflite model as the basis for tensorflow lite.
Using Picamera.
To test any model; you just have to change the labels.txt and trained.tflite files for each model.
1. Go to / examples / lite / examples / image_classification / raspberry_pi
2. Put the next code:
   python3 classify_picamera.py --model trained.tflite --labels labels.txt
