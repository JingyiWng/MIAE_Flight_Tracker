from api import utils
from api import fetch

def main_wrapper():
    print(f"This is the start of the the Python project. The name of this function is {main_wrapper.__name__}") #Even the function we defined has an attribute

    # utils.solid_example_1(example_param_1="a", example_param_2=1)
    # utils.solid_example_2(2.90)

    # Code here
    fetch.states_accessor()


    print("This is the end of the the Python project")
    pass

if __name__ == "__main__":
    main_wrapper()