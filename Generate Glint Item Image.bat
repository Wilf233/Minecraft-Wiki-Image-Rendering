cd C:\Users\34395\Desktop\Image Rendering\Cropped Images
ffmpeg -i item_image_%%d.png -vf palettegen=reserve_transparent=1 palette.png
ffmpeg -i item_image_%%d.png -framerate 20 -i palette.png -lavfi paletteuse=alpha_threshold=128 -gifflags -offsetting item_image.gif