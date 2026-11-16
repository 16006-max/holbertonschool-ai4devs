def calculate_pass_rate(scores, passing_threshold=60):
    """
    Calculates the percentage (0-100) of students who passed.
    """
    passed = 0
    for score in scores:
        # Bug 1: Strict `>` excludes students who scored exactly `passing_threshold`
        if score > passing_threshold:
            passed += 1

    # Bug 2: Raises ZeroDivisionError when `scores` list is empty
    percentage = (passed / len(scores)) * 100
    return round(percentage, 2)


if __name__ == "__main__":
    print(calculate_pass_rate([60, 75, 90]))  # Expected: 100.0
    print(calculate_pass_rate([]))            # Expected: 0.0
