import logging
from utils.logging_setup import logger  # Assume built progressively

class CustomError(Exception):
    pass

try:
    raise CustomError("Test")
except CustomError as e:
    logger.error(e)
else:
    print("No error")
finally:
    print("Cleanup")

# Robust script
def robust_func():
    try:
        1 / 0
    except ZeroDivisionError:
        logger.warning("Div by zero")

# Debugging: Use pdb.set_trace() in code for practice
if __name__ == "__main__":
    robust_func()