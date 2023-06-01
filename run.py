"""
1. 将视频转换为图片
2. 检查图片中是否出现人脸
3. 若出现人脸则进行替换，然后保存，否则直接保存
4. 将图片合成视频
"""
import cv2
import shutil

from utils import split_video_to_images, images_to_video, extract_audio, add_audio_to_video
from core.analyser import get_face
from core.swapper import process_img
from glob import glob


def run(src_path,
        video_path,
        output_path,
        audio_file="src/audio.mp3"):
    # 分割视频
    split_video_to_images(video_path)

    # 获取音频
    extract_audio(video_path, audio_file)

    # 换脸
    for img_path in glob("original_imgs/*.jpg"):
        has_face = get_face(cv2.imread(img_path))
        if has_face:
            process_img(src_path, img_path, img_path.replace("original_imgs", "processed_imgs"))
        else:
            shutil.move(img_path, img_path.replace("original_imgs", "processed_imgs"))

    # 合成视频
    images_to_video("processed_imgs/output-%04d.jpg", output_path)
    # 插入音频
    add_audio_to_video(output_path, audio_file, "outputs/output_all.mp4")


if __name__ == '__main__':
    src_path = "src/man.jpg"
    video_path = "src/cd.mp4"
    output_path = "outputs/cd.mp4"
    run(src_path, video_path, output_path)





