#!/usr/bin/python3
"""Fabric script that creates and distributes an archive to your web servers"""
import os.path
from datetime import datetime
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["52.204.64.21", "54.145.156.40"]


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


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True


def deploy():
    """
    Deploy function do_pack and do_deploy.
    """
    path = do_pack()
    if path:
        do_deploy(path)
    return False
