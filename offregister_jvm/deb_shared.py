# -*- coding: utf-8 -*-
from logging import getLogger
from sys import modules

from offregister_fab_utils.apt import apt_depends

logger = getLogger(modules[__name__].__name__)


def install0(c, jvm="oracle", jvm_version=18, **kwargs):
    """
    Install JVM

    :param c: Connection
    :type c: ```fabric.connection.Connection```

    :param jvm: Which Java Virtual Machine to use
    :type jvm: ```Literal['oracle', 'openjdk']```

    :param jvm_version: Which JVM version to install
    :type jvm_version: ```int```

    :return: Install response
    :rtype: ```Union[str,fabric.runners.Result]```
    """
    if jvm == "oracle":
        apt_depends(c, "curl")
        deb_file = "jdk-{}_linux-x64_bin.deb".format(jvm_version)
        c.run(
            "curl -OL https://download.oracle.com/java/{}/latest/{}".format(
                jvm_version, deb_file
            )
        )
        res = c.sudo("dpkg -i {}".format(deb_file))
        c.run("rm {}".format(deb_file))
        return res
    elif jvm == "openjdk":
        apt_depends(c, "openjdk-{}-jdk".format(jvm_version))
        return "Installed OpenJDK {}".format(jvm_version)
    raise NotImplementedError(jvm)


__all__ = ["install0"]
