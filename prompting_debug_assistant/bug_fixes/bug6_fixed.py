def get_grade(score):
    """Return a letter grade: A (90+), B (70-89), C (50-69), F (below 50)."""
    if score >= 90:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "F"


print(get_grade(95))  # expected: A
print(get_grade(75))  # expected: B
print(get_grade(30))  # expected: F
