Task
        Read two integers from STDIN and print three lines where:

        The first line contains the sum of the two numbers.
        The second line contains the difference of the two numbers (first - second).
        The third line contains the product of the two numbers.
    Input Format

        The first line contains the first integer, . The second line contains the second integer, .

    Output Format

        Print the three lines as explained above.
#Code

a = int(input())
b = int(input())
sum=a+b
substraction=a-b
product=a*b
print(sum)
print(substraction)
print(product)
