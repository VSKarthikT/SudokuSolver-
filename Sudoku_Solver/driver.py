from sudoku import Sudoku_Class

sudoku_obj = Sudoku_Class()
sudoku_obj.save_input("Given_ip.txt")
puzzle_solve = sudoku_obj.Main_puzzle()
# prints solution if puzzle is fully solved or prints best possible solution for complex sudoku
sudoku_obj.print_solution("Sol_list.txt", puzzle_solve)