# -*- coding:utf-8 -*-

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/Misengkang/mysite.git"

env.user = 'kangkang'
env.password = 'k61119891k'

# 填写你自己的主机对应的域名
env.hosts = ['www.kangkangblog.site']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '28632'


def deploy():
    source_folder = '/home/kangkang/sites/kangkangblog.site/mysite/newblog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../../vir/bin/pip install -r requirements.txt &&
        ../../vir/bin/python3 manage.py collectstatic --noinput &&
        ../../vir/bin/python3 manage.py makemigrations &&
        ../../vir/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-kkblog')
    sudo('service nginx reload')