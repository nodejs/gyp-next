#!/usr/bin/env python3

"""Copies an input to several outputs and records each invocation."""

import sys

source, log, mode, *outputs = sys.argv[1:]

with open(source) as in_file:
    contents = in_file.read()

for output in outputs:
    with open(output, "w") as out_file:
        out_file.write(contents)

with open(log, "a") as log_file:
    log_file.write(f"{mode}\n")
