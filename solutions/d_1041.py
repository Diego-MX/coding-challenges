from functools import reduce

class Solution:
    def isRobotBounded(self, instructions: str) -> bool: 
        # Use complex tuples, and WLOG face East at start. 
        state = (0, 1) 
        for ins in instructions: 
            state = move_state(state, ins)

        r1, th1 = state
        return (r1 == 0) or (th1 != 1) 

    
    def isRobotBounded2(self, instructions: str) -> bool:
        basic = {
            'G': (1,  1 ), 
            'L': (0,  1j), 
            'R': (0, -1j)}
        start = (0, 1)
        affine = map(basic.get, instructions)
        rr, theta = reduce(compose_moves, affine, start)
        return (rr == 0) or (theta != 1)


def compose_moves(m0, m1): 
    d0, th0 = m0
    d1, th1 = m1
    return (d0 + th0*d1, th0*th1) 


def move_state(state, move): 
    pos, face = state
    if move == 'G': 
        return (pos + face, face)
    if move == 'L': 
        return (pos, 1j*face)
    if move == 'R': 
        return (pos,-1j*face)

