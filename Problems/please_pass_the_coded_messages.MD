<h1 align= "center"><b>Please Pass the Coded Messages</b></h1

You need to pass a message to the bunny prisoners, but to avoid detection, the code you agreed to use is... obscure, to say the least. The bunnies are given food on standard-issue prison plates that are stamped with the numbers 0-9 for easier sorting, and you need to combine sets of plates to create the numbers in the code. The signal that a number is part of the code is that it is divisible by 3. You can do smaller numbers like 15 and 45 easily, but bigger numbers like 144 and 414 are a little trickier. Write a program to help yourself quickly create large numbers for use in the code, given a limited number of plates to work with.

You have L, a list containing some digits (0 to 9). Write a function answer(L) which finds the largest number that can be made from some or all of these digits and is divisible by 3. If it is not possible to make such a number, return 0 as the answer. L will contain anywhere from 1 to 9 digits.  The same digit may appear multiple times in the list, but each element in the list may only be used once.

<h3 align= "center"><b>Test Cases </b></h3>

```
Inputs:
   
(int list) l = [3, 1, 4, 1]

Output:

(int) 4311


Inputs:

(int list) l = [3, 1, 4, 1, 5, 9]

Output:

(int) 94311
```