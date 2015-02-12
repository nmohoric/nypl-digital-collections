from distutils.core import setup

files = ["nyplcollections.py"]

setup(
    name="nyplcollections",
    version = "1",
    description = "new york public library image collections api",
    author = "nick mohoric",
    author_email = "nick.mohoric@gmail.com",
    package_data = {'package' : files },
    install_requires=["xmltodict"],
    packages = ['nyplcollections'],
    long_description = """Really long text here.""" 
) 
