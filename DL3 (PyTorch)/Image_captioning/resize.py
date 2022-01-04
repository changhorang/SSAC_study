# resize.py
import argparse
import os
from PIL import Image

def resize_image(image, size):
    """Resize an image to the giben size."""
    return image.resize(size, Image.ANTIALIAS)
    # 높은 해상도의 사진 또는 영상을 낮은 해상도로 변환하거나 나타낼때,
    # 깨진 패턴의 형태로 나타나게 되는데 이를 최소화 시킴

def resize_images(image_dir, output_dir, size):
    """Resize the images in 'image_dir' and save into 'output_dir'."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = os.listdir(image_dir)
    num_images = len(images)
    for i, image in enumerate(images):
        with open(os.path.join(image_dir, image), 'r+b') as f:
            with Image.open(f) as img:
                img = resize_image(img, size)
                img.save(os.path.join(output_dir, image), img.format)

        if (i+1)%100 == 0:
            print(f'[{i+1}/{num_images}] Resized the images and saved into {output_dir}')

def main(args):
    image_dir = args.image_dir
    output_dir = args.output_dir
    image_size = [args.image_size, args.image_size]
    resize_images(image_dir, output_dir, image_size)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', type=str, default='./data/train2014/',
                        help='directory for train images')
    parser.add_argument('--output_dir', type=str, default='./data/resized2014/',
                        help='directory for saving resized images')
    parser.add_argument('--image_size', type=int, default=256,
                        help='size for image after processing')
    args = parser.parse_args()
    main(args)