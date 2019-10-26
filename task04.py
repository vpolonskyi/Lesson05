import unittest
import datetime
import task01


class ITEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.res = task01.ITEmployee("арфист", 2, 2300, "Зеленухина Любовь", 1979)

    def testExceptions(self):
        with self.assertRaises(AssertionError):
            task01.ITEmployee("арфист", 2, 2300, "зеленухина Любовь", 1979)
        self.assertRaises(AssertionError, task01.ITEmployee, "арфист", 2, 2300, "Зеленухина Любовь", -979)

    def testAttributes(self):
        self.assertEqual(self.res.full_name, "Зеленухина Любовь")
        self.assertEqual(self.res.birth_year, 1979)
        self.assertEqual(self.res.pos, "арфист")
        self.assertEqual(self.res.exp, 2)
        self.assertEqual(self.res.salary, 2300)

    def testFunc(self):
        self.assertEqual(self.res.name(), "Любовь")
        self.assertEqual(self.res.surname(), "Зеленухина")
        self.assertEqual(self.res.age(), datetime.date.today().year - self.res.birth_year)
        self.assertEqual(self.res.age(2000), 21)
        self.assertEqual(self.res.full_pos(), "Junior арфист")
        self.res.exp = 4
        self.assertEqual(self.res.full_pos(), "Middle арфист")
        self.res.exp = 6
        self.assertEqual(self.res.full_pos(), "Middle арфист")
        self.res.add_salary(5)
        self.assertEqual(self.res.salary, 2305)
        self.res.add_salary(-10)
        self.assertEqual(self.res.salary, 2295)
        self.res.add_skill("Лентяй")
        self.assertEqual(self.res.skills, ["Лентяй"])
        self.res.add_skill("Дважды лентяй")
        self.assertEqual(self.res.skills, ["Лентяй", "Дважды лентяй"])
        self.res.add_skills(["C", "C++"])
        self.assertEqual(self.res.skills, ["Лентяй", "Дважды лентяй", "C", "C++"])
        self.res.add_skills(["C#", "C$"])
        self.assertEqual(self.res.skills, ["Лентяй", "Дважды лентяй", "C", "C++", "C#", "C$"])
        self.res.skills = []
        self.res.add_skills(["py", "go"])
        self.assertEqual(self.res.skills, ["py", "go"])
        self.res.add_skill("fortran")
        self.assertEqual(self.res.skills, ["py", "go", "fortran"])
