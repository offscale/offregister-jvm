from logging import getLogger
from sys import modules

from offregister_fab_utils.apt import apt_depends

logger = getLogger(modules[__name__].__name__)


def install0(c, jvm="oracle", **kwargs):
    """
    :param c: Connection
    :type c: ```fabric.connection.Connection```
    """
    if jvm == "oracle":
        apt_depends(c, "curl")
        deb_file = "jdk-18_linux-x64_bin.deb"
        c.run("curl -OL https://download.oracle.com/java/18/latest/{}".format(deb_file))
        return c.sudo("dpkg -i {}".format(deb_file))
    elif jvm == "openjdk":
        apt_depends(c, "openjdk-18-jdk")
        return "Install OpenJDK"


__all__ = ["install0"]
