from config import ConfigMixin
import os


class Searcher(ConfigMixin):
    def search_note(self, note):
        note_path = f"{self.vault_path}/{note}"
        if not os.path.exists(note_path):
            raise FileNotFoundError("Note does not exist")
        print("found!")
