from distutils.core import setup

files = ["nyplcollections.py"]

setup(name = "NYPLsearch",
    version = "1",
    description = "new york public library image collections api",
    author = "nick mohoric",
    author_email = "nick.mohoric@gmail.com",
    packages = ['NYPLsearch'],
    package_data = {'package' : files },
    install_requires=["xmltodict"],
    long_description = """Really long text here.""" 
) 
