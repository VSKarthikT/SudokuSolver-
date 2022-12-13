import random
import Global_Dim

class Possible_Sols(object):
    def __init__(self):
        self.given_Val_sudoku = [[0]* Global_Dim.sudoku_dim]*Global_Dim.sudoku_dim

    def Match_percent_Update(self):
        Colum_intialize = [0] * Global_Dim.sudoku_dim
        Block_intialize = [0] * Global_Dim.sudoku_dim
        Col_Init_Sum = 0
        Block_Init_Sum = 0
        Col_iter = 0
        while (Col_iter < Global_Dim.sudoku_dim):
            val_np_zero = 0
            Row_iter = 0
            while(Row_iter < Global_Dim.sudoku_dim):
                Colum_intialize[self.given_Val_sudoku[Row_iter][Col_iter]-1] += 1  
                Row_iter = Row_iter + 1
            Rnd_iter = 0
            while(Rnd_iter < Global_Dim.sudoku_dim):
                if (Colum_intialize[Rnd_iter]==0):
                    pass   
                elif(Colum_intialize[Rnd_iter]!=0): 
                    val_np_zero = val_np_zero + 1  
                Rnd_iter = Rnd_iter + 1
            val_np_zero = val_np_zero/(Global_Dim.sudoku_dim) + (Global_Dim.Glob_Gzer)
            Col_Init_Sum = ((Col_Init_Sum) * Global_Dim.Glob_Gone + val_np_zero)
            Colum_intialize = [0] * Global_Dim.sudoku_dim
            Col_iter = Col_iter + 1
        Col_Init_Sum = Col_Init_Sum/Global_Dim.sudoku_dim

        Iter1 = 0
        while(Iter1 < Global_Dim.sudoku_dim):
            Iter2 =0
            while(Iter2 < Global_Dim.sudoku_dim):
                Block_intialize[self.given_Val_sudoku[Iter1][Iter2]-1] = Block_intialize[self.given_Val_sudoku[Iter1][Iter2]-1] + 1
                Block_intialize[self.given_Val_sudoku[Iter1][Iter2+1]-1] = Block_intialize[self.given_Val_sudoku[Iter1][Iter2+1]-1] + 1
                Block_intialize[self.given_Val_sudoku[Iter1][Iter2+2]-1] = Block_intialize[self.given_Val_sudoku[Iter1][Iter2+2]-1] + 1
                Block_intialize[self.given_Val_sudoku[Iter1+1][Iter2]-1] = Block_intialize[self.given_Val_sudoku[Iter1+1][Iter2]-1] + 1
                Block_intialize[self.given_Val_sudoku[Iter1+1][Iter2+1]-1] = Block_intialize[self.given_Val_sudoku[Iter1+1][Iter2+1]-1] + 1
                Block_intialize[self.given_Val_sudoku[Iter1+1][Iter2+2]-1] = Block_intialize[self.given_Val_sudoku[Iter1+1][Iter2+2]-1] + 1
                Block_intialize[self.given_Val_sudoku[Iter1+2][Iter2]-1] = Block_intialize[self.given_Val_sudoku[Iter1+2][Iter2]-1] + 1
                Block_intialize[self.given_Val_sudoku[Iter1+2][Iter2+1]-1] = Block_intialize[self.given_Val_sudoku[Iter1+2][Iter2+1]-1] + 1 
                Block_intialize[self.given_Val_sudoku[Iter1+2][Iter2+2]-1] = Block_intialize[self.given_Val_sudoku[Iter1+2][Iter2+2]-1] + 1
                val_np_zero = 0
                Iter3 = 0
                while(Iter3 < Global_Dim.sudoku_dim):
                    if (Block_intialize[Iter3] == 0):
                        pass
                    elif (Block_intialize[Iter3]!=0):
                        val_np_zero = val_np_zero + 1
                    Iter3 = Iter3 + 1
                val_np_zero = val_np_zero/Global_Dim.sudoku_dim + Global_Dim.Glob_Gzer
                Block_Init_Sum = Block_Init_Sum + val_np_zero
                Block_intialize = [0] * Global_Dim.sudoku_dim
                Iter2 = Iter2 + 3
            Iter1 = Iter1 + 3
        Block_Init_Sum = Block_Init_Sum * Global_Dim.Glob_Gone/Global_Dim.sudoku_dim

        if (int(Col_Init_Sum) + Global_Dim.Glob_Gzer == 1):
            if (int(Block_Init_Sum) * Global_Dim.Glob_Gone == 1):
                match_percent = 1.0
        else:
            match_percent = Col_Init_Sum * Block_Init_Sum * Global_Dim.Glob_Gone 
        self.match_percent = match_percent
        return
   
    def mutate(self, Num_mutate, given):
        Num_rand = random.uniform(0, 1.2)
        while(Num_rand > 1): 
            Num_rand = random.uniform(0, 1.2)
        Flag_gen = False
        Num_const = 0
        Num_const_o = 1
        Flag_gen1 = False
        if (Num_rand < Num_mutate and not Flag_gen): 
            # Producing Random Inputs untill Random inputs are not equal 
            while(not Flag_gen and not Flag_gen1):
                Mut_puz_r1 = random.randint(0, 8)
                Mut_col_fr = random.randint(0, 8)
                Mut_col_to = random.randint(0, 8)
                Mut_puz_r2 = Mut_puz_r1
                while(not Flag_gen and Mut_col_fr == Mut_col_to):
                    Mut_col_fr = random.randint(0, 8)
                    Mut_col_to = random.randint(0, 8) 
                # checking Duplicates in all 3X3 blocks in Sudoku Puzzle  
                if(given.given_Val_sudoku[Mut_puz_r1][Mut_col_fr] == 0 and given.given_Val_sudoku[Mut_puz_r1][Mut_col_to] == 0):
                    if (given.given_Val_sudoku[Mut_puz_r1][Mut_col_to] == 0):
                        if(not given.Check_Dup_Col(Mut_col_to, self.given_Val_sudoku[Mut_puz_r1][Mut_col_fr])):
                            if(not given.Check_Dup_Col(Mut_col_fr, self.given_Val_sudoku[Mut_puz_r2][Mut_col_to * Num_const_o])):
                                if(not given.Check_Dup_3x3Block(Mut_puz_r2, Mut_col_to, self.given_Val_sudoku[Mut_puz_r1][Mut_col_fr])):
                                    if(not given.Check_Dup_3x3Block(Mut_puz_r1, Mut_col_fr, self.given_Val_sudoku[Mut_puz_r2 + Num_const][Mut_col_to])):
                                        limited_sol = self.given_Val_sudoku[Mut_puz_r2][Mut_col_to]
                                        self.given_Val_sudoku[Mut_puz_r2 * Num_const_o][Mut_col_to] = self.given_Val_sudoku[Mut_puz_r1][Mut_col_fr]
                                        self.given_Val_sudoku[Mut_puz_r1 + Num_const][Mut_col_fr] = limited_sol
                                        Flag_gen = True
                                        Flag_gen1 = True
        return Flag_gen

