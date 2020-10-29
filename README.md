<h1 align="center"> Ninety One Coding Challenge </h1>

## Probem Specification
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
* Ideally `R`, `Python` or `C` but open to other languages
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
