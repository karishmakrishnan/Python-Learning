# Static type checking in Python involves verifying the types of variables, function parameters,
# and return values without executing the code
from typing import Dict, Tuple, List, Optional

age: int  = 38

def greet(name: str) -> str:
    return f"Hello {name}"

print(greet("karishma"))
num = [1,2,3,4,5,6,7,8,9]
def process_numbers(numbers: List[int]) -> Tuple[int, int]:
    return min(numbers), max(numbers)
def find_person(name: str) -> Optional[Dict[str, str]]:
# Returns a dictionary with person details or None if not found
    return {"name": name, "age": "30"} if name == "Alice" else None
print(process_numbers(num))
print(find_person("Viju"))
print(find_person("Alice"))

# zip is used to combine iterables and return a tuple, the values from the same index position will be the one tiple values

list1 = [11,23,4,5]
lisst2 = [56,77,8,0]

zipped = list(zip(list1, lisst2))
print(zipped)

list3 = [1,3,5]
list4 = [5,2,5,8,9]

zipped = list(zip(list3, list4))
print(zipped)