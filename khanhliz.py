# Import the libraries
import cv2
import time

# Create a video capture object
video = cv2.VideoCapture(0)

# Define a counter for the image name
count = 0

# Start an infinite loop
while True:
    # Read a frame from the video
    ret, frame = video.read()

    # Check if the frame is valid
    if ret:
        # Increment the counter
        count += 1

        # Generate an image name with the counter
        image_name = "image_" + str(count) + ".jpg"

        # Save the frame as an image file
        cv2.imwrite(image_name, frame)

        # Print a message
        print("Saved " + image_name)

        # Wait for 15 seconds
        time.sleep(15)

    # Check if the user pressed Esc key
    if cv2.waitKey(1) == 27:
        # Break the loop
        break

# Release the video object
video.release()

# Close all windows
cv2.destroyAllWindows()