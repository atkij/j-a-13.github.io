import os
import time

old_contents = ""

while True:
    document = open("higher-computing.md", "r")
    contents = document.read()

    if contents != old_contents:
        print("Converting document...")
        os.system("pandoc higher-computing.md --toc -s -o higher-computing.html")
        old_contents = contents

    document.close()

    time.sleep(1)
