import unittest

from rdflib import Graph


class TestRDFLIBExtraNamespaces(unittest.TestCase):
    def test_extra_namespaces(self):
        """ Make sure that the brick and 40+ other namespaces aren't in the default graph """
        g = Graph()
        g_namespaces = [ns for ns, url in g.namespaces()]
        self.assertNotIn('brick', g_namespaces)
        self.assertIn('rdf', g_namespaces)


if __name__ == '__main__':
    unittest.main()
