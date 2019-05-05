# Frontend Masters - Two Day Python Workshop

These are the resources for Nina Zakharenko's Two Day Intro to and Intermediate Python Course

* [Watch Python Fundamentals on Frontend Masters](https://frontendmasters.com/courses/python/)

The majority of the content can be found on the course website.

* [Course Website - learnpython.netlify.com](https://learnpython.netlify.com)
* [This Repo - git.io/python3](https://git.io/python3)
* [Follow Nina on Twitter](https://twitter.com/nnja)




----




# Course Notes

To start REPL, press CMD+SHIFT+P and select Python REPL

## Useful Methods in Python
Three most useful Python Tools
```py
  # Get the type of something
  type(variable)
  # Get all the functions available for something
  dir(variable)
  # Get Help on something
  help(str)
  help(str.upper)
```

## Chapter 1: Why Choose Python
- Don't start variables with a number
- Be careful when naming variables as not to override built-in types


## Chapter 2: Basic Data Types

### Variables
- Use lowercase letters and underscores
- Variables are dynamic so you don't need to specify type
- Python uses `None` as their null/nil


### Numbers
- Add a decimal to make a number a float
- You can specify number types using `int()` or `float()`

### Strings
- Can use single or double quotes – It doesn't matter
- Best practice is to use double quotes
- `"""` is a long string
- F-String: `f"Hello, {name}"`

### Practice: Data Type
[Practice Link](https://www.learnpython.dev/02-introduction-to-python/020-basic-data-types/10-exercise/)





## Chapter 3: Functions

### Functions
- Function uses indentation to scope things
```py
def test_function(x, y):
  return x + y

test_function(5, 7)
```


### [Function Arguments](https://www.learnpython.dev/02-introduction-to-python/060-functions/30-function-arguments/)
- Default arguments go last
- Don't use empty lists because Python will just keep adding to them when you call the function

```py
def say_greeting(name, greeting="Hello")
  print(f"{greeting}, {name}")
```


### [Function Scope](https://www.learnpython.dev/02-introduction-to-python/060-functions/40-scope/)
```py
def twitter_info():
    twitter_account = "nnja"
    print(f"Account inside function: {twitter_account}")
twitter_info()
print(f"Account outside of function: {twitter_account}")
```

```py
name = "Nina"
print(f"Name outside of function: {name}")
def try_change_name():
    name = "Max"
    print(f"Name inside of function: {name}")
try_change_name()
print(f"Name outside of function: {name}")
```



## [Chapter 4: Advanced Container Types](https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/)

### [Lists, Part 1](https://www.learnpython.dev/02-introduction-to-python/080-advanced-datatypes/10-lists/)
- Lists maintain the order of the items inside them

---


## Notes
- Read errors bottom to top
