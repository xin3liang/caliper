#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    E-mail    :    wu.wu@hisilicon.com
#    Data      :    2015-08-04 11:34:40
#    Desc      :

import os
import stat
import shutil

try:
    import caliper.common as common
except ImportError:
    import common

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import client.setup
import server.setup


def _combine_dicts(list_dicts):
    result_dict = {}
    for d in list_dicts:
        for k in d:
            result_dict[k] = d[k]
    return result_dict


def get_packages():
    return (client.setup.get_packages() + server.setup.get_packages())


def get_package_dirs():
    return _combine_dicts(
            [client.setup.get_package_dirs(),
            server.setup.get_package_dirs()]
            )


def run():
    caliper_data_dir = os.path.join(os.environ['HOME'], '.caliper')
    caliper_tmp_dir = os.path.join(caliper_data_dir, 'benchmarks')
    if os.path.exists(caliper_tmp_dir):
        shutil.rmtree(caliper_tmp_dir)

    shutil.copytree(
            os.path.join(os.getcwd(), 'benchmarks'),
            caliper_tmp_dir
            )
    shutil.copystat(
            os.path.join(os.getcwd(), 'benchmarks'),
            caliper_tmp_dir
    )
    os.chmod(caliper_data_dir, stat.S_IRWXO + stat.S_IRWXU)
    setup(
            name='caliper',
            description='A test suite for automatically running on different\
                devices, and compare the test results',
            package_dir=get_package_dirs(),
            package_data=server.setup.get_package_data(),
            packages=get_packages(),
            data_files=server.setup.get_data_files(),
            scripts=server.setup.get_scripts(),
            url='http://github.com/hisilicon/caliper-dev',
            maintainer="hisilicon HTSAT",
            install_requires=[
                'pyYAML',
                'django >= 1.6.1', ]
            )
    if os.path.exists('caliper.egg-info'):
        shutil.rmtree('caliper.egg-info')
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    if os.path.exists('build'):
        shutil.rmtree('build')

if __name__ == "__main__":
    run()
