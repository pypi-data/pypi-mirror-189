import setuptools


VERSION = "0.0.1"
NAME = "injectdep"
DESCRIPTION = "Injección de dependencias para python"
AUTHOR = "jbuendia1y - jbuendia1y@gmail.com"
AUTHOR_EMAIL = "jbuendia1y@gmail.com"

REPOSITORY_URL = "https://github.com/jbuendia1y/py-injectdep"


with open("README.md") as f:
    long_description = f.read()
    long_description_content_type = "text/markdown"


setuptools.setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    packages=setuptools.find_packages(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords=[
        "python",
        "injection",
        "dependency",
        "jbuendia1y",
        "library"
        ],
    version=VERSION,
    url=REPOSITORY_URL,
    )