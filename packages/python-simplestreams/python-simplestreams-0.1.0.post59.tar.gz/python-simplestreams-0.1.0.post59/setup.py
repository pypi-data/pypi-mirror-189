from setuptools import setup
from glob import glob
import os

VERSION = '0.1.0.post59'


def is_f(p):
    return os.path.isfile(p)


setup(
    name="python-simplestreams",
    description='Library and tools for using Simple Streams data',
    version=VERSION,
    author='Scott Moser',
    author_email='scott.moser@canonical.com',
    license="AGPL",
    url='http://launchpad.net/simplestreams/',
    packages=['simplestreams', 'simplestreams.mirrors',
              'simplestreams.objectstores'],
    scripts=glob('bin/*'),
    data_files=[
        ('lib/simplestreams', glob('tools/hook-*')),
        ('share/doc/simplestreams',
         [f for f in glob('doc/*') if is_f(f)]),
    ]
)
