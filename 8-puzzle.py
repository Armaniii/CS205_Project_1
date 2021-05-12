import numpy
import math
from collections import deque
numrows = 3
class Node():
    def __init__(self, state, priority, depth):
        self.state = state
        self.priority = priority
        self.depth = depth
        self.leaves = []
        self.locX = 0
        self.locY = 0
        i = 0
        for j in range(0,8):
            if state[j] == 0:
                continue
            i+=1
        self.locX = math.floor(i%3)
        self.locY = math.floor(i/3)
            


    def move(self, direction):
        index = int(0)
        # if(self.locY<=2 or self.locY>=6):
        #     return False
        # elif(self.locX >= 2 or self.locX == 0):
        #     return False
        if(direction == 0 and self.locY != 0):
            index = (self.locY - 1) * numrows + self.locX
        elif(direction == 1 and self.locY != numrows - 1):
            index = (self.locY + 1) * numrows + self.locX
        elif(direction == 2 and self.locX != 0):
            index = self.locY * numrows + self.locX - 1
        elif(direction == 3 and self.locX != numrows - 1):
            index = self.locY*numrows + self.locX + 1
        else:
            return -1
        print("locx", self.locX)
        print("locy", self.locY)
        print("index",index)
        state_update = self.state.copy()
        print(state_update)

        temp = state_update[int(index)]
        #print(int(self.locY * numrows + self.locX))
        state_update[int(index)] = state_update[int(self.locY * numrows + self.locX)]
        state_update[int(self.locY * numrows + self.locX)] = temp
        return state_update

    def push(self,n):
        self.leaves.append(n)

    def print_state(self):
        for i in range(0,numrows):
            print(self.state[i * numrows],end='')
            for j in range(1, numrows):
                print("",self.state[i* numrows + j],end='')
            print("")
        
    

class Problem():
    def __init__(self, init_state, algo):
        self.init_state = init_state
        self.goal_state = [1,2,3,4,5,6,7,8,0]
        self.algo = algo
        self.head = Node(init_state,0,0)
        self.frontier = []

    def priority(self, state, depth):
        height = 0
        if(self.algo==0):
            return depth  #Uniform

        elif(self.algo==1):
            for i in range(0,numrows*numrows):
                if(state[i] != goal_state[i] and state != 0):
                    height+=1       #A* misplaced
        elif(self.algo==2):  #A* hamming
            for i in range(0, numrows*numrows):
                if(state[i] != 0):
                    height += math.floor(abs((i+1) % numrows) - math.floor(state[i] % numrows))
                    height += math.floor(abs((i+1) % numrows) - math.floor(state[i] / numrows))
        return depth + height       

    def add_frontier(self,n):
        print("came to frontier")
        for i in range(len(self.frontier)):
            print("frontier", self.frontier[i].priority)
            if(self.frontier[i].priority > n.priority):
                self.frontier.insert(i,n)
                
                return
            self.frontier.append(n)
        
    def solve(self):
        repeated = set([])
        limit = 0
        max_limit = 200000
        max_size = 0
        
        queue = [self.head]      
        
        #frontier = deque[(front,0)]
        self.frontier.append(self.head)
        curr = self.frontier.pop()

        #curr.print()
        while limit < max_limit:
            curr = queue.pop(0)
            curr.print_state()         

            for i in range(0,3):
                print("i = ",i)
                update_state = curr.move(i)
                if update_state !=-1:
                    if tuple(update_state) not in repeated:
                        
                        repeated.add(tuple(update_state))
                        update = Node(update_state, self.priority(update_state, curr.depth + 1), curr.depth + 1)

                        curr.push(update)
                        #curr = update
                        queue.append(update)
                        self.add_frontier(update)
                        #print("came here", curr.leaves[0])
                        curr.print_state()

                    
            if(curr.state == self.goal_state):
                print("Goal reached")
                return
            else:
                print("Came to pop frontier")
                curr = self.frontier.pop()
                d = curr.depth
            limit+=1
        print("Reached the end")




if __name__ == "__main__":
    print("Welcome to the 8-Puzzle")

    print("Enter Algorithm of choice")
    choice = input("1: Uniform, 2: A* w/ misplaced, 3: A* w/ manhattan distance")

    input_state = [1, 2, 3, 4, 8, 0, 7, 6, 5]

    prob = Problem(input_state, choice)
    prob.solve()