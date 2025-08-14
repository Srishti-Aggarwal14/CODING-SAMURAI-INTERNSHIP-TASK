#!/usr/bin/env python3
import math

def print_board(b):
    for i in range(0,9,3):
        print(*(b[i+j] or '.' for j in range(3)))

def winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a,b_,c in wins:
        if b[a] and b[a]==b[b_]==b[c]:
            return b[a]
    if all(b): return "Draw"
    return None

def minimax(b, ai):
    w = winner(b)
    if w=="O": return 1,None
    if w=="X": return -1,None
    if w=="Draw": return 0,None
    best = -math.inf if ai else math.inf
    move = None
    for i in range(9):
        if not b[i]:
            b[i] = "O" if ai else "X"
            score,_ = minimax(b, not ai)
            b[i] = None
            if ai and score>best:
                best,move = score,i
            if not ai and score<best:
                best,move = score,i
    return best,move

def main():
    b = [None]*9
    while True:
        pos = int(input("Your move (1-9):"))-1
        if b[pos]: continue
        b[pos]="X"
        print_board(b)
        if winner(b): break
        _,m = minimax(b, True)
        b[m]="O"
        print("AI move:")
        print_board(b)
        if winner(b): break
    print("Winner:", winner(b))

if __name__=="__main__":
    main()
