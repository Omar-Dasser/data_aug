from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import os 

aug = ImageDataGenerator(
	rotation_range=3.5,
	zoom_range=0.15,
	width_shift_range=0.039,
	height_shift_range=0.039,
	shear_range=0.15,
	horizontal_flip=False,
	fill_mode="nearest")
print("[INFO] loading example image...")
alles = 3  #or 4 

pos_ori_dir = os.path.join(os.getcwd(),'Unsecured')

out_dir = os.path.join(os.getcwd(),'generated_Unsecured')


for img in os.listdir(pos_ori_dir):

	print(img)
	image = load_img(os.path.join(pos_ori_dir,img))
	image = img_to_array(image)
	image = np.expand_dims(image, axis=0)

	total = 0

	

	print("[INFO] generating images...")
	imageGen = aug.flow(image, batch_size=1, save_to_dir=out_dir,
		save_prefix="image", save_format="jpg")

	
	for image in imageGen:

		total += 1

		if total == alles:
			break