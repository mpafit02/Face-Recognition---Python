import face_recognition as fr
import os
import cv2
import face_recognition
import numpy as np
import sys
from time import sleep


def get_encoded_faces(folder):
    """
    looks through the faces folder and encodes all
    the faces

    :return: a dict of (name, image encoded)
    """
    # Dictionary with the names of the images and the images
    encoded = {}
    # Find all the images in the folder and add them in the dictionary
    for dirpath, dnames, fnames in os.walk("./" + folder):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file(folder + "/" + f)
                encoded[f] = fr.face_encodings(face)[0]
    return encoded


def classify_face(im, folder):
    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    # Get the images and their names
    faces = get_encoded_faces(folder)
    # The images from the folder
    faces_encoded = list(faces.values())
    # The names of the images from the folder
    known_face_names = list(faces.keys())
    # Read the image that we take as inout
    img = cv2.imread(im, 1)
    # Find the face in the image that we toock as input
    face_locations = fr.face_locations(img)
    unknown_face_encodings = fr.face_encodings(img, face_locations)

    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = fr.compare_faces(faces_encoded, face_encoding)
        # use the known face with the smallest distance to the new face
        face_distances = fr.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        # If we matched the image then we return thr appropriate message
        if matches[best_match_index]:
            # Return the filename tha matched the image
            file_name = known_face_names[best_match_index]
            return im + " matched " + file_name + " in " + folder
    # Image not matched
    return im + " not matched in " + folder


def main():
    # Check if the arguments are correct
    if(len(sys.argv) != 3):
        print("Wrong input!")
        sys.exit(0)
    else:
        # Take as input the Image and the Folder and exectue the algorithm
        print(classify_face(sys.argv[1], sys.argv[2]))


if __name__ == '__main__':
    main()
