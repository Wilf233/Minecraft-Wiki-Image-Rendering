import os
from PIL import Image, ImageDraw
import math

# 此程序用于批量在Invicon上添加一半耐久的耐久条

max_durability = 25 # 物品的最大耐久度
folder_path = "32px"  # 文件夹路径

def hsv_to_rgb(h, s, v):
    h = h / 360
    i = int(h * 6)
    f = (h * 6) - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    
    i = i % 6
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    else:
        r, g, b = v, p, q
    
    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)
    
    return r, g, b

h, s, v = math.ceil(0.5 * max_durability) / max_durability * 120, 1, 1
r, g, b = hsv_to_rgb(h, s, v)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if max_durability > 0:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            try:
                image = Image.open(file_path).convert("RGBA")
                draw = ImageDraw.Draw(image)

                draw.rectangle([(4,26), (29,29)], fill=(0, 0, 0, 255))
                draw.rectangle([(4,26), (17,27)], fill=(r, g, b, 255))

                image.save(os.path.join(folder_path, filename.replace("Invicon", "Invicon Damaged")))
                print(f"已处理：{filename}")
            
            except Exception as e:
                print(f"处理图片 {filename} 时出错: {e}")
    else:
        print("最大耐久度不合法")
        break

