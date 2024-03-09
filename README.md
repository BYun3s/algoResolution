# Algorithme de Resolution


## Objectif : Résolution de formules logiques

Ce script Python permet de saisir des expressions logiques et de vérifier si elles sont valides en les convertissant en forme normale conjonctive (CNF) et en résolvant les clauses.


## Prérequis

Assurez-vous d`avoir ``Python 3.11``</br>
Ce script utilise la bibliothèque ``sympy``. Pour l'installer, vous pouvez exécuter cette commande dans votre terminal ``pip install sympy``    


## Utilisation

1. Lancez le script.

2. Saisissez une expression logique. 

3. Le programme affichera si l`expression logique est valide ou non.


## Forme de formules a saisir

La formule doit être écrite en utilisant les opérateurs suivants:

 - les quantificateurs `et` pour `&`, `ou` pour `|`, `!` pour `~`, `=>` pour `>>`.

 - Les alphabets autorise sont  les lettres majuscules ou miniscules (A, B, ... ) a l'exception de (E, Q)

 - les alphabets et les quantificateur doivent  être séparés par des espaces.


## Exemples

Voici quelques exemples d`expressions logiques que vous pouvez saisir :

- B & (A | C) 

- ~((~P | ~Z | R) & (~R) & P & (~T | Z) & T)


## Auteur

 - Ce script a été développé par **Younes BASRAOUI**