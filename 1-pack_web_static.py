#!/usr/bin/python3
"""
compressing static folder into tgz
"""

import tarfile
from datetime import datetime
from os import path, makedirs

from fabric import operations

def do_pack():
    """
    packs static folder
    """
    archive_name = "web_static_" + str(datetime.now().strftime("%Y%m%d%H%M%S"))

    makedirs("./versions", exist_ok=True)

    operations.local("tar -cvzf versions/{}.tgz web_static/".format(archive_name))
