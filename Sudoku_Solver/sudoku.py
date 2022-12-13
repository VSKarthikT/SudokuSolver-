from input import Possible_Sols, Given
from cluster import Generator
from comp import Compete_Sols
from solution_gen import Mutate_solution_Class
import numpy
import Global_Dim

class Sudoku_Class(object):
    # Standard NumPy Actions for loading files, Setting up and printing values as arrays
    #  Referenced from https://numpy.org

    def save_input(self, file_path):
        with open(file_path) as file:
            given_Val_sudoku = numpy.loadtxt(file).astype(int) 
            self.given = Given(given_Val_sudoku) 
        print("Given input from file is \n", given_Val_sudoku)

    def print_solution(self, file_dir, solved_val):
        with open(file_dir, 'w') as sol_file:
            # Standard NumPy to convert values into Sudoku type matrix
            numpy.savetxt(sol_file, solved_val.given_Val_sudoku.reshape(Global_Dim.Glob_Gone * Global_Dim.sudoku_dim * Global_Dim.sudoku_dim + Global_Dim.Glob_Gzer), fmt='%d')
        
    def Main_puzzle(self):
        # Setting Parameters for Generation of possible solutions Referenced from various Genetic algorithms Reasearch papers
        #Mutation rate of solutions are referred from Genetic Algorithms Wikipedia pages
        Num_unique_gens = 200  
        x = int(0.6*Num_unique_gens)
        Num_best_possible_sols = x  
        Num_tot_gens = 1500 
        Num_cross_gens = 0  
        Num_regens_done = 0 
        Fit_intial = 0
        superior_child_count = 0 
        mut_rate_update = 1 
        F_zer = 0
        change_rate = 0.5
        F_on = 1
        Gen_Obj = Generator()
        Gen_Obj.pop_gen(Num_unique_gens, self.given)
        Sudoku_Sol_Generated = 0
        while Sudoku_Sol_Generated < Num_tot_gens:
            Match_percentage = 0.0
            Curr_soln = self.given
            check = 0
            while check < Num_unique_gens:
                match_percent = Gen_Obj.PossibleSolns[check].match_percent
                if(int(match_percent) + F_zer == 1):
                    print("Solution found for Sudoku at Genertion %d!" % Sudoku_Sol_Generated)
                    print(Gen_Obj.PossibleSolns[check].given_Val_sudoku)
                    return Gen_Obj.PossibleSolns[check]
                if(match_percent * F_on > Match_percentage + F_zer):
                    Match_percentage = match_percent
                    Curr_soln = Gen_Obj.PossibleSolns[check].given_Val_sudoku
                check = check + 1
            num = Match_percentage * 100
            my_num = round(num, 2)       
            print("Solution match percentage for generation %d: %.2f" %(Sudoku_Sol_Generated, my_num), "%")
            BestSolution_After = []
            Gen_Obj.sort()
            Solutions_Best = []
            it1 = 0
            while it1 < Num_best_possible_sols:
                elite = Possible_Sols()
                elite.given_Val_sudoku = numpy.copy(Gen_Obj.PossibleSolns[it1].given_Val_sudoku) * F_on + F_zer
                Solutions_Best.append(elite)
                it1 = it1 + 1
            count = Num_best_possible_sols
            while count < Num_unique_gens:
                # Creating Objects for Mutation and Check Solutions
                tourn_obj = Compete_Sols()
                cc = Mutate_solution_Class()
                tourn_pick1 = tourn_obj.pick_sol(Gen_Obj.PossibleSolns)
                tourn_pick2 = tourn_obj.pick_sol(Gen_Obj.PossibleSolns)
                mut_sol1, mut_sol2 = cc.mutate_parents(tourn_pick1, tourn_pick2, mutate_parentsRate=1.0)
                mut_sol1.Match_percent_Update()
                sol_fit_prev = mut_sol1.match_percent
                Flag_gen = mut_sol1.mutate(change_rate, self.given)
                mut_sol1.Match_percent_Update()
                if(Flag_gen == True):
                    Num_cross_gens += 1
                    if(mut_sol1.match_percent < sol_fit_prev):
                        continue
                    elif(mut_sol1.match_percent > sol_fit_prev):
                        superior_child_count = superior_child_count + 1
                mut_sol2.Match_percent_Update()
                sol_fit_prev = mut_sol2.match_percent
                Flag_gen = mut_sol2.mutate(change_rate, self.given)
                mut_sol2.Match_percent_Update()
                if(Flag_gen == True):
                    Num_cross_gens = Num_cross_gens + 1
                    if (mut_sol2.match_percent < sol_fit_prev):
                        continue
                    elif(mut_sol2.match_percent > sol_fit_prev):
                        superior_child_count = superior_child_count + 1
                BestSolution_After.append(mut_sol1)
                BestSolution_After.append(mut_sol2)
                count = count + 2
            cnt = 0
            while cnt < Num_best_possible_sols:
                BestSolution_After.append(Solutions_Best[cnt])
                cnt = cnt + 1
            Gen_Obj.PossibleSolns = BestSolution_After
            Gen_Obj.Match_percent_Update()
            if(Num_cross_gens != 0):
                superior_child_count = F_zer + (superior_child_count / Num_cross_gens) * F_on
            else:
                superior_child_count = 0 
            if(superior_child_count > 0.2):
                mut_rate_update = mut_rate_update*0.998    
            if(superior_child_count < 0.2):
                mut_rate_update = mut_rate_update/0.998    
            change_rate = abs(numpy.random.normal(loc=0.0, scale=mut_rate_update, size=None))
            while change_rate > 1:
                change_rate = abs(numpy.random.normal(loc=0.0, scale=mut_rate_update, size=None))
            Gen_Obj.sort()
            zero = 0
            if Sudoku_Sol_Generated==0 + zero:
                Fit_intial = Match_percentage
                Num_regens_done = 1 + zero
            elif Fit_intial == Match_percentage * F_on:
                    Num_regens_done += 1 + zero
            elif Fit_intial!=Match_percentage:
                Num_regens_done = 0 + zero
                Fit_intial = Match_percentage
            if(Num_regens_done > 100 or Num_regens_done == 100):
                Gen_Obj.pop_gen(Num_unique_gens, self.given)
                Num_regens_done = 0 + zero
                mut_rate_update = 1 + zero
                superior_child_count = 0 + zero
                change_rate = 0.5 + zero
                print("solutions are RE-generated")
            Sudoku_Sol_Generated = Sudoku_Sol_Generated + 1
        print("No solution found and Best Possible is:", Curr_soln)
        return None

