import numpy as np
import math
import matplotlib.pyplot as plt

numrows = 3
class Node():
    def __init__(self, state, priority, depth):
        self.state = state
        self.priority = priority
        self.depth = depth
        self.leaves = []
        self.loc_x = 0
        self.loc_y = 0
        i = 0
        for j in range(0,9):
            if state[j] == 0:
                break
            i+=1
        self.loc_x = math.floor(i%3)
        self.loc_y = math.floor(i/3)
            


    def move(self, direction):
        if(direction == 0 and self.loc_y != 0):
            index = (self.loc_y - 1) * numrows + self.loc_x
        elif(direction == 1 and self.loc_y != numrows - 1):
            index = (self.loc_y + 1) * numrows + self.loc_x
        elif(direction == 2 and self.loc_x != 0):
            index = self.loc_y * numrows + self.loc_x - 1
        elif(direction == 3 and self.loc_x != numrows - 1):
            index = self.loc_y*numrows + self.loc_x + 1
        else:
            return -1

        state_update = self.state.copy()
        print(state_update)

        temp = state_update[int(index)]

        state_update[int(index)] = state_update[int(self.loc_y * numrows + self.loc_x)]
        state_update[int(self.loc_y * numrows + self.loc_x)] = temp
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

        #Uniform cost search
        if(self.algo=="0"):
            return depth  

        #A* with misplaced tile distance calculations
        elif(self.algo=="1"):
            for i in range(0,numrows*numrows):
                if(state[i] != self.goal_state[i] and state[i] != 0):
                    height+=1       
        #Manhattan Distance Calculations
        elif(self.algo=="2"):                            
            for i in range(0, numrows*numrows):
                if(state[i] != 0):
                    height += abs(math.floor((i+1) % numrows) - math.floor(state[i] % numrows))
                    height += abs(math.floor((i+1) / numrows) - math.floor(state[i] / numrows))
        return depth + height       

    def add_frontier(self,n):
        
        if len(self.frontier) == 0:                                 # Handles initial case when the queue is empty.
            self.frontier.append(n)
        for i in range(len(self.frontier)):  
            if(self.frontier[i].priority > n.priority):             # Sorting the queue by priority
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

        while limit < max_limit:
            curr.print_state()         

            for i in range(0,4):
                update_state = curr.move(i)
                if update_state !=-1:
                    if tuple(update_state) not in repeated:
                        repeated.add(tuple(update_state))
                        update = Node(update_state, self.priority(update_state, curr.depth + 1), curr.depth + 1)
                        curr.push(update)
                        self.add_frontier(update)
                        # print("------------------------------------",len(self.frontier))
                        curr.print_state()

            if(max_size < len(self.frontier)):
                max_size = len(self.frontier)


            if(curr.state == self.goal_state):
                print("Goal reached")
                # print("Iterations:", limit)
                # print("Max size", max_size)
                return limit, max_size

            else:
                curr = self.frontier.pop(0)
                d = curr.depth
            limit+=1
        print("Reached the time limit with no solution")


if __name__ == "__main__":

    print("Welcome to the 8-Puzzle Solver")
    print("Enter '1' to test the default puzzle or '2' to perform time/space analysis on an easy and hard puzzle.")
    choice = input("Choice #: ")
    
    if choice == "1":
        default = [1, 2, 3, 4, 8, 0, 7, 6, 5]
        print("Enter Algorithm of choice")
        print("0: Uniform Cost Search, 1: A* with the Misplaced Tile heuristic, 2: A* with the Manhattan Distance heuristic")
        algorithm = input("Choice #: ")
        prob = Problem(default, algorithm)
        limit,front_size = prob.solve()
        print("Maximum space: ", front_size)
        print("Nodes expanded (time) ", limit)
        
    elif choice == "2":
        ## Analysis ##

        ##Easy Puzzle##
        # 1 2 3
        # 0 4 6
        # 7 5 8

        names = ["Uniform Cost Search", "A* with the Misplaced Tile heuristic", "A* with the Manhattan Distance heuristic"]
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
        plt.bar(names, hard_limit, color="red")
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
        plt.bar(names, hard_front, color="red")
        plt.xlabel("Algorithms")
        plt.ylabel("Space Complexity")
        plt.title("Space Complexity -- Hard Puzzle")
        plt.xticks(x_pos, names)
        plt.show()

    else:
        print("Error, invalid input. Please run the program again.")



