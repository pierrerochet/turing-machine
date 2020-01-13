#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:52:39 2019

@author: rochet
"""

import sys
import numpy as np


class Machine:
    def __init__(self):
        self.tape = np.zeros(70, dtype='int32')     # la bande
        self.head = 0                               # la tête de lecture
        self.pile = []                              # la pile
      
    def init(self, args):
        '''initilise la bande de la machine avec les nombres passés en argument'''
        for n in args:
            for _ in range(n+1):
                self.put('1')
                self.move('>')
            self.move('>')
        self.head = 0
            
    def move(self, direction):
        '''déplace la tête de lecture à gauche ou à droite'''
        if direction == '>':
            self.head += 1
        if direction == '<':
            self.head -= 1
            
    def put(self, element):
        '''écrit un élement sur la bande (normalment 0 ou 1)'''
        self.tape[self.head] = element
    
    def state(self):
        '''renvoie l'état de la machine (repreoduction de la sortie de la 
                                         machine JAVA de M. Del Vigna)'''
        tape_str = [str(ele) for ele in self.tape]
        head_str = [" " for ele in self.tape]
        head_str[self.head] = 'X'
        return f'{"".join(tape_str)}\n{"".join(head_str)}\n'
    
    def loop(self, i):
        '''ajoute les adresses de début et de fin d'une boucle dans la pile'''
        start = i #adresse de la première instruction de la boucle
        end = i #adresse de la fin de la boucle
        n = len(self.pile) +1
        while len(prog) != end and (prog[end].startswith('\t'*n) or prog[end].startswith(' '*4*n)):
             end += 1
        self.pile.append(slice(start, end))
        
    def out(self, condition):
        '''vérifie si la condition de sortie est réalisée'''
        if self.tape[self.head] == int(condition):
            return True

    def execute_progr(self, prog_path):
        '''lit le programme et exécute ses instructions'''
        with open(prog_path, 'r', encoding='utf8') as sc:
            global prog # variable global pour se faciliter la vie
            prog = sc.read().split('\n')
        self.execute_inst(end=len(program))

    def execute_inst(self, start=0, end=0, boucle=False):
        '''exécute une liste d'instructions de l'indice "start" à l'indice 
        "end" avec une option de récursivité'''
        # i est l'indice de l'instruction courante
         
        i = start
        while i != end:
            
            # Vérifie l'identité de l'instruction courante --------------------
            line = prog[i]
            if '<' in line or '>' in line :
                self.move(line[-1])
            elif 'put' in line:
                self.put(line[-2])
            elif 'state' in line:
                print(self.state())
            elif 'out' in line:
                # === Fonciotnnement de la sortie de boucle ===================
                
                # Si on rencontre un out(0|1) valide alors on arrête la 
                # récursivité et on sort de la boucle. Permet également de 
                # quitter le programme si nous ne sommes pas dans une boucle.
                if self.out(line[-2]) == True:
                    boucle = False
                    break
                # =============================================================
                
                
            if 'loop:' in line:
            # -----------------------------------------------------------------
            
                # ==== Foncionnement d'une boucle =============================
            
                i += 1
                # 1.
                # On cherche l'adresse de la première instruction et l'adresse
                # de la dernière instruction de la boucle que l'on ajoute à la 
                # pile.
                self.loop(i)
                
                # 2.
                # On exécute la même fonction avec les indices stockés dans le 
                # dernier élément de la pile. Puisque c'est une boucle : 
                # on indique boucle=True pour lancer la récursivité
                self.execute_inst(start=self.pile[-1].start, 
                                  end=self.pile[-1].stop, 
                                  boucle=True)
                # 3.
                # La boucle est terminée donc on dépile. Le dernier élément de 
                # la pile est donc retiré. On en profite pour mettre à jour 
                # notre indice d'instruction qui devient l'indice de la dernière 
                # instruction de la dernière boucle.
                addr = self.pile.pop(-1)
                i = addr.stop - 1
                
                # 4.
                # On remet à jour la limite des instructions à éxécuter.
                # On reprend donc l'indice de la dernière instruction de la 
                # boucle parent ou la dernière instruction du programme si 
                # la pile est vide
                if self.pile != []: end = self.pile[-1].stop
                else: end = len(prog)
                
                # =============================================================
            
            # on augmente notre indice pour chaque instruction traitée
            i += 1
        
        # Si nous sommes dans une boucle alors elle est éxécutée tant que nous
        # ne rencontrons pas de out(0|1) valide.
        if boucle:
            self.execute_inst(start=start, end=end, boucle=True)
            

if __name__ == '__main__':
    program = sys.argv[1]
    numbers = [int(n) for n in sys.argv[2:]]
    machine = Machine()
    machine.init(numbers)
    machine.execute_progr(program)
    
