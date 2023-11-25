import os
# 定义输入文件夹和输出文件路径
# 输入文件夹
dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.join(dir_path, 'demo')
# 输出文件
output_file=os.path.join( dir_path, 'output.txt')
# 获取输入文件夹中的所有文件路径

# 遍历文件夹中的所有文件和子文件夹
for root, dirs, files in os.walk(folder_path):
    for file_name in files:
        # 构造文件的完整路径
        file_path = os.path.join(root, file_name)
        # 读取文件内容
        with open(file_path, 'r') as f:
            data=f.read()
            with open(output_file, 'a+') as fw:
                fw.write(data)
                fw.write('\n')
                fw.write('-----------------------')
                fw.write('\n')