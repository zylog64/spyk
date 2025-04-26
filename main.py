import argparse
from note import Searcher, Reader

parser = argparse.ArgumentParser()
parser.add_argument("note", help="Name of the note you want to read")


def main(args):
    searcher = Searcher()
    note_path = searcher.get_note_path(args.note)
    assert note_path is not None
    Reader().read(note_path)


if __name__ == "__main__":
    args = parser.parse_args()
    main(args)
