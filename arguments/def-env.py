#!/usr/bin/python

import os

stage = (os.getenv("$1") or "development").upper()

output = "We're running %s" % stage

if stage.startswith("PROD"):
    output = "DANGER!!! - " + output

print(output)
