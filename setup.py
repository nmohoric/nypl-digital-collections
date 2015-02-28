from setuptools import setup

setup(
    name="nyplcollections",
    version="1.1",
    description="new york public library image collections api",
    author="nick mohoric",
    author_email="nick.mohoric@gmail.com",
    install_requires=[
        "requests"
    ],
    packages=['nyplcollections'],
    url="https://github.com/nmohoric/nypl-digital-collections",
    download_url="https://github.com/nmohoric/nypl-digital-collections/tarball/v1.1"
)
