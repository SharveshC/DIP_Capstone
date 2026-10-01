import nibabel as nib

file_path = r"C:\Users\mmadh\dataset\data\sub-01\func\sub-01_task-rest_bold.nii.gz"

img = nib.load(file_path)

print("========== NeuroEmo fMRI Inspection ==========")
print("Shape:", img.shape)
print("Voxel size:", img.header.get_zooms())
print("Data type:", img.get_data_dtype())

print("\nAffine matrix:")
print(img.affine)


