#!/usr/bin/env python

import pprint
from nyplcollections import NYPLsearch

# Create search object
# Could also pass in a format of 'xml' if you want to use the raw_results
# and require xml. Otherwise the search will return json in raw_results
searchObj = NYPLsearch('dkh183x9ibxj4x8f')

# Find captures based on uuid
# Don't need to set this equal to anything, could also access results from
# searchObj.results
temp = searchObj.mods('acfeeb2d-7c5e-4ce7-e040-e00a180644aa')

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(temp)

