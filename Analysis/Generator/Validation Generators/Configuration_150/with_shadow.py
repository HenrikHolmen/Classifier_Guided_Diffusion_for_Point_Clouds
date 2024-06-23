import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the point cloud data from the provided .npy file
file_path = r'C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_150\out_150.npy'
point_cloud = np.load(file_path)

# Extract the first point cloud
first_point_cloud = point_cloud[1]

x = first_point_cloud[:, 0]
y = first_point_cloud[:, 1]
z = first_point_cloud[:, 2]

# Define the shadow plane's Z offset
shadow_z_offset = z.min() - 0.1

# Plotting the point cloud with shadow effect
fig = plt.figure(figsize=(10, 10), dpi=150)
ax = fig.add_subplot(111, projection='3d')

# Main scatter plot
ax.scatter(x, y, z, c='deepskyblue', s=10, edgecolors='w', alpha=0.9)

# Shadow scatter plot on the "ground"
ax.scatter(x, y, np.full_like(z, shadow_z_offset), c='gray', s=10, edgecolors='none', alpha=0.3)

# Removing the axes
ax.set_axis_off()

# Setting the same scale for all axes
ax.set_box_aspect([1, 1, 0.5])  # aspect ratio is 1:1:0.5 for better perspective

# Adjusting the view angle
ax.view_init(elev=30, azim=240)  # Adjust these values to get a better view

plt.show()
