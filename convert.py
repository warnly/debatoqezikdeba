import subprocess
import os
import os.path
while True:
    for dirpath, dirnames, filenames in os.walk("."):
        for filename in [f for f in filenames if f.endswith(".md")]:
            fpath = os.path.join(dirpath, filename)
            print(fpath)
            filename = filename.split('.')[0]
            subprocess.call(f'C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe pandoc {fpath} -s -o index.html', shell=True)
            print("...")

    k = input()
            #for filename in os.listdir('.'):
            #    if ".md" in filename:
            #        filename = filename.split('.')[0]
            #        subprocess.call(f'C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe pandoc {filename}.md -s -o {filename}.html', shell=True)
