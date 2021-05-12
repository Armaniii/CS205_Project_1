import numpy as np
import math
import time

import matplotlib.pyplot as plt
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
        for j in range(0,9):
            if state[j] == 0:
                break
            i+=1
        self.locX = math.floor(i%3)
        self.locY = math.floor(i/3)
            


    def move(self, direction):
 
        print("directions", direction)
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
        if(self.algo=="0"):
            return depth  #Uniform

        elif(self.algo=="1"):
            for i in range(0,numrows*numrows):
                if(state[i] != self.goal_state[i] and state[i] != 0):
                    height+=1       #A* misplaced
        elif(self.algo=="2"):  
            for i in range(0, numrows*numrows):
                if(state[i] != 0):
                    height += abs(math.floor((i+1) % numrows) - math.floor(state[i] % numrows))
                    height += abs(math.floor((i+1) / numrows) - math.floor(state[i] / numrows))
        return depth + height       

    def add_frontier(self,n):
        
        if len(self.frontier) == 0:
            self.frontier.append(n)
        for i in range(len(self.frontier)):
            #print("frontier", self.frontier[i].priority)
            if(self.frontier[i].priority > n.priority):
                self.frontier.insert(i,n)

                return
        self.frontier.append(n)
        
    def solve(self):
        repeated = set([])
        limit = 0
        max_limit = 200000
        max_size = 0


        self.frontier.append(self.head)
        curr = self.frontier.pop()

        #curr.print()
        while limit < max_limit:
            print("Printing State")
            curr.print_state()         

            for i in range(0,4):
                print("i = ",i)
                update_state = curr.move(i)
                if update_state !=-1:
                    if tuple(update_state) not in repeated:
                        repeated.add(tuple(update_state))
                        update = Node(update_state, self.priority(update_state, curr.depth + 1), curr.depth + 1)
                        print("update", update.state)
                        curr.push(update)
                        #curr = update
                        #queue.append(update)
                        self.add_frontier(update)
                        print("------------------------------------",len(self.frontier))
                        curr.print_state()

            #limit == Number of Nodes expanded == Time complexity
            #Queuesize == frontier == Space complexity


            if(max_size < len(self.frontier)):
                print("coming here")
                max_size = len(self.frontier)


            if(curr.state == self.goal_state):
                print("Goal reached")
                print("Iterations:", limit)
                print("Max size", max_size)
                return limit, max_size

            else:
                print("Came to pop frontier")
                curr = self.frontier.pop(0)
                d = curr.depth
            limit+=1
        print("Reached the end")


if __name__ == "__main__":
    print("Welcome to the 8-Puzzle")

    print("Enter Algorithm of choice")
    #choice = input("0: Uniform, 1: A* w/ misplaced, 2: A* w/ manhattan distance")

    #input_state = [1, 2, 3, 4, 8, 0, 7, 6, 5]
    # time.sleep(5)




    ## Analysis ##

    ##Easy Puzzle##
    # 1 2 3
    # 0 4 6
    # 7 5 8

    names = ["Uniform Cost Search", "A * with the Misplaced Tile heuristic", "A* with the Manhattan Distance heuristic"]
    easy_front = []
    easy_limit = []
    easy_puzzle = [1, 2, 3, 0, 4, 6, 7, 5, 8]


    prob_easy_0 = Problem(easy_puzzle, "0")
    limit_easy_0, frontier_size_easy_0 = prob_easy_0.solve()
   
    prob_easy_1 = Problem(easy_puzzle, "1")
    limit_easy_1, frontier_size_easy_1 = prob_easy_1.solve()

    prob_easy_2 = Problem(easy_puzzle, "2")
    limit_easy_2, frontier_size_easy_2 = prob_easy_2.solve()

    easy_front.extend((frontier_size_easy_0,frontier_size_easy_1,frontier_size_easy_2))
    easy_limit.extend((limit_easy_0, limit_easy_1, limit_easy_2))
  ##Hard Puzzle##
    # 1 6 7
    # 5 0 3
    # 4 8 2

    hard_puzzle = [1, 6, 7, 5, 0, 3, 4, 8, 2]   
    hard_front = []
    hard_limit = []
    prob_hard_0 = Problem(hard_puzzle, "0")
    limit_hard_0, frontier_size_hard_0 = prob_hard_0.solve()
   
    prob_hard_1 = Problem(hard_puzzle, "1")
    limit_hard_1, frontier_size_hard_1 = prob_hard_1.solve()

    prob_hard_2 = Problem(hard_puzzle, "2")
    limit_hard_2, frontier_size_hard_2 = prob_hard_2.solve()

    hard_front.extend((frontier_size_hard_0,frontier_size_hard_1,frontier_size_hard_2))
    hard_limit.extend((limit_hard_0,limit_hard_1,limit_hard_2))

    x_pos = [i for i, _ in enumerate(names)]


    # Graph showing time complexity for easy puzzle #
    plt.bar(names, easy_limit, color="green")
    plt.xlabel("Algorithms")
    plt.ylabel("Time Complexity")
    plt.title("Time Complexity -- Easy Puzzle")
    plt.xticks(x_pos, names)
    plt.show()


    # Graph showing time complexity for hard puzzle #
    plt.bar(names, hard_limit, color="green")
    plt.xlabel("Algorithms")
    plt.ylabel("Time Complexity")
    plt.title("Time Complexity -- Hard Puzzle")
    plt.xticks(x_pos, names)
    plt.show()

    # Graph showing space complexity for easy puzzle
    plt.bar(names, easy_front, color="green")
    plt.xlabel("Algorithms")
    plt.ylabel("Space Complexity")
    plt.title("Space Complexity -- Easy Puzzle")
    plt.xticks(x_pos, names)
    plt.show()


    # Graph showing space complexity for hard puzzle #
    plt.bar(names, hard_front, color="green")
    plt.xlabel("Algorithms")
    plt.ylabel("Time Complexity")
    plt.title("Time Complexity -- Hard Puzzle")
    plt.xticks(x_pos, names)
    plt.show()



