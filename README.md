Machine de turing simple programmée en python

# Utilisation
```python3 turingMachine.py programme [arguments]```

## Example
```python3 turingMachine.py programs/duplique.TSP 2```

# Fonctionnement

## Représentation de la machine 

![graph-machine](./report/turing-machine.png)

## Les programmes

### Commandes disponibles

| Commande | Signification |
| --- | --- |
| <, > | Déplacer la tête de lecture à gauche ou à droite. |
| state | Afficher l'état de la machine. |
| put(0) et put(1) | Inscrire un 0 ou un 1 sur la bande. |
| loop: | Créer une boucle. |
out(0) et out(1) | Tester la cellule courante avec un 0 ou un 1, quitte la boucle si la condition est validée, quitte le programme s'il n'y a pas de boucle parent. |

### Fonctionnement des boucles
La syntaxe respecte les indentations pour la gestion des boucles (c'est à dire des multiples de tabulation ou 4 espaces)
Observez le schéma suivant : 

```
loop:
    ....
    ....
    loop:
        ....
        ....
        out(0)
        ....
    ....
    out(1)
....
```

*Attention! Veuiillez inclure au moins un out() valide par boucle sous peine d'obtenir une erreur ou une boucle infinie. ¯\\_(ツ)_/¯

### Example
Programme qui duplique un nombre donné
```
state
out(0)
loop:
    out(0)
    >
>
state
loop:
    put(1)
    loop:
        <
        out(0)
    loop:
        <
        out(1)
    state
    <
    out(0)
    >
    put(0)
    loop:
        >
        out(1)
    loop:
        >
        out(0)
state
>

loop:
    >
    out(1)
    put(1)
<
put(0)
>
state
```

### Voici la sortie obtenue :
```
0000000000000000000000000000000000011100000000000000000000000000000000
                                   X                                  

0000000000000000000000000000000000011100000000000000000000000000000000
                                       X                              

0000000000000000000000000000000000011101000000000000000000000000000000
                                     X                                

0000000000000000000000000000000000011001100000000000000000000000000000
                                    X                                 

0000000000000000000000000000000000010001110000000000000000000000000000
                                   X                                  

0000000000000000000000000000000000010001110000000000000000000000000000
                                  X                                   

0000000000000000000000000000000000011101110000000000000000000000000000
                                       X  
```
