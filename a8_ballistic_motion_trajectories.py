import numpy as np
import matplotlib.pyplot as plt
import cv2
from IPython.display import clear_output
from time import sleep

def examine_frames(rows=5, cols=5):

	# Set up faceted plot with appropriate size (arbitrary)
	fig = plt.figure(figsize=(25, 25))

	for n in range(1, 26):
	    fig.add_subplot(rows, cols, n)
	    
	    # Access each frame pic in the 'frames' folder
	    image = cv2.imread('frames/frame' + str(n) + '.png')
	    image_circle = image.copy()
	    
	    # Get circle center
	    circle_center = (int(df[n-1][0]),int(df[n-1][1]))
	    radius = 40
	    
	    # Create circle drawing on top of frame
	    cv2.circle(image_circle, circle_center, radius, (255, 0, 0), thickness=3, lineType=cv2.LINE_AA)
	    plt.imshow(image_circle)
	    plt.axis('off')
	    plt.title(str(n))

	return None

def fit_parabola():
	# Create empty x and y coordinate lists
	x = []
	y = []

	# Add each X and Y coordinate from the coords array into the separate lists
	for i in range(0, 25):
	    x.append(df[i][0])
	    y.append(df[i][1])

	# Create X matrix from x data points
	X = np.stack((np.square(x), x, np.ones(25)), axis=1)
	# Create U vector using least squares equaltion (x_transpose*x)inv*x_transpose*y
	u = np.linalg.inv(np.transpose(X)@X)@np.transpose(X)@y

	# Set up plot 
	x_parab = np.array(x)
	y_parab = u[0]*x_parab**2 + u[1]*x_parab + u[2]
	plt.figure(figsize=(20,20))

	# Plot points in red as dotws 
	plt.plot(x,y,'ro')

	# Plot parabola as line in blue 
	plt.plot(x_parab, y_parab, 'b' )

	# Flip image horizontally so it matches a real life ball trajectory
	plt.gca().invert_yaxis()
	plt.show()

	return None