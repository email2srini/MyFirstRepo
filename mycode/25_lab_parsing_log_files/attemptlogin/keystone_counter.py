#!/usr/bin/env python3
loginfail = 0
with open("/home/student/MyFirstRepo/mycode/25_lab_parsing_log_files/attemptlogin/keystone.common.wsgi") as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail +=1
print("the number of failed login attempts is", loginfail)
