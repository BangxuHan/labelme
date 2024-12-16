# 把label.png改名为原图名.png
import os
for root, dirs, names in os.walk("/home/kls/PycharmProjects/Mask_RCNN/samples/train_data/labelme_json"):   # 改成你自己的json文件夹所在的目录
    for dr in dirs:
        file_dir = os.path.join(root, dr)
        # print(dr)
        file = os.path.join(file_dir, 'label.png')
        # print(file)
        new_name = dr + '.png'
        new_file_name = os.path.join(file_dir, new_name)
        os.rename(file, new_file_name)
