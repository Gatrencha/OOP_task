class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def mean_grading(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.mean_grading() < other.mean_grading()


    def __str__(self):
        result = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mean_grading()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
            f'Завершенные курсы: {", ".join(self.finished_courses)}\n')
        return (result)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def mean_grading(self):
        result = sum(*self.grades.values()) / len(*self.grades.values())
        return result


class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}

    def __str__(self):
        result = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.mean_grading()}\n')
        return (result)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a  Lecturer!')
            return
        return self.mean_grading() < other.mean_grading()

class Reviewer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        result = (
            f'Имя: {self.name}\nФамилия: {self.surname}\n')
        return (result)

#student-1
ryo_student = Student('Ruoy', 'Eman', 'your_gender')
ryo_student.courses_in_progress += ['Python','Git']
ryo_student.finished_courses += ['Знакомство с платформой']

#student-2
jhon_student = Student('Jhon', 'MClane', 'your_gender')
jhon_student.courses_in_progress += ['Python','Git']
jhon_student.finished_courses += ['Знакомство с платформой']

#lecturer-1
best_lecturer = Lecturer('Some', 'Buddy')
best_lecturer.courses_attached += ['Python']

#lecturer-2
notbest_lecturer = Lecturer('Buddy', 'Some')
notbest_lecturer.courses_attached += ['Python']

#reviewer-1
good_reviewer = Reviewer('Cool', 'Guy')
good_reviewer.courses_attached += ['Python']

bad_reviewer = Reviewer('Bad', 'Guy')
bad_reviewer.courses_attached += ['Python']

#lecture_ratings
ryo_student.rate_lect(best_lecturer,'Python',10)
ryo_student.rate_lect(best_lecturer,'Python',9)
ryo_student.rate_lect(best_lecturer,'Python',8)

ryo_student.rate_lect(notbest_lecturer,'Python',10)
ryo_student.rate_lect(notbest_lecturer,'Python',9)
ryo_student.rate_lect(notbest_lecturer,'Python',8)

jhon_student.rate_lect(best_lecturer,'Python',10)
jhon_student.rate_lect(best_lecturer,'Python',9)
jhon_student.rate_lect(best_lecturer,'Python',8)

jhon_student.rate_lect(notbest_lecturer,'Python',10)
jhon_student.rate_lect(notbest_lecturer,'Python',9)
jhon_student.rate_lect(notbest_lecturer,'Python',8)

#hw_ratings
good_reviewer.rate_hw(ryo_student,'Python',10)
good_reviewer.rate_hw(jhon_student,'Python',7)

bad_reviewer.rate_hw(ryo_student,'Python',8)
bad_reviewer.rate_hw(jhon_student,'Python',7)


student_list = []
lecture_list = []

student_list.append(ryo_student)
student_list.append(jhon_student)
student_grades = []


lecture_list.append(best_lecturer)
lecture_list.append(notbest_lecturer)
lecture_grades = []

def average_rate_stud(student_list,course_name):
    for student in student_list:
        for key, value in student.grades.items():
            if key is course_name:
                student_grades.extend(value)
    mean_gr_st = sum(student_grades) / len(student_grades)
    print('Средний балл по всем студентам курса ',course_name,' :',mean_gr_st)

def average_rate_lect(lecture_list,course_name):
    for lecturer in lecture_list:
        for key, value in lecturer.grades.items():
            if key is course_name:
                lecture_grades.extend(value)
    mean_gr_lr = sum( lecture_grades) / len( lecture_grades)
    print('Средний балл по всем лекторам курса ',course_name,' :',mean_gr_lr)


print('Данные о студентах:')
print(ryo_student,"\n",jhon_student)

print('Данные о лекторах:')
print(best_lecturer,"\n",notbest_lecturer)

print('Данные о ревьюерах:')
print(good_reviewer,"\n",bad_reviewer)

print(ryo_student > jhon_student)
print(best_lecturer < notbest_lecturer)

average_rate_lect(lecture_list,'Python')
average_rate_stud(student_list,'Python')

