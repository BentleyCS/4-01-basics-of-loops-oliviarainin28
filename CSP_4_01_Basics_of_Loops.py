#All questions must use a loop for full points.

def oddNumbers(n:int) ->str:
    """
    Print out all odd numbers from 1 to n(inclusive) in a single string seperated by spaces.
    example oddNumbers(5) -> "1 3 5"
    example oddNumbers(8) -> "1 3 5 7"
    example oddNumbers(-8) -> ""
    """
    answer = ""
    for x in range(1,n+1):
        if x%2 ==1:
            answer += str(x)
            if x+2 <= n:
                answer += " "
    return answer
def backwards(n)-> int:
    """
    modify the below function such that it prints out all the numbers from n to 1
    inclusive starting at n and counting down to 1
    example backwards(5) -> "5 4 3 2 1"
    example backwards(8) -> "8 7 6 5 4 3 2 1"
    example backwards(-2) -> ""
    """
    if n < 1:
       return ""

    result = str(n)

    for x in range(n-1,0,-1):
       result += " " + str(x)

    return result

def randomRepeating():
    """
    Print out a random number from 1-10 until you get a 10. Then print out how many
    times it took to roll a 10
    NOTE: Given randomness no test for this question
    :return:
    """
    tries = 0
    #print(random.randint(1, 10))
    #print(f"it took {tries} tries to get a 10")
    num = 0

    while num != 10:
        num = random.randint(1,10)
        tries += 1
    print(f"It took {tries} to get a 10")

def randomRange(n):
    """
    Generate a random number from 1 to 100 n number of times. Then after that is
    done print out what the highest number and the lowers number was from the rolled numbers.
    NOTE: Given randomness no test for this question
    :param n:
    :return:
    """
    nums = []
    for _ in range(n):
        nums.append(random.randint(1,100))

    print("Highest:", max(nums))
    print("Lowest:", min(nums))

def reverse(word:str)->str:
    """
    Takes in a string as an argument and return the given string in reverse.
    example reverse("cat") -> "tac"
    example reverse("Hello") -> "olleH"
    """
    answer = ""
    for c in word:
        answer = c + answer
    return answer

def fizzBuzzContinuous(n):
    """
    Modify the function such that it does the fizzbuzz operation on all numbers
    from 1 to n(inclusive).
    Fizz buzz is defined as
    if the number is divisble by 3 print fizz
    if the number is divisible by 5 print buzz
    if the number is divisible by both 3 and 5 print fizzbuzz
    if none of the above apply print the number.

    As with above questions add each anseer to a string and return the final string.
    :param n:
    :return:
    """
    answer = ""
    first = True

    for x in range(1, n+1):
        if not first:
            answer += " "
        if x%3 == 0 and x%5 == 0:
            answer += "fizzbuzz"
        elif x%3 == 0:
            answer += "fizz"
        elif x%5 == 0:
            answer += "buzz"
        else:
            answer += str(x)
        first = False
    return answer
    return answer
def collatz(n):
    """
    Modify this function such that it mimics the collatz conjecture starting at n
    and prints out each number.
    The collatz conjecture is that if n is an even number divide it by 2. if n is
    an odd number multiply it by 3 and add 1.
    Repeat this process until n == 1.
    :param n:
    :return:
    """
    result = str(n)

    while n != 1:
        if n%2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        result += " " + str(n)
    return result

def fibonacci(n):
    """
    for the given argument n print out the first n numbers of the fibonacci
    sequence in a single string seperated by spaces.
    The fibonacci sequence is defined as a sequence that starts with 0 then 1 as
    the first two numbers. Every subsequent number is the prior two numbers added together.
    Example fibonacci(6) -> "0 1 1 2 3 5"
    Example fibonacci(10) -> "0 1 1 2 3 5 8 13 21 34"
    Example fibonacci(1) -> "0"
    :param n:
    :return:
    """
    if n <= 0:
        return ""
    if n == 1:
        return "0"
    a = 0
    b = 1
    answer = "0 1"
    count = 2

    while count < n:
        c = a + b
        answer += " " + str(c)
        a = b
        b = c
        count += 1
    return answer

def test_odd_numbers():
    assert oddNumbers(5) == "1 3 5"
    assert oddNumbers(8) == "1 3 5 7"
    assert oddNumbers(-8) == ""
    assert oddNumbers(80) == "1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79"

test_odd_numbers()
