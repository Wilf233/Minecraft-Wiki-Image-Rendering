cd C:\Users\34395\Desktop\Image Rendering\Cropped Images
ffmpeg -i Invicon_%%d.png -framerate 20 -vf palettegen=reserve_transparent=1 palette.png
ffmpeg -framerate 20 -i Invicon_%%d.png -i palette.png -lavfi "paletteuse=alpha_threshold=128" -r 20 inv.gif