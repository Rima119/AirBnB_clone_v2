#!/usr/bin/python3
"""Fabric script that deletes out-of-date archives"""
import os
from fabric.api import *

env.hosts = ["52.204.64.21", "54.145.156.40"]


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    archive = sorted(os.listdir("versions"))
    [archive.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for n in archive]
    with cd("/data/web_static/releases"):
        archive = run("ls -tr").split()
        archive = [n for n in archive if "web_static_" in n]
        [archive.pop() for j in range(number)]
        [run("rm -rf ./{}".format(n)) for n in archive]
