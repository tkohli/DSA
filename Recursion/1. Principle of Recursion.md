# Principle of Recursion

Recursion is an approach to solving problems using a function that calls itself as a subroutine.<br>

You might wonder how we can implement a function that calls itself. The trick is that each time a recursive function calls itself, it reduces the given problem into subproblems. The recursion call continues until it reaches a point where the subproblem can be solved without further recursion.<br>

A recursive function should have the following properties so that it does not result in an infinite loop:<br>

A simple base case (or cases) — a terminating scenario that does not use recursion to produce an answer.<br>
A set of rules, also known as recurrence relation that reduces all other cases towards the base case.<br>
Note that there could be multiple places where the function may call itself.<br>

## Some basic / small tasks we can do in recursion.

1. Print a string in reverse order. https://leetcode.com/problems/reverse-string/<br>
2. Print a linked list.<br>

## Steps

function F(X), we will:<br>

1. Break the problem down into smaller scopes, <br>
2. Call function F(x_0), F(x_1), ..., F(x_n)F(x) recursively to solve the subproblems of <br>
3. Finally, process the results from the recursive function calls to solve the problem corresponding to X.

# Recurrence Relation

There are two important things that one needs to figure out before implementing a recursive function:<br>

1. recurrence relation: the relationship between the result of a problem and the result of its subproblems.<br>
2. base case: the case where one can compute the answer directly without any further recursion calls. Sometimes, the base cases are also called bottom cases, since they are often the cases where the problem has been reduced to the minimal scale, i.e. the bottom, if we consider that dividing the problem into subproblems is in a top-down manner.<br>

## Case Study

Now solve fibonacci sequence using recursion, make it recursive tree.<br>
You'll realize that it is doing same calculation again and again<br>
Bigger number would start giving TLE.<br>
Here the concept of memoization comes to play we basically store the values returned by function it either dict or arr such that we do not perform calculation again and again.<br>
Similarly solve climbing stairs.

# Time complexity of recursion

Given a recursion algorithm, its time complexity O(T) is typically the product of the number of recursion invocations (denoted as R) and the time complexity of calculation (denoted as O(s)) that incurs along with each recursion call:
<br><br>
O(T) = R \* O(s)
<br>
Thoughts on time complexity of reverse string

# Space Complexity of recursion

The recursion related space refers to the memory cost that is incurred directly by the recursion, i.e. the stack to keep track of recursive function calls. In order to complete a typical function call, the system allocates some space in the stack to hold three important pieces of information:
<br>
The returning address of the function call. Once the function call is completed, the program must know where to return to, i.e. the line of code after the function call.<br>
The parameters that are passed to the function call. <br>
The local variables within the function call.<br>
This space in the stack is the minimal cost that is incurred during a function call. However, once the function call is done, this space is freed.<br>
<br>
O(N) Space

## Tail recursion

Tail recursion is a recursion where the recursive call is the final instruction in the recursion function. And there should be only one recursive call in the function.
