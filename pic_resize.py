from PIL import Image
import os.path
import glob


def convertjpg(jpgfile, outdir, width=128, height=128):
    img = Image.open(jpgfile)
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(os.path.join(outdir, os.path.basename(jpgfile)))


src_path = '/home/kls/data/marathon/mydata'
target_path = '/home/kls/data/marathon/mydata128'
for jpgfile in glob.glob("{}/*.jpg".format(src_path)):  # 来源文件夹
    convertjpg(jpgfile, target_path)  # 目标文件夹
