# **CSCK541_Floyd**

## **Description**
<br>

The Floyd Warshall Algorithm is a shortest path algorithm that identifies teh shortest path between  two nodes on a graph.<br>

CSCK541_floyd is a directory that contains iterative and recursive functions for the Floyd Warshall Algorithm. <br>

There ardirectory also contains a unit test file for the recursive function and a performance test file which compared performacne of the iterative and recursive functions.<br>
<br>

## **Installing Dependencies**
<br>

First download the directory to a local file path.<br>

From the command line navigate to this file path and run the following command to install the required python packages:<br>
```
pip install -r requirements.txt
```
For more information on installing packages see the [pip documentation](https://pip.pypa.io/en/stable/user_guide/#installing-packages)<br>
<br>

## **Usage**
<br>

### **Running the shortest path files**
<br>

From the command line navigate to the src file. <br>

To run the recursive_floyd_warshall module use the command:

```
python recursive_floyd_warshall.py
```

To run the iterative_floyd_warshall module use the command:

```
python iterative_floyd_warshall.py
```
<br>

### **Finding the Shortest Path for any Matrix**
<br>

To find the shortest path for any n x n matrix open, either or both, recursive_floyd_warshall.py or iterative_floyd_warshall.py in an IDE.<br>

Replace the matrices starting on line 9 and 10 respectively with your own n x n matrix that defines the direct distance between each pair of nodes and run the file.<br>

To find the performance differences between recursive and iterative functions for matrices of different size or characteristics open the fw_performance_tests.py file in an IDE and  edit the matrix shown in line 20.<br>
<br>

### **Unit Tests**
<br>

The unit tests define 5 test cases to ensure correct functioning of the floyd_warshall_recursive function defined in recursive_floyd_warshall.py.<br>

To run the unit tests from the command line, navigate to the tests file and run the following command<br>

```
python fw_unit_tests.py
```
To update this unit test file for other functions open the file in your IDE. 

Update line 7 to import your own function from its reference path and update all references to floyd_warshall_recursive to your own function name.<br>

To add more test cases, add a new function to the class TestFloyd. <br>

<br>

### **Performance tests**
<br>

To understand the performance differences of the iterative and recursive functions, navigate to the tests file on the command line and run the following prompt:<br>

```
python fw_performance_tests.py
```

This file will show the mean execution time of each function over 2000 calls to the function for a given input graph. <br>

The Shapiro-Wilk statistical test for normal distribution will be run on the execution times of each function and the shapiro statistic and p value will be displayed in th terminal. <br>

If data is not normally distributed the outcome of a t-test comparing the statistical difference between the recursive and iterative functions will be shown.<br>

A visualisation of  execution time distribution for each function will also be displayed.<br>

To compare the performance of recursive and iterative functions for matrices of different sizes or characteristics, you can change the input graph by opening the fw_performance_tests.py file and editing the input graph shown in line 20.<br>
<br>

## **Author**
<br>

Joseph Passant<br>

j.passant@liverpool.ac.uk<br>
<br>

## **LICENSE**
<bR>

MIT License

Copyright (c) 2023 Joseph Passant

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
