from bowling_score import calculate_score

def test_all_open_frames():
    assert calculate_score("9-9-9-9-9-9-9-9-9-9-") == 90

def test_all_strikes():
    assert calculate_score("XXXXXXXXXXXX") == 300

def test_all_spares():
    assert calculate_score("5/5/5/5/5/5/5/5/5/5/5") == 150

def test_mixed_game():
    assert calculate_score("X7/9-X-88/-6XXX81") == 167

def test_zero_score():
    assert calculate_score("--------------------") == 0

if __name__ == "__main__":
    print("Running tests...")
    test_all_open_frames()
    test_all_strikes()
    test_all_spares()
    test_mixed_game()
    test_zero_score()
    print("All tests passed!")
