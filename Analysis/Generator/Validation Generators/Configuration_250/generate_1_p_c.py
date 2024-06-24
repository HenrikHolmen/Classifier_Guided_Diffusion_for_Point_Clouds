import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

# Load the point cloud data from the provided .npy file
file_path = r'C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_250\out.npy'
point_cloud = np.load(file_path)

# Extract the first point cloud
first_point_cloud = point_cloud[191]

x = first_point_cloud[:, 0]
y = first_point_cloud[:, 1]
z = first_point_cloud[:, 2]

# Create a DataFrame for Plotly Express
df = pd.DataFrame({'x': x, 'y': y, 'z': z, 'color': z})

# Create the plot
fig = px.scatter_3d(
    df, x='x', y='y', z='z', color='color',
    color_continuous_scale='viridis', title='Interactive 3D Point Cloud',
    labels={'x': 'X Axis', 'y': 'Y Axis', 'z': 'Z Axis', 'color': 'Z Value'},
    opacity=0.7
)

# Customize marker size
fig.update_traces(marker=dict(size=4))

# Add annotations (example: adding a text at the mean point)
mean_x = df['x'].mean()
mean_y = df['y'].mean()
mean_z = df['z'].mean()
fig.add_trace(go.Scatter3d(
    x=[mean_x], y=[mean_y], z=[mean_z],
    mode='markers+text',
    marker=dict(size=10, color='red'),
    text=['Mean Point'],
    textposition='top center'
))

# Enhance background and grid
fig.update_layout(
    scene=dict(
        xaxis=dict(backgroundcolor='rgb(230, 230,230)', gridcolor='white', showbackground=True),
        yaxis=dict(backgroundcolor='rgb(230, 230,230)', gridcolor='white', showbackground=True),
        zaxis=dict(backgroundcolor='rgb(230, 230,230)', gridcolor='white', showbackground=True)
    )
)

# Save the plot as HTML
output_file = r"C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_250\interactive_3d_point_cloud_config1.html"
fig.write_html(output_file)

# Save the plot as a high-DPI PNG image
#output_file_png = r"C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_150\interactive_3d_point_cloud.png"
#fig.write_image(output_file_png, scale=5)  # scale increases the DPI

# Print the paths to the saved files
print(f"HTML file saved to: {output_file}")
#print(f"PNG file saved to: {output_file_png}")
