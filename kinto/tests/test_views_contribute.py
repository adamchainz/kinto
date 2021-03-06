from .support import BaseWebTest, unittest


class ContributeViewTest(BaseWebTest, unittest.TestCase):

    def test_returns_info_about_project(self):
        response = self.app.get('/contribute.json')
        keys = sorted(response.json.keys())
        expected = ['description', 'keywords', 'name', 'participate',
                    'repository', 'urls']
        self.assertEqual(keys, expected)
