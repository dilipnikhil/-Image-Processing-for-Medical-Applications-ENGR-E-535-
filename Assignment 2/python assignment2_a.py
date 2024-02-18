import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import binary_dilation, binary_erosion, binary_opening, binary_closing


# Define structuring element for 4-connected morphology
struct_element = np.array([[0, 1, 0],
                  [1, 1, 1],
                  [0, 1, 0]], dtype=bool)

# Create a binary image with noise and a black point
binary_image = np.zeros((32, 32), dtype=np.uint8) 
binary_image[15:23, 15:19] = 1
binary_image[18, 18] = 0
binary_image[8, 11] = 1


# Scipy operations
scipy_dilated = binary_dilation(binary_image, structure=struct_element)
scipy_eroded = binary_erosion(binary_image, structure=struct_element)
scipy_closed = binary_closing(binary_image, structure=struct_element)
scipy_opened = binary_opening(binary_image, structure=struct_element)

# helper function to perform Custom morphological
def morph_operation(image, struct_element, operation):
    padded = np.pad(image, pad_width=1, mode='constant') #pad the image
    morphed = np.zeros_like(image) #placeholder array
    for i in range(image.shape[0]): #iterte through the image
        for j in range(image.shape[1]):
            morphed[i, j] = operation(padded[i:i+3, j:j+3][struct_element])
    return morphed

#helper functions to call the above function with individual operations
def custom_dilate(image):
    return morph_operation(image, struct_element, np.max)

def custom_erode(image):
    return morph_operation(image, struct_element, np.min)

def custom_close(image):
    return custom_erode(custom_dilate(image))

def custom_open(image):
    return custom_dilate(custom_erode(image))
# Custom morphological operations
custom_dilated = custom_dilate(binary_image)
custom_eroded = custom_erode(binary_image)
custom_closed = custom_close(binary_image)
custom_opened = custom_open(binary_image)

# Plotting
plt.figure(figsize=(12, 10))
plt.subplot(4, 4, 1)
plt.imshow(binary_image, cmap='gray')
plt.title('Original Image')

plt.subplot(3, 4, 5)
plt.imshow(custom_dilated, cmap='gray')
plt.title('Custom Dilation')

plt.subplot(3, 4, 6)
plt.imshow(custom_eroded, cmap='gray')
plt.title('Custom Erosion')

plt.subplot(3, 4, 7)
plt.imshow(custom_closed, cmap='gray')
plt.title('Custom Closing')

plt.subplot(3, 4, 8)
plt.imshow(custom_opened, cmap='gray')
plt.title('Custom Opening')

plt.subplot(3, 4, 9)
plt.imshow(scipy_dilated, cmap='gray')
plt.title('Scipy Dilation')

plt.subplot(3, 4, 10)
plt.imshow(scipy_eroded, cmap='gray')
plt.title('Scipy Erosion')

plt.subplot(3, 4, 11)
plt.imshow(scipy_closed, cmap='gray')
plt.title('Scipy Closing')

plt.subplot(3, 4, 12)
plt.imshow(scipy_opened, cmap='gray')
plt.title('Scipy Opening')

plt.savefig('python assignment2_a.png')
plt.show()