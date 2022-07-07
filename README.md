# Matya-Uasset-Samples
Cooked uassets I made to test my tools.<br>

They are terrible quality.<br>
But small size, 100% free, and redistributable.<br>
It'll help you if you are using online CI tools to test UE related contents.<br>
<br>
<img src="https://user-images.githubusercontent.com/69258547/177767824-1aa691b2-a5f7-4602-b0d8-90f075f50af1.png" height="200">

## Contents

- raw: Uncooked 3D models and textures.
- database.json: Database for uassets. It has file path, UE version, and class for each asset.
- databasegen.py: A python script to make `database.json`.
- others: `.uasset` files. Root folder names mean UE versions.

## Naming Convention
#### Prefix
- T_: Texture
- M_: Material
- SK_: Skeletal mesh
- SM_: Static mesh
#### Suffix
- _PhysicsAsset: Physics asset for skeletal mesh
- _Skeleton: Skeleton asset for skeletal mesh