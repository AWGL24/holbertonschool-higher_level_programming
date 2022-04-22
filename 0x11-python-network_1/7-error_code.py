#!/usr/bin/python3
''' Python script that tajes in a URL '''

import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    status = res.status_code
    if status >= 400:
        print("Error cose: {}".format(status))
    else:
        print(res.content.decode('utf8'))
