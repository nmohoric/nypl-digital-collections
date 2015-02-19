from setuptools import setup

setup(
    name="nyplcollections",
    version="1",
    description="new york public library image collections api",
    author="nick mohoric",
    author_email="nick.mohoric@gmail.com",
    install_requires=[
        "xmltodict",
        "requests"
    ],
    packages=['nyplcollections'],
    long_description="""Really long text here."""
)
