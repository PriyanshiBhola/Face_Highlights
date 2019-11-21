import numpy as np
import cv2
import time
import face_recognition
import datetime
import os 
font = cv2.FONT_HERSHEY_SIMPLEX

#Open Camera
cap = cv2.VideoCapture(0)

#For writing video
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

while True:
	ret , frame = cap.read()
	if ret == True:

		#date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
		small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)#Just for faster processing
		rgb_small_frame = small_frame[:, :, ::-1]#Converting frame from BGR to RGB [OpenCV:Uses BGR & face_recognition:Uses RGB]
		loc = face_recognition.face_locations(rgb_small_frame)#Finding faces
		
		
		
		

		if loc:
			encode = face_recognition.face_encodings(rgb_small_frame , loc)[0]
			for (top, right, bottom, left) in loc:
			# Scale back up face locations since the frame we detected in was scaled to 1/4 size
				top *= 4
				right *= 4
				bottom *= 4
				left *= 4
				cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
				area = frame[top:bottom , left:right]

			start = time.time()
			duration = 60
			date_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
			d1 = datetime.datetime.now().strftime('%d_%m_%y')
			d2 = datetime.datetime.now().strftime('%H-%M-%S')

			cv2.putText(frame , d1 , (left+5,top+15) , font , 0.5 , (255,0,0) , 1 , cv2.LINE_AA)
			cv2.putText(frame , d2 , (left+90,top+15) , font , 0.5 , (255,0,0) , 1 , cv2.LINE_AA)

			cv2.imwrite("Faces/"+date_time+".jpg", area)
			#os.system("gdrive upload --parent 1Qw2a2YCD9Raf9oMUFPxEtDjwjwNx9OtI Faces/"+date_time+".jpg")
			out = cv2.VideoWriter("Vids/"+date_time+".mov",fourcc, 20.0, (1280,720))


			while(int(time.time() - start) < duration):
				ret, frame = cap.read()
				out.write(frame)
				small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
				rgb_small_frame = small_frame[:, :, ::-1]#Converting frame from BGR to RGB [OpenCV:Uses BGR & face_recognition:Uses RGB]
				loc1 = face_recognition.face_locations(rgb_small_frame)#Finding faces
				if loc1:

					encode1 = face_recognition.face_encodings(rgb_small_frame, loc1)[0]
				

					for (top, right, bottom, left) in loc1:
					# Scale back up face locations since the frame we detected in was scaled to 1/4 size
						top *= 4
						right *= 4
						bottom *= 4
						left *= 4
						cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
						area1 = frame[top:bottom , left:right]

					
					d1 = datetime.datetime.now().strftime('%d_%m_%y')
					d2 = datetime.datetime.now().strftime('%H-%M-%S')

					cv2.putText(frame , d1 , (left+5,top+15) , font , 0.5 , (255,0,0) , 1 , cv2.LINE_AA)
					cv2.putText(frame , d2 , (left+90,top+15) , font , 0.5 , (255,0,0) , 1 , cv2.LINE_AA)

					result = face_recognition.compare_faces([encode],encode1)
					if(result[0] == True):
						encode = encode
						
					else:
						

						d_t = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
						cv2.imwrite("Faces/"+d_t+".jpg" , area1)
						#os.system("gdrive upload --parent 1Qw2a2YCD9Raf9oMUFPxEtDjwjwNx9OtI Faces/"+d_t+".jpg")
						encode = encode1
						



				
				
				
				cv2.imshow('frame',frame)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					exit()



		cv2.imshow('frame',frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			exit()

cap.release()
out.release()
cv2.destroyAllWindows()





