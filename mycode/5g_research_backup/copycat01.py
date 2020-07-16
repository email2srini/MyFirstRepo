#!/usr/bin/env python3

import shutil
import os

## os.chdir:("student@pyb-7488-bchd/MyFirstRepo/mycode")

os.chdir("/home/student/MyFirstRepo/mycode/")

shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network_copy.txt")


shutil.copytree("5g_research/", "5g_research_backup/")

