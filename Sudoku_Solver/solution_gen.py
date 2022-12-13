from input import Possible_Sols
import numpy
import random
import Global_Dim
from math import remainder

class Mutate_solution_Class(object):
    
    def mutate_parents(self, parent1, parent2, mutate_parentsRate):
        mut_sol1 = Possible_Sols()
        mut_sol2 = Possible_Sols()
        mut_sol1.given_Val_sudoku = numpy.copy(parent1.given_Val_sudoku)
        mut_sol1.match_percent = parent1.match_percent
        mut_sol2.given_Val_sudoku = numpy.copy(parent2.given_Val_sudoku)
        mut_sol2.match_percent = parent2.match_percent
        # Random numbers and distribution is given by hit and trail and set to 1.2 
        # for faster solutions when given easier puzzles
        rand_num = random.uniform(0, 1.2)
        while(rand_num * Global_Dim.Glob_Gone > 1):  
            rand_num = random.uniform(0, 1.2)   
        if (rand_num > mutate_parentsRate):
            pass
        elif(rand_num < mutate_parentsRate):
            # Producing Random Numbers into Mutated parents
            mutate_parentsPoint1 = random.randint(0, 8)
            mutate_parentsPoint2 = random.randint(1, 9)
            while(mutate_parentsPoint1 == mutate_parentsPoint2):
                  mutate_parentsPoint1 = random.randint(0, 8)
                  mutate_parentsPoint2 = random.randint(1, 9)  
            if(mutate_parentsPoint1 < mutate_parentsPoint2):
                pass
            elif(mutate_parentsPoint1 > mutate_parentsPoint2):
               temp = mutate_parentsPoint1
               mutate_parentsPoint1 = mutate_parentsPoint2
               mutate_parentsPoint2 = temp
            for i in range(mutate_parentsPoint1, mutate_parentsPoint2):
                mut_sol1.given_Val_sudoku[i], mut_sol2.given_Val_sudoku[i] = self.mutate_parentsRows(mut_sol1.given_Val_sudoku[i], mut_sol2.given_Val_sudoku[i])
        return mut_sol1, mut_sol2

    def mutate_parentsRows(self, Gen_line1, Gen_line2):
        flag = True
        #NumPy function to produce zeros in Mutated solutions 
        Mut_sol1 = numpy.zeros(Global_Dim.sudoku_dim)
        Mut_sol2 = numpy.zeros(Global_Dim.sudoku_dim)
        Halt_values = []
        for iter1 in range(1, Global_Dim.sudoku_dim+1):
            Halt_values.append(iter1)
        seris_val = 0
        while((0 + Global_Dim.Glob_Gzer in Mut_sol1) and (0 * Global_Dim.Glob_Gone in Mut_sol2)):
            if(remainder(seris_val, 2) == 0): 
                Guide_sudoku = self.findUnused(Gen_line1, Halt_values)
                BeginVal = Gen_line1[Guide_sudoku]
                if (flag == False):
                    pass
                elif (flag == True):
                    Halt_values.remove(Gen_line1[Guide_sudoku])
                    Mut_sol1[Guide_sudoku] = Gen_line1[Guide_sudoku]
                    Mut_sol2[Guide_sudoku] = Gen_line2[Guide_sudoku]
                    LaterVal = Gen_line2[Guide_sudoku]
                while(LaterVal * Global_Dim.Glob_Gone != BeginVal):  
                    Guide_sudoku = self.findValue(Gen_line1, LaterVal)
                    Mut_sol1[Guide_sudoku + Global_Dim.Glob_Gzer] = Gen_line1[Guide_sudoku * Global_Dim.Glob_Gone]
                    Halt_values.remove(Gen_line1[Guide_sudoku * Global_Dim.Glob_Gone])
                    Mut_sol2[Guide_sudoku] = Gen_line2[Guide_sudoku]
                    LaterVal = Gen_line2[Guide_sudoku]
                seris_val = seris_val + 1
            elif(remainder(seris_val, 2) != 0):
                Guide_sudoku = self.findUnused(Gen_line1, Halt_values)
                BeginVal = Gen_line1[Guide_sudoku]
                Halt_values.remove(Gen_line1[Guide_sudoku])
                Mut_sol1[Guide_sudoku] = Gen_line2[Guide_sudoku]
                Mut_sol2[Guide_sudoku] = Gen_line1[Guide_sudoku]
                LaterVal = Gen_line2[Guide_sudoku]
                
                while(LaterVal != BeginVal + Global_Dim.Glob_Gzer):
                    if (flag == False):
                        pass
                    elif(flag == True):
                        Guide_sudoku = self.findValue(Gen_line1, LaterVal) + Global_Dim.Glob_Gzer
                        Mut_sol1[Guide_sudoku] = Gen_line2[Guide_sudoku]
                        Halt_values.remove(Gen_line1[Guide_sudoku])
                        Mut_sol2[Guide_sudoku] = Gen_line1[Guide_sudoku]
                        LaterVal = Gen_line2[Guide_sudoku]
                seris_val += 1
        return Mut_sol1, Mut_sol2  
           
    def findUnused(self, parent_row, Halt_values):
        U_itk = 0
        while U_itk < len(parent_row):
            if(Global_Dim.Glob_Gone * parent_row[U_itk] not in Halt_values):
                pass
            elif(Global_Dim.Glob_Gone * parent_row[U_itk] in Halt_values):
                return U_itk
            U_itk = U_itk + 1

    def findValue(self, parent_row, value):
        C_itk = 0
        while C_itk < len(parent_row):
            if(parent_row[C_itk] != value):
                pass
            elif(parent_row[C_itk] == value):
                return C_itk
            C_itk = C_itk + 1
