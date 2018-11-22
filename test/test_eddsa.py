import unittest
from os import urandom


from ethsnarks.jubjub import JUBJUB_L, Point, FQ
from ethsnarks.eddsa import eddsa_sign, eddsa_verify


class TestEdDSA(unittest.TestCase):
	def test_signverify(self):
		B = Point.from_hash(b'eddsa_base')
		k = FQ.random(JUBJUB_L)
		m = urandom(32)
		R, S, A = eddsa_sign(m, k, B)
		self.assertTrue(eddsa_verify(A, R, S, m, B))

	def test_fixedcase_1(self):
		B = Point(FQ(21609035313031231356478892405209584931807557563713540183143349090940105307553),
				  FQ(845281570263603011277359323511710394920357596931617398831207691379369851278))
		A = Point(FQ(5616630816018221659484394091994939318481030030481519242876140465113436048304),
				  FQ(8476221375891900895034976644661703008703725320613595264559419965669922411183))
		R = Point(FQ(17883110238616315155327756854433987355427639458557188556819876765548551765197),
				  FQ(11833558192785987866925773659755699683735551950878443451361314529874236222818))
		s = 9920504625278683304895036460477595239370241328717115039061027107077120437288
		m = b'abc'
		self.assertTrue(eddsa_verify(A, R, s, m, B))


if __name__ == "__main__":
	unittest.main()
