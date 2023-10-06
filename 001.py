import os
import json

# 获取脚本所在目录
script_directory = os.path.dirname(os.path.realpath(__file__))

# 拼接脚本目录和文件夹名
folder_path = os.path.join(script_directory, 'cover')

# 确保文件夹存在
if os.path.exists(folder_path):
    # 获取文件夹中以 .webp 结尾的文件列表
    image_files = [file for file in os.listdir(folder_path) if file.endswith('.webp')]

    # 生成图片链接
    image_links = ['http://gallery.erat.top/cover/' + file for file in image_files]

    # 构建 JSON 数据
    json_data = {'images': image_links}

    # 将 JSON 写入文件
    json_file_path = os.path.join(script_directory, 'images.json')
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)

    print(f'JSON 文件生成在: {json_file_path}')
else:
    print(f'文件夹不存在: {folder_path}')