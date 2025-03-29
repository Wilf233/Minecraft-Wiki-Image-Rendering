initialization=["CALL tick freeze","CALL gamemode spectator", "CALL fill 24 -61 24 -8 -61 -8 air"]
block_image_initialization=["CALL kill @e[type=minecraft:item_display]", "CALL tp @s 1.5 -0.3035 1.5 135 30", "WSIZE 300x300", "OSIZE 1.6x1.6", "ORTHO"]
block_inv_initialization=["CALL setblock 0 0 0 air", "CALL tp @s 0 -1.62 1 180 0", "ORTHO", "OSIZE 12x12", "WSIZE 384x384", "BLOCKLIGHT"]
block_name=[]

suffix=" JE1" # 需要填写方块渲染图后缀

def capitalize_string(s):
    lowercase_words = {"a", "an", "the", "and", "but", "or", "nor", "for", "on", "in", "at", "to", "by", "with", "of", "as", "so", "yet"} # up

    words = s.split("_")
    result = [
        word if word in lowercase_words else word.capitalize()
        for word in words
    ]
    return "_".join(result)

with open("input.txt", "r", encoding="utf-8") as file: # 在input.txt中传入需要渲染的方块ID
    block_id = list(map(str.strip, file))

for word in block_id:
    block_name.append(capitalize_string(word))

with open("output.txt", "w", encoding="utf-8") as file:
    for line in initialization:
        file.write(line + "\n")
    for line in block_image_initialization:
        file.write(line + "\n")
    for id, name in zip(block_id, block_name):
        file.write("CALL setblock 0 0 0 " + id + "\nSKIPTICK\nSSHOT " + name + suffix + ".png\n")
    for line in block_inv_initialization:
        file.write(line + "\n")
    for id, name in zip(block_id, block_name):
        file.write("CALL summon item_display 0 0 0 {item:{id:" + id +"},transformation:[-1,0,0,0,0,1,0,0,0,0,-1,0,0,0,0,1],item_display:gui}\nCALL tick step 1\nSKIPTICK\nSSHOT Invicon " + name + ".png\nCALL kill @e[type=minecraft:item_display]\n")
    file.write("LEVELLIGHT\n")

print("output.txt已生成")
