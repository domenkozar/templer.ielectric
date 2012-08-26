from ${project}.testing import FunctionalTests


class ViewsTests(FunctionalTests):

    def test_index(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue('Hello!' in res.body)
