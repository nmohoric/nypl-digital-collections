#!/usr/bin/env python

import requests
import xmltodict

class NYPLsearch(object):
    raw_results = ''
    request = dict()
    error = None

    def __init__(self, token, format=None, page=None, per_page=None):
        self.token = token
        self.format = format or 'json'
        self.page = page or 1
        self.per_page = per_page or 10
        self.base = "http://api.repo.nypl.org/api/v1/items"

    def captures(self, uuid, withTitles=False):
        """Return the captures for a given uuid
            optional value withTitles=yes"""
        picker = lambda x: x.get('capture', [])
        return self._get((uuid,), picker, withTitles='yes' if withTitles else 'no')

    def uuid(self, type, val):
        """Return the item-uuid for a identifier"""
        picker = lambda x: x.get('uuid', x)
        return self._get((type, val), picker)

    def search(self, q, field=None, page=None, per_page=None):
        """Search across all (without field) or in specific field
        (valid fields at http://www.loc.gov/standards/mods/mods-outline.html)"""

        def picker(results):
            if type(results['result']) == list:
                return results['result']
            else:
                return [results['result']]

        return self._get(('search',), picker, q=q, field=field, page=page, per_page=per_page)

    def mods(self, uuid):
        """Return a mods record for a given uuid"""
        picker = lambda x: x.get('mods', {})
        return self._get(('mods', uuid), picker)

    def _get(self, components, picker, **params):
        """Generic get which handles call to api and setting of results
        Return: Results object"""
        url = '/'.join((self.base,) + components)

        self.raw_results = self.results = None

        headers = {"Authorization": "Token token=" + self.token}

        params['page'] = params.get('page') or self.page
        params['per_page'] = params.get('per_page') or self.per_page

        r = requests.get(".".join([url, self.format]),
                         params=params,
                         headers=headers)

        self.raw_results = r.text
        results = self._to_dict(r)['nyplAPI']['response']

        self.headers = results['headers']
        self.request = r.json()['nyplAPI'].get('request', dict())

        if self.headers['status'] == 'error':
            self.error = {
                'code': self.headers['code'],
                'message': self.headers['message']
            }
        else:
            self.error = None

        return picker(results)

    def _to_dict(self, r):
        return r.json() if self.format == 'json' else xmltodict.parse(r.text)
