import cv2 #pip install opencv-python

#Configurable Parameters
source = "krishna.jpg"
destination = "ResizedImage.jpg"
scale_percent = 50 #Percent by which the image is resized #use alt+shift to take/move a line upward

src = cv2.imread(source, cv2.IMREAD_UNCHANGED) #loads the image from the specified source file # The cv2.IMREAD_UNCHANGED flag ensures the image is loaded with all its original channels, including any alpha transparency channel.
#cv2.imshow("title", src) #displays the original image in a window with the title "title"

#Calculating the 50 percent of original dimensions
new_width = int(src.shape[1] * scale_percent / 100) #20*200/100 #shape is a numpy array function which gives you height by width #calculating new width by multiplying the original dimensions by the scale_percent i.e. 50
new_height = int(src.shape[0] * scale_percent / 100) #calculating new height by multiplying the original dimensions by the scale_percent i.e. 50

#Resize image
output = cv2.resize(src, (new_width, new_height)) #made a tuple (,) and putted it in output #resize takes a tuple(nw,nh) with src #performs the actual resizing. It takes the source image and the new dimensions as arguments and returns the resized image

cv2.imwrite(destination, output) #saves the output to the file specified by destination
#cv2.waitKey(0) #this line keeps the display window open until the user presses a key