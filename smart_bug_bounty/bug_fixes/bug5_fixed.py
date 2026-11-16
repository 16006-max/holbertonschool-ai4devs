def calculate_pass_rate(scores, passing_threshold=60):
    """
    Calculates the percentage (0-100) of students who passed.
    """
    # Fixed: Guard against empty list to avoid ZeroDivisionError
    if not scores:
        return 0.0

    passed = 0
    for score in scores:
        # Fixed: Use `>=` so scores equal to passing_threshold count as passed
        if score >= passing_threshold:
            passed += 1

    percentage = (passed / len(scores)) * 100
    return round(percentage, 2)


if __name__ == "__main__":
    assert calculate_pass_rate([60, 75, 90]) == 100.0
    assert calculate_pass_rate([40, 59, 60, 80]) == 50.0
    assert calculate_pass_rate([]) == 0.0
    assert calculate_pass_rate([30, 45]) == 0.0
    print("All bug5_fixed.py test cases passed!")
