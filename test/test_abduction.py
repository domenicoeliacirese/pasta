import unittest

import importlib.util

import utils_for_tests

import sys
sys.path.append("../pasta/")

spec = importlib.util.spec_from_file_location(
    "pasta", "../pasta/pasta_solver.py")
past = importlib.util.module_from_spec(spec)
spec.loader.exec_module(past)


class TestClassAbduction(unittest.TestCase):

    def wrap_test_abduction(self,
                            filename: str,
                            query: str,
                            evidence: str,
                            test_name: str,
                            expected_lp: float,
                            expected_up: float,
                            expected_abd: 'list[list[str]]'):

        pasta_solver = past.Pasta(filename, query, evidence)
        lp, up, abd = pasta_solver.abduction()

        if lp is not None and up is not None and abd is not None:
            self.assertTrue(utils_for_tests.almostEqual(lp, expected_lp, 5),
                            test_name + ": wrong lower probability")
            self.assertTrue(utils_for_tests.almostEqual(up, expected_up, 5),
                            test_name + ": wrong upper probability")

            self.assertTrue(utils_for_tests.check_if_lists_equal(
                abd, expected_abd), test_name + ": wrong abduction")

    def test_bird_4_abd_prob(self):
        self.wrap_test_abduction("../examples/abduction/bird_4_abd_prob.lp", "fly(1)", "", "bird_4_abd_prob", 0.5, 0.5, [['fa(1)', 'not fa(2)', 'not fa(3)', 'not fa(4)'],
                                                                                                                         ['fa(1)', 'fa(2)', 'not fa(3)', 'not fa(4)'], ['fa(1)', 'not fa(2)', 'fa(3)', 'not fa(4)'], ['fa(1)', 'not fa(2)', 'not fa(3)', 'fa(4)']])

    def test_ex_1_det(self):
        self.wrap_test_abduction("../examples/abduction/ex_1_det.lp",
                                 "query", "", "ex_1_det", 1, 1, [['abd_a', 'abd_b', 'q']])

    def test_ex_1_prob(self):
        self.wrap_test_abduction("../examples/abduction/ex_1_prob.lp",
                                 "query", "", "ex_1_prob", 0.25, 0.25, [['a', 'b']])

    def test_ex_2_det(self):
        self.wrap_test_abduction("../examples/abduction/ex_2_det.lp", "query", "", "ex_2_det", 1, 1, [['q', 'abd_b', 'not_abd_a'],
                                                                                                      ['abd_a', 'not_abd_b', 'q']])

    def test_ex_2_prob(self):
        self.wrap_test_abduction("../examples/abduction/ex_2_prob.lp",
                                 "query", "", "ex_2_prob", 0.75, 0.75, [['a', 'b']])

    def test_ex_3_det(self):
        self.wrap_test_abduction("../examples/abduction/ex_3_det.lp", "query", "", "ex_3_det", 1, 1, [['q', 'abd_a', 'not_abd_d', 'not_abd_c', 'not_abd_b'],
                                                                                                      ['q', 'abd_c', 'abd_b', 'not_abd_d', 'not_abd_a']])

    def test_ex_3_prob(self):
        self.wrap_test_abduction("../examples/abduction/ex_3_prob.lp",
                                 "query", "", "ex_3_prob", 0.58, 0.58, [['a', 'b', 'c', 'not d']])

    def test_ex_4_det(self):
        self.wrap_test_abduction("../examples/abduction/ex_4_det.lp", "query", "", "ex_4_det", 1, 1, [['q', 'abd_a(1)', 'not_abd_d', 'not_abd_c', 'not_abd_b'],
                                                                                                      ['q', 'abd_c', 'abd_b', 'not_abd_d', 'not_abd_a(1)']])

    def test_ex_4_prob(self):
        self.wrap_test_abduction("../examples/abduction/ex_4_prob.lp",
                                 "query", "", "ex_4_prob", 0.648, 0.648, [['c', 'e']])

    def test_ex_5_det(self):
        self.wrap_test_abduction("../examples/abduction/ex_5_det.lp", "qr", "", "ex_5_det", 1, 1, [['q', 'abd_c', 'abd_b', 'abd_a', 'not_abd_e', 'not_abd_d'],
                                                                                                   ['q', 'abd_e', 'abd_d', 'abd_b', 'abd_a', 'not_abd_c']])

    def test_ex_6_prob(self):
        self.wrap_test_abduction(
            "../examples/abduction/ex_6_prob.lp", "qry", "", "ex_6_prob", 1.0, 1.0, [['a(1)']])

    def test_kn_4_prob(self):
        self.wrap_test_abduction("../examples/abduction/kn_4_prob.lp", "path(1,4)", "", "kn_4_prob", 0.734375,
                                 0.734375, [['edge(1,2)', 'edge(1,3)', 'edge(1,4)', 'edge(2,3)', 'edge(2,4)', 'edge(3,4)']])

    def test_smokes_det(self):
        self.wrap_test_abduction("../examples/abduction/smokes_det.lp", "smokes(c)", "", "smokes_det", 1, 1, [['q', 'abd_e(b,c)', 'not_abd_e(e,c)', 'not_abd_e(d,e)', 'not_abd_e(a,d)', 'not_abd_e(a,b)'],
                                                                                                              ['q', 'abd_e(e,c)', 'abd_e(d,e)', 'not_abd_e(b,c)', 'not_abd_e(a,d)', 'not_abd_e(a,b)']])

    def test_smokes_prob(self):
        self.wrap_test_abduction("../examples/abduction/smokes_prob.lp", "smokes(c)", "", "smokes_prob",
                                 0.125, 0.425, [['not e(a,b)', 'e(b,c)', 'not e(a,d)', 'e(d,e)', 'e(e,c)']])


def main():
    unittest.main(buffer=True)

if __name__ == '__main__':
    unittest.main(buffer=True)
