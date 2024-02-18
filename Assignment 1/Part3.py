import numpy as np
import numpy as np 
import cv2
import matplotlib.pyplot as plt
from imageio import imread



image = cv2.imread("binary_image.png")

red = image[..., 0] # data[:, :, 0]
green = image[..., 1]
blue = image[..., 2]

bw_image= 0.21 * red + 0.72 * green + 0.07 * blue #numbers based on visual 

binarized_image = np.where(bw_image > 0, 255, 0).astype(np.uint8)
final_image = binarized_image.copy()
final_image = np.where(final_image > 0, 1, 0).astype(np.uint8) # make the image binary with only 0s and 1s

image = binarized_image.copy()

labeled_image = np.zeros_like(image, dtype=np.int32) # initialze an array with the same dimension as binary image
equivalence_list = {}

current_label = 1
for i in range(image.shape[0]): # get rows
    for j in range(image.shape[1]): # get columns
        if image[i, j] != 0: # if pixel is activated
            neighbors = [] # initialize neigbouring pixel values
            if i > 0 and labeled_image[i-1, j] != 0: # check if row ==0 and neighbours is not equal to zero
                neighbors.append(labeled_image[i-1, j]) # append the neigbour values
            if j > 0 and labeled_image[i, j-1] != 0: #check if column is not equal to 0 and neighbour column value is not equal to 0
                neighbors.append(labeled_image[i, j-1])# append the neigbour values

            if not neighbors: # if there are no neighbours then
                labeled_image[i, j] = current_label # assign the current label as the value of that pixel in labelled image
                current_label += 1 # increase the count
            else:
                labeled_image[i, j] = min(neighbors) # if not get the min neighbours
                min_neighbor_label = min(neighbors)
                for neighbor_label in neighbors:
                        if neighbor_label != min_neighbor_label:
                            equivalence_list[neighbor_label] = min_neighbor_label # if there are labelled regions asssign the smallest label among them to the current pixel

# Update labels in equivalence list
for label, equivalent_label in equivalence_list.items(): # if two connected components have different labels, then merge them based on equivalence list
    while equivalent_label in equivalence_list:
        equivalent_label = equivalence_list[equivalent_label]
    equivalence_list[label] = equivalent_label

# Update labels in labeled image based on equivalence list
for i in range(labeled_image.shape[0]): # finally check the labels that are similar and update untill all of objects are labelled
    for j in range(labeled_image.shape[1]):
        if labeled_image[i, j] != 0:
            labeled_image[i, j] = equivalence_list.get(labeled_image[i, j], labeled_image[i, j])

unique_values = np.unique(labeled_image[labeled_image != 0])
for i in unique_values:
    labeled_image[labeled_image == i] = np.random.randint(0,255)
    # Plot the image using Matplotlib
plt.figure(figsize=(8, 6))  # Set the size of the plot
plt.imshow(labeled_image, cmap='tab20b')  # Plot the image with the 'viridis' colormap
plt.title('labelled Components in a Binary Image')  # Set the title of the plot
plt.axis('off')  # Hide the axes
plt.colorbar()  # Show the colorbar for the colormap
plt.show()  # Display the plot


# please run it again to see a better plot.
#issues with M and W, i honestly tried my best to rectify it, i tired scanning from bottom to top as well, but it only made the algorithm worse. Perhaps by the end of this sem i should be able to do it.