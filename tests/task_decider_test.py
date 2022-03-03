import unittest
from src.task_decider import get_preferred_option
from src.task import Task

class TaskDeciderTest(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("Cook Dinner", 10)
        self.task2 = Task("Clean Windows", 15)
        self.task3 = Task("Wash Dishes", 30)
        self.task4 = Task("Do Ironing", 25)
        self.task5 = Task("Wash Clothes", 50)
    

    def test_cook_dinner_over_do_ironing(self):
        self.assertEqual(self.task1, get_preferred_option(self.task1, self.task4))
        # self.assertEqual(self.task2, get_preferred_option(self.task2, self.task1))

    def test_do_ironing_under_cook_dinner(self):
        self.assertEqual(self.task1, get_preferred_option(self.task4, self.task1))

    def test_clean_windows_over_wash_dishes(self):
        self.assertEqual(self.task2, get_preferred_option(self.task2, self.task3))

    def test_wash_dishes_under_clean_windows(self):
        self.assertEqual(self.task2, get_preferred_option(self.task3, self.task2))


        
    
        


