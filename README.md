 Lab 06 - Object-oriented Programming

In this lab, we'll learn how to create classes, unit test those classes and their functions, as well as file input and output.

## Getting Started

Be sure that you have accepted the assignment invitation within GitHub Classroom (by clicking on the link provided in the lab assignment on Canvas), before you proceed.  You want to clone your own copy of the repository (not the original, since you can't write to that repository).  The command to do so will look something like this:

```
git clone https://github.com/CSCI1030U/lab06-rana-muniz
```

Be sure to change directory to a place where the rest of your CSCI1030U labs are stored, first, so that this command copies your lab assignment starter code into the proper place.

## Instructions

In this lab, you will write a `shapes.py` file so that it meets the requirements described in the following sections.  This file has no basic code to start, and it will be up to you to write all of the code for this lab.

#### Part 1

In `shapes.py`, write a Python class (`Rectangle`) which represents the data associated with a rectangle shape.  The `Rectangle` class will have three functions:

- a constructor
- `get_area()`
- `get_perimeter()`

Your class will store the `width` and the `height` of the rectangle, as floating point value instance variables.  The constructor will take two arguments (`width`, `height`), and will initialize those instance variables to those supplied values.

The `get_area()` will return the area of the rectangle, calculated in the body of the function using this formula:

```python
area = width * height
```

The `get_perimeter()` will return the perimeter of the rectangle, calculated in the body of the function using this formula:

```python
perimeter = width * 2 + height * 2
```

You can include some test code for your class, or you can exclude it when you submit.  The class itself will be all that is tested.

#### Part 2

In `shapes.py`, write a Python class (`Circle`) which represents a circle shape.  The `Circle` class will have three functions:

- a constructor
- `get_area()`
- `get_perimeter()`

Your class will store the `radius` of the circle, as a floating point value instance variable.  The constructor will take one arguments (`radius`), and will initialize that instance variable to this supplied value.

The `get_area()` will return the area of the circle, calculated in the body of the function using this formula:

	area = π * radius2

The `get_perimeter()` will return the perimeter (circumference) of the circle, calculated in the body of the function using this formula:

	perimeter = 2π * radius

You can include some test code for your class, or you can exclude it when you submit.  The class itself will be all that is tested.

#### Part 3

In `shapes.py`, write a Python class (`Shape`) which represents a general shape.  Modify the `Rectangle` and `Circle` classes from parts 1 and 2 to have the `Shape` class as a parent class (i.e. add an inheritance relationship between `Circle` and `Shape`, as well as between `Rectangle` and `Shape`).

You can include some test code for your classes, or you can exclude it when you submit.  The classes themselves will be all that is tested.

_**Note:** Since this part eliminates the need for parts 1 and 2, you will not need to submit the code for parts 1 and 2, but rather will submit the new set of three classes with the inheritance relationships for your lab submission._

## Verifying Correctness

Run the pre-written tests that verify that your lab assignment code passes, using the following command:

```
pytest
```

Examine the output closely.  There should be hints about what went wrong, if any of the tests fail.  If you are struggling to figure it out, you can always ask for help (see __Getting Help__ for details).


## Getting Help

If your code does not work, there is always a lab instructor present during your lab period for assistance.  Them not having to mark lab assignment submissions means that they should have plenty of time to ensure that you are able to get your lab assignment submission working by the end of the lab period.

_**Note:** The lab instructor is likely to help you figure out what is wrong with your code, rather than tell you how to fix it directly.  The goal is for you to learn how to diagnose and fix your bugs on your own._



## How to Submit

First, ensure that your code passes the tests (see the section __Verifying Correctness__ for details).  If you are certain that your code passes all of the tests, then you can submit your work using the following commands:

```
git add --all
git commit -m "Lab 06 completed code"
git push origin main
```

Once you have submitted your work, you can also double check that your auto-grading was successful by clicking on the `Actions` tab in your repository page on GitHub.  Sometimes, this takes a few minutes to complete, so please be patient.
