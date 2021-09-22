# 1 Lists
# - Create an empty list. Append 4 strings to the list. Then pop one
# - item off the end of the list.

plistlib1 = []
plistlib1 += ["string1", "string2"]
plistlib1.append("string3")
print(plistlib1)
plistlib1.pop()
print(plistlib1)

# 2 Dictionaries

# - Create a dictionary using a zip and two lists
# - Add to this dictionary using the key "HW2" with value "Done"
# - Define a dictionary using both string literals   and variables containing strings.

requirements = ['HW2', 'done', 'class']
plistlib2 = [11, 22, 33]

D = dict(zip(requirements, plistlib2))
print(D)
# print(D.values())
# print(D.keys())
# print(D.items())

# Solution 2 :
first = 'Dave'
last = 'Bowie'
name_dict = {first: last, 'Elvis': 'Presley'}
print(name_dict)


## 3 Strings
# - Use a literal to create a string containing:
# * a single quote,
# * a double quote,
# * both a single and double quote.

a = 'A string'
b = "B string"
print(a + ' ', b)

# or

c = "some 'quoted' text"


## 4 Strings Multi-line# -   Write a string literal that spans multiple lines.

print("""This string literal
...has more than one
...line""")

print("Hello \
World")

## 5 `join`
# -   Use the string `join` operation to create a string that contains a# colon as a separator.

text = ['My name is Gerald Hills', ';', 'and I am studying computer science.']
print(' '.join(text))

# solution

content = ['finch', 'sparrow', 'thrush', 'jay']
content.append('new word') #example of how to add to a list
new_str = ':'.join(content)
print(new_str)

## 6 String Format.# -   Use string formatting to produce a string containing your last and
# first names, separated by a comma.

custom_string = "Hills, Gerald"
print(f"{custom_string} is learning to code again")

# example of how to take string input and pass it in
first = 'Dave'
last = 'Bowie'
full = '%s, %s' % (last, first, )
print(full)
