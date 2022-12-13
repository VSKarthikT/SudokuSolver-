import random
import Global_Dim

class Compete_Sols(object):
        
    def pick_sol(self, Solutions_pool):  
        Rand_mut_sol1 = Solutions_pool[random.randint(0, len(Solutions_pool)-1)]
        Rand_mut_sol2 = Solutions_pool[random.randint(0, len(Solutions_pool)-1)]
        Fit_sol1 = Rand_mut_sol1.match_percent
        Fit_sol2 = Rand_mut_sol2.match_percent
        if (Global_Dim.Flag):
            if(Fit_sol1 < Fit_sol2 and Global_Dim.Flag):
                Best_Solution = Rand_mut_sol2
                Worst_Solution = Rand_mut_sol1  
            else:
                Best_Solution = Rand_mut_sol1
                Worst_Solution = Rand_mut_sol2   
        # selection rate is done by hit and trail and referenced form Genetic algoritm online sources
        Fit_percent = 0.85
        rand_numbers = random.uniform(0, 1.2)
        while(Global_Dim.Flag == True and rand_numbers > 1):
            rand_numbers = random.uniform(0, 1.2)
        if(rand_numbers > Fit_percent):
            return Worst_Solution
        else:
            return Best_Solution
    