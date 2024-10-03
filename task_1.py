import shutil
import sys
from pathlib import Path


def copy_files(from_path, to_path):
    if not to_path.exists():
        to_path.mkdir(exist_ok=True)

    for item in from_path.iterdir():
        if item.is_file():
            extension = item.suffix[1:] if item.suffix else 'no_extension'
            ext_dir = to_path / extension
            if not ext_dir.exists():
                ext_dir.mkdir(exist_ok=True)
            try:
                shutil.copy(item, ext_dir / item.name)
            except Exception as e:
                print(f"Failed to copy file {item}: {e}")
        elif item.is_dir():
            try:
                copy_files(item, to_path)
            except Exception as e:
                print(f"Failed to process directory {item}: {e}")


def parse_args():
    if len(sys.argv) < 2:
        print("Please provide the source directory path.")
        sys.exit(1)

    from_path = Path(sys.argv[1])
    to_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('dist')

    if not from_path.exists() or not from_path.is_dir():
        print(f"The directory {from_path} does not exist or is not a directory.")
        sys.exit(1)

    return from_path, to_path


def main():
    from_path, to_path = parse_args()
    copy_files(from_path, to_path)


if __name__ == "__main__":
    main()
