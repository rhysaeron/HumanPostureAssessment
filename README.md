# HumanPostureAssessment
This repository contains a CNN system which analyses human posture. This simply detects whether the user has good or bad posture, from a perpendicular angle of where the user is facing.

This does not contain the datasets required to train the model, but includes the model to use, which has already been trained. The files which will be downloaded are:

HumanPostureAssessment.h5
This is the model that will be loaded into the pythons script to run the experiment.
video_test.py
This is the python script required to run the model, using the built in laptop camera to steam a live experiment.

The environment that this will be run out of is spyder, which is built into Anaconda Navigator. Anaconda allows the python libraries to be stored and used within Spyder IDE. 

To install Anaconda Navigator: https://anaconda.org/anaconda/anaconda-navigator 

Within Anaconda, create a new environment for this experiment, for example: ‘Human Posture’. This will require three libraries to be installed:

Tensorflow
Keras
Pandas 

Other libraries may be required to be updated or downloaded when running the project. Download where necessary.

Spyder will not be installed into this Anaconda Environment, so download this from ‘Home’ within Anaconda.

Now the project is ready to be opened. When the files required have been downloaded from GitHub, save them in a folder somewhere on your laptop/PC (requires a webcam). Open the python script in Spyder and run. This will open up a live video linked to the webcam. This is ready to go! 

The good/bad classification will be displayed on the top left of the screen.


