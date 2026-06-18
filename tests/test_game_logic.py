from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Regression tests for the high/low direction bug ---
# The bug: when a guess was too high, the hint said "Go HIGHER!" (and vice
# versa), sending the player the wrong way. The outcome label was correct, but
# the message pointed in the opposite direction. These tests pin the message to
# the correct direction.

def test_too_high_message_says_go_lower():
    # Guess is above the secret -> player must go LOWER.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_message_says_go_higher():
    # Guess is below the secret -> player must go HIGHER.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


# --- Regression tests for the out-of-range input bug ---
# The bug: parse_guess accepted any integer, so guesses like -500 or 99999
# were accepted even though the UI promised a fixed range. These tests pin
# parse_guess to reject values outside the given range.

def test_guess_within_range_is_accepted():
    ok, value, err = parse_guess("50", 1, 100)
    assert ok is True
    assert value == 50
    assert err is None


def test_guess_below_range_is_rejected():
    ok, value, err = parse_guess("-500", 1, 100)
    assert ok is False
    assert value is None
    assert "between 1 and 100" in err


def test_guess_above_range_is_rejected():
    ok, value, err = parse_guess("99999", 1, 100)
    assert ok is False
    assert value is None
    assert "between 1 and 100" in err


def test_range_boundaries_are_inclusive():
    assert parse_guess("1", 1, 100)[0] is True
    assert parse_guess("100", 1, 100)[0] is True


def test_non_number_still_rejected_with_range():
    ok, value, err = parse_guess("abc", 1, 100)
    assert ok is False
    assert err == "That is not a number."
