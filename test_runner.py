import unittest
from runner_and_tournament import Runner, Tournament

class RunnerTest(unittest.TestCase):
    is_frozen = False
    def setUp(self):
        self.runner1 = Runner('Useyn', 10)
        self.runner2 = Runner('Andrey',9)
        self.runner3 = Runner('Nick',3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testRun_1(self):
        self.runner1.run()
        self.assertEqual(self.runner1.distance, 20)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testRun_2(self):
        self.runner2.run()
        self.assertEqual(self.runner2.distance, 18)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testRun_3(self):
        self.runner3.run()
        self.assertEqual(self.runner3.distance, 6)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testWalk_1(self):
        self.runner1.walk()
        self.assertEqual(self.runner1.distance, 10)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testWalk_2(self):
        self.runner2.walk()
        self.assertEqual(self.runner2.distance, 9)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testWalk_3(self):
        self.runner3.walk()
        self.assertEqual(self.runner3.distance, 3)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testStr_1(self):
        self.assertEqual(str(self.runner1), 'Useyn')

    def testStr_2(self):
        self.assertEqual(str(self.runner2), 'Andrey')

    def testStr_3(self):
        self.assertEqual(str(self.runner3), 'Nick')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testEq_1(self):
        self.assertTrue(self.runner1 == 'Useyn')
        self.assertFalse(self.runner1 == 'Nick')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testEq_2(self):
        self.assertTrue(self.runner2 == 'Andrey')
        self.assertFalse(self.runner2 == 'Nick')

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def testEq_3(self):
        self.assertTrue(self.runner3 == 'Nick')
        self.assertFalse(self.runner3 == 'Useyn')


if __name__ == '__main__':
    unittest.main()