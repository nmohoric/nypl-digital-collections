#!/usr/bin/env python

import requests
import xmltodict


class NYPLsearch(object):
    raw_results = None
    results = None
    error = None

    def __init__(self, token, format='json', page=1, per_page=10):
        self.token = token
        self.page = page
        self.per_page = per_page
        self.format = format
        self.base = "http://api.repo.nypl.org/api/v1/items"

    def captures(self, uuid, withTitles=False):
        """Return the captures for a given uuid
            optional value withTitles=yes"""
        return self._get('/'.join([self.base, uuid]),
                         {'withTitles': 'yes' if withTitles else 'no'})

    def uuid(self, type, val):
        """Return the item-uuid for a identifier"""
        return self._get('/'.join([self.base, type, val]))

    def search(self, q, field=None):
        """Search across all (without field) or in specific field
        (valid fields at http://www.loc.gov/standards/mods/mods-outline.html)"""
        params = {'q': q}
        if field:
            params['field'] = field

        return self._get('/'.join([self.base, 'search']), params)

    def mods(self, uuid):
        """Return a mods record for a given uuid"""
        return self._get('/'.join([self.base, 'mods', uuid]))

    def _get(self, url, params=None):
        """Generic get which handles call to api and setting of results
        Return: Results object"""
        self.raw_results = self.results = None

        headers = {"Authorization": "Token token=" + self.token}
        params = params or dict()
        params['page'] = self.page
        params['per_page'] = self.per_page

        r = requests.get(".".join([url, self.format]),
                         params=params,
                         headers=headers)

        self.raw_results = r.text
        self.results = self._to_dict(r)['nyplAPI']['response']

        if self.results['headers']['status'] == 'error':
            self.error = {
                'code': self.results['headers']['code'],
                'message': self.results['headers']['message']
            }
        else:
            self.error = None

        return self.results

    def _to_dict(self, r):
        return r.json() if self.format == 'json' else xmltodict.parse(r.text)
