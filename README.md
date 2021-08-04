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









































