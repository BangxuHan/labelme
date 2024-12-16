import os
from shutil import copyfile

for root, dirs, names in os.walk(
        "/home/kls/PycharmProjects/Mask_RCNN/samples/train_data/labelme_json"):  # 改成你自己的json文件夹所在的目录
    for dr in dirs:
        file_dir = os.path.join(root, dr)
        print(dr)
        file = os.path.join(file_dir, dr + '.png')
        print(file)
        new_name = dr + '.png'
        new_file_name = os.path.join(file_dir, new_name)
        print(new_file_name)

        tar_root = '/home/kls/PycharmProjects/Mask_RCNN/samples/train_data/cv2_mask'  # 目标路径
        tar_file = os.path.join(tar_root, new_name)
        copyfile(new_file_name, tar_file)
