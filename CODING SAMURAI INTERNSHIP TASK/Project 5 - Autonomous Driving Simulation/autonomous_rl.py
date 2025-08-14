#!/usr/bin/env python3
import random, numpy as np

class LaneEnv:
    def __init__(self,len_=10,lanes=3):
        self.len=len_; self.lanes=lanes; self.center=lanes//2
    def reset(self):
        self.pos=[self.center,0]; return tuple(self.pos)
    def step(self,a):
        lane,x=self.pos
        if a==0 and lane>0: lane-=1
        elif a==2 and lane<self.lanes-1: lane+=1
        x+=1
        r=1-0.2*abs(lane-self.center)
        self.pos=[lane,x]
        return tuple(self.pos),r,x>=self.len,{}

def qlearn(ep=5):
    env=LaneEnv()
    Q={}
    for _ in range(ep):
        s=env.reset()
        while True:
            a=random.choice([0,1,2])
            s2,r,d,_=env.step(a)
            Q[(s,a)]=Q.get((s,a),0)+0.1*(r)
            s=s2
            if d: break
    print("Q-table size",len(Q))

if __name__=="__main__":
    qlearn()
