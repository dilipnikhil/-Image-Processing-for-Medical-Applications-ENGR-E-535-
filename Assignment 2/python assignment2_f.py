import numpy as np
import cv2
import matplotlib.pyplot as plt


#helper function for convolution
def convolution(image, kernel):
    h, w = image.shape
    k_h, k_w = kernel.shape
    pad_height = k_h // 2
    pad_width = k_w // 2
    # Create an empty array to store the result
    result = np.zeros_like(image)
    padded_image = np.pad(image, ((pad_height, pad_height), (pad_width, pad_width)), mode='constant') #pad the image to avoid informtion loss
    # Perform convolution
    for y in range(h):
        for x in range(w):  # ietreate through the image
            reg_interest = padded_image[y:y+k_h, x:x+k_w] #extract the region of interest
            result[y, x] = np.sum(reg_interest * kernel) # Apply element-wise multiplication and sum
    return result


#helper function for correlation
def correlation(image, filter):
    # Flip the kernel
    flipped_kernel = np.flipud(np.fliplr(kernel)) #flip kerner up and down and left and right
    result = convolution(image, flipped_kernel) #perform convolution
    return result

# Load the grayscale image
image = cv2.imread('image_grayscale.PNG', cv2.IMREAD_GRAYSCALE)

#define a simple kernel
kernel = np.array([[1, -1],
                   [-1, 1]])

#call the methods
convolution_image = convolution(image, kernel)
correlation_image = correlation(image, kernel)

#plot the results
plt.figure(figsize=(10, 6))

plt.subplot(3, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(3, 1, 2)
plt.imshow(convolution_image, cmap='gray')
plt.title('Convolution Result')

plt.subplot(3, 1, 3)
plt.imshow(correlation_image, cmap='gray')
plt.title('Correlation Result')

plt.tight_layout()
plt.show()