import os
from PIL import Image

# 此程序用于将游戏中的方块图像转换成中文Minecraft Wiki上要求的大小和文件名，其中方块Invicon可能需要另行渲染。

def capitalize_words(filename, hyphen=False):
    lowercase_words = {"a", "an", "the", "and", "but", "or", "nor", "for", "on", "in", "at", "to", "by", "with", "of", "as", "so", "yet"} # 省略了up
    if hyphen:
        filename = filename.replace('_', '-')
        return filename
    else:
        filename = filename.replace('_', ' ')
        name, ext = os.path.splitext(filename)
        capitalized_name = ' '.join(
            word if word in lowercase_words else word.capitalize()
            for word in name.split()
        )
        return capitalized_name + ext

def resize_images(input_folder, output_folder, prefix='', suffix='', size=160, hyphen=False):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            img_path = os.path.join(input_folder, filename)
            try:
                img = Image.open(img_path)
                resized_img = img.resize((size, size), Image.NEAREST)

                new_filename = capitalize_words(filename, hyphen)
                if suffix:
                    new_filename = f"{os.path.splitext(new_filename)[0]} {suffix}{os.path.splitext(new_filename)[1]}"
                if prefix:
                    new_filename = prefix + " " + new_filename

                output_path = os.path.join(output_folder, new_filename)
                resized_img.save(output_path)
                print(f'Resized and saved {filename} as {new_filename} in {output_folder}')
            except Exception as e:
                print(f"Error processing {filename}: {e}")

input_folder = r'original'

resize_images(input_folder, r'32px', 'Invicon', '', 32)
resize_images(input_folder, r'16px', 'BlockSprite', '', 16, True)
