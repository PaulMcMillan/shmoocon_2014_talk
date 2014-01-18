import tempfile
import shutil
import os

from fabric.api import *

env.use_ssh_config = True

DEBS = [
    'git',
    'emacs23-nox',
    'unattended-upgrades',
    'ntp',  # turns out to be more important than you'd think
    'collectd',
    'nginx',
    'libhiredis*',
    'ethtool',
    'python-setproctitle',
    ]

@task
def install_debs():
    "Install and upgrade debian dependencies."
    sudo('apt-get update')
    sudo('apt-get dist-upgrade -y')
    sudo('apt-get install -y ' + ' '.join(DEBS))
    sudo('apt-get autoremove -y')

@task
def configure_upgrades():
    "Configure unattended upgrades"
    put('configs/50unattended-upgrades',
        '/etc/apt/apt.conf.d/50unattended-upgrades',
        use_sudo=True)
    put('configs/unattended-upgrades-10periodic',
        '/etc/apt/apt.conf.d/10periodic',
        use_sudo=True)

@task
def set_timezone():
    "Set timezone to Etc/UTC."
    sudo('echo "Etc/UTC" > /etc/timezone')
    sudo('dpkg-reconfigure -f noninteractive tzdata')

@task
def install_pip():
    "Install latest setuptools and pip."
    sudo('wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/'
         'ez_setup.py -O - | python')
    run('rm setuptools-*.tar.gz')
    sudo('wget https://raw.github.com/pypa/pip/master/contrib/'
         'get-pip.py -O - | python')

@task
def install_ssh_configs():
    try:
        put('configs/id_rsa', '~/.ssh/id_rsa', mode=0o600)
        put('configs/id_rsa.pub', '~/.ssh/id_rsa.pub', mode=0o600)
    except IOError:
        print "Not installing private keys."
    put('configs/known_hosts', '~/.ssh/known_hosts', mode=0o644)

@task
def install_tasa():
    "Install tasa."
    sudo('pip install -U tasa')

@task
def configure_tasa():
    "Configure tasa."
    sudo('mkdir -p /etc/tasa')
    put('configs/tasa.conf', '/etc/tasa/tasa.conf')

@task
def configure_collectd():
    "Configure collectd"
    put('configs/collectd.conf', '/etc/collectd/collectd.conf', use_sudo=True)
    sudo('service collectd restart')

@task
def configure_nginx():
    "Configure nginx"
    sudo('rm /etc/nginx/sites-enabled/*')
    put('configs/optout.nginx',
        '/etc/nginx/sites-enabled/optout',
        use_sudo=True)
    sudo('mkdir -p /usr/share/nginx/www')
    put('configs/optout.html',
        '/usr/share/nginx/www/index.html')
    sudo('service nginx restart')

@task
@runs_once  # do this once, locally
def compile_masscan():
    "Download and compile latest masscan"
    try:
        os.remove('masscan')
    except OSError:
        pass
    local('sudo apt-get install -y build-essential libpcap-dev')
    tempdir = tempfile.mkdtemp()
    with lcd(tempdir):
        local('git clone https://github.com/robertdavidgraham/masscan')
        with lcd('masscan'):
            local('make')
            local('make regress')
    shutil.move(os.path.join(tempdir, 'masscan/bin/masscan'),
                '.')
    shutil.rmtree(tempdir)

@task
def configure_masscan():
    "Copy masscan configuration"
    remote_hostname = run('hostname')
    sudo('mkdir -p /etc/masscan')
    with tempfile.NamedTemporaryFile() as f:
        with open('configs/masscan.conf') as f2:
            base_conf = f2.read()
        try:
            with open('configs/masscan.conf.%s' % remote_hostname) as f2:
                extra_conf = f2.read()
        except IOError:
            extra_conf = ''
        f.write(base_conf)
        f.write(extra_conf)
        f.flush()
        put(f.name, '/etc/masscan/masscan.conf',
            use_sudo=True)
    put('configs/excludes.txt', '/etc/masscan/excludes.txt',
        use_sudo=True)
    put('masscan', '/usr/local/bin/masscan',
        use_sudo=True, mirror_local_mode=True)

@task
def install_masscan():
    "Compile masscan locally and install remotely"
    compile_masscan()
    configure_masscan()
    # don't worry about cleaning up the local masscan binary

@task
def install_looksee():
    sudo('pip install -U tasa python-redis-log requests')
    with cd('/opt'):
        sudo('rm -rf shmoocon_2014_talk')
        sudo('git clone --depth 1 '
             'git@github.com:PaulMcMillan/shmoocon_2014_talk.git')
    # upstart doesn't play nice with symlinks, so we have to actually
    # copy this file
    put('configs/looksee.upstart', '/etc/init/looksee.conf',
        use_sudo=True)
    with settings(warn_only=True):
        sudo('service looksee restart')

@task
def update_looksee():
    with cd('/opt/shmoocon_2014_talk'):
        sudo('git reset --hard HEAD')
        sudo('git pull')
    with settings(warn_only=True):
        sudo('service looksee restart')

@task
def reboot():
    "Reboot. Doesn't wait."
    sudo('shutdown -r 0')

@task(default=True)
def configure_survey():
    "Run all configuration to set up survey slave"
    install_masscan()  # do this first because it uses local sudo

    install_ssh_configs()
    install_debs()
    configure_upgrades()
    set_timezone()
    install_pip()
    install_tasa()
    configure_tasa()
    configure_collectd()
    configure_nginx()

    install_looksee()

    reboot()


@task
def check_networking():
    sudo('ethtool -k eth0')
    sudo('ethtook -k eth1')
