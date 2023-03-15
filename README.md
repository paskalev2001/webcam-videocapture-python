# Python Webcam videocapture software 

## Installation

Install the required modules:
```
pip3 install -r requirements.txt
```

## Run the application

```
python3 main.py
```

## Using the application

#### The application has the following inputs:

1. Video Source - The default is 0 which usually should work just fine. If you have multiple cameras you could increment the number to see which number corresponds to their interface.

2. File Name - This is the filename that will be recorded when you click "Start Recording"

3. Width & Height - This is the output resolution of the recording.

#### Controls:

1. Start Recording - Initiates the recording.

2. Test Camera - Run a videostream withouts recording it to a file.

3. Exit - Closes the application.