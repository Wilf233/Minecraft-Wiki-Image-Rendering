# Minecraft-Wiki-Image-Rendering

自动生成精灵图和渲染图（参见[Help:精灵图](https://zh.minecraft.wiki/w/Help:精灵图)、[Help:ISO](https://zh.minecraft.wiki/w/Help:ISO)和[等轴渲染客户端](https://github.com/Nickid2018/AutoGenerateWikiData)）

## 方块精灵图（BlockSprite）操作步骤
1. 将`client.jar/assets/minecraft/textures/block`（Java版）或`/data/resource_packs/vanilla/textures/blocks`（基岩版）中的目标图像放入`/original`。
2. 运行`Wiki Image Size Convert block.py`。
3. 如果InvSprite为等轴渲染图，则需用等轴渲染客户端另行渲染。
4. 压缩图片并上传至Wiki。

## 物品精灵图（ItemSprite）、物品栏精灵图（InvSprite）和渲染图操作步骤
1. 将`client.jar/assets/minecraft/textures/item`（Java版）或`/data/resource_packs/vanilla/textures/items`（基岩版）中的目标图像放入`/original`。
2. 运行`Wiki Image Size Convert item.py`。
3. 如果需要制作有一半耐久条的物品InvSprite，请先将`Wiki Image Damage Bar half.py`中`durability`变量的值改为该物品的最大耐久度，随后运行。这个程序会将`/32px`中的所有图片添加上耐久条并添加`Damaged`前缀。
4. 压缩图片并上传至Wiki。

## 生成方块渲染图和物品栏精灵图渲染脚本（配合等轴渲染客户端）
1. 在input.txt中输入需要渲染的方块ID，每行一个。
2. 运行`Generate Auto Rendering script.py`，得到output.txt。
3. 在等轴渲染客户端中运行output.txt。
