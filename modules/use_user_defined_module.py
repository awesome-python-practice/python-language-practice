from modules import factorial_definition
from modules import factorial_definition as fact
import sys

print(factorial_definition.factorial(3))
print(fact.factorial(3))

log = open("test.log", "a")
sys.stdout = log
if __name__ == '__main__':
    print("hello")
