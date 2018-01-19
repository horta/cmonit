import os
import sys
import re
from time import sleep


def monitor_folder(fld):
    while True:
        walk_this_way(fld)
        sleep(10)


def fetch_data(filepath):
    try:
        return open(filepath, 'r').read()
    except Exception:
        return ""


SUC_MSG = "Successfully completed."
ERR_MSG = "Exited with exit code 1."
MEMLIM_MSG = "TERM_MEMLIMIT"


def print_memlim(filepath, data):
    c = re.compile(r"^.*Total Requested Memory : (.*)$", re.MULTILINE)
    m = c.search(data)
    if m is None:
        return

    req = m.groups()[0]
    c = re.compile(r"^.*Max Memory : *(.*)$", re.MULTILINE)
    m = c.search(data)
    if m is None:
        return

    ma = m.groups()[0]
    print("- MEMORY LIMIT ERROR")
    print("  File     : {}".format(filepath))
    print("  Requested: {}".format(req))
    print("  Max used : {}".format(ma))


def walk_this_way(fld):
    for root, dirs, files in os.walk(fld):
        for file in files:
            if file.endswith(".out"):
                fp = os.path.join(root, file)
                data = fetch_data(fp)
                if ERR_MSG in data:
                    if MEMLIM_MSG in data:
                        print_memlim(fp, data)


def entry_point():
    fld = sys.argv[1]
    monitor_folder(fld)
