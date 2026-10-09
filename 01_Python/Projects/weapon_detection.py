import numpy as np
import cv2
import imutils
import datetime

gun_casde = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

