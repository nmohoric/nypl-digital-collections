#!/usr/bin/env python

import requests

class NYPLsearch:
  def __init__(self,token=None):
    self.token = token or ""

    try:
      assert self.token
    except:
      AssertionError:
        print "You will need to use your Authenticaton Token.\n
               This can be retrieved at http://api.repo.nypl.org/sign_up"

    self.base = "http://api.repo.nypl.org/api/v1/items"

  def return_captures(self, uuid, withTitle=False, format='json'):
    # Return the captures for a given uuid 
    # optional value withTitles=yes

  def return_uuid(self, type, val, format='json'):
    # Return the item-uuid for a identifier.

  def return_mods(self, uuid, format='json'):
    # Return a mods record for a given uuid

  def search_mods(self, q, field=None, format='json'):
    # Search across all (without field) or in specific field 
    # (valid fields at http://www.loc.gov/standards/mods/mods-outline.html)

