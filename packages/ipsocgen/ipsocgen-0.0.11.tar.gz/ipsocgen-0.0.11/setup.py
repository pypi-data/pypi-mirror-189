from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.11'
DESCRIPTION = 'Generic SoC builder in HDL'
LONG_DESCRIPTION = 'Build SoCs (System-on-Chip) and MPSoCs (Multi-Processor) through yaml configuration files.'

# Setting up
setup(
    name="ipsocgen",
    version=VERSION,
    author="aignacio (Anderson Ignacio)",
    author_email="<anderson@aignacio.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pytest','argparse'],
    keywords=['soc', 'hdl', 'builder'],
    entry_points = {
        'console_scripts': ['ipsocgen=ipsocgen.ipsocgen_cli:main'],
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
