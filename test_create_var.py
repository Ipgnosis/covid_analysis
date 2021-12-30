

list1 = ['USA', 'GBR']
list2 = ['KOR', 'JAP', 'DEU', 'FRA']

for i, val in enumerate(list1):
    print(i, val)
    var_name1 = 'y1-' + str(i)

    print(var_name1)
    globals()[var_name1] = 1000
    temp_var = str('y1-' + str(i))
    print(temp_var)

    var_name2 = 'y2-' + str(i)
    print(var_name2)
    #globals()(var_name1)


for j, val in enumerate(list2):
    print(j, val)
    var_name1 = 'z1-' + str(j)
    print(var_name1)
    #globals()(var_name1)

    var_name2 = 'z2-' + str(j)
    print(var_name2)
    #globals()(var_name2)
