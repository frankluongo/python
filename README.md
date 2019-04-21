# Frontend Masters - Two Day Python Workshop

These are the resources for Nina Zakharenko's Two Day Intro to and Intermediate Python Course

* [Watch Python Fundamentals on Frontend Masters](https://frontendmasters.com/courses/python/)

The majority of the content can be found on the course website.

* [Course Website - learnpython.netlify.com](https://learnpython.netlify.com)
* [This Repo - git.io/python3](https://git.io/python3)
* [Follow Nina on Twitter](https://twitter.com/nnja)

## License

The content of this project itself is licensed under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) license](https://creativecommons.org/licenses/by-nc-nd/4.0/), and the underlying source code used to format and display that content, along with the code exercises is licensed under the [MIT license](LICENSE.md).

# Course Notes

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

## Python Don'ts
- Don't start variables with a number
- Be careful when naming variables as not to override built-in types


## Data Types

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

## Functions

### Functions
- Function uses indentation to scope things
```py
def test_function(x, y):
  return x + y

test_function(5, 7)
```

---


## Notes
- Read errors bottom to top
