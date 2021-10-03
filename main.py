#Cортировочка подсчетом
def SortStart(massivchik):
    if len(massivchik)<2:
        return "Ну тут нечего и сортировать то c:"
    else:
        b = max(massivchik)+1
        c = [0]*b
        for i in massivchik:
            c[i] += 1
        massivchik[:] = []
        for i in range(b):
            massivchik += [i]*c[i]
        return massivchik


b = input("Введите массив чисел: ")
a = b.split()
massiveNoSort = [int(item) for item in a if item.isdigit()]#массив из чисел
print(SortStart(massiveNoSort))