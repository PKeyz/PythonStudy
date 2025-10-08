import random
import constants

def populate_AB():
    """Populates the initial values for A and B at the start of the game from constants.data
    """
    is_finished = False
    a_random_int = random.randint(0, constants.data_length - 1)
    b_random_int = random.randint(0, constants.data_length - 1)
    
    while not is_finished: 
        for key in constants.data[a_random_int]:
            value = constants.data[a_random_int].get(key)
            constants.dict_A.append(value)
            
        for key in constants.data[b_random_int]:
            value = constants.data[b_random_int].get(key)
            constants.dict_B.append(value)
            
        if a_random_int != b_random_int:
            is_finished = True

def repopulate_B():
    """Generates new values for B after the first turn and the old B is now A
    """
    constants.dict_B = []
    b_random_int = random.randint(0, constants.data_length - 1)
    
    for key in constants.data[b_random_int]:
            value = constants.data[b_random_int].get(key)
            constants.dict_B.append(value)
