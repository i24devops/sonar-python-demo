def classify(x):
    # Intentionally similar to calculator.duplicate_logic to trigger "duplicated code"
    if x > 10:
        return "BIG"
    elif x > 5:
        return "MID"
    else:
        return "SMALL"
