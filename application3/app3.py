# app3.py website blocker

import time,filecmp
from datetime import datetime as dt
#host_path = r"C:\Windows\System32\drivers\etc"
host_path = "hosts"
redirect = "127.0.0.1"

website_list = ['www.facebook.com','facebook.com','other.com','random.org']

while True:
    a = dt.now()
    if dt(a.year,a.month,a.day,8) < dt.now() < dt(a.year,a.month,a.day,15):

        with open(host_path, 'r+') as file: #r+ is append
            content = file.read()

            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(website + '\t' + redirect + '\n')

    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()

        new_lines = []

        for website in website_list:
            for line in content:
                if line.startswith('#') or line.startswith('\n'):
                    new_lines.append(line)

        information = ''.join(new_lines)

        with open('new_file','w') as file:
            file.write(information)

        if filecmp.cmp('new_file',host_path) != True:
            with open(host_path,'w') as file:
                file.write(information)


    time.sleep(300)
