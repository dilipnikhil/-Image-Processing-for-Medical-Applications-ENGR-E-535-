from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import laplace

#define image paths
input_image_path = 'color_image.PNG'
output_image_path = 'image_grayscale.png'

#helper function to convert color image to gray

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert('L')  # Convert to grayscale
    grayscale_image.save(output_path)


convert_to_grayscale(input_image_path, output_image_path)

#define laplacian filter
lapla_filter = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])


gray_scale_image = cv2.imread("image_grayscale.png", cv2.IMREAD_GRAYSCALE)

#helper function to convolve over image
def convolve_custom(image, filter):
    output_image = np.zeros_like(image, dtype=np.float32) #placeholder array
    for i in range(image.shape[0] - filter.shape[0] + 1): # iterate thrhouh rows
        for j in range(image.shape[1] - filter.shape[1] + 1):# iterate through
            output_image[i, j] = np.sum(image[i:i+filter.shape[0], j:j+filter.shape[1]] * filter) # sum the array values of kernel[i,j] and image[i,j]
    return output_image.astype(np.uint8)

result_custom = convolve_custom(gray_scale_image, lapla_filter)

#scipy.ndimage laplacian transformation
result_scipy = laplace(gray_scale_image)

# Display results
plt.figure(figsize=(12, 6))
plt.subplot(1, 3, 1)
plt.imshow(gray_scale_image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(result_custom, cmap='gray')
plt.title('Custom Laplacian Filter')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(result_scipy, cmap='gray')
plt.title('Scipy Laplacian Filter')
plt.axis('off')