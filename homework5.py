immutable_var = 1, 2, 'a', 'b'
print(immutable_var)

mutable_list = [1, 2, 'a', 'b']
print(mutable_list)
mutable_list [0] = 5
print(mutable_list)

immutable_var[0]= 5   # пренесла ниже, чтобы остальной код работал
print(immutable_var) # изменение не возможно, так как объекты "tuple" не поддерживает изменение элементов
