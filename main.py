from math import nan
import os
from PIL import Image
from datetime import datetime

def resize_image(image_path, output_path, size):
	with Image.open(image_path) as img:
		old_size = img.size
		old_ratio = old_size[0] / old_size[1]
		new_ratio = size[0] / size[1]
		if old_ratio != new_ratio:
			print(f"Warning: The image {image_path} does not have the same proportion as the new size.")
			if old_ratio > new_ratio:
				new_height = int(old_size[1])
				new_width = int(new_height * new_ratio)
			else:
				new_width = int(old_size[0])
				new_height = int(new_width / new_ratio)
			left = (old_size[0] - new_width) / 2
			top = (old_size[1] - new_height) / 2
			right = (old_size[0] + new_width) / 2
			bottom = (old_size[1] + new_height) / 2
			img = img.crop((left, top, right, bottom))
		img = img.resize(size, Image.LANCZOS)
		img.save(output_path)

def process_images_in_folder(folder_path, size):
	ref_folder = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{size[0]}x{size[1]}"
	results_folder = os.path.join(folder_path, "Results", ref_folder)
	for root, _, files in os.walk(folder_path):
		if "Results" in root:
			continue
		for file in files:
			if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
				image_path = os.path.join(root, file)
				diff_path = os.path.relpath(root, folder_path)
				results_folder_file = os.path.join(results_folder, diff_path)
				os.makedirs(results_folder_file, exist_ok=True)
				output_path = os.path.join(results_folder_file, f"adjusted_{file}")
				resize_image(image_path, output_path, size)
				print(f"Resized image saved to {output_path}")

def find_min_size(folder_path):
	min_width, min_height = float('inf'), float('inf')
	for root, _, files in os.walk(folder_path):
		if "Results" in root:
			continue
		for file in files:
			if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.webp')):
				image_path = os.path.join(root, file)
				with Image.open(image_path) as img:
					width, height = img.size
					if width < min_width:
						min_width = width
					if height < min_height:
						min_height = height
	return min_width, min_height

def error_message(error_code, message):
	mapping_errors = {
		1: "Invalid path.",
		2: "Invalid value.",
		None: "Internal error."
	}
	if error_code in mapping_errors:
		print(f"[ERROR] {mapping_errors[error_code]}", message)
	else:
		print("[ERROR] Unknown error code:", message)
	print("Exiting...")
	exit()

if __name__ == "__main__":
	folder_path = input("Enter the folder path: ")
	size = find_min_size(folder_path)

	if size == (float('inf'), float('inf')):
		error = f"No images found in the folder. \nCheck if the path is correct: {folder_path}"
		error_message(1, error)

	print(f"We made a check in the imagens inside this folder. \nThe minimum size found is: \nWIDTH {size[0]} px \nHEIGHT {size[1]} px")
	width_size = input("Enter the WIDTH in pixels (px): ")

	if not width_size.isdigit() and width_size != '':
		error = "The value entered to WIDTH is not valid. Please enter only numbers."
		error_message(2, error)

	height_size = input("Enter the HEIGHT in pixels (px): ")

	if not height_size.isdigit() and height_size != '':
		error = "The value entered to HEIGHT is not valid. Please enter only numbers."
		error_message(2, error)

	if(width_size == '' or nan == width_size):
		width_size = size[0]
	if(height_size == '' or nan == height_size):
		height_size = size[1]

	new_size = (int(width_size), int(height_size))
	process_images_in_folder(folder_path, new_size)