#!/usr/bin/python
# -*- coding: utf-8 -*-

''' Exec: ./barcenas_world <Size> [Step1] [Step2] ...

    In order to find Barcenas, following a given steps we recollect some
    information about his position. Mariano and Cospedal will add extra info
    of the suspect position

    Every info collected is added into a CNF used by pycosat.'''

import sys
import pycosat

__author__ = "Marcos Susin Nasarre"
__license__ = "GPL 3"
__version__ = "1.0"
__maintainer__ = "Marcos Susin"
__email__ = "msn3@alumnes.udl.cat"


class World(object):
    ''' Create a new "world" in order to search Barcenas on it
        You will be helped by Mariano and Cospedal once you find them
    '''

    def __init__(self, size):
        self.size = size  #Size of the world NxN

    ######### Print World #########

    def print_world(self, positions):
        ''' Print whole map '''
        self.print_superior() #Print top border

        for i in xrange(1, self.size+1): #Print body
            for j in xrange(0, self.size):
                sys.stdout.write("║ " + str(positions[self.size-i+\
                (j*self.size)])+ " ")
            sys.stdout.write("║")
            if i < self.size:
                self.print_row()

        self.print_inferior() #Print bot border

    def print_row(self):
        ''' Print row separation '''
        sys.stdout.write("\n╠═")
        for _ in xrange(0, self.size-1):
            sys.stdout.write("══╬═")
        sys.stdout.write("══╣\n")

    def print_superior(self):
        ''' Print top border '''
        sys.stdout.write("╔═")
        for _ in xrange(0, self.size-1):
            sys.stdout.write("══╦═")
        sys.stdout.write("══╗\n")

    def print_inferior(self):
        ''' Print inferior border '''
        sys.stdout.write("\n╚═")
        for _ in xrange(0, self.size-1):
            sys.stdout.write("══╩═")
        print "══╝"


class Problem(object):
    ''' In order to find Barcenas' position, will use the help of SatSolver '''

    def __init__(self):
        self.size = int(sys.argv[1])
        self.world = World(self.size) #World to print
        self.globalsize = self.size * self.size #Number of total positions
        self.cnf = self.initformula()
        self.top, self.bot = self.getlimits()
        self.discard = [1]
        self.process_steps()

    def initformula(self):
        '''
            Init clauses: [1|2|3...][-1]
            Position: (1,1) discard automatically
        '''
        cnf = [] #Global formula used to accumulate information = Gamma Formula
        cnf.append(range(1, self.globalsize + 1)) #Global OR Clause
        cnf.append([-1]) #Barcenas not in (1,1)
        return cnf

    def process_steps(self):
        ''' Process all the given steps '''
        not_mariano = True  #Mariano not found yet
        not_cospedal = True #Cospedal not found yet
        mariano_lie = False #Cospedal info about Mariano
        pos_mariano = None  #Initialize var of Mariano position
        info_mariano = None #Initialize var of Mariano information

        print "+--+ THIS IS THE INITIAL STATE OF BARCENAS WORLD +--+"
        self.world.print_world(self.check_sat()) #Print initial status world

        for step in sys.argv[2:]:
            step = eval(step)
            pos = self.size * (step[0]-1) + step[1] #Number position <-- coord
            print "\n\n--> Processing position (" + str(step[0]) +\
                    "," + str(step[1]) + ")"

            self.discard.append(pos) #Actual position is not valid for Barcenas
            self.smell(pos, step[2]) #Process smell info

            if step[3] != -1 and not_mariano: #Mariano detected now
                not_mariano = False #Ignore future possible encounter
                if not_cospedal: #Cospedal is not found yet, save Mariano Pos.
                    print "-- Mariano says Barcenas is on direction " \
                            + str(step[3]) + " from position num: " + str(pos)
                    pos_mariano = pos
                    info_mariano = step[3]

                else:
                    if mariano_lie: #If Cospedal said before Mariano will lie
                        self.process_mariano(pos_mariano, abs(step[3]-1))
                        #We reverse the process cause Mariano lied

                    else: #Mariano is telling the truth, said Cospedal
                        self.process_mariano(pos_mariano, step[3])

            if step[4] != -1 and not_cospedal:#Cospedal detected and not before
                not_cospedal = False
                if step[4] and not_mariano: #Mariano not found yet
                    print " -- Cospedal warn that Mariano will LIE --"
                    mariano_lie = True

                elif not not_mariano: #Mariano found before Cospedal
                    if step[4]:
                        print "-- Cospedal says Mariano LIED --"
                        self.process_mariano(pos_mariano, abs(info_mariano-1))

                    else:
                        print "-- Cospedal says Mariano said the TRUTH --"
                        self.process_mariano(pos_mariano, info_mariano) #no Lie

            print "-- ACTUAL MAP STATUS -- "
            self.world.print_world(self.check_sat()) #Map status after Step

    def smell(self, position, smelt):
        ''' If Barcenas is smelt, we discard every position in the map, except
            surround position '''

        if position in self.top: #Position is in top limit
            smells = [position - 1, position + self.size, position - self.size]
        elif position in self.bot: #Position is on bot limit
            smells = [position + 1, position + self.size, position - self.size]
        else: #Position is in the middle of the map
            smells = [position + 1, position - 1, position + self.size,\
                    position - self.size]

        if smelt: #Barcenas is detected in sorrounding positions
            for pos in xrange(1, self.globalsize+1):#Every not surround discard
                if (pos not in smells) and (pos not in self.discard):
                    self.discard.append(pos)
                    self.cnf.append([-pos])
        else:
            for pos in smells: #Only sorrounding positions are discard
                if (pos > 0) and (pos < self.globalsize):
                    self.discard.append(pos)
                    self.cnf.append([-pos])

    def check_sat(self):
        ''' pycosat to resolve the formula '''
        solution = []
        for i in xrange(self.globalsize):
            clau = self.cnf + [[i+1]] #Try every position with actual formula
            sat = pycosat.solve(clau) #--- Call to pycosat ---
            if isinstance(sat, basestring): #Pycosat return "UNSAT" = String
                solution.append(0)
            else: #Pycosat retorn a solution = SAT
                solution.append(1)
        return solution

    def process_mariano(self, pos, left):
        ''' With the information provided by Mariano & Cospedal, discard every
            positions not related with this information '''

        # 1 Left || 0 Right
        column = pos/self.size

        if pos%self.size == 0: #Limit of column
            column = column - 1

        if not left: #Barcenas is on right side of Mariano
            for i in xrange(1, ((column + 1)*self.size) + 1): #Discard leftside
                if i not in self.discard:
                    self.discard.append(i) #Discard Positions = Add Clause CNF
                    self.cnf.append([-i])

        else: #Barcenas is on left side of Mariano
            for i in xrange((column*self.size) + 1, self.globalsize):
                print i
                if i not in self.discard:
                    self.discard.append(i) #Discard Positions = Add Clause CNF
                    self.cnf.append([-i])

    def getlimits(self):
        ''' Return map limits positions '''
        top = []
        bot = []
        for i in xrange(self.size):
            top.append(self.size*(i+1)) #Add top position of each column
            bot.append(self.size*i+1)   #Add bottom position of each column
        return top, bot

if __name__ == '__main__':
    Problem() #Init principal class problem
