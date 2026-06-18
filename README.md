# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

Game Purpose:
This is a number guessing game where you pick a difficulty, get a hidden number within a range, and try to guess it in as few attempts as possible. The game gives you higher/lower hints after each guess and scores you based on how quickly you find the number.

Bugs Found:
- The higher/lower hints were completely backwards — guessing too high told you to go higher, and guessing too low told you to go lower, making it impossible to win without luck. It was even saying go lower on inputs that were already negative.
- On every even-numbered attempt, the secret number was secretly converted to a string behind the scenes, which broke all comparisons and made the outcome basically random.
- The attempts counter started at 1 instead of 0, so the first guess was treated as the second attempt, throwing off the score and the attempts-remaining display.
- The new game button didn't actually reset anything — score, history, and status were all left over, and no new inputs were accepted after clicking it.
- Switching difficulty mid-game didn't generate a new secret, so the hidden number could end up completely outside the new difficulty's range.
- Hard mode had a range of 1–50, which was narrower and easier than Normal's 1–100 — the opposite of what hard should be.
- The hint message disappeared immediately after submitting a guess because Streamlit reruns wiped it before it could render on screen.

Fixes Applied:
- Swapped the hint messages so "Too High" says Go LOWER and "Too Low" says Go HIGHER.
- Removed the even/odd turn type conversion so the secret stays an integer the whole game.
- Changed the starting attempts value from 1 to 0.
- Made the new game button fully reset score, history, status, and secret, and had difficulty changes trigger the same full reset automatically.
- Fixed Hard difficulty range to 1–200 and updated the info bar to always show the correct range for whatever difficulty is active.
- Stored the hint in session state so it persists across reruns and shows up reliably above the input field.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters guess of 50
2. Game returns "Go LOWER!"
3. User enters guess of 25
4. Game returns "Go LOWER!"
5. User enters guess of 25
6. Game returns "Go LOWER!"
7. User keeps guessing until they guess correctly
8. The game ends with balloons and the users score

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
=================================================================== test session starts ===================================================================
platform win32 -- Python 3.14.3, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\miken\OneDrive\Desktop\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 5 items                                                                                                                                          

tests\test_game_logic.py .....                                                                                                                       [100%]

==================================================================== 5 passed in 0.03s ====================================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
