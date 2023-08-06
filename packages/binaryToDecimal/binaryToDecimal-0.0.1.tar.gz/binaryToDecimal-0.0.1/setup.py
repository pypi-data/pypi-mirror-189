from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Convert binary bits to decimal numbers'
LONG_DESCRIPTION = 'A package that converts binary form of data to decimal, to contact me use my website https://karthiks-digital-resume-react.netlify.app and send your queries in contact section'

# Setting up
setup(
    name="binaryToDecimal",
    version=VERSION,
    author="karthik mummadi",
    author_email="<karthikmumadi@icloud.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'binary to decimal', 'binarydecimal', 'bits to numbers'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)