#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """return the archive path if the archive has been correctly generated"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(date)
    gzip_archive = local("tar -cvzf {} web_static".format(archive_path))

    if gzip_archive.succeeded:
        return archive_path
    else:
        return None
