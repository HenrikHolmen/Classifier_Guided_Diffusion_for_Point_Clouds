import numpy as np
import pandas as pd
import plotly.express as px

# Load the point cloud data from the provided .npy file
file_path = r'C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_250\out.npy'
point_cloud = np.load(file_path)

# Extract the first point cloud
first_point_cloud = point_cloud[337]

x = first_point_cloud[:, 0]
y = first_point_cloud[:, 1]
z = first_point_cloud[:, 2]

# Create a DataFrame for Plotly Express
df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'color': z})

# Create the plot
fig = px.scatter_3d(df, x='x', y='y', z='z', color='color', color_continuous_scale='viridis', title='Interactive 3D Point Cloud')

# Save the plot as HTML
output_file = r"C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_250\interactive_3d_point_cloud.html"
fig.write_html(output_file)

# Print the path to the saved HTML file
print(f"HTML file saved to: {output_file}")
