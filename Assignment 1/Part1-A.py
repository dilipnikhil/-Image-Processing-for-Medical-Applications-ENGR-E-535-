# Load opencv module
import cv2
import numpy as np

# Create a VideoCapture object
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if (cap.isOpened() is False):
    print("Unable to read camera feed")


frame_width = 640  # Width of the frames in the video
frame_height = 480  # Height of the frames in the video
fps = 30 

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec to be used for writing the video
out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height), False)

prev_frame = None
while(True):
    ret, current_frame = cap.read()
    if ret:
        def gray(frame): #helper function to convert frame to gray
            red = frame[..., 0] # data[:, :, 0]
            green = frame[..., 1]
            blue = frame[..., 2]
            frame_gray = 0.21 * red + 0.72 * green + 0.07 * blue #numbers based on visual science
            return frame_gray
        
        gray_current_frame = gray(current_frame)

        if prev_frame is not None:

            abs_diff_frame = np.abs(gray_current_frame - prev_frame)
            abs_diff_frame_threshold= np.where(abs_diff_frame>20,255,0).astype(np.uint8)  # threshold of 20
            cv2.imshow("frame",abs_diff_frame_threshold)
            out.write(abs_diff_frame_threshold) # write frames into video file

        prev_frame = gray_current_frame # set current frame as previous frame
        # Press Q on keyboard to stop recording
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done,
# release the video capture and write objects
cap.release()
out.release()      # release video writer
# Closes all the frames
cv2.destroyAllWindows()
