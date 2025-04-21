# SPYK

## What is it?

This cli tool is a mix between Cheat and Obsidian.
You can read markdown notes from your vault in the cli with a simple command.

```
spyk <name_of_note>
```
## Configuration
The location of your vault is managed in 
```
$XDG_HOME_CONFIG/spyk/config.ini
# or
$HOME/.config/spyk/config.ini
```
example config:

```
[vault]
path = /home/user/notes
```

## Roadmap
- make reading notes work.
- edit your vault with text editor
- search subdirectories
- handle multiple notes with the same name
- fuzzy finder





