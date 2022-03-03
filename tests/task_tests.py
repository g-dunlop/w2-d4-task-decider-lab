import unittest
from src.task import Task

class TaskTest(unittest.TestCase):

    def setUp(self):
        self.task1 = Task("Wash dishes", 30)
        self.task2 = Task("Walk dog", 15)
    
    def test_task_description(self):
        self.assertEqual("Wash dishes", self.task1.description)
        self.assertEqual("Walk dog", self.task2.description)
        
        
    def test_task_has_duration(self):
        self.assertEqual(30, self.task1.duration)
        self.assertEqual(15, self.task2.duration)

    # def test_task_has_preferred_over(self):
    #     self.assertEqual("Walk dog", self.task1.preferred_over[0])