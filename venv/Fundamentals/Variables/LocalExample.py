'''
Local variables in Python are variables that are defined within a function and are only accessible within the scope of that function.
'''

'''
Example 1: Local Variable Inside a Function
'''
def my_function():
    # Define a local variable
    local_var = 10
    print("Inside the function:", local_var)

# Call the function
my_function()


'''
Example 2: Modifying a Local Variable Inside a Function
'''

def my_function():
    # Define a local variable
    local_var = 10
    print("Inside the function (before modification):", local_var)
    # Modify the local variable
    local_var = 20
    print("Inside the function (after modification):", local_var)

# Call the function
my_function()

'''
Example 3: Local Variables with the Same Name in Different Functions
'''

def function_one():
    # Define a local variable
    local_var = 10
    print("Inside function_one:", local_var)

def function_two():
    # Define another local variable with the same name
    local_var = 20
    print("Inside function_two:", local_var)

# Call both functions
function_one()
function_two()

'''
Example 4: Nested Functions with Local Variables
'''

def outer_function():
    # Define a local variable
    outer_var = 10
    print("Inside outer_function (before inner function):", outer_var)

    def inner_function():
        # Define another local variable
        inner_var = 20
        print("Inside inner_function:", inner_var)
        print("Inside outer_function:", outer_var)

    # Call the inner function
    inner_function()

# Call the outer function
outer_function()
