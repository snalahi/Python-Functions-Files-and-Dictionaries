# Python-Functions-Files-and-Dictionaries
.readlines() turns a file object into a list of strings

.read() turns a file object into continuous string

Use relative path instead of absolute path which makes your data portable. So instead of saying something like `'User/Name/myFiles/allProjects/myData/data2.txt` (absolute path) do this `'../myData/data2.txt` (relative path) where `..` takes you to the parent folder.

#### ../ means one folder up in the directory search. ../../ means two folders up and goes on like ../../../ => three folders up

When you open a file using `with` then you don't have to bother in closing it. The Context Manager feature in python takes care of it. For instance:
`# Python program showing a use of with keyword:
 with open("test.txt") as f:   
    data = f.read()
 `













































