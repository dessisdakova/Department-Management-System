from models import *


def main():
    """
    dev1 = Developer("John", "Doe", 55000, 5)
    dev2 = Developer("Alice", "Smith", 60000, 7)
    dev3 = Developer("Tom", "Harris", 62000, 6)
    dev4 = Developer("Olivia", "Brown", 68000, 8)
    dev5 = Developer("James", "Wilson", 54000, 4)
    dev6 = Developer("Liam", "Davis", 71000, 9)
    dev7 = Developer("Sophia", "Miller", 65000, 7)
    dev8 = Developer("Lucas", "Anderson", 53000, 3)
    dev9 = Developer("Mia", "Thomas", 49000, 2)
    dev10 = Developer("Benjamin", "Jackson", 66000, 6)

    des1 = Designer("Tanya", "Taylor", 50000, 4, 0.8)
    des2 = Designer("Eva", "Johnson", 52000, 6, 0.9)
    des3 = Designer("Rachel", "Martinez", 48000, 3, 0.85)
    des4 = Designer("William", "Clark", 52000, 5, 0.25)
    des5 = Designer("Chloe", "Rodriguez", 46000, 4, 0.75)
    des6 = Designer("Megan", "Lewis", 55000, 7, 0.65)
    des7 = Designer("Ethan", "Walker", 60000, 6, 0.8)
    des8 = Designer("Ava", "Young", 51000, 4, 0.1)
    des9 = Designer("Jackson", "Scott", 53000, 5, 0.85)
    des10 = Designer("Grace", "King", 54000, 6, 0.7)

    manager1 = Manager("Sarah", "Lee", 70000, 10)
    manager2 = Manager("Mark", "White", 75000, 12)
    manager3 = Manager("Emma", "Lopez", 78000, 14)
    manager4 = Manager("David", "Martinez", 80000, 15)
    manager5 = Manager("Charlotte", "Gonzalez", 73000, 11)

    manager1.add_employees_to_team(dev1, dev2, dev3, des1, des2, des3)
    manager2.add_employees_to_team(dev4, des4, des5)
    manager3.add_employees_to_team(dev5, dev6, dev7, des6)
    manager4.add_employees_to_team(des7, des8, des9)
    manager5.add_employees_to_team(dev8, dev9, dev10, des10)

    my_department = Department()
    my_department.add_manager(manager1, manager2, manager3, manager4, manager5)
    my_department.give_salary()
    my_department.save_employees()
    """
    my_department = Department()
    my_department.load_employees()
    for manager in my_department.managers:
        print(manager)
        for member in manager.team:
            print(member)


if __name__ == '__main__':
    main()
