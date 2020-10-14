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

## Datasets

1. Flu Like Symptoms BIISC (source: https://web.bii.a-star.edu.sg/~chengli/FluRecognition.htm)
2. Cough Sound (source: https://github.com/hernanmd/COVID-19-train-audio/tree/master/not-covid19-coughs)
3. Urban Sound 8K (source: https://www.kaggle.com/chrisfilo/urbansound8k)
