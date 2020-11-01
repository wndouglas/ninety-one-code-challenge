<h1 align="center"> Ninety One Coding Challenge </h1>

<!-- content -->

## Table of Contents
- [Problem Specification](#Problem-Specification)
  - [Problem](#Problem)
  - [Test cases](#Test-cases)
  - [Notes](#Notes)
  - [Evaluation criteria](#Evaluation-criteria)
- [Design Choices and Assumptions](#Design-Choices-and-Assumptions)
  - [Programming Language](#programming-language)
  - [Application type](#Application-type)
  - [Key assumptions](#Key-assumptions)
- [Getting Started](#Getting-Started)
  

## Problem Specification
### Problem
Write a function that converts a given number into words. For example, given the number "1234" as input, return the output "one thousand, two hundred and thirty-four".

The input will consist of lines of text containing random digits. You are expected to handle invalid numbers appropriately.

### Test cases
| Test input                                          | Expected output                                                                                     |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| The pump is 536 deep underground.                   | five hundred and thirty-six                                                                         |
| We processed 9121 records.                          | nine thousand, one hundred and twenty-one                                                           |
| Variables reported as having a missing type #65678. | number invalid                                                                                      |
| Interactive and printable 10022 ZIP code.           | ten thousand and twenty-two                                                                         |
| The database has 66723107008 records.               | sixty-six billion, seven hundred and twenty-three million, one hundred and seven thousand and eight |
| I received 23 456,9 KGs.                            | number invalid                                                                                      |
 
### Notes
* Ideally R, Python or C but open to other languages
* Application should include a way to input data via a plain-text file
* Application must be able to run with the output directed to `STDOUT`
* Application should output correct values for inputs *other* than those specified above
* Should provide sufficient evidence that your application is complete by including an example using the above test cases
* Should *not* use 3rd party libraries specifically designed for this purpose

| **Please include an explanation of your design choices and assumptions, along with your code and any instructions necessary to run the application**

### Evaluation criteria
* Looking for the **thought process** and approach to deriving a solution, not the most *technically correct* solution
* This is an opportunity to showcase knowledge and highlight what I value within a software project
* Small problem, but ensure that should be able to:
    * run
    * maintain
    * evolve

---

## Design Choices and Assumptions
### Programming language
For this problem, optimised performance is likely *not* a critical factor. The main difficulty arises from parsing text 
and converting this parsed text into a different output. For this problem, **Python** is particularly well suited and 
this is the programming language I have chosen to use. If better performance is desired, it would be possible to 
parallelise certain elements within the application where performance bottlenecks present themselves.

### Application type
I have chosen to create a Python package that can be installed via Pip. A wrapper to the package allows it to be used
as a command line application.

### Key assumptions
The key assumptions made during the design were:
* The user only wishes to use a text file input, with each line separated by a new line.
* In general, the user wishes to send their output to a text file. If a name is not specified then the output goes to
standard output.
* Numbers cannot grow larger than 999,999,999,999,999.
* Users only wish their output to be displayed in UK English (although the groundwork for internationalisation is there)
* Users only wish to extract one number per line (in the current implementation, subsequent numbers are ignored).

---
## Getting Started
Getting started is easy. The top-level functionality is provided in the `runner.py` script. In the top-level directory
`ninety-one-code-challenge`, simply run:

```python runner.py --i <input-file-location> --o <output-file-location>```

If you leave the output file location blank, the program defaults to outputting to STDOUT. In this case, simply run:

```python runner.py --i <input-file-location>```

If you would like to try out the examples (which includes the test input given in the problem spec, along with an
example containing a large number of numbers), then I recommended navigating into the ``examples`` folder on the command
line. Once inside this folder, you need to add the root directory to your *Python path*. To do so, run

```export PYTHONPATH=".."```

Once this is added to your Python path, you should be able to run

```python test_input_example.py```

for example.

To run the test suite, navigate back to the top level directory and run

```python -m unittest```

Please do not hesitate to reach out if you have any questions or recommendations.