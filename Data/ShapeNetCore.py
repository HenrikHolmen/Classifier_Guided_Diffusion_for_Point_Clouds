# from datasets import *
# print(list_datasets("ShapeNet/ShapeNetCore"))

# # If the dataset is gated/private, make sure you have run huggingface-cli login

# # dataset = load_dataset("ShapeNet/ShapeNetCore", data_files="02747177.zip")
# # dataset.save_to_disk("./test-hf")

import h5py
f = h5py.File(r'C:\Users\Henrik\Documents\Git\Git_projects\Classifier_Guided_Diffusion_for_Point_Clouds\Data\shapenet.hdf5', 'r')
print(list(f.keys()))
dset = f['02691156']
print(dset.keys())
ddset = dset['train']
print(ddset.shape)
f.close()