import itertools 
from random import choice, shuffle, randint
import numpy as np
import matplotlib.pyplot as plt

def rnd_subset(input_set):
	""" Generate a random subset from the input set """
	shuffled = input_set[:]
	shuffle(shuffled)
	return shuffled[:randint(0, len(input_set))]

def rnd_family(input_set, index_set):
	""" Generate a random family from index_set to a power set
		of input_set """

	return [rnd_subset(input_set) for i in index_set]		
	

def power_set(input_set):
	""" Generate lazily the power set of inptu set """
	for r in range(len(input_set) + 1):
		for subset in itertools.combinations(input_set, r):
			yield subset

def cart_product(input_A, input_B):
	return [element for element in itertools.product(input_A, input_B)]

input_set = [1, 2, 3]

p_set = list(power_set(input_set))

index_set = list(range(3)) 

family_A = rnd_family(input_set, index_set)
family_B = rnd_family(input_set, index_set)

cart_prod = cart_product(index_set, index_set)

pairwise_intersection = []

for x, y in cart_prod:
	pairwise_intersection.append(set(family_A[x]).union(set(family_B[y])))

print(cart_prod)
print(family_A)
print(family_B)
print(pairwise_intersection)

total_union = set(input_set).intersection(*pairwise_intersection)
print(total_union)
