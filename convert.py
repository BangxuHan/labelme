import os

root = '/home/kls/PycharmProjects/Mask_RCNN/samples/train/json1'

filelist = os.listdir(root)
filelist.sort()

for file in filelist:
    print(file)
    cmd = 'labelme_json_to_dataset {}/{}'.format(root, file)
    os.system(cmd)
