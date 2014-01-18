"""
Hostname and other misc fixups.
"""

from fabric.api import *

@task
def set_hostname(new_hostname):
    """ Run this as root user """
    old_hostname = run('hostname')
    run('echo "%s" > /etc/hostname' % new_hostname)
    run('sed -i "s/%s/%s/g" /etc/hosts' % (old_hostname, new_hostname))
    run('hostname %s' % new_hostname)
