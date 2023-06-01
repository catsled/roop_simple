import subprocess
from PIL import Image


def split_video_to_images(input_file, output_pattern='original_imgs/output-%04d.jpg'):
    """
    generate by chatgpt
    :param input_file:
    :param output_pattern:
    :return:
    """
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-vf', 'fps=30',
        output_pattern
    ]
    subprocess.call(cmd)


def images_to_video(input_pattern, output_file, framerate=30):
    cmd = [
        'ffmpeg',
        '-framerate', str(framerate),
        '-i', input_pattern,
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        output_file
    ]
    subprocess.call(cmd)


def extract_audio(input_file, output_file):
    cmd = [
        'ffmpeg',
        '-i', input_file,
        '-f', "mp3",
        '-ar', '16000',
        output_file
    ]
    subprocess.call(cmd)


def add_audio_to_video(video_file, audio_file, output_file):
    cmd = [
        'ffmpeg',
        '-i', video_file,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'aac',
        '-map', '0:v:0',
        '-map', '1:a:0',
        '-shortest',
        output_file
    ]
    subprocess.call(cmd)


def concatenate_images_horizontally(image1, image2, output_image):
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    # 确保两张图片高度相同
    if img1.height != img2.height:
        raise ValueError("The heights of the images do not match.")

    # 计算新图像的宽度
    new_width = img1.width + img2.width

    # 创建一个新的空图像，宽度为两张图片之和，高度与任一图片相同
    new_image = Image.new('RGB', (new_width, img1.height))

    # 将第一张图片粘贴到新图像的左侧
    new_image.paste(img1, (0, 0))

    # 将第二张图片粘贴到新图像的右侧
    new_image.paste(img2, (img1.width, 0))

    # 保存新图像
    new_image.save(output_image)


def crop_image(image_path, x, y, width, height):
    image = Image.open(image_path)
    cropped_image = image.crop((x, y, x + width, y + height))
    cropped_image.save(image_path)


# if __name__ == '__main__':
    # input_file = "src/cd.mp4"
    # output_file = "src/cd.mp3"
    # add_audio_to_video("outputs/cd.mp4", output_file, "outputs/tt.mp4")
    # extract_audio(input_file, output_file)
#     split_video_to_images("src/input.mp4")
#     images_to_video("outputs/output-%04d.jpg", "test.mp4")
