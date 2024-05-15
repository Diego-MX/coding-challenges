from typing import List
from copy import deepcopy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        queener = Queener(n)
        int_sols = queener.solve_it()
        return [Queener.string_it(sol) for sol in int_sols]


class Queener: 
    def __init__(self, n:int):
        self.queens = [None]*n
        self.options = {ii: set(range(n)) for ii in range(n)}
        # self.options = dict.fromkeys(range(n), set(range(n)))
    
    
    def solve_it(self): 
        none_item = (None, {None})
        small_val = lambda ii_opts: len(ii_opts[1])
        i1, j_opts = min(self.options.items(), key=small_val, default=none_item)

        sols_set = (
            {tuple(self.queens)} if (i1 is None) 
            else set.union(*(qq.solve_it() for jj in j_opts 
                    if (qq := self.queen_at(i1, jj))), set()))  
                    # always True, set for clarity ... is it?
        return sols_set
        

    def queen_at(self, i0, j0): 
        if j0 not in self.options.get(i0, {}): 
            raise AttributeError(f"Cannot set Q at ({i0}, {j0})")
        
        # This reccursion is expensive. 
        qn = deepcopy(self)

        qn.queens[i0] = j0
        qn.options.pop(i0)
        for ii, s_opt in qn.options.items():
            s_opt.discard(j0)
            s_opt.discard(j0+(i0-ii))
            s_opt.discard(j0-(i0-ii))
        return qn


    @staticmethod
    def string_it(sol_list: List[int]) -> List[str]:
        if None in sol_list:
            raise AttributeError(f"{sol_list} is not a solution.")
        nn = len(sol_list)
        λ_queen = lambda jj: jj*"." + "Q" + "."*(nn-jj-1)
        return list(map(λ_queen, sol_list))


class Queener2: 
    def __init__(self, n:int):
        self.n = n 
        self.queens = [None]*n
        self.options = {ii: set(range(n)) for ii in range(n)}
        self.solutions = set()


    def run_solutions(self):
        pass

    
    def store_queens(self):
        if None in self.queens: 
            raise AttributeError("Can't store queens")
        λ_queen = lambda jj: jj*"." + "Q" + "."*(self.n-jj-1)
        as_list = list(map(λ_queen, self.queens))
        self.solutions.add(as_list)
        return





if __name__ == "__main__": 
    a_queener = Queener(5)
    all_sols = a_queener.solve_it()
    for sol in all_sols: 
        print(Queener.string_it(sol))
