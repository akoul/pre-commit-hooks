import argparse
from typing import Optional
from typing import Sequence
import re


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check')
    args = parser.parse_args(argv)

    aws_key_files = []

    for filename in args.filenames:
        with open(filename, 'rb') as f:
            content = f.read()
            if re.search("AKIA[0-9A-Z]{16}", content):
                aws_key_files.append(filename)

    if aws_key_files:
        for aws_key_file in aws_key_files:
            print(f'AWS key found: {aws_key_file}')
            print("Please review the WeWork Application Secret Storage Policy here:")
            print("https://connect.weworkers.io/display/SEC/Application+Secret+Storage+Policy")
        return 1
    else:
        return 0


if __name__ == '__main__':
    exit(main())
