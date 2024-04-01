# Python Notes 

## Python internal Working 

-----------------------------------------

1. Details of .pyc file 

- Name of the .pyc file ==> source code changes + python version

- A `.pyc` file is a compiled ( its a term not defines actual "compile" ) Python file. When you write a Python script and execute it, Python compiles the script into bytecode before interpreting it. This bytecode is what actually gets executed by the Python interpreter. When Python compiles a script, it creates a corresponding `.pyc` file, which contains the bytecode version of the script.

- The purpose of `.pyc` files is to speed up the execution of Python programs. Instead of recompiling the source code every time it's executed, Python can simply load the precompiled bytecode from the `.pyc` file, which is generally faster.

- Here's a brief overview of how `.pyc` files work:

1. When you run a Python script (`example.py`), Python first checks if there's a corresponding `.pyc` file (`example.pyc`) with the same name and in the same directory as the script.
2. If a `.pyc` file exists and is up-to-date (i.e., the source `.py` file hasn't been modified since the last `.pyc` file was generated),  here python usess Diffing ALgo to find out the changes , Python loads the bytecode from the `.pyc` file and executes it directly.
3. If there's no `.pyc` file or if it's outdated, Python compiles the source code into bytecode and then saves the bytecode to a new `. pyc` file before executing it.

4. `.pyc` files are platform-independent, meaning you can distribute them and execute them on different platforms without recompiling the source code. However, they are specific to the Python version that generated them, so you can't use a `.pyc` file compiled with one Python version with a different Python version.

- It's worth noting that `.pyc` files are not meant to be edited directly. They are meant for Python's internal use and are generally automatically generated and managed by the Python interpreter.

- .pyc file only works  with  imported files  , not for top level files ( mostly hidden )


--------------------------------------------------

### __pycache__ ==> its consists of .pyc files
-------------------------------------------------
- PVM ==> its python Virtual Machine 
        code loop to iterate byte code 
        Run time Engine 
        Also Known as python Interpeter 

--------------------------------------------------

## Immutable and Mutable ::

- In python this concepts works differenly . In python we call everything as object  . when we assign a value to a variable , first in memory a object created with the value and then the variable is referencing the object , so 

- for Immutable you can't change the content object ,  but you can create a new object and refereve the same variable to that object 

str = "python"

 str[1] ='i' <-- this will not happen as we want to change the str variable content , 

str = "pithon" <-- In this case a new "pithon" object created and the str variable is pointing to this object now 

Immutable = 
Mutable =


-----------------------------------------------------

## DataTypes 

#### Dictionary 
- dict["key"] = value 
- { key1 : value1 , key2 : value2 , key3: value3} 
- dict1.pop(key)
- dict1.popitems()
- len(dict1)
- dict1 = {x : x**2 for x in range(0,10)} 
- dict1.keys() --> view object
- dict1.values --> view object 
- dict1.items() --> view object 
- dict1.clear() 

##### Tuples
- 