#
# Upload to pypi:
#   python setup.py sdist bdist_wheel
#   twine upload dist/*
#
#   To use these commands install wheel and twine
#   pip install wheel twine
#
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import os
import io
import itertools
import re
import ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')
_license_re = re.compile(r'__license__\s+=\s+(.*)')
_author_re = re.compile(r'__author__\s+=\s+(.*)')
line_numbers = 20

with io.open('femagtools/__init__.py', 'r') as f:
    meta_data = list(itertools.islice(f, line_numbers))
meta_data = ''.join(meta_data)

version = str(ast.literal_eval(_version_re.search(meta_data).group(1)))
license = str(ast.literal_eval(_license_re.search(meta_data).group(1)))
author = str(ast.literal_eval(_author_re.search(meta_data).group(1)))


def get_extra_requires(add_all=True):
    import re
    from collections import defaultdict

    extra_requires = [
        'lxml:             dxfsl',
        'dxfgrabber:       dxfsl',
        'networkx:         dxfsl',
        'matplotlib:       plot',
        'meshio:           meshio',
        'vtk:              vtk',
        'pyzmq:            zmq'
    ]

    extra_deps = defaultdict(set)
    for k in extra_requires:
        if k.strip() and not k.startswith('#'):
            tags = set()
            if ':' in k:
                k, v = k.split(':')
                tags.update(vv.strip() for vv in v.split(','))
            tags.add(re.split('[<=>]', k)[0])
            for t in tags:
                extra_deps[t].add(k)

    # add tag `all` at the end
    if add_all:
        extra_deps['all'] = set(vv for v in extra_deps.values() for vv in v)

    return extra_deps


setup(
    description='Python API for FEMAG',
    author=author,
    url='https://github.com/SEMAFORInformatik/femagtools',
    author_email='tar@semafor.ch',
    version=version,
    platforms="any",
    install_requires=['numpy', 'scipy>=1.7', 'mako', 'six', 'lmfit',
                      'netCDF4'],
    extras_require=get_extra_requires(),
    tests_require=['pytest', 'meshio', 'matplotlib'],
    packages=['femagtools', 'femagtools.moo',
              'femagtools.dxfsl', 'femagtools.machine'],
    package_data={'femagtools': ['templates/*.mako']},
    license=license,
    name='femagtools',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering'],
    entry_points={"console_scripts": [
        "femagtools-plot = femagtools.plot:main",
        "femagtools-convert = femagtools.convert:main",
        "femagtools-bchxml = femagtools.bchxml:main",
        "femagtools-dxfsl = femagtools.dxfsl.conv:main"]}
)
