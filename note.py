from config import ConfigMixin
import os


class Searcher(ConfigMixin):
    def get_note_path(self, note):
        note_path = self.search_dirs(note, self.vault_path)
        return note_path

    def search_dirs(self, note, path):
        os.chdir(path)
        if os.path.exists(note):
            cwd = os.getcwd()
            note_path = f"{cwd}/{note}"
            if not os.path.isdir(note_path):
                return note_path

        for entry in os.listdir(path):
            entry_path = f"{path}/{entry}"
            if os.path.isdir(entry_path):
                if note_path := self.search_dirs(note, entry_path):
                    return note_path


class Reader(ConfigMixin):
    def read(self, note_path):
        read_func = self.get_read_func(note_path)
        read_func(note_path)

    def get_read_func(self, note_path):
        extension = os.path.splitext(note_path)[-1].lower()
        if extension == ".md":
            return self.read_markdown
        return self.read_text

    def read_markdown(self, note_path):
        self.read_text(note_path)

    def read_text(self, note_path):
        with open(note_path, "r", encoding=self.encoding) as note:
            print(note.read())
