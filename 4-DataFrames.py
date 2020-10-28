# pandas DataFrames - Data containers, pt 4

# Get a DataFrame when impoting a file

# Or from a dict:
foo1 = [True, False, False, True, True, False]
foo2 = ["Liver", "Brain", "Testes", "Muscle", "Intestine", "Heart"]
foo3 = [13, 88, 1233, 55, 233, 18]

# Collect list into a dataframe
foo_df = pd.DataFrame({'healthy': foo1, 'tissue': foo2, 'quantity': foo3})
foo_df
type(foo_df)

# Or from a list of keys and values:
list_names = ['healthy', 'tissue', 'quantity']
# A list of lists
list_cols = [foo1, foo2, foo3]
# zip put the key/value pairs together
pd.DataFrame(dict(zip(list_names, list_cols)))

# Access information by:
# Name (here)
# Position (later, indexing)

# columns
foo_df.columns
# rows
foo_df.index

foo_df['healthy'] # Series
type(foo_df['healthy'])

foo_df[['healthy']] # DataFrame
type(foo_df[['healthy']])

foo_df.healthy # a Series

foo_df[['quantity', 'healthy']] # DataFrame

# each column is a Series
# DataFrames are build upon np.arrays
# i.e. Series can only be ONE type!

foo_df.info()

quantity_list = foo3.copy()
# quantity_list.mean() # no!
np.mean(quantity_list) # yes :)
# quantity_list/100 # no!

quantity_array = np.array(foo3)
quantity_array.mean()
quantity_array/100
quantity_array.astype("str")
# quantity_array.name # no!

quantity_Series = foo_df['quantity']
quantity_Series.mean()
quantity_Series/100
quantity_Series.astype("str")
quantity_Series.name

test_Series = pd.Series(quantity_array)
test_Series.name = "hello"
test_Series

# four main data containers
# list - 1-dimensional, heterogenous type
# dictionary - key/value pairs
# np.array - n-dimensional, homogenous type
# pd.DataFrame - 2-dimensional, collection of Series

# plus these special ones
# tuple - 1-dimensiona, immutable, heterogenous type
# Series - Special case of np.array in a DF

# Beginning with two lists
cities = ['Munich', 'Paris', 'Amsterdam', 'Madrid', 'Istanbul']
dist = [584, 1054, 653, 2301, 2191]

# Exercise 4.1: Make a dictionary manually, then a DF
pd.DataFrame({'cities':cities,
              'dist':dist})

# Exercise 4.2: 
list_names = ['cities', 'dist']
list_values = [cities, dist]

pd.DataFrame(dict(zip(list_names, list_values)))

# Broadcasting
# We already saw...
foo_df.quantity / 100
foo_df['quantity'] / 100

foo_df['new'] = 0
foo_df

foo_df['new'] = range(6, 12)
foo_df

foo_df['new'] = ['A', 'B', 'C', 'a', 'b', 'c']
foo_df

# Removing a column
foo_df = foo_df.drop('new', axis = 1)
# axis 0 = rows  
# axis 1 = columns
foo_df
foo_df_2 = foo_df.copy()
foo_df_2.drop(['healthy', 'tissue'], axis = 1)

# mtcars case study
mtcars = pd.read_csv('./data/mtcars.csv')
mtcars.info()
# import os
# os.listdir()

# Calculate the correlation between mpg and wt and test if it is significant
mtcars['mpg'].corr(mtcars['wt'])
mtcars.mpg.corr(mtcars['wt'])

# Visualize the relationship in an XY scatter plot
sns.scatterplot('wt', 'mpg', data=mtcars)
sns.regplot('wt', 'mpg', data=mtcars)

# Calculate linear model
reg1 = sm.OLS(endog = mtcars['mpg'], 
              exog = mtcars['wt'])
regResults = reg1.fit()
regResults.summary()
0.720 # R^2 from model
-0.8676**2 # R^2 from correlation function

