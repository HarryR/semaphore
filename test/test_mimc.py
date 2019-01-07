import unittest

from ethsnarks.mimc import mimc, mimc_hash


class TestJubjub(unittest.TestCase):
    def test_encipher(self):
        # Verify cross-compatibility with EVM/Solidity implementation
        assert mimc(3703141493535563179657531719960160174296085208671919316200479060314459804651,
                    134551314051432487569247388144051420116740427803855572138106146683954151557,
                    b'mimc') == 11437467823393790387399137249441941313717686441929791910070352316474327319704
        assert mimc_hash([3703141493535563179657531719960160174296085208671919316200479060314459804651,
                          134551314051432487569247388144051420116740427803855572138106146683954151557],
                         918403109389145570117360101535982733651217667914747213867238065296420114726,
                         b'mimc') == 15683951496311901749339509118960676303290224812129752890706581988986633412003


if __name__ == "__main__":
    unittest.main()