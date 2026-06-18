# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guess 10| Too high        |Too low           |       None |
| New game| Clear and restart| No allowed input/clear |      none |
| | | | |
Alleged number was 12, inputs of 10 and 9 were made and each time although the number was higher the hint was to go lower, and then after the input 8 was made hint was to go higher

New game button also does not work and leaves all previous inputs aswell as not allowing any new ones

Also the go lower/higher feature seems to be completly random because it can even say go lower on negative inputs;

The point system seems to be incorrect aswell and the game history displays your prior guess after you make your next one not after the prior one

Switching difficulty mid game does not reset the secret number, so the hidden number can be outside the new difficultys range and the difficulty ranges are incorrect hard is 1-50 which would be easier than normal

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude as my main AI teammate. One correct suggestion was its diagnosis of the high/low bug. It found that the messages in check_guess were flipped and that the secret was turned into text on even turns. I verified this by reading the code and playing the game, where the hints lined up after the fix. One misleading suggestion was that its first tests assumed check_guess returned just a string when it returns two values. I caught this and it fixed the tests. Another incorrect part was during the game score history fix the AI just removed a ton of code which confused me and after I told it about the code being unnecessary to remove it just told me good catch, after further investigation it actually broke the hint feature while doing this because the rerun didnt allow the hint to happen

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I decided a bug was fixed by checking the code change and then playing the game to watch the behavior. For the high/low bug I guessed above and below the secret and confirmed the hints pointed the right way. I also used pytest on check_guess, with tests that the hint says go lower when too high and go higher when too low, and they passed. AI helped by writing the tests to target the exact bug and explaining what each one checked. One of the bugs with the new game when the AI fixed it and I asked it to make a test it was doing a lot of extra code to create the test so I decided against it and just did a mmanual test.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I still have little experience with it so im not sure I could explain it well to someone whos never used it but from what im seeing its like react in a way but for python you have to add rerun after certain areas in order to make sure the page has proper information after you make a change
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Using AI for test, testing is one of those things I dont really find myself doing so thats probably something im going to do a ton now
