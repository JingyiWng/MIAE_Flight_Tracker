def solid_example_1(*, example_param_1: str, example_param_2: int):
# * means keyword argument. This means, you have to specify the keyword when you are using this function
# E.g. you have to type out example_param_1
    """

    :param example_param_1:
    :param example_param_2:
    :return:
    """

    # TODO: This is a TODO

def solid_example_2(example_param_1: float) -> int:
    #this tells us what the function expects to return.
    # In this case, -> wants us to return an integer
    return 2

def solid_example_3(*, example_param_1: float =4.0):
    pass

