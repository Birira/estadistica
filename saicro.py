def contarRep(num, comp):
    cont = 0
    for i in str(num):
        if int(i) == comp:
            cont += 1
    return cont

var = contarRep(123455565, 5)
print(var)