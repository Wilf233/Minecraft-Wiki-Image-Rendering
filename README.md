# Minecraft-Wiki-Image-Rendering

自动生成精灵图和渲染图（参见[Help:精灵图](https://zh.minecraft.wiki/w/Help:精灵图)和[Help:ISO](https://zh.minecraft.wiki/w/Help:ISO)）

## 方块操作步骤
1. 将`client.jar/assets/minecraft/textures/block`（Java版）或`/data/resource_packs/vanilla/textures/blocks`（基岩版）中的目标图像放入`/original`。
2. 运行`Wiki Image Size Convert block.py`。
3. 如果InvSprite为等轴渲染图，则另行渲染。（等轴渲染客户端参见[Wiki自动值](https://github.com/Nickid2018/AutoGenerateWikiData)）
4. 压缩图片并上传至Wiki。

## 物品操作步骤
1. 将`client.jar/assets/minecraft/textures/item`（Java版）或`/data/resource_packs/vanilla/textures/items`（基岩版）中的目标图像放入`/original`。
2. 运行`Wiki Image Size Convert item.py`。
3. 如果需要制作有一半耐久条的物品InvSprite，请先将`Wiki Image Damage Bar.py`中`durability`变量的值改为该物品的最大耐久度，随后运行。这个程序会将`/32px`中的所有图片添加上耐久条并添加`Damaged`前缀。
4. 压缩图片并上传至Wiki。

## 注意事项
部分含有介词的英文名可能需要手动命名为小写。
