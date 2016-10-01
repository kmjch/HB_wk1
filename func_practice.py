"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE:

    >>> hello_world()
    Hello World

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn

    >>> print_product(3, 5)
    15

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False

    >>> num_spaces("Balloonicorn is awesome!")
    2

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0



PART TWO:

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn

"""
################################################################################
# PART ONE

# 1. Write a function called 'hello_world' that does not take any arguments and
#    prints "Hello World".


def hello_world():
    """ Prints "Hello World".

    >>> hello_world()
    Hello World
    """
    print "Hello World"


# 2. Write a function called 'say_hi' that takes a name as a string and
#    prints "Hi" followed by the name.


def say_hi(input_name):
    """ Greets the person whose name you enter.

    >>> say_hi("Balloonicorn")
    Hi Balloonicorn
    """
    print "Hi " + input_name


# 3. Write a function called 'print_product' that takes two integers and multiplies
#    them together. Print the result.


def print_product(int1, int2):
    """ Gives you the product of two user-inputted numbers.

    >>> print_product(3, 5)
    15
    """
    print int1 * int2


# 4. Write a function called 'repeat_string' that takes a string and an integer and
#    prints the string that many times


def repeat_string(input_word, num_repeat):
    """ Repeats a word a given number of times.

    >>> repeat_string("Balloonicorn", 3)
    BalloonicornBalloonicornBalloonicorn
    """
    print input_word * num_repeat


# 5. Write a function called 'print_sign' that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".


def print_sign(num):
    """ Tells you whether your number is greater, less than, or equal to 0.

    >>> print_sign(3)
    Higher than 0

    >>> print_sign(0)
    Zero

    >>> print_sign(-3)
    Lower than 0
    """
    if num > 0:
        print "Higher than 0"
    elif num < 0:
        print "Lower than 0"
    else:
        print "Zero"


# 6. Write a function called 'is_divisible_by_three' that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


def is_divisible_by_three(num):
    """ Tells you whether or not your number can be evenly divided by 3.

    >>> is_divisible_by_three(12)
    True

    >>> is_divisible_by_three(10)
    False
    """
    return num % 3 == 0


# 7. Write a function called 'num_spaces' that takes a sentence as one string and
#    returns the number of spaces.


def num_spaces(sentence):
    """ Counts the number of spaces in your sentence.

    >>> num_spaces("Balloonicorn is awesome!")
    2
    """
    words = sentence.split(" ")
    return len(words) - 1


# 8. Write a function called 'total_meal_price' that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


def total_meal_price(price, tip=.15):
    """ Calculates the total meal price with tip.

    >>> total_meal_price(30)
    34.5

    >>> total_meal_price(30, .3)
    39.0
    """
    return price * (1 + tip)


# 9. Write a function called 'sign_and_parity' that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.


def sign_and_parity(num):
    """ Tells you whether your number is even or odd, positive or negative.

    >>> sign_and_parity(3)
    ['Odd', 'Positive']

    >>> sign_and_parity(-2)
    ['Even', 'Negative']
    """
    def check_parity(num):
        if num % 2 == 0:
            return 'Even'
        return 'Odd'

    def check_sign(num):
        if num > 0:
            return 'Positive'
        return 'Negative'

    return [check_parity(num), check_sign(num)]

sign = sign_and_parity(3)[0]
parity = sign_and_parity(3)[1]

print "Sign of 3: ", sign
print "Parity of 3: ", parity


################################################################################
# PART TWO

# 1. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.


def full_title(name, job_title="Engineer"):
    """ Addresses your person with their job title.

    >>> full_title("Balloonicorn")
    'Engineer Balloonicorn'

    >>> full_title("Jane Hacks", "Hacker")
    'Hacker Jane Hacks'
    """
    return (job_title + " " + name).title()


# 2. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #1 to construct the full title for the letter's
#    greeting.


def write_letter(recipient, job_title, sender):
    """ Writes fanmail to the person whose job you admire.

    >>> write_letter("Jane Hacks", "Hacker", "Balloonicorn")
    Dear Hacker Jane Hacks, I think you are amazing! Sincerely, Balloonicorn
    """
    print "Dear %s %s, I think you are amazing! Sincerely, %s" % (job_title.title(), recipient.title(), sender.title())


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
