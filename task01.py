import datetime


def is_name(full_name: str) -> bool:
    """
    Проверяем full_name это фамилия/имя? Возвращает True/False
    :param full_name: Жду str "Фамилия Имя"
    :return: Возвращаю True если это так
    """
    if type(full_name) == str and len(full_name.split()) == 2 \
            and full_name.istitle() and full_name.replace(" ", "").isalpha():
        return True
    return False


def check_year(year: int) -> bool:
    """
    Проверяем попадает ли введенный год в диапазон от 1900 до текущего года
    :param year: Жду int, год
    :return: Возвращаю True если год в диапазоне 1900 до текущего года
    """
    if type(year) == int and 1900 < year <= datetime.date.today().year:
        return True
    return False


class Person:
    """
    Class desc
    """
    def __init__(self, full_name: str, birth_year: int):
        self.full_name = full_name
        self.birth_year = birth_year
        assert is_name(self.full_name), "Должно быть два слова с большой буквы через пробел"
        assert check_year(self.birth_year), "Год не может быть меньше 1900 и больше текущего"

    def __str__(self):
        return f"{self.__class__} object: full_name:{self.full_name} birth_year:{self.birth_year}"

    def __iter__(self):
        return iter([self.full_name, self.birth_year])

    def name(self):
        return self.full_name.split()[1]

    def surname(self):
        return self.full_name.split()[0]

    def age(self, year: int = None) -> int:
        if year is None:
            year = datetime.date.today().year
        return year - self.birth_year


class Employee(Person):
    """
    Class desc
    """
    def __init__(self, pos: str = '', exp: int = 0, salary: int = 0, *args):
        self.pos = pos
        self.exp = exp
        self.salary = salary
        super().__init__(*args)
        assert exp >= 0, "Опыт не может быть отрицательным"
        assert salary >= 0, "Зарплата не может быть отрицательной"

    def __str__(self):
        return super().__str__() + f" pos:{self.pos} exp:{self.exp} sal:{self.salary}"

    def __iter__(self):
        return iter([self.pos, self.exp, self.salary] + list(super().__iter__()))

    def full_pos(self):
        if self.exp < 3: return "Junior " + self.pos
        if self.exp > 6: return "Senior " + self.pos
        return "Middle " + self.pos

    def add_salary(self, more_money: int):
        self.salary = self.salary + more_money


class ITEmployee(Employee):
    """
    Class desc
    """
    def __init__(self, *args):
        super().__init__(*args)

    def __str__(self):
        try:
            self.skills
        except AttributeError:
            return super().__str__()
        else:
            return super().__str__() + f" skills:{self.skills}"

    def __iter__(self):
        try:
            self.skills
        except AttributeError:
            return iter(list(super().__iter__()))
        else:
            return iter(self.skills + list(super().__iter__()))

    def add_skill(self, skill: str):
        try:
            self.skills
        except AttributeError:
            self.skills = [skill]
        else:
            self.skills.append(skill)

    def add_skills(self, skills: list):
        try:
            self.skills
        except AttributeError:
            self.skills = skills
        else:
            self.skills.extend(skills)


if __name__ == '__main__':
    p1 = Person("Иванов Иван", 1980)
    print(f"Имя:{p1.name()} Фамилия:{p1.surname()} Возраст в 2000-м:{p1.age(2000)} Возраст сейчас:{p1.age()}")
    # p2 = Person("Ванечка", 2018)
    # p3 = Person("томилов игнат", 1974)
    p1 = Employee("виолончелист", 7, 2300, *p1)
    p2 = Person("Лапушкина Тамара", 1990)
    p2 = Employee("кларнетист", 4, 1500, *p2)
    p3 = Employee("скрипач", 2, 1200, "Передомов Тимур", 1975)
    print(p3.full_pos())
    print(p1.full_pos())
    print("Подняли зарплату", p2.full_name, "c", p2.salary, "до ", end="")
    p2.add_salary(300)
    print(p2.salary)
    p1 = ITEmployee(*p1)
    print(p1)
    p1.add_skill("Лентяй")
    print(p1)
    p1.add_skills(["C", "C++"])
