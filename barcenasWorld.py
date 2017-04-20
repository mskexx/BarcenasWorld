#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pycosat


class World(object):
    ''' Create a new "world" in order to search Barcenas on it
        You will be helped by Mariano and Cospedal once you find them
    '''

    def __init__(self, size):
        self.size = size
        self.world = self.generate_world()

    def generate_world(self):
        ''' Generate matrix filled with 1 '''

        tmp = [1] * self.size
        matrix = []
        for i in xrange(0, self.size):
            matrix.append(list(tmp))

        matrix[-1][0] = 0
        matrix[-1][1] = 2
        return matrix

    ######### Print World #########

    def print_world(self, positions):
        ''' Print whole map '''
        #First Row
        self.print_superior()
        #Body
        for i in xrange(1, self.size+1):
            for j in xrange(0, self.size):
                sys.stdout.write("║ " + str(positions[self.size-i+(j*self.size)])+ " ")
            sys.stdout.write("║")
            if i < self.size:
                self.print_row()
        #Last Row
        self.print_inferior()


    def print_row(self):
        ''' Print row separation '''
        sys.stdout.write("\n╠═")
        for i in xrange(0, self.size-1):
            sys.stdout.write("══╬═")
        sys.stdout.write("══╣\n")


    def print_superior(self):
        ''' Print superior border '''

        sys.stdout.write("\n╔═")
        for i in xrange(0, self.size-1):
            sys.stdout.write("══╦═")
        sys.stdout.write("══╗\n")


    def print_inferior(self):
        ''' Print inferior border '''

        sys.stdout.write("\n╚═")
        for i in xrange(0, self.size-1):
            sys.stdout.write("══╩═")
        print "══╝"

class Problem():
    ''' In order to find Barcenas' position, we will use the help of SatSolver '''

    def __init__(self):
        self.size = int(sys.argv[1])
        self.world = World(self.size)
        self.globalsize = self.size * self.size
        self.cnf = self.initformula()
        self.top,self.bot = self.getlimits()
        self.discard = [1]
        self.process_steps()

    def initformula(self):
        ''' Init clauses '''
        cnf = []
        cnf.append(range(1, self.globalsize + 1))
        cnf.append([-1]) #Barcenas not in (1,1)
        return cnf

    def process_steps(self):
        ''' Process the steps '''
        self.world.print_world(self.check_sat()) #Print initial status of the world

        for step in sys.argv[2:]:
            step = eval(step)
            pos = step[0] + self.size * (step[1]-1)
            print "Procesando posicion " + str(step[0]) + "," + str(step[1]) +\
                    " correspondiente a " + str(pos)

            self.discard.append(pos)
            self.smell(pos, step[2])
            self.world.print_world(self.check_sat())

    def smell(self, position, smelled):
        if position in self.top:
            smells = [position - 1, position + self.size, position - self.size]
        elif position in self.bot:
            smells = [position + 1, position + self.size, position - self.size]
        else:
            smells = [position + 1, position - 1, position + self.size, position - self.size]

        if smelled:
            for i in xrange(1, self.globalsize+1):
                if (i not in smells) and (i not in self.discard):
                    self.discard.append(i)
                    self.cnf.append([-i])
        else:
            for pos in smells:
                if (pos > 0) and (pos < self.globalsize):
                    self.discard.append(pos)
                    self.cnf.append([-pos])

    def check_sat(self):
        solution = []
        for i in xrange(self.globalsize):
            clau = self.cnf + [[i+1]]
            sat = pycosat.solve(clau) #--- Call to pycosat ---
            if isinstance(sat, basestring):
                solution.append(0)
            else:
                solution.append(1)
        return solution

    def getlimits(self):
        top = []
        bot = []
        for i in xrange(self.size):
            top.append(self.size*(i+1))
            bot.append(self.size*i+1)
        return top,bot
if __name__ == '__main__':
    Problem()
