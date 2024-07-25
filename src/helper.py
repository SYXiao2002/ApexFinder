# 遍历dir文件夹下的所有内容
import os
import shutil


def remove_dir_contents(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
        return
    for item in os.listdir(dir):
        item_path = os.path.join(dir, item)  # 构造完整路径
        if os.path.isfile(item_path):
            os.remove(item_path)  # 删除文件
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)  # 删除文件夹及其所有内容
