import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the image
gray_image = cv2.imread('image_grayscale.png',cv2.IMREAD_GRAYSCALE)

# Define Gaussian kernels
#reference https://www.geeksforgeeks.org/how-to-generate-2-d-gaussian-array-using-numpy/
def gaussian_kernel(size, sigma):
    guassian_filter = np.fromfunction(lambda x, y: 
                             (1/(2*np.pi*sigma**2)) * np.exp(-((x-size//2)**2 + 
                                                               (y-size//2)**2) 
                                                               / (2*sigma**2)), 
                                                               (size, size))
    return (guassian_filter / np.sum(guassian_filter))


# Convolve the image
def convolve(image, kernel):
    return cv2.filter2D(image, -1, kernel)

# Define our kernel sizes
kernel_sizes = [3, 5, 7, 9]

# Plot the original image
plt.figure(figsize=(12,8))
plt.subplot(1, len(kernel_sizes) + 1, 1)
plt.imshow(gray_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

# Apply convolution with different kernel sizes
for i, size in enumerate(kernel_sizes):
    kernel = gaussian_kernel(size, sigma=2) # the strength of the guassian can be altered based on changing the sigma values
    convolved_image = convolve(gray_image, kernel)
    # Plot the kernel and convolved image
    plt.subplot(1, len(kernel_sizes) + 1, i + 2)
    plt.imshow(convolved_image, cmap='gray')
    plt.title(f'Convolved (size={size})')
    plt.axis('off')
plt.tight_layout()
plt.show()
#the images will look very similar, please zoom in to visualize the difference