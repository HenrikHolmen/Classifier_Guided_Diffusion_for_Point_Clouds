import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.subplots as sp

# Load the point cloud data from the provided .npy file
file_path = r'C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_150\out_150.npy'
point_cloud = np.load(file_path)

# Number of point clouds to plot
num_plots = 3

# Create subplots
fig = sp.make_subplots(rows=1, cols=num_plots, specs=[[{'type': 'scatter3d'}] * num_plots])

for i in range(num_plots):
    x = point_cloud[i][:, 0]
    y = point_cloud[i][:, 1]
    z = point_cloud[i][:, 2]
    colors = z

    scatter = go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=2, color=colors, colorscale='viridis'),
                           name=f'Point Cloud {i + 1}')

    fig.add_trace(scatter, row=1, col=i + 1)

fig.update_layout(title='Interactive 3D Point Clouds')

# Save the plot as HTML
output_file = r"C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_150\interactive_3d_point_clouds.html"
fig.write_html(output_file)

# Print the path to the saved HTML file
print(f"HTML file saved to: {output_file}")
