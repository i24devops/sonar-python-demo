from app.calculator import add, divide, is_even
from app.db import find_user_by_name

if __name__ == "__main__":
    print("Sum:", add(1, 2))
    print("Divide:", divide(10, 0))
    print("Is 3 even?", is_even(3))
    # Demo only; assumes a local sqlite db path
    # print(find_user_by_name("/tmp/demo.db", "admin"))
