import unittest
from src.task_decider import get_preferred_option
from src.task import Task

class TaskDeciderTest(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("Cook Dinner", 10)
        self.task2 = Task("Clean Windows", 15)
        self.task3 = Task("Wash Dishes", 30)
    

    def test_is_task_passing(self):
        self.assertEqual(self.task1, get_preferred_option(self.task1, self.task2))
        # self.assertEqual(self.task2, get_preferred_option(self.task2, self.task1))

    def test_clean_windows_over_wash_dishes(self):
        self.assertEqual(self.task2, get_preferred_option(self.task2, self.task3))

    def test_wash_dishes_under_clean_windows(self):
        self.assertEqual(self.task2, get_preferred_option(self.task3, self.task2))
        
    
        


