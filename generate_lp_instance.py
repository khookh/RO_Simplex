#!/usr/bin/env python3

# Donne Stefano 408801

from sys import argv  # pour récupérer le path d'instance

if len(argv) > 2:
    raise Exception('This script takes only one argument : the instance file path')

instance_path = argv[1]
instance_liste = []

# extract informations from instance file and get it into a list
with open(instance_path, "r") as f:
    for line in f:
        a = ['', '']
        k = 0
        for x in range(0, len(line)):
            if line[x] == ' ':
                k = 1
            if line[x] != ' ' and line[x] != '\n':
                a[k] += line[x]
        instance_liste.append(a)

print(instance_liste)


# create and fill the cplex file
def generate_cplex_lp():
    print('a')
    cplex_lp = open('CPLEX.lp', "w+")

    cplex_lp.write("Minimize\n")
    cplex_lp.write("    " + "obj: ")
    for c in range(0, int(instance_liste[0][1])):
        if c == 0:
            cplex_lp.write("C_" + str(c + 1))
        else:
            cplex_lp.write(" + C_" + str(c + 1))
    cplex_lp.write("\n")

    cplex_lp.write("Subject To\n")
    for j in range(0, int(instance_liste[0][1])):
        cplex_lp.write("    " + "cst"+": ")

    cplex_lp.write("Bounds\n")
    for i in range(0, len(instance_liste) - 1):
        for j in range(0, int(instance_liste[0][1])):
            cplex_lp.write("    " + "X_" + str(i + 1) + "_" + str(j + 1) + " >= 0" + "\n")

    cplex_lp.write("Integer\n")
    for i in range(0, len(instance_liste) - 1):
        for j in range(0, int(instance_liste[0][1])):
            cplex_lp.write("    " + "X_" + str(i + 1) + "_" + str(j + 1) + "\n")

    cplex_lp.write("Binary\n")
    for c in range(0, int(instance_liste[0][1])):
        cplex_lp.write("    " + "C_" + str(c + 1) + "\n")


generate_cplex_lp()
