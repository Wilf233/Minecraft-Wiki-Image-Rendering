from PIL import Image
import os

input_folder = "D:\Minecraft Java Edition\PCL2\.minecraft\screenshots"
output_folder = "Cropped Images"
os.makedirs(output_folder, exist_ok=True)

crop_box = (176, 176, 208, 208)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png')) and filename.startswith("Invicon"):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        cropped_img = img.crop(crop_box)
        cropped_img.save(os.path.join(output_folder, filename))
        os.remove(img_path)
        print(f"已处理: {filename}")

print("运行结束")
