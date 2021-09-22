# Python for Data Analysis 101
## Homework
### Instructor: Evelyn J. Boettcher, DiDacTex, LLC
### Week 1: Lecture 3


## HW

# - 1. Write a conditional expression statement with, "if, elif and else." to check if my_string = "Hello World" is a string
import itertools

my_string = 'Hello World'

if isinstance(my_string, float):
    print('1 - This statement is false')
elif isinstance(my_string, str):
    print('2 - True statement', my_string, 'is a string')
else:
    print('3 - guess I did it wrong')

# - 2. Write a list comprehension that returns all the keys in a dictionary whose associated values are greater than zero.
# -   The dictionary: `{'aa': 11, 'cc': 33, 'LESS Than': -55, 'bb': 22}`
# - Output should be a list

d = {'aa': 11, 'cc': 33, 'LESS Than': -55, 'bb': 22}
l = [x[0] for x in d.items() if x[1] > 0]
print(l)

# - 3.  Write a list comprehension that produces even integers from 0 to 10.
# Use a `for` statement to iterate over those values and print results to screen.

even_integer = [even for even in range(11) if even % 2 == 0]
print(even_integer)

# Teacher solution
    # for x in [y for y in range(10) if y % 2 == 0]:
    # print( 'x: %s' % x)

# - 4. Write a list comprehension that iterates over two lists and produces all the combinations of items from the lists.


list_1 = ['a', 'b']
list_2 = [1, 2]

combined_list = []
permut = itertools.permutations(list_1, len(list_2))
for comb in permut:
    zipped = zip(comb, list_2)
    combined_list.append(list(zipped))
print(combined_list)



# - 5. Using `break`, write a `while` statement that prints integers from zero to 5.

num = 1
while num > 0:
    print('current number is:', num)
    num = num + 1
    if num == 6:
        break

print('done!')


# -   Using `continue` , write a `while` statement that processes
# only even integers from 0 to 10. Note: `%` is the modulo operator.

count = 0
while count < 10:
    count += 1
    if count % 2 == 1:
        continue
    print(count)

# currious on this last one I had to % by 1 to get out even numbers and not 0 but on the previous
# question I did 0 and got ou the correct numbers. Tested in termainal as well still same thing?
