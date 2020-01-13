Machine de turing simple programmée en python


# Utilisation

```python turingMachine.py [programme] [argument1] [argument2] [...]```

## Exemple
```python turingMachine.py programs/duplique.TSP 2```


# Syntaxe des programmes

## Commandes disponibles

| Commande | Signification |
| --- | --- |
| > | Déplacer la tête de lecture à droite. |
| < | Déplacer la tête de lecture à gauche. |
| state | Afficher l'état de la machine. |
| put(0) et put(1) | Inscrire un 0 ou un 1 sur la bande. |
| loop: | Créer une boucle. |
out(0) et out(1) | Tester la cellule courante avec un 0 ou un 1, quitte la boucle si la condition est validée, quitte le programme s'il n'y a pas de boucle parent. |

## Fonctionnement des boucles
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

*Attention! Ne pas oublier d'inclure au moins un out() valide pour chaque boucle sous peine de créer une boucle infinie*. Sauf si vous aimez vivre dangereusement   ¯\\_(ツ)_/¯

## Exemple
Programme qui duplique un nombre donné
```
state
out(0)
state
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
0000000000000000000000000000000000011111111111111111000000000000000000
                                   X                                  

0000000000000000000000000000000000011111111111111111000000000000000000
                                   X                                  

0000000000000000000000000000000000011111111111111111000000000000000000
                                                     X                

0000000000000000000000000000000000011111111111111111010000000000000000
                                                   X                  

0000000000000000000000000000000000011111111111111110011000000000000000
                                                  X                   

0000000000000000000000000000000000011111111111111100011100000000000000
                                                 X                    

0000000000000000000000000000000000011111111111111000011110000000000000
                                                X                     

0000000000000000000000000000000000011111111111110000011111000000000000
                                               X                      

0000000000000000000000000000000000011111111111100000011111100000000000
                                              X                       

0000000000000000000000000000000000011111111111000000011111110000000000
                                             X                        

0000000000000000000000000000000000011111111110000000011111111000000000
                                            X                         

0000000000000000000000000000000000011111111100000000011111111100000000
                                           X                          

0000000000000000000000000000000000011111111000000000011111111110000000
                                          X                           

0000000000000000000000000000000000011111110000000000011111111111000000
                                         X                            

0000000000000000000000000000000000011111100000000000011111111111100000
                                        X                             

0000000000000000000000000000000000011111000000000000011111111111110000
                                       X                              

0000000000000000000000000000000000011110000000000000011111111111111000
                                      X                               

0000000000000000000000000000000000011100000000000000011111111111111100
                                     X                                

0000000000000000000000000000000000011000000000000000011111111111111110
                                    X                                 

0000000000000000000000000000000000010000000000000000011111111111111111
                                   X                                  

0000000000000000000000000000000000010000000000000000011111111111111111
                                  X                                   

0000000000000000000000000000000000011111111111111111011111111111111111
                                                     X 
```
