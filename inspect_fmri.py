import nibabel as nib

file_path = r"D:\coding\coding\projects\PROJECTS\Dip_capstone\code\data\sub-40\func\sub-40_task-fe_bold.nii.gz"

img = nib.load(file_path)

print("========== NeuroEmo fMRI Inspection ==========")

print("Shape:", img.shape)
print("Voxel size:", img.header.get_zooms())
print("Data type:", img.get_data_dtype())

print("\nAffine matrix:")
print(img.affine)