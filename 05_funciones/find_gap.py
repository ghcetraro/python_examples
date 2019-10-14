#!/usr/bin/python3


def solution(N):
    con = 0
    cont_old = 0
    cont_new = 0
    num_new = 0
    num_old = 0

    for var in N:
        vara = bin(var)
        for car in vara:
            if car != "b":
                car = int(car)
                if car == 0:
                    con = con + 1
                    print("contador : " + str(con))
        print("numero: " + vara + " contador: " + str(con))
        if 1 < con:
            cont_new = con
            if cont_new > cont_old :
                cont_old = cont_new
                num_old = var
        con = 0

    print("gap :" + str(num_old))
    return num_old

N = [1, 3]
print(solution(N))
