nypl-digital-collections
========================

Library to access the New York Public Library's [Digital Collections API](http://api.repo.nypl.org).

Basics: 

````python
from nyplcollections import NYPLsearch

# Create search object
nypl = NYPLsearch(API_KEY)
````

Methods:
* NYPLsearch.captures
* NYPLsearch.mods
* NYPLsearch.search
* NYPLsearch.uuid

Search:

````python
cats = self.nypl.search('cats')

cats.results
# [...]
````

MODS:

````python
# Get a MODS record based on uuid
mods = nypl.mods('acfeeb2d-7c5e-4ce7-e040-e00a180644aa')

mods.status_code
200

mods.results
# {...}
````
