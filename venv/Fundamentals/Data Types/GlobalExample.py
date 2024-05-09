'''
Global variables in Python are those that are declared outside of any function or class and can be accessed from anywhere within the script
'''

'''
Example 1: Using a Global Variable Inside a Function
'''
# Define a global variable
global_var = 10

def my_function():
    # Access the global variable inside the function
    print("Inside the function:", global_var)

# Call the function
my_function()


'''
Example 2: Modifying a Global Variable Inside a Function
'''

# Define a global variable
global_var = 10

def my_function():
    # Modify the global variable inside the function
    global global_var
    global_var = 20

# Call the function
my_function()

# Print the value of the global variable after modification
print("After modification:", global_var)


'''
Example 3: Global Variable Inside Nested Functions
'''
# Define a global variable
global_var = 10

def outer_function():
    # Access the global variable inside the outer function
    print("Inside outer function:", global_var)

    def inner_function():
        # Access the global variable inside the inner function
        print("Inside inner function:", global_var)

    # Call the inner function
    inner_function()

# Call the outer function
outer_function()