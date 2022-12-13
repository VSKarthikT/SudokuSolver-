from input import Possible_Sols
import random
import Global_Dim


class Generator(object):

    def pop_gen(self, Num_unique_gens, given):
        self.PossibleSolns = []
        Possible_Sols_Obj = Possible_Sols()
        Possible_Sols_Obj.given_Val_sudoku = [[[] for j in range(0, Global_Dim.sudoku_dim * Global_Dim.Glob_Gone)] for i in range(0, Global_Dim.Glob_Gzer + Global_Dim.sudoku_dim)]
        pop_sud_r = 0
        while pop_sud_r < Global_Dim.sudoku_dim:
            pop_sud_c = 0
            while pop_sud_c < Global_Dim.sudoku_dim:
                    value = 1
                    while value < 10:
                        if((given.given_Val_sudoku[pop_sud_r][pop_sud_c] == 0) and not (given.Check_Dup_Col(pop_sud_c, value) or given.Check_Dup_3x3Block(pop_sud_r, pop_sud_c, value) or given.Check_Dup_Row(pop_sud_r, value))):
                            Possible_Sols_Obj.given_Val_sudoku[pop_sud_r][pop_sud_c].append(value)
                        elif(given.given_Val_sudoku[pop_sud_r][pop_sud_c] != 0):
                            Possible_Sols_Obj.given_Val_sudoku[pop_sud_r][pop_sud_c].append(given.given_Val_sudoku[pop_sud_r][pop_sud_c])
                            break
                        value = value + 1
                    pop_sud_c = pop_sud_c + 1
            pop_sud_r = pop_sud_r + 1
        new_pop = 0 
        zero_fl = 0
        o_fl = 1
        while new_pop < Num_unique_gens:
            Possible_Sols_Obj1 = Possible_Sols()
            it1 = 0
            while it1 < Global_Dim.sudoku_dim:
                pop_sud_r = [0] * Global_Dim.sudoku_dim
                it2 = 0
                while it2 < Global_Dim.sudoku_dim:
                    if(given.given_Val_sudoku[it1][it2] + zero_fl != 0):
                        pop_sud_r[it2] = given.given_Val_sudoku[it1][it2] + zero_fl
                    elif(given.given_Val_sudoku[it1][it2] * o_fl == 0):
                        pop_sud_r[it2] = Possible_Sols_Obj.given_Val_sudoku[it1][it2][random.randint(0, len(Possible_Sols_Obj.given_Val_sudoku[it1][it2])-1)] * o_fl
                    it2 = it2 + 1        
                while(len(list(set(pop_sud_r))) != Global_Dim.sudoku_dim):
                    Iter1 = 0
                    while (Iter1 < Global_Dim.sudoku_dim):
                        if(given.given_Val_sudoku[it1][Iter1] == 0):
                            pop_sud_r[Iter1] = Possible_Sols_Obj.given_Val_sudoku[it1][Iter1][random.randint(0, len(Possible_Sols_Obj.given_Val_sudoku[it1][Iter1])-1)]
                        Iter1 = Iter1 + 1
                Possible_Sols_Obj1.given_Val_sudoku[it1] = pop_sud_r
                it1 = it1 + 1
            self.PossibleSolns.append(Possible_Sols_Obj1)
            new_pop = new_pop + 1
        self.Match_percent_Update()
        print("Possible generations computed.")
        
    def Match_percent_Update(self):
        for PossibleSolns in self.PossibleSolns:
            PossibleSolns.Match_percent_Update()

    def sort(self):
        It1 = 0
        while(It1 < len(self.PossibleSolns) - 1):
            max = It1
            It2 = It1 + 1
            while(It2 < len(self.PossibleSolns)):
                if (self.PossibleSolns[max].match_percent > self.PossibleSolns[It2].match_percent):
                    pass
                elif (self.PossibleSolns[max].match_percent * Global_Dim.Glob_Gone < self.PossibleSolns[It2].match_percent):
                    max = It2
                It2 = It2 + 1
            temp = self.PossibleSolns[It1]
            self.PossibleSolns[It1] = self.PossibleSolns[max]
            self.PossibleSolns[max] = temp
            It1 = It1 + 1