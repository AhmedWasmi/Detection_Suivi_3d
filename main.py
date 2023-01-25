import cv2
import os

# Define the path to the images and the filename for the video
path = "C:/Users/Ahmed/Desktop/2011_09_26/2011_09_26_drive_0048_sync/image_02/data/"
video_filename = "video.avi"

# Get the list of images in the path
images = [f for f in os.listdir(path) if f.endswith('.png')]

# Sort the images by name
images.sort()
print(images)
# Get the first image to get the shape of the video
img = cv2.imread(os.path.join(path, images[0]))
height, width, layers = img.shape

# Define the codec and create the video writer
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(video_filename, fourcc, 30, (width,height))

# Add each image to the video
for image in images:
    image_path = os.path.join(path, image)
    frame = cv2.imread(image_path)
    video.write(frame)

# Release the video writer
video.release()