import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the grayscale image
image = cv2.imread('image_grayscale.png',cv2.IMREAD_GRAYSCALE)


#helper function to equalize the image
def histogram_equalization(image):
    flat_image = image.flatten()
    hist, bin_edges = np.histogram(flat_image, bins=256, range=(0, 256))
    cdf = np.cumsum(hist) #calculate cumulative distribition of the histogram values
    cdf_normalized = 0.6 * cdf / cdf[-1]
    equalized_image = np.interp(flat_image, bin_edges[:-1], cdf_normalized * 255) #map the intensities to the cdf of the pixel values
    eq_hist, eq_bin_edges = np.histogram(equalized_image, bins=256, range=(0, 256)) # histogram of the eqialized image
    equalized_image = equalized_image.reshape(image.shape) #reshape to display
    return equalized_image, eq_hist, eq_bin_edges,


#call the function
equalized_image, hist_eq, cdf_eq = histogram_equalization(image)


#display the results
plt.figure(figsize=(12, 6))

# Display the original 
plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

#display the equalized image
plt.subplot(2, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Equalized Image')


# Plotting original image histogram
plt.subplot(2, 2, 3)
plt.hist(image.flatten(),bins = 256, range = [0,256], color = "blue")
plt.title('Original Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')

# Plotting equalized image histogram
plt.subplot(2, 2, 4)
plt.hist(equalized_image.flatten(), bins  = 85, range = [0,150], color = "blue")
plt.title('Equalized Image Histogram')
plt.xlabel('Pixel Intensity')
plt.ylabel('Number of Pixels')
plt.tight_layout()
plt.show()