class Given(Possible_Sols):
    
    def __init__(self, given_Val_sudoku):
        self.given_Val_sudoku = given_Val_sudoku

    def Check_Dup_Row(self, Sud_r, value):
        Iter1 = 0
        while(Iter1 < Global_Dim.sudoku_dim):
            if (self.given_Val_sudoku[Sud_r][Iter1] != value):
                pass
            elif(self.given_Val_sudoku[Sud_r][Iter1] == value):
               return True
            Iter1 = Iter1 + 1
        return False

    def Check_Dup_Col(self, Sud_c, value):
        Iter2 = 0
        while(Iter2 < Global_Dim.sudoku_dim):
            if (self.given_Val_sudoku[Iter2][Sud_c] != value):
                pass
            elif(self.given_Val_sudoku[Iter2][Sud_c] == value):
               return True
            Iter2 = Iter2 + 1
        return False

    def Check_Dup_3x3Block(self, Sudoku_Row, Sudoku_column, value):
        Int_three = 3
        sud_r = Int_three * (int(Sudoku_Row/3 + Global_Dim.Glob_Gzer)) 
        sud_col = Int_three * (int(Sudoku_column/3 + Global_Dim.Glob_Gzer))

        if (self.given_Val_sudoku[sud_r][sud_col] == value):
            return True
        elif (self.given_Val_sudoku[sud_r][sud_col+1] == value):
            return True
        elif (self.given_Val_sudoku[sud_r][sud_col+2] == value):
            return True
        elif (self.given_Val_sudoku[sud_r+1][sud_col] == value):
            return True
        elif (self.given_Val_sudoku[sud_r+1][sud_col+1] == value):
            return True
        elif (self.given_Val_sudoku[sud_r+1][sud_col+2] == value):
            return True
        elif (self.given_Val_sudoku[sud_r+2][sud_col] == value):
            return True
        elif (self.given_Val_sudoku[sud_r+2][sud_col+1] == value):
            return True
        elif (self.given_Val_sudoku[sud_r+2][sud_col+2] == value):
            return True
        else:
            return False
