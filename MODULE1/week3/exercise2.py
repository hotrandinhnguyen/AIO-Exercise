from typing import Any


class Ward:

    def __init__(self, name):
        self.__name = name
        self.__ward_list = []

    def add_person(self, person):
        self.__ward_list.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for person in self.__ward_list:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__ward_list:
            if isinstance(person, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.__ward_list.sort(key=lambda person: person.age(), reverse=True)
        return self.__ward_list

    def compute_average(self):
        self.sum_of_age = 0
        self.count = 0
        for person in self.__ward_list:
            if isinstance(person, Teacher):
                self.sum_of_age += person.age()
                self.count += 1
        return self.sum_of_age/self.count


class Student:

    def __init__(self, name, yob, grade):
        self.__name = name
        self.__yob = yob
        self.__grade = grade

    def age(self):
        return self.__yob

    def describe(self):
        print(
            f"Student - Name: {self.__name} - YoB: {self.__yob} - Grade: {self.__grade}")

    def __call__(self):
        return f"Student - Name: {self.__name} - YoB: {self.__yob} - Grade: {self.__grade}"


class Doctor:

    def __init__(self, name, yob, specialist):
        self.__name = name
        self.__yob = yob
        self.__specialist = specialist

    def age(self):
        return self.__yob

    def describe(self):
        print(
            f"Doctor - Name: {self.__name} - YoB: {self.__yob} - Specialist: {self.__specialist}")

    def __call__(self):
        return f"Doctor - Name: {self.__name} - YoB: {self.__yob} - Specialist: {self.__specialist}"


class Teacher:

    def __init__(self, name, yob, subject):
        self.__name = name
        self.__yob = yob
        self.__subject = subject

    def age(self):
        return self.__yob

    def describe(self):
        print(
            f"Teacher - Name: {self.__name} - YoB: {self.__yob} - Subject: {self.__subject}")

    def __call__(self):
        return f"Teacher - Name: {self.__name} - YoB: {self.__yob} - Subject: {self.__subject}"


if __name__ == "__main__":
    # 2a
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()
    # 2b
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()
    # 2c
    print(f"\nNumber of doctors : {ward1.count_doctor()}")
    # 2d
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()
    # 2e
    print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
