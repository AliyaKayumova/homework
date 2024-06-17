grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_abc = sorted(students)
a = sum(grades[0])/len(grades[0])
b = sum(grades[1])/len(grades[1])
c = sum(grades[2])/len(grades[2])
d = sum(grades[3])/len(grades[3])
i = sum(grades[4])/len(grades[4])
end = {students_abc [0]: a , students_abc [1]: b , students_abc[2]: c , students_abc[3]: d , students_abc[4]: i}
print(end)
