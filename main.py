import argparse
from note import Searcher

parser = argparse.ArgumentParser()
parser.add_argument("note", help="Name of the note you want to read")


def main(args):
    searcher = Searcher()
    searcher.search_note(args.note)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
