from statistics import mode
from spot import *
import cv2
from keras.models import load_model
import time
import numpy as np
import matplotlib.pyplot as plt
import random

from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input

# parameters for loading data and images
detection_model_path = '../trained_models/detection_models/haarcascade_frontalface_default.xml'
emotion_model_path = '../trained_models/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5'
emotion_labels = get_labels('fer2013')

# hyper-parameters for bounding boxes shape
frame_window = 10
emotion_offsets = (20, 40)

# loading models
face_detection = load_detection_model(detection_model_path)
emotion_classifier = load_model(emotion_model_path, compile=False)

def r8k9(fileName='dog.jpg',score=10,length=10):
	# getting input model shapes for inference
	emotion_target_size = emotion_classifier.input_shape[1:3]

	# starting lists for calculating modes
	emotion_window = []

	# starting video streaming
	cv2.namedWindow('window_frame')
	video_capture = cv2.VideoCapture(0)

	im = cv2.imread(fileName)
	im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)
	countdown = ["Ready?","3","2","1"]
	#plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
	#for i in range(4):
	#	print(countdown[i])
	#	time.sleep(1)
	#print("GO")
	#plt.show(block=False)
	t      = time.time()
	td     = []
	while time.time() < t + length:
	    bgr_image = video_capture.read()[1]
	    try:
	    	gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
	    except:
	    	time.sleep(.5)
	    	gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
	    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
	    faces = detect_faces(face_detection, gray_image)

	    for face_coordinates in faces:

	        x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
	        gray_face = gray_image[y1:y2, x1:x2]
	        try:
	            gray_face = cv2.resize(gray_face, (emotion_target_size))
	        except:
	            continue

	        gray_face = preprocess_input(gray_face, True)
	        gray_face = np.expand_dims(gray_face, 0)
	        gray_face = np.expand_dims(gray_face, -1)
	        emotion_prediction = emotion_classifier.predict(gray_face)
	        #print(emotion_prediction)
	        if len(td) == 0:
	        	data = emotion_prediction
	        	td   = [time.time() - t]
	        else:
		        data = np.concatenate((data,emotion_prediction), axis = 0)
		        td   = td + [time.time() - t]

	        emotion_probability = np.max(emotion_prediction)
	        emotion_label_arg = np.argmax(emotion_prediction)
	        emotion_text = emotion_labels[emotion_label_arg]
	        emotion_window.append(emotion_text)

	        if len(emotion_window) > frame_window:
	            emotion_window.pop(0)
	        try:
	            emotion_mode = mode(emotion_window)
	        except:
	            continue

	        if emotion_text == 'angry':
	            color = emotion_probability * np.asarray((255, 0, 0))
	        elif emotion_text == 'sad':
	            color = emotion_probability * np.asarray((0, 0, 255))
	        elif emotion_text == 'happy':
	            color = emotion_probability * np.asarray((255, 255, 0))
	        elif emotion_text == 'surprise':
	            color = emotion_probability * np.asarray((0, 255, 255))
	        else:
	            color = emotion_probability * np.asarray((0, 255, 0))

	        color = color.astype(int)
	        color = color.tolist()

	        draw_bounding_box(face_coordinates, rgb_image, color)
	        draw_text(face_coordinates, rgb_image, emotion_mode,
	                  color, 0, -45, 1, 1)

	    bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
	    cv2.imshow('window_frame', bgr_image)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	#print(np.transpose(data))
	#print(emotion_labels)
	plt.clf()
	plt.plot(td,data)
	
	plt.legend(['angry', 'disgust', 'fear','happy','sad','surprise','neutral'], loc = 2)
	plt.savefig('Graph.png')
	#splt.show()
	totals = [0,0,0,0,0,0,0]
	for j in range(7):
		for i in range(1,len(td)):
			#print(time[i-1])
			#print(data[i-1+l*(j+1)])
			#print(time[i],time[i-1])
			totals[j] += (data[i][j] + data[i-1][j])/2*(td[i]-td[i-1])/(td[-1]-td[0])
	np.append(totals,np.std(data))
	print(totals)
	#print(td[-1] - td[0])
	#print(sum(totals))
	#f = open("DogData.txt","a+")
	#f.write((str(score) + ' ' + ' '.join(str(t) for t in totals) + "\n"))
	print("Rating:", 15-spot(np.array(totals))/10,"/10")
	return (15-spot(np.array(totals))/10)

def gatherData():
	dogs = [["WoofYou.jpg",42], #42k
		["Yawn.jpg",28],    #28k
		["Daisy.jpg",48],   #48k
		["Snow.jpg",59],    #59k
		["TootToot.jpg",36],#36k
		["Orange.jpg",10], 
		["Apple.jpg",10],
		["Pear.jpg",10],
		["Grapes.jpg",10],
		["Tomatoe.jpg",10]]
	print(dogs)
	np.random.shuffle(dogs)
	print(dogs)
	for dog in dogs:
		r8k9(dog[0],dog[1])

if __name__ == '__main__':
	#gatherData()
	r8k9("dog.jpg")
	print(spot(np.array([0.12199731211317869, 6.80409156135084e-05, 0.09506887585027701, 0.24940838665531148, 0.12121258319468693, 0.04203010739639894, 0.37021472131102023])))
	print(spot(np.array([0.12933559562628646, 0.000431463081843903, 0.06281908189197115, 0.12297435607783164, 0.09106757738233524, 0.03209377200810974, 0.5612781585677399])))

