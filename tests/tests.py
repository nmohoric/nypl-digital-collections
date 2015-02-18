from nyplcollections import NYPLsearch
import unittest

# todo: use mock to mock in NYPL responses

KEY = # insert your key here

class TestNYPLsearch(unittest.TestCase):

    def setUp(self):
        self.nypl = NYPLsearch(KEY)

    def test_search(self):
        cats = self.nypl.search('cats')

        assert 200 == cats.status_code

        assert cats.request['perPage'] == 10

        assert cats.results

        assert len(cats.results)

        assert cats.results[0].get('uuid')


    def test_next(self):
        cats = self.nypl.search('cats')
        mor_cats = next(cats)
        assert 200 == mor_cats.status_code

    def test_search_fields(self):
        maps = self.nypl.search('cartographic', field='typeOfResource')

        assert 200 == maps.status_code

        assert maps.results

        assert maps.results[0].get('uuid')

    def test_per_page(self):
        cats = self.nypl.search('cats', per_page=1)
        assert len(cats.results) == 1

    def test_mods(self):
        uuid = '510d47dd-ab68-a3d9-e040-e00a18064a99'
        hades = '423990'
        mods = self.nypl.mods(uuid)
        assert 200 == mods.status_code

        identifiers = mods.results['identifier']
        u = [i for i in identifiers if i['type'] == 'local_hades']
        assert u[0]['$'] == hades

        assert mods.results['titleInfo'][1]['title']['$'] == u'Gowanus Bay - Brooklyn - 30th Street Pier.'

    def test_uuid(self):
        uuid = self.nypl.uuid('local_hades', '1017240')

        assert 200 == uuid.status_code
        assert 'ecaf7d80-c55f-012f-e3c7-58d385a7bc34' == uuid.results

    def test_captures(self):
        captures = self.nypl.captures('5fa75050-c6c7-012f-e24b-58d385a7bc34')

        assert 200 == captures.status_code

        assert 125 == captures.count

        assert type(captures.results) == list

if __name__ == '__main__':
    unittest.main()
