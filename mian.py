import os

# Returns a list of all html files inside 'path' directory
def fileFinder(path, ftype = '.html'):
    collected_files = []
    dir_queue = [path]

    for path in dir_queue:
        for file_dir in os.listdir(path):
            if os.path.isdir(path + '\\' + file_dir):
                dir_queue.append(path + '\\' + file_dir)
            elif file_dir.endswith(ftype):
                collected_files.append(path + '\\' + file_dir)
    return collected_files


# Remove all infected vbscript from html file 'f_path'
def cleanFile(f_path):
    with open(f_path, 'r', errors='ignore') as f:
        data = f.read()
        start = data.find('<SCRIPT Language=VBScript>')
        if start != -1:
            data = data[:start]
            with open(f_path, 'w') as f:
                f.write(data)
    return None


# Path of folder from which html files is to be cleaned.
path = "C:\\"

for html_file in fileFinder(path):
    cleanFile(html_file)