model = ols("mpg ~ wt", mtcars)
# call the fit method
results = model.fit()
# results
print(results)
results.params
dir(results)
results.summary()

# Convert weight from pounds to kg
mtcars['wt_kg'] = (mtcars['wt']*1000)*0.4536


# If statements in brief:
# Each conditional should return a single True/False
xx = 2
if (xx > 1):
    print("too large")
elif (xx < -5):
    print("too small")
else: 
    print("yesssss!")


# Iterations
letters = ['A', 'B', 'C'] # list
letters = "Rick" # string
letters = range(6) # range

for names in letters:
    print(names)

# i.e. list, string, range are "iterable"
# They return an "iterator" object
# in which we can call next()

letters = "Hello"
it = iter(letters)
next(it)
next(it)
next(it)
next(it)
next(it)
next(it)

letters = "Hello"
iter(letters)

# We can add a counter with the enumerate() function
letters = "Hello"
letters = ['A', 'B', 'C'] # list

# we can also specify where to strat the counter:
e = enumerate(letters, start = 1)
e
# view
e_list = list(e)
e_list

for index, value in e:
    print(f"position {index} has letter {value}")

for index, value in enumerate(['A', 'B', 'C']):
    print(f"position {index} has letter {value}")

# enumerate basically makes a list of tuples

# We can use a zip object
heights = [167, 188, 178, 194, 171, 169]
persons = ["Mary", "John", "Kevin", "Elena", "Doug", "Galin"]

for z1, z2, z3 in zip(persons, heights, range(6)):
    print(f"person {z3} is {z1}, who is {z2} cm tall.")

# for z1, z2 in [persons, heights]:
#     print(f"{z1} is {z2} cm tall.")

# Exercise 9.1, DataFrames:
myGroups = plant_growth.group.unique()

for value in myGroups:
    result = np.mean(plant_growth.weight[plant_growth.group == value])
    print(f"The mean of {value}: {round(result, 2)}")

# Split-Apply-Combine

myRes = list(range(1000))
l = [None]*3
l

for index, value in enumerate(myGroups):
    result = np.mean(plant_growth.weight[plant_growth.group == value])
    l[index] = result
    print(f"The mean of {value}: {round(result, 2)}")
l
myRes

# List and dict comprehensions
# very compact for loops

heights # in cm

# heights/100 # in meters, no-go
heights_a = np.array(heights)/100 # yes :)
#list(heights_a)

new_list = []
for num in heights:
    new_list.append(num/100)
new_list

# list comprehensions 
[[output expression] for [iterator variable] in [iterable object]]

# for example:
[num/100 for num in heights]

# Nested loops
pairs_1 = []
for num1 in range(2):
    for num2 in range(6,8):
        pairs_1.append([num1, num2])
pairs_1

# as comprehension:
[[num1, num2] for num1 in range(2) for num2 in range(6,8)]

# 0,6
# 1,7
[[num1, num1+6] for num1 in range(2)]

# A more practical example:
[[j for j in range(5)] for i in range(5)]
# [[col for col in range(2)] for row in range(8)]
# [print("hi") for row in range(8)]
# [col for col in range(2)]
[list(range(5)) for row in range(5)]

# Loops with conditionals
# on input or output

# No filter
[num ** 2 for num in range(10)]

# on input
[num ** 2 for num in range(10) if num % 2 == 0]

# on output
[num ** 2 if num % 2 == 0 else 0 for num in range(10)]
res = [num ** 2 for num in range(10)]
res

# Exercise 10.1, 10.2:
cities = ['Munich', 'Paris', 'Amsterdam', 'Madrid', 'Istanbul']
# Which ones are long (>6 characters)
[a for a in cities if len(a) > 6]

for a in cities:
    if len(a) > 6:
        print(a)

# [len(a) for a in cities]

[a if len(a) > 6 else "" for a in cities]
