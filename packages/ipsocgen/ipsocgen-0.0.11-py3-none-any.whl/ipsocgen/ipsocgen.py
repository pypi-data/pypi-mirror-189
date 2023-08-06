import logging
import argparse

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
                        default=default_serial)
    parser.add_argument('--speed',
                        nargs='?',
                        type=int,
                        default=default_speed)
    args = parser.parse_args()

if __name__ == '__main__':
    main()
