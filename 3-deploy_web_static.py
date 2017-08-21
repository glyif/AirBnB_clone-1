#!/usr/bin/python3
"""
deploying AirBnB fabric
"""

import tarfile
from datetime import datetime
from os import path, makedirs
from pathlib import Path

from fabric.api import *
from fabric import operations


env.hosts = ["66.70.186.21", "54.227.54.155"]


def do_pack():
    """
    packs static folder
    """
    try:
        archive_name = "web_static_" + str(datetime.now().
                                           strftime("%Y%m%d%H%M%S"))

        makedirs("./versions", exist_ok=True)

        operations.local("tar -cvzf versions/{}.tgz web_static/".
                         format(archive_name))

        return "versions/{}.tgz".format(archive_name)
    except:
        return None


def do_deploy(archive_path):
    """
    deploys archives to servers
    @param: archieve_path: path to archived tar.gz
    """
    a_path = Path(archive_path)
    if not a_path.is_file():
        return False

    try:
        updated_version = archive_path.split("/")[-1]
        new_release = "/data/web_static/releases/" + \
            updated_version.split(".")[0]

        operations.put(archive_path, "/tmp/")
        operations.run("sudo mkdir -p {:s}".format(new_release))
        operations.run(
            "sudo tar -xzf /tmp/{:s} -C {:s}".format(updated_version,
                                                     new_release))
        operations.run(
            "sudo mv {:s}/web_static/* {:s}/".format(new_release, new_release))
        operations.run("sudo rm -rf {:s}/web_static".format(new_release))

        operations.run("sudo rm -rf /data/web_static/current")
        operations.run(
            "sudo ln -sf {:s} /data/web_static/current".format(new_release))

        operations.run("sudo rm /tmp/{:s}".format(updated_version))

        return True
    except:
        return False

def deploy():
    """
    packs and deploys
    """
    pack_status = do_pack()

    if not do_pack():
        return False
    else:
        return do_deploy(pack_status)
