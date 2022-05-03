# Sync Helper For Canvas
a self-use tool to copy files with certain rules

## how to use
- put `.py` or `.exe` in the right folder (parent)
- set the path in `.sync_config`
- run `.py` or `.exe`

## what can it do

it's designed for working with grabbing tools for canvas.

this tool can simply copy an entire folder to the setted path. But it will keep your edited files safe from overwritten, also it will tell you the change of files.

it can auto fix the onedrive syncing problems caused by unsupported file names.

## how to create an exe file
`shift` + `right key (mouse)` in the file manager, run Powershell, enter `pyinstaller -F main.py`, get the `.exe` file in `dist` folder.
Do not do this in your daily working folder, this will generate many trash files.
