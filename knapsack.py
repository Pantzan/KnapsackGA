import random
import sys
import operator

class Knapsack(object):	

	#initialize variables and lists
	def __init__(self):	

		self.C = 0
		self.weights = []
		self.profits = []
		self.opt = []
		self.parents = []
		self.newparents = []
		self.bests = []
		self.best_p = [] 
		self.iterated = 1
		self.population = 0

		# increase max recursion for long stack
		iMaxStackSize = 15000
		sys.setrecursionlimit(iMaxStackSize)

	# create the initial population 
	def initialize(self):

		for i in range(self.population):
			parent = []
			for k in range(0, 5):
				k = random.randint(0, 1)
				parent.append(k)
			self.parents.append(parent)

	# set the details of this problem
	def properties(self, weights, profits, opt, C, population):

		self.weights = weights
		self.profits = profits
		self.opt = opt
		self.C = C
		self.population = population
		self.initialize()

	# calculate the fitness function of each list (sack)
	def fitness(self, item):

		sum_w = 0
		sum_p = 0

		# get weights and profits
		for index, i in enumerate(item):
			if i == 0:
				continue
			else:
				sum_w += self.weights[index]
				sum_p += self.profits[index]

		# if greater than the optimal return -1 or the number otherwise
		if sum_w > self.C:
			return -1
		else: 
			return sum_p
	
	# run generations of GA
	def evaluation(self):

		# loop through parents and calculate fitness
		best_pop = self.population // 2
		for i in range(len(self.parents)):
			parent = self.parents[i]
			ft = self.fitness(parent)
			self.bests.append((ft, parent))

		# sort the fitness list by fitness		
		self.bests.sort(key=operator.itemgetter(0), reverse=True)
		self.best_p = self.bests[:best_pop]
		self.best_p = [x[1] for x in self.best_p]

	# mutate children after certain condition
	def mutation(self, ch):

		for i in range(len(ch)):		
			k = random.uniform(0, 1)
			if k > 0.5:
				#if random float number greater that 0.5 flip 0 with 1 and vice versa
				if ch[i] == 1:
					ch[i] = 0
				else: 
					ch[i] = 1
		return ch

	# crossover two parents to produce two children by miixing them under random ration each time
	def crossover(self, ch1, ch2):

		threshold = random.randint(1, len(ch1)-1)
		tmp1 = ch1[threshold:]
		tmp2 = ch2[threshold:]
		ch1 = ch1[:threshold]
		ch2 = ch2[:threshold]
		ch1.extend(tmp2)
		ch2.extend(tmp1)

		return ch1, ch2

	# run the GA algorithm
	def run(self):

		# run the evaluation once
		self.evaluation()
		newparents = []
		pop = len(self.best_p)-1

		# create a list with unique random integers
		sample = random.sample(range(pop), pop)
		for i in range(0, pop):
			# select the random index of best children to randomize the process
			if i < pop-1:
				r1 = self.best_p[i]
				r2 = self.best_p[i+1]
				nchild1, nchild2 = self.crossover(r1, r2)
				newparents.append(nchild1)
				newparents.append(nchild2)
			else:
				r1 = self.best_p[i]
				r2 = self.best_p[0]
				nchild1, nchild2 = self.crossover(r1, r2)
				newparents.append(nchild1)
				newparents.append(nchild2)

		# mutate the new children and potential parents to ensure global optima found
		for i in range(len(newparents)):
			newparents[i] = self.mutation(newparents[i])

		if self.opt in newparents:
			print ("optimal found in {} generations" .format(self.iterated))
		else:
			self.iterated += 1
			print("recreate generations for {} time" .format(self.iterated))
			self.parents = newparents
			self.bests = []
			self.best_p = []
			self.run()	

# properties for this particular problem
weights = [12,  7, 11, 8, 9]
profits = [24, 13, 23, 15, 16]
opt     = [0, 1, 1, 1, 0]
C = 26
population = 10

k = Knapsack()
k.properties(weights, profits, opt, C, population)
k.run()