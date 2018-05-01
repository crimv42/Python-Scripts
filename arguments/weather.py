#!/usr/bin/env python2

import os
import requests
import sys

print(requests.__file__)
from argparse import ArgumentParser

parser= ArgumentParser(description="Get the current weather info")
parser.add_argument('zip', help="zip/postal code of weather area")
parser.add_argument('--country', default='us', help='counrty zip/postal belogs to, default is US.')

args = parser.parse_args()

url = "http://api.openweathermap.org/data/2.5/weather?zip=%s,%s&APPID=%s" % (args.zip, args.country, os.getenv("OWM_API_KEY"))


res = requests.get(url)

if res.status_code != 200:
    print("error talking to weather provider: %s" % res.status_code)
    sys.exit(1)

print (res.json())
