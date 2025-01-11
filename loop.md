# Loop

## 1. **While Loop**
   - **Syntax**:
     ```python
     while condition:
         code
     ```
   - **Example**: Print numbers from 1 to 10.
     ```python
     i = 1
     while i <= 10:
         print(i)
         i += 1
     ```

## 2. **While Loop - Reverse Counting**
   - **Example**: Print numbers from 5 to 1.
     ```python
     i = 5
     while i >= 1:
         print(i)
         i -= 1
     ```

## 3. **Print Numbers from 1 to 100**
   - **Example**:
     ```python
     i = 1
     while i <= 100:
         print(i)
         i += 1
     ```

## 4. **Print Numbers from 100 to 1**
   - **Example**:
     ```python
     i = 100
     while i >= 1:
         print(i)
         i -= 1
     ```

## 5. **Multiplication Table of a Given Number**
   - **Example**:
     ```python
     n = int(input("Enter a number:"))
     i = 1
     while i <= 10:
         print(n * i)
         i += 1
     ```

## 6. **Loop Through List**
   - **Example**:
     ```python
     num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
     idx = 0
     while idx < len(num):
         print(num[idx])
         idx += 1
     ```

## 7. **Search a Number in a Tuple**
   - **Example**:
     ```python
     x = 9
     num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
     i = 0
     while i < len(num):
         if num[i] == x:
             print("Found")
         i += 1
     ```

## 8. **Break and Continue**
   - **Break**: Stops the loop.
     ```python
     i = 1
     while i <= 5:
         print(i)
         if i == 3:
             break
         i += 1
     ```
   - **Continue**: Skips the current iteration and continues to the next one.
     ```python
     i = 0
     while i <= 5:
         if i == 3:
             i += 1
             continue
         print(i)
         i += 1
     ```

## 9. **For Loop - Sequential Traversal**
   - **Example with a list**:
     ```python
     num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
     for val in num:
         print(val)
     ```

   - **Example with a tuple**:
     ```python
     tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
     for num in tup:
         print(num)
     ```

   - **Example with a string**:
     ```python
     str = "noushad"
     for char in str:
         print(char)
     ```

## 10. **Using Range Function**
   - Generate a sequence of numbers:
     ```python
     seq = range(10)  # range(stop)
     for i in seq:
         print(i)
     ```
   - **Example with start and stop**:
     ```python
     for i in range(2, 10):  # range(start, stop)
         print(i)
     ```
   - **Example with step**:
     ```python
     for i in range(2, 10, 2):  # range(start, stop, step)
         print(i)
     ```

## 11. **Print Even Numbers**
   - **Example**:
     ```python
     for i in range(2, 101, 2):
         print(i)
     ```

## 12. **Print Numbers 1 to 100**
   - **Example**:
     ```python
     for i in range(1, 101):
         print(i)
     ```

## 13. **Print Numbers 100 to 1**
   - **Example**:
     ```python
     for i in range(100, 0, -1):
         print(i)
     ```

## 14. **Multiplication Table of a Number**
   - **Example**:
     ```python
     n = int(input("Enter a number:"))
     for i in range(1, 11):
         print(n * i)
     ```

## 15. **Pass Statement**
   - Used when you need to write a block of code but don't want to execute it yet.
     ```python
     for i in range(10):
         pass
     print("Some useful work")
     ```

## 16. **Sum of First n Numbers**
   - **Example**:
     ```python
     n = 5
     sum = 0
     for i in range(1, n + 1):
         sum += i
     print("Total sum is", sum)
     ```

## 17. **Factorial of a Number Using For Loop**
   - **Example**:
     ```python
     n = 5
     fact = 1
     for i in range(1, n + 1):
         fact *= i
     print("Factorial of", n, "is", fact)
     ```

