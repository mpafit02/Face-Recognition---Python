# Face Recognition

## Description

The whoiswho.py script uses the MIT licenced face_recognition library for 64 bit Python 3 to identify a person. It takse as input a folder with pictures for the algorithm to learn and the picture that we search for. The file names in the pictures of the folder should be unique. No two pictures whould have the same name in the same folder. The algorithm will try to identify the person in the picture, in comparisson with the input folder's pictures and return the appropriate message if the folder contains the person or not.

The GitHub Repository of face_recognition library: https://github.com/ageitgey/face_recognition

## Requirments

**Important:** Python has to be version 3 and 64 bit! Use a Windows 10, 64 bit device to run this script.

1. Download Python 3 64 bit from the webiste https://www.python.org/downloads/

2. Doanload pip from the website https://pip.pypa.io/en/stable/installing/

3. To download a C++ compiler, download Visual Studio 2019 Community edition from the link: https://visualstudio.microsoft.com/downloads/?utm_medium=microsoft&utm_source=docs.microsoft.com&utm_campaign=button+cta&utm_content=download+vs2019+rc

a. In the Workloads tab select Desktop development with C++ module in the Windows section.

b. Press Install and after the installation restart your computer.

c. Use the CMD and go to the folder with the whoiswho.py

d. Type the following commands in the folder.

4. Use the following command to download dlib:

python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf

or

pip install dlib

5. Use the following command to download face_recognition

pip install face_recognition

6. Use the following command to download numpy

pip install numpy

7. Use the following command to download opencv-python

pip install opencv-python

Make sure everything had been installed correctly without any errors.

## Run

To run the script you should have a folder with pictures in the folder of the whoiswho.py and a picture (.jpg or .png)
Use the command:

"python whoiswho.py photo1 folder1"

and receive as output "photo1 matched document1 in folder1" if the code matched photo1 to document1 in folder1
or "photo1 not matched in folder1" if the photo1 doesn't match to any picuters in folder1.

## Authors

**@ Authors:** Marios Pafitis, Demetris Shmitras, Valentinos Parizza

**@ Emails:** mpafit02@ucy.ac.cy, dshimi01@ucy.ac.cy, vpariz01@ucy.ac.cy
