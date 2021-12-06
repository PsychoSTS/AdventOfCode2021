import argparse
import importlib
import inspect


def main():
    parser = argparse.ArgumentParser(description='Advent of code 2021 project.')
    parser.add_argument('day', metavar='D', type=int, nargs="+",
                        help='run the code for this day')
    parser.add_argument('--part', '-p', type=int, nargs="?", default=1, help="run another variation")

    args = parser.parse_args()
    day_module = importlib.import_module(f"days.day{args.day[0]}")
    if not bool(day_module):
        raise RuntimeError(f"No module found for days.day{args.day[0]}")

    main_name = "main" if args.part == 1 else f"main_pt{args.part}"

    if hasattr(day_module, main_name):

        main_fn = getattr(day_module, main_name)
        main_fn_comments = inspect.getcomments(main_fn)

        print("*" * 25)
        if bool(main_fn_comments):
            print(main_fn_comments.strip())
        print("*" * 25)
        print(f"Answer: {main_fn()}")
    else:
        raise RuntimeError("Day module does not have a `main` entry point function defined.")


if __name__ == '__main__':
    main()
