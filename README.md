# Ibot
Simple project for detecting the basic motion of pupil in an image received from flask based server and send the motion detected.

## Getting Started
Download zip file and extract it in a new folder.

### Prerequisites
Install packages mentioned in requirements.txt and openface.

### Installing
In the project folder
```
Install packages using pip install -r requirements.txt
```
```
Install openface from https://cmusatyalab.github.io/openface/setup/
```

## Running the tests
To check if everything is running alright use mai_test.py
```
python mai_test.py
```
To run the project run main file 
```
python main.py
```

### For training from your own data 

Use scripts in data_making for converting images into proper .csv format and name data as 'inl1.csv' for left and 'ir1.csv' for right eye and output as 'out.csv'.
```
Use python crop.py to get eyes data
```
```
Use python resi.py to resize it.
```
```
Use data_making to make training data and labels for randomforest.
```
face_landmarks.py can be used for estimation of performance on different devices.
```
For training do python ranfor.py
```

## Deployment
To detect motion of pupil either use mai_test.py or send data to flask server and get movement data.

## Authors
* **Bharat Kumar** - ratcoder(https://github.com/ratcoder)

