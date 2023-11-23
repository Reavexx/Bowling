test_results = {}

# Testfall 1
expected_result = 150
actual_result = calculate_bowling_score([5, 5, 10, 9, 0, 3, 7, 6, 3, 8, 1, 10, 8, 0, 10, 10, 10])
test_results["Testfall 1"] = expected_result == actual_result

for test, result in test_results.items():
    print(f"{test}: {'Erfolgreich' if result else 'Fehlgeschlagen'}")
