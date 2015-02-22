#!/usr/bin/env python
import requests


class NYPLsearch(object):

    def __init__(self, token, page=None, per_page=None):
        self._token = token
        self.format = 'json'
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

        headers = {"Authorization": "Token token=" + self._token}

        params['page'] = params.get('page') or self.page
        params['per_page'] = params.get('per_page') or self.per_page

        r = requests.get(".".join([url, self.format]),
                         params=params,
                         headers=headers)

        _next = self._nextify(components, picker, params)

        return Result(r, picker, _next)

    def _nextify(self, components, picker, params):
        params['page'] = 1 + params.get('page', 0)
        return lambda: self._get(components, picker, **params)


class Result(object):

    '''Iterable wrapper for responses from NYPL API'''
    error = None

    def __init__(self, request_object, picker, _next):
        self.raw = request_object.text
        self.status_code = request_object.status_code

        self._next = _next

        response = request_object.json().get('nyplAPI', {})

        try:
            self.headers = response['response'].get('headers')

            if self.headers['status'] == 'error':
                self.error = {
                    'code': self.headers['code'],
                    'message': self.headers['message']
                }

            else:
                self.request = response.get('request', {})

                for k in ('numResults', 'totalPages', 'perPage', 'page'):
                    v = self.request.get(k)
                    if v:
                        self.request[k] = int(v)

                if response['response'].get('numResults'):
                    self.count = int(response['response']['numResults'])

                self.results = picker(response['response'])

        except IndexError:
            raise IndexError("Couldn't parse response.")

    def next(self):
        if self.request.get('totalPages') > self.request.get('page'):
            return self._next()
        else:
            raise StopIteration
