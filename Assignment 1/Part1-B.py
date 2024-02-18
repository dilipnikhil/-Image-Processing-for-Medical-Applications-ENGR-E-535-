# Load opencv module
import cv2
import numpy as np
from scipy import misc
from scipy.ndimage import gaussian_filter
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
import time

# Check if camera opened successfully
if (cap.isOpened() is False):
    print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

prev_frame = None

while(True):
    ret, current_frame = cap.read()
    if ret:
        def gray(frame): # helper function to extract RGB and convert to gray scale
            red = frame[..., 0] # data[:, :, 0]
            green = frame[..., 1]
            blue = frame[..., 2]
            frame_gray = 0.21 * red + 0.72 * green + 0.07 * blue #numbers based on visual science
            return frame_gray
        
        gray_current_frame = gray(current_frame)

        if prev_frame is not None:

            abs_diff_frame = np.abs(gray_current_frame - prev_frame) 
            abs_diff_frame_threshold= np.where(abs_diff_frame>20,255,0).astype(np.uint8) # convert any values greater than 20 to 255, if not 0.
            cv2.imshow("frame",abs_diff_frame_threshold)

            finger_frame = abs_diff_frame_threshold.copy() # copy the threshold frame

            # Resize the image using scipy.misc.imresize
            resized_image = cv2.resize(finger_frame, (64, 64), interpolation=cv2.INTER_AREA) # resize the frame to 64 by 64 to decrease computational times
            result = gaussian_filter(resized_image, sigma=0.6) # apply guassuan filter so that we get smooth edges

            result = np.where(result > 0, 255, 0).astype(np.uint8)# any pixel value greater than 0 is converted to 255 so that we have clear boundaries

            for row_index, row in enumerate(result): # iterate through the row of the image array
                
                # Check if any value in the row is greater than > 0
                
                if any(value > 0 for value in row): 
                    index_split = row_index # find the row where we first see a white pixel so that we can localize the top of any finger
                    break
            try:
                split_index = index_split + 20

                """ 
                split the image from that row to 20 rows below and get that 
                row so that we can count the number of times the pattern of black and white pixel sequence appears in that row
                  """
                split_image = result[split_index-1].tolist()  

            except Exception as ex:
                pass
            count = 0  # initialize count to zero
            try:
                for i in range(len(split_image)): # iterate over the row to find the count of that pattern
                    if split_image[i] < 1:
                        continue
                    if split_image[i] > 0 :
                        pass
                        if split_image[i+1] < 1 :
                            count = count + 1
                        else:
                            continue
                if count < 6:
                    print(count) # print that count indicating the number of fingers
            except Exception as ex:
                pass
        prev_frame = gray_current_frame
        # Press Q on keyboard to stop recording
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done,
# release the video capture and write objects
cap.release()

# Closes all the frames
cv2.destroyAllWindows()
