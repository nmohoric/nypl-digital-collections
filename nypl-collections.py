#!/usr/bin/env python

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

  
