import itertools
def pin_combination(arr):
	return set(itertools.permutations(arr))
arr=input("Enter numbers by giving space = ").split()
combinations=pin_combination(arr)
for i in sorted(combinations):
	print("  ".join(i).center(200))
print("Number of possible combinations of numbers  = " ,len(combinations))
