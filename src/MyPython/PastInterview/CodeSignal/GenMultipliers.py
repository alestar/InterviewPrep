"""
Create up to '4' multipliers of each number < 5
"""
result = [[] for _ in range(5)]

# for i in range(5):
#     result[i] = generate_multipliers(i, 4)
# print(result)

def create_multipliers():
    return [lambda x, i=i: i * x for i in range(5)] # Create multipliers for 0,1,2,3,4

for i in range(5): # For each number less than 5
    for j, f in enumerate(create_multipliers()): # For each multiplier
        result[j].append(f(i)) # Apply each multiplier to i
print(result)

"""                                                                                                                        
Generate a list of the first 'length' multiples of 'n'.                                                                    
                                                                                                                             
:param n: The integer to generate multiples for.                                                                           
:param length: The number of multiples to generate.                                                                        
:return: A list containing the first 'length' multiples of 'n'.                                                            
"""

def generate_multipliers(n, length):
    return [n * i for i in range(1, length + 1)]


result = [[] for _ in range(5)]

for i in range(5):
     result[i] = generate_multipliers(i, 4)
print(result)




# # Example usage:
# n = 5
# length = 10
# multipliers = generate_multipliers(n, length)
# print(f"The first {length} multiples of {n} are: {multipliers}")
# # Output: The first 10 multiples of 5 are: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]