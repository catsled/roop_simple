from utils import *
from glob import glob


# 1. 将原始图像与当前图像进行拼接
original_img_paths = glob("original_imgs/*.jpg")
processed_img_paths = glob("processed_imgs/*.jpg")

for oip, pip in zip(original_img_paths, processed_img_paths):
    tgt_img_path = oip.replace("original_imgs", "con_imgs")
    concatenate_images_horizontally(oip, pip, tgt_img_path)
    crop_image(tgt_img_path, 0, 50, 736, 590)


# 2. 合成视频y
input_pattern = "con_imgs/output-%04d.jpg"
output_file = "outputs/con.mp4"
images_to_video(input_pattern, output_file)


# 3. 添加声音
add_audio_to_video("outputs/con.mp4", "src/cd.mp3", "outputs/con_all.mp4")