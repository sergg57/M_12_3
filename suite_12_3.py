import unittest
import test_runner
import test_turnament

testerST = unittest.TestSuite()
testerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.RunnerTest))
testerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_turnament.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testerST)