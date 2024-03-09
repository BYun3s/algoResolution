# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 11:01:54 2024

@author: Younes BASRAOUI
"""
from sympy.logic.boolalg import to_cnf, to_dnf

# exp = B & (A | C)  --- non valid
# exp = ~((~P | ~Z | R) & (~R) & P & (~T | Z) & T) ---valid

def main():
    while True:
        exp = input("Entrer une expression logique (Tapez '0' pour quitter) : ")
        
        if exp == '0':
            print("\nFin du programme\n")
            break
        
        not_exp = '~(' + exp + ')'
        print("Expression négation : ", not_exp)

        exp_simp = to_cnf(not_exp)
        print("Expression simplifiée : ", exp_simp)

        exp_simp = str(exp_simp)
        clauses = [clause.split("(")[-1].split(")")[0] for clause in exp_simp.split(" & ")]
        print("clauses : ", clauses)

        clauses_resolvants = []

        i = 0
        taille_cls = len(clauses)

        if taille_cls > 1:
            clauses_resolvants.append(clauses[1])
            del clauses[1]

        while taille_cls - i > 1:
            clause = ''
            c1 = clauses[i].split(" | ")
            c2 = clauses_resolvants[i].split(" | ")

            for literal_c1 in c1[:]:
                for literal_c2 in c2[:]:
                    if (literal_c1 == '~' + literal_c2) or ('~' + literal_c1 == literal_c2):
                        c1.remove(literal_c1)
                        c2.remove(literal_c2)
                        if len(c1) == 0 and len(c2) == 0:
                            print("\nLa Formule est valide\n")
                            return

            for j in range(len(c1)):
                clause = clause + c1[j] + " | "

            for k in range(len(c2)):
                clause = clause + c2[k] + " | "

            clause = clause[0: len(clause) - 2]
            clause = str(to_dnf(clause))

            clauses_resolvants.append(clause)

            i += 1

        clauses.extend(clauses_resolvants)

        print("\nLa Formule n\'est pas valide\n")

if __name__ == "__main__":
        main()