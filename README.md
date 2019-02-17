# This is the Knapsack Problem solved using Genetic optimization algorithm
More data for this problem can be found [here](http://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html)

Requirements: 
  Python >= 3.4.2
  
  
GA for Knapsack problem

The Knapsack problem is simple. You have a Knapsack and N objects which each of them can be described with two properties, value (profit)P and weigh W. Using GA we are trying to fit in knapsack as many object as possible with a certain limit depending  of the complexity of the problem. In this case we are going to experiment with limit C 26 and 5 objects. It is a maximization problem with Fitness function as much sum of profit as we can without exceeding the space limit C.

GA algorithms philosophy is related to life being generation evolution with the only difference of keeping the good generations and throw away to the bin “bad generations” that might not have good fitness function. The algorithm starts by creating 100 random arrays with size 5. This array consists of binary values 0's and 1's. The selection method runs after the initialization and selects the best 50 arrays with the best fitness.  The best fitness is a method which checks each array for the correspondence weight and profit. Those two arrays contain the weight and the profit for each index of the parents array which is 1. 
Now the mutation method randomizes those arrays for optimization purposes. In this case, my method generates random numbers for each index for each array with range 0,1. Then it checks if the value is less than 0.5 and if true, it swaps the index from 0 to 1 or 1 to 0. Next method which takes place in the running time is the crossover which mixes two parents (arrays) and makes children. The purpose of this method is to create back 100 parents for further iteration of the algorithm as well as find the optimal value of profits we are looking for. The program stops when we found the optimal value otherwise generates again new children until it finds the optimal which in this case is [0, 1, 1, 1, 0]
