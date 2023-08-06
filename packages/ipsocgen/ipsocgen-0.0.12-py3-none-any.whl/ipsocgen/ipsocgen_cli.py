import logging
import argparse
import pathlib
import sys

def main():
    parser = argparse.ArgumentParser(
        description='IP SoC Generator CLI'
    )
    parser.add_argument('--elf',
                        nargs='?',
                        type=pathlib.Path,
                        default=sys.stdin)
    parser.add_argument('--device',
                        nargs='?',
                        type=str,
                        default='42')
    parser.add_argument('--speed',
                        nargs='?',
                        type=int,
                        default='42')
    args = parser.parse_args()

if __name__ == '__main__':
    main()
