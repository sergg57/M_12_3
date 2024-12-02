import unittest
from runner_and_tournament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Useyn', 10)
        self.runner2 = Runner('Andrey',9)
        self.runner3 = Runner('Nick',3)

    @classmethod
    def tearDownClass(self):
       pass


    def tearDown(self):
        print({key: value.name for key, value in self.all_results.items()})

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testRun_1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        self.all_results = tournament.start()
        # for key, value in self.all_results.items():
        #     print(f'{key} - {value}')
        self.assertTrue(self.all_results.get(max(self.all_results)) == self.runner3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testRun_2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results.get(max(self.all_results)) == self.runner3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testRun_3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results.get(max(self.all_results)) == self.runner3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testRun_4(self):
        tournament = Tournament(6, self.runner1, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results.get(max(self.all_results)) == self.runner3)



if __name__ == '__main__':
    unittest.main()