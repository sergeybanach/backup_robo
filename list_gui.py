# Scan D:\ folder with re expr
# sort matched by date
# get folder sizes
# display em in a nice table
# restore up to date to destination

import PySimpleGUI as sg
import re, os, datetime

def get_fold_size(start_path="."):
    total_size = 0
    # return 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

os.chdir("d:\\")
print("directory changed to " + os.getcwd())
dates = []

print("size scanning...")
for f in os.listdir():
    m = re.match("sotr_backup_(\d\d).(\d\d).(\d\d\d\d)_(\d\d).(\d\d).(\d\d)", f)
    if m:
        d = datetime.datetime(day=int(m.group(1)), month=int(m.group(2)), year=int(m.group(3)), hour=int(m.group(4)), minute=int(m.group(5)), second=int(m.group(6)))
        dates.append([d, f, get_fold_size(f)])

dates = sorted(dates, key=lambda date: date[0])

table_headings = ["date", "filename", "size"]
layout = [
    [sg.Table(values=dates, headings=table_headings, max_col_width=35, auto_size_columns=True, display_row_numbers=True, justification="right", num_rows=20, key="-TABLE-", tooltip="dates", enable_events=True)],
    [sg.Button(button_text="Merge", key="-BTNMERGE-"), sg.In(enable_events=True, key="-FOLDER-"), 
        sg.FolderBrowse(key="-FOLDBROWSE-", target="-FOLDER-", button_text="Select dest folder")],
    []
]

window = sg.Window("Robocopy merge folder", layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == "-BTNMERGE-" and values["-TABLE-"] != [] and values["-FOLDER-"] != "":
        for i in range(values["-TABLE-"][0]):
            copy_com = f"robocopy {dates[i][1]} {values['-FOLDER-']} /e"
            os.system(copy_com)

window.close()