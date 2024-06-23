import numpy as np
import open3d as o3d

# Load the point cloud data from the provided .npy file
file_path = r'C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_150\out_150.npy'
point_cloud = np.load(file_path)

# Extract the first point cloud
first_point_cloud = point_cloud[0]

# Create an Open3D PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(first_point_cloud)

# Save the point cloud to a .ply file
output_ply_file = r'C:\Users\henri\Documents\Git\Git_Projects\Classifier_Guided_Diffusion_for_Point_Clouds-1\Analysis\Generator\Validation Generators\Configuration_150\first_point_cloud.ply'
o3d.io.write_point_cloud(output_ply_file, pcd)

print(f"PLY file saved to: {output_ply_file}")
