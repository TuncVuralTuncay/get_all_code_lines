import os

rootdir = "."
lin = 0
skip_dirs = ['enter the folder names to skip']
file_count = 0
h_line = 0
for subdir, dirs, files in os.walk(rootdir, topdown=True):
    dirs[:] = [d for d in dirs if d not in skip_dirs]
    for file in files:
        if file.endswith('.py') or file.endswith(".js") or file.endswith('.html'):
            filepath = subdir + os.sep + file
            try:
                with open(filepath, encoding="utf-8") as f:
                    rdl = len(f.readlines())
                if(h_line <= rdl):
                    h_line = rdl
                lin += rdl
                file_count += 1 
                print(f"{filepath} lines : {rdl}")
            except UnicodeDecodeError as e:
                print(f"Error: {e} in {filepath}")

average = lin / file_count
print(f"Total lines : {lin}")
print("Total files : "+str(file_count))
print("Average lines : " + str(average))
print("Highest line count : "+str(h_line))
