from pathlib import Path
import typer
from PIL import Image


def main(image_dir: str):
    image_dir = Path(image_dir)
    for f in image_dir.glob("*"):
        img = Image.open(f)
        print(
            f"{f.name}\t{img.height}\t{img.width}\t{max(img.height / img.width, img.width / img.height)}"
        )


if __name__ == "__main__":
    typer.run(main)
