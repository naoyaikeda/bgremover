from withoutbg import WithoutBG
from rembg import remove, new_session  
from PIL import Image
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Remove background from images using WithoutBG API.")
    parser.add_argument("input", help="Path to the input image file.")
    parser.add_argument("output", help="Path to save the output image file.")
    parser.add_argument("--method", choices=["withoutbg", "rembg"], default="withoutbg",)
    parser.add_argument("--foreground_threshold", type=int, default=240, help="Threshold for foreground detection.  ")
    parser.add_argument("--background_threshold", type=int, default=10, help="Threshold for background detection.  ")
    parser.add_argument("--model", choices=["isnet-anime", "isnet-general-use", "sam", "u2net", "u2net_cloth_seg", "u2net_human_seg", "u2netp", "silueta", "silueta-512", ""], default="", help="Model to use for background removal.")

    args = parser.parse_args()

    if args.method == "withoutbg":
        result = WithoutBG.opensource().remove_background(args.input)
        result.save(args.output)
    elif args.method == "rembg":
        if args.model == "":
            input_image = Image.open(args.input)
            output_image = remove(input_image, alpha_matting_background_threshold=args.background_threshold, alpha_matting_foreground_threshold=args.foreground_threshold)
            output_image.save(args.output)
        else:
            session = None
            session = new_session(args.model)

            print(session)
            if session is None:
                print(f"Model '{args.model}' is not recognized. Please choose a valid model.")
                return

            print(args.output)

            input_image = Image.open(args.input)
            output_image = remove(input_image, alpha_matting_background_threshold=args.background_threshold, alpha_matting_foreground_threshold=args.foreground_threshold, session=session)
            output_image.save(args.output)

if __name__ == "__main__":
    main()
