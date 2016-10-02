# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%


def calculate_item_cost(item, state, tax=.05):
    """ Calculate total cost of an item including tax given a state abbreviation.

    >>> calculate_item_cost(3, 'CA')
    3.21

    >>> calculate_item_cost(3, 'OR')
    3.15
    """
    if state == 'CA':
        tax = .07
    print item * (1 + tax)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".


def is_berry(fruit_name):
    """ Tells you whether your word is a type of a berry, excluding blueberries.

    >>> is_berry('banana')
    False

    >>> is_berry('strawberry')
    True
    """
    berry_list = ['strawberry', 'cherry', 'blackberry']
    return fruit_name in berry_list


#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def shipping_cost(fruit_name):
    """ Tells you the cost of shipping for your fruit. Berry friendly service.

    >>> shipping_cost('apple')
    5

    >>> shipping_cost('cherry')
    0
    """
    if is_berry(fruit_name):
        return 0
    return 5

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def is_hometown(town_name):
    """ Checks to see if your hometown is the same as Michelle's.

    >>> is_hometown('Valencia')
    False

    >>> is_hometown('Seoul')
    True
    """
    return town_name == 'Seoul'


def full_name(first_name, last_name):
    """ Combines your first and last names into one string.

    >>> full_name('Michelle', 'Kim')
    'Michelle Kim'
    """
    return (first_name + ' ' + last_name).title()


def hometown_greeting(your_hometown, first_name, last_name):
    """ Someone who cares about where you're from greets you.

    >>> hometown_greeting('Valencia', 'Michelle', 'Kim')
    Hi, Michelle Kim, where are you from?

    >>> hometown_greeting('Seoul', 'Michelle', 'Kim')
    Hi, Michelle Kim, we're from the same place!
    """
    if is_hometown(your_hometown):
        print "Hi, %s, we're from the same place!" % full_name(first_name, last_name)
    else:
        print "Hi, %s, where are you from?" % full_name(first_name, last_name)

#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def increment(x=1):
    """ Creates a function inception: increment calls add, adding 1 to your
    number unless you specify another number by which you want to increment.

    >>> increment()(2)
    3

    >>> increment(2)(5)
    7
    """

    def add(y):
        return x + y
    return add

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.

addfive = increment(5)
addfive(5)
addfive(20)

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def list_of_nums(number, list_of_nums):
    """ Appends a given number to a given list of numbers.

    >>> list_of_nums(1, [4, 3, 2])
    [4, 3, 2, 1]

    >>> list_of_nums('cheese', [4, 3, 2])
    'Please specify an integer to append to your list.'
    """
    if type(number) is not int:
        return 'Please specify an integer to append to your list.'
    return list_of_nums + [number]


#####################################################################

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "All student-generated tests passed!"
    print
