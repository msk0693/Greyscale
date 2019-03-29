import numpy as np
import cv2
import tkinter as TK
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

root = TK.Tk()
root.withdraw()
messagebox.showinfo(" ", "Select an image to turn it greyscale. ")
root.withdraw()

#open image file
filename = askopenfilename()
img = cv2.imread(filename, 0)

#show image in grey
cv2.imshow('ImageWindow', img)

#save options
cv2.moveWindow("ImageWindow", 100, 100)
result = messagebox.askyesno(" ","Would you like to save the data?")
if result :
	cv2.imwrite("my_image_grey.png",img)
	messagebox.showinfo(" ", "Image Saved. Enter any key to exit.")
else:
	messagebox.showinfo(" ", "Enter any key to exit.")

#quit with 0 key
cv2.waitKey(0)
