# Intentionally messy code for Sonar demo

HARDCODED_PASSWORD = "P@ssw0rd"  # Noncompliant: hardcoded secret

def add(a, b):
    temp = 0  # Unused variable (code smell)
    return a + b

def divide(a, b):
    try:
        return a / b
    except Exception as e:  # Noncompliant: overly broad exception
        print("Something went wrong:", e)  # Noncompliant: uses print for logging
        return None

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False  # Redundant else (style)

def duplicate_logic(x):
    # Duplicate code; similar block exists in utils.py
    if x > 10:
        return "BIG"
    elif x > 5:
        return "MID"
    else:
        return "SMALL"

def unreachable_example(flag):
    return True
    if flag:  # Unreachable code
        return False  # Noncompliant
