#!/usr/bin/env python

import requests
import xmltodict

class NYPLsearch():
  def __init__(self,token=None):
    self.token = token or ""

    try:
      assert self.token
    except AssertionError:
        print "You will need to use your Authenticaton Token.\n This can be retrieved at http://api.repo.nypl.org/sign_up"

    self.base = "http://api.repo.nypl.org/api/v1/items"

  # Return the captures for a given uuid 
  # optional value withTitles=yes
  def captures(self, uuid, withTitles=False, format='json'):
    return self._get( '/'.join([self.base, uuid]) + '.' + format, 
        { 'withTitles' : 'yes' if withTitles else 'no' } )


  # Return the item-uuid for a identifier.
  def uuid(self, type, val, format='json'):
    return self._get( '/'.join([self.base, type, val]) + '.' + format )


  # Search across all (without field) or in specific field 
  # (valid fields at http://www.loc.gov/standards/mods/mods-outline.html)
  def search(self, q, field=None, format='json'):
    params = { 'q' : q }
    if field:
      params['field'] = field

    return self._get( '/'.join([self.base, 'search']) + '.' + format, params )

  # Return a mods record for a given uuid
  def mods(self, uuid, format='json'):
    return self._get( '/'.join([self.base, 'mods', uuid]) + '.' + format )


  def _get(self, url, params=None):
    headers = { "Authorization" : "Token token=" + self.token }
    return requests.get(url, params=params, headers=headers)

  def to_dict(self, r, format='json'):
    return r.json() if format == 'json' else xmltodict.parse(r.text)

