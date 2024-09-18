# app.py
import numpy as np
def square(num):
    return np.square(num)

if __name__ == "__main__":
    number = 6
    result = square(number)
    print(f"The square of {number} is {result}")
