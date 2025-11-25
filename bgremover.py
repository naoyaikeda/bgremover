from withoutbg import WithoutBG
from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description="Remove background from images using WithoutBG API.")
    parser.add_argument("input", help="Path to the input image file.")
    parser.add_argument("output", help="Path to save the output image file.")

    args = parser.parse_args()

    result = WithoutBG.opensource().remove_background(args.input)
    result.save(args.output)

if __name__ == "__main__":
    main()
