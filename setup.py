from distutils.core import setup

files = ["nyplcollections.py"]

setup(name = "nyplcollections",
    version = "1",
    description = "new york public library image collections api",
    author = "nick mohoric",
    author_email = "nick.mohoric@gmail.com",
    packages = ['nyplcollections'],
    package_data = {'package' : files },
    long_description = """Really long text here.""" 
) 
