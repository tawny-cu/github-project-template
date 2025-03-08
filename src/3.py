import random

def get_random_code():
    # Generate a random 5-digit code
    return "".join(str(random.randint(0, 9)) for i in range(5))