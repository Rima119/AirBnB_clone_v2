#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """return the archive path if the archive has been correctly generated"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None
