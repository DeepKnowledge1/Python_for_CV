import cv2
import os

import argparse

# Mini Project: Complete OOP-Based Image Processing Library
# Simple Image Processing with OpenCV (No OOP)


def load_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        raise FileExistsError(f" The {image_path} file is not found")

    return img


def save_image(img, outpath):
    cv2.imwrite(outpath, img)


def convert_to_grayscale(img):

    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def convert_bgr2rgb(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


def convert_rgb2bgr(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


def convert_bgr2hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def split_channel(img):
    return cv2.split(img)


def rotate(img, degree=45):
    (rows, cols) = img.shape[:2]
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), degree, 1)
    rotated_cv = cv2.warpAffine(img, M, (cols, rows))
    return rotated_cv


def flip_image(img, flip_code):
    return cv2.flip(img, flip_code)  # 1: horizontal, 0: vertical


def resize_image(img, width, height):
    return cv2.resize(img, (width, height))


def blur_image(img, ksize=(5, 5)):
    return cv2.GaussianBlur(img, ksize, 0)


def detect_edges(img, low_thresh=100, high_thresh=200):
    if len(img.shape) == 3:
        img = convert_to_grayscale(img)
    return cv2.Canny(img, low_thresh, high_thresh)


def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Simple image processing with no OOP")

    parser.add_argument(
        "--input", required=False, default="./img1.jpg", help="Input image"
    )
    parser.add_argument(
        "--output_dir", default="results", help="Directory to same the results images"
    )
    parser.add_argument(
        "--grayscale", action="store_true", help="Convert image to grayscale image"
    )
    parser.add_argument(
        "--rotate",
        type=int,
        default=None,
        help="Rotate the image with a certain degree",
    )

    parser.add_argument(
        "--resize",
        nargs=2,
        type=int,
        metavar=("WIDTH", "HEIGHT"),
        help="Resize image to WIDTH HEIGHT, e.g., --resize 256 256",
    )
    parser.add_argument(
        "--flip",
        type=int,
        choices=[0, 1],
        default=None,
        help="Flip image: 1 for horizontal, 0 for vertical, e.g., --flip 1",
    )
    parser.add_argument("--blur", action="store_true", help="Apply Gaussian blur")
    parser.add_argument("--edges", action="store_true", help="Detect edges (Canny)")

    parser.add_argument(
        "--bgr2rgb", action="store_true", help="Convert image from BGR to RGB"
    )
    parser.add_argument(
        "--rgb2bgr", action="store_true", help="Convert image from RGB to BGR"
    )
    parser.add_argument(
        "--bgr2hsv", action="store_true", help="Convert image from BGR to HSV"
    )
    parser.add_argument(
        "--split_channel", action="store_true", help="Split image into color channels"
    )

    args = parser.parse_args()

    ensure_dir(args.output_dir)

    img = load_image(image_path=args.input)
    base_name = os.path.splitext(os.path.basename(args.input))[0]

    if args.grayscale:
        im_res = convert_to_grayscale(img.copy())
        im_apth = os.path.join(args.output_dir, f"{base_name}_grayscale.png")
        save_image(img=im_res, outpath=im_apth)

    # Color space conversions
    if args.bgr2rgb:
        im_res = convert_bgr2rgb(img.copy())
        save_image(
            img=im_res,
            outpath=os.path.join(args.output_dir, f"{base_name}_bgr2rgb.png"),
        )

    if args.rgb2bgr:
        im_res = convert_rgb2bgr(img.copy())
        save_image(
            img=im_res,
            outpath=os.path.join(args.output_dir, f"{base_name}_rgb2bgr.png"),
        )

    if args.bgr2hsv:
        im_res = convert_bgr2hsv(img.copy())
        save_image(
            img=im_res,
            outpath=os.path.join(args.output_dir, f"{base_name}_bgr2hsv.png"),
        )

    # Channel split
    if args.split_channel:
        channels = split_channel(img.copy())
        for idx, ch in enumerate(channels):
            save_image(
                img=ch,
                outpath=os.path.join(args.output_dir, f"{base_name}_channel_{idx}.png"),
            )

    if args.flip is not None:
        im_res = flip_image(img.copy(), args.flip)
        flip_type = "h" if args.flip == 1 else "v"
        save_image(
            img=im_res,
            outpath=os.path.join(args.output_dir, f"{base_name}_flip_{flip_type}.png"),
        )

    if args.rotate is not None:
        im_res = rotate(img.copy(), args.rotate)
        save_image(
            img=im_res,
            outpath=os.path.join(
                args.output_dir, f"{base_name}_rotated_{int(args.rotate)}.png"
            ),
        )

    if args.resize:
        width, height = args.resize
        im_res = resize_image(img.copy(), width, height)
        save_image(
            img=im_res,
            outpath=os.path.join(
                args.output_dir, f"{base_name}_resized_{width}x{height}.png"
            ),
        )

    if args.blur:
        im_res = blur_image(im_res)
        save_image(
            img=im_res,
            outpath=os.path.join(args.output_dir, f"{base_name}_blurred.png"),
        )

    if args.edges:
        im_res = detect_edges(img.copy())
        save_image(
            img=im_res, outpath=os.path.join(args.output_dir, f"{base_name}_edges.png")
        )

    print(f"Processing complete. Results saved in '{args.output_dir}'.")


if __name__ == "__main__":
    main()


# python .\Sec3_Working_with_Images\sec3_project.py `
#   --input img1.jpg `
#   --output_dir results `
#   --grayscale `
#   --rotate 45 `
#   --resize 256 256 `
#   --flip 1 `
#   --blur `
#   --edges `
#   --bgr2rgb `
#   --rgb2bgr `
#   --bgr2hsv `
#   --split_channel


# python .\Sec3_Working_with_Images\sec3_project.py `
#   --input img1.jpg `
#   --output_dir results `
#   --bgr2hsv `
#   --split_channel
