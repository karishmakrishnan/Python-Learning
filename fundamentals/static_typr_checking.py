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