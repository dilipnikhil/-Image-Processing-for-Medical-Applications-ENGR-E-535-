import numpy as np
import cv2
import matplotlib.pyplot as plt

#read gray_scale image
gray_image = cv2.imread("image_grayscale.png", cv2.IMREAD_GRAYSCALE)

# Plot the grayscale image
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
#read grayscale image
plt.title("Original Image")
plt.imshow(gray_image, cmap='gray')

#calculate values for the instagram
hist, num_bins = np.histogram(gray_image.flatten(),256,[0,256])

#plt the histogram
plt.subplot(2, 2, 2)
plt.hist(gray_image.flatten(), bins  =256, range = [0,256], color = "gray")
plt.title("Histogram of the grayscale image")
plt.xlabel("Instensities of pixel")
plt.ylabel("Frequencies")


# Plot normalized histogram
plt.subplot(2, 2, 3)
plt.hist(gray_image.flatten(), bins=256, range=[0,256], color='gray', density=True)
plt.title('Normalized Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Normalized Frequency')

# Change number of bins
plt.subplot(2, 2, 4)
plt.hist(gray_image.flatten(), bins=16, range=[0,256], color='gray', density=True)
plt.title('Normalized Histogram with 16 Bins')
plt.xlabel('Pixel Intensity')
plt.ylabel('Normalized Frequency')

plt.tight_layout()
plt.show()