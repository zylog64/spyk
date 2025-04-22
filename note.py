from config import ConfigMixin
import os


class Searcher(ConfigMixin):
    def search_note(self, note):
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
