# Python-Functions-Files-and-Dictionaries
.readlines() turns a file object into a list of strings

.read() turns a file object into continuous string

Use relative path instead of absolute path which makes your data portable. So instead of saying something like `'User/Name/myFiles/allProjects/myData/data2.txt` (absolute path) do this `'../myData/data2.txt` (relative path) where `..` takes you to the parent folder.

#### ../ means one folder up in the directory search. ../../ means two folders up and goes on like ../../../ => three folders up

When you open a file using `with` then you don't have to bother in closing it. The Context Manager feature in python takes care of it. For instance, python program showing a use of with keyword:
` with open("test.txt") as f:   
    data = f.read()
 `

In order to create a dictionary, we use curly braces {}

Dictionaries like strings, lists, and tuples are a collection of items. But unlike strings, lists or tuples, they're an unordered collection of items meaning that they don't have a first, second or third item, they're kind of a bag of key value pairs.

A dictionary is an unordered collection of key value pairs.

`len(dict)` returns the total number of key-value pairs in a dictionary.

`in` only asks for a key in the dictionary.

Dictionary Accumulation

#### def hello(s,n): => 'def' implies that it is a function definition; 'hello' is the function name; 's,n' are the function parameters / parameter names / input parameters / formal parameters.

#### hello('David',4) => 'hello()' is the function invocation; ''David',4' are the provided arguments or values (function arguments) / parameter values / actual parameters.

The scope of a variable is the set of statements where a variable name can be accessed. 

#### As a problem-solving strategy, it's helpful to decompose, to find a function by referring to other functions that don't yet exist and then write those functions.

#### Variables are local, but objects are not.

#### List objects are always mutable in python.

When a python function returns multiple values, it automatically transforms the values in a form of tuple. This phenomenon is called `Tuple Packing`.

Listener loop uses while statement.

When we mention a data structure in the function parameter, then it will only take arguments of that same data structure. For instance, the following function will only take 'list' as its argument => `def stop_at_z(list):`

You can initiate some parameters as optional in the function call. Such as, `def func(a, L=[])`. L = [] is an optional parameter when the function is called. For instance, func(1), func(4) or func(3, ['s']) etc. Anything will work!!!

Keyword arguments should always be placed after the positional arguments. Unless, it will show up an error.

We can make a lambda expression an anonymous function which does not have a name. For instance, `lambda x,y: x + y` or with name such as
`total = lambda x,y: x + y` where total is the function name.

In lambda expression, the return is implicit.

#### There are three key differences between .sort() method and sorted() function:
==> .sort() is a method called upon an object and sorted() is a function which takes an object as an argument
==> .sort() does not return anything, it just sorts the original object; sorted() returns a new sorted object
==> .sort() changes the original object, sorted() does not change the original object.

#### sorted() function is the safest option to use. Because, it can be applied to any sequence (highly flexible), can be implemented with additional parameters, always returns value with a new sorted sequence.

If you want to sort items in the descending order, then use the optional parameter `reverse=True` inside the sorted() function!!!

#### The sorted() function has the following implimentations in it's full form: `sorted(sequence, reverse=boolean value, key=function can be applied to the sequence)`.

#### `key` is a major aspect inside the sorted() function. We can apply distinctive functions on the designated sequence of items upon which the sorted() function is applied through the `key optional parameter`. Key is meant to be a property here upon which the sequence is sorted. Check the picture of an implementation in the repository.

#### Mind it: the `key function` can be a named function or a lambda expression!!!

Lambda expressions are expressions that produce anonymous functions. 

If d is a dictionary then while iterating through the keys of that dictionary, we can use just d instead of d.keys() in the for loop. It's actually a shorthand!

If you want to specify a tie-breaking property, have your key function return a tuple. Like key functions everywhere, they always take one item from the sequence as input, but now it's going to return a tuple, where the first element of the tuple is the primary property to sort by, the next element is the secondary property to sort by, and you could even have more elements in the tuple. We also saw that if you just want to reverse order for one of the properties but not the others, instead of using reverse equals true, you can make the key function return negative of all the numbers.

For the implementation, check this out:
https://www.coursera.org/learn/python-functions-files-dictionaries/lecture/kHMob/breaking-ties

Here's a little way of the programmer advice on when to use a Lambda expression, and when to use a named function for key parameter when sorting. Basically, rule of thumb is if the lambda expression is short and simple, so that it's pretty easy to understand what it's doing, use the lambda expression, and as soon as it gets too complex, refer to a named function instead, and give it a good name that describes the property you're trying to sort by. 

#### When to Use a Lambda Expression: https://www.coursera.org/learn/python-functions-files-dictionaries/lecture/m97K5/way-of-the-programmer-when-to-use-a-lambda-expression

#### To get the last `n` items from a list use the `[-n]` syntax.

#### When we introduce a `key` property to a sorted() function, the `key` implies to each element of that sequence. Mind it!!!








































