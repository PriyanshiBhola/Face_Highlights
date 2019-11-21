import cv2
import os
import matplotlib.pyplot as plt 
from shutil import copyfile

faces_dir = "Tracker/"
vids_dir = "Vids/"
#os.mkdir("user_vids/")
result = 0
flag = 0
flag2 = 0
while True:
	if(os.listdir(faces_dir)):

		# for tracker folder
		for files in os.listdir(faces_dir):
			l_string = files[-23:-4]

		# for videos folder
		vids_labels = []

		for videos in os.listdir(vids_dir):
			v_string = videos[-23:-4]
			vids_labels.append(v_string)

		del vids_labels[1]
		# checking if a video exists by the same name that of the image which user chose

		for j in vids_labels:
			if j == l_string:
				flag = 1
				result = j
				break

		# backtracking begins if above doesn't exists

		# only changing the seconds stamp

		if flag == 0:
			sec = int(l_string[-2:]) 	
			name = l_string[:-2]

			for k in range(sec):	
				sec -= 1
				name_ = name + str(sec)
				for z in range(len(vids_labels)):
					if vids_labels[z] == name_:
						result = name_
						flag2 = 1	
						break	
				

		# changed the minute stamp and now again checking the second stamp

		if flag2 == 0:
			sec = int(l_string[-2:]) 
			name = l_string[:-2]	
			min_ = int(l_string[-5:-3])
			min_ -= 1
			min_ = str(min_) +'-'
			name__ = name[:-3]
			stringy = name__ + str(min_)
			full_string = stringy + str(sec)
			final_string = full_string[:-2]

			for m in range(60-sec):
				sec += 1
				name_ = final_string + str(sec)
				for t in range(len(vids_labels)):
					if vids_labels[t] == name_:
						result = name_
						break

		print(result+'.mov')
		# giving the required video file to the user
		if result:
			result = result + '.mov'

			src = "Vids/"+result
			dst = "Results/"+result
			
			

			copyfile(src, dst)
		os.remove('Tracker/'+files)





