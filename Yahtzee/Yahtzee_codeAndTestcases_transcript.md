# Yahtzee Code

## I want to write a python code to implement yahtzee game that plays with me
what functions can i use?

Here's a breakdown of functions you can use to write a Python code for a Yahtzee game that plays against you (the computer):

- `roll_dice(num_dice)`: Generates a list of random numbers representing the results of rolling a specified number of dice.
- `reroll_dice(dice, dice_to_reroll)`: Rerolls only the specified dice indices while keeping the rest of the dice values unchanged.
- `print_dice(dice)`: Prints out the current state of the dice.
- `print_scorecard(scorecard)`: Prints out the current scorecard, showing the scores for each category.
- `yahtzee_score(dice, category)`: Calculates the score for a given set of dice and a chosen scoring category according to Yahtzee rules.
- `main()`: Controls the main flow of the game, allowing players to roll dice, select which dice to keep, choose scoring categories, and updates the scorecard accordingly.

## write code for roll_dice(num_dice):

**Arguments:**

- `num_dice` (integer): This optional argument specifies the number of dice to roll. The default value is 5, which simulates rolling five dice. You can call the function with a different number of dice if needed.

**What it does:**

This function simulates rolling the specified number of dice. It uses the `random` module to generate random numbers between 1 and 6 for each die.

**Return type:**

The function returns a list of integers, where each integer represents the value rolled on a single die. For example, if you call `roll_dice(3)`, the function might return a list like `[4, 2, 6]`, indicating that you rolled a 4, a 2, and a 6.

## write code for reroll_dice(dice, dice_to_reroll):

This code defines a function named `reroll_dice` that takes two arguments:

- `dice` (list of integers): This represents the current state of the dice, where each integer in the list is the value of a single die.
- `dice_to_reroll` (list of integers): This represents the indices (1-based indexing) of the dice that you want to reroll. For example, `[2, 4]` would indicate that you want to reroll the second and fourth dice (assuming there are at least four dice).

**What it does:**

The function performs the following actions:

1. It checks if the `dice_to_reroll` list is empty or contains invalid indices. If it's empty, it simply returns the original `dice` list since there's nothing to reroll. If it contains invalid indices (less than 1 or greater than the number of dice), it raises a `ValueError` exception to indicate an error.
2. It creates a copy of the `dice` list using the `.copy()` method. This ensures that the original `dice` list remains unchanged, and the function operates on a separate copy.
3. It iterates through the `dice_to_reroll` list. For each index in the list, it subtracts 1 (because Python indexing starts from 0) to get the actual index in the `new_dice` list. Then, it replaces the corresponding value in the `new_dice` list with a new random integer between 1 and 6, simulating the re-rolling of those specific dice.
4. Finally, the function returns the `new_dice` list, which contains the original dice values with the specified dice replaced by new random values.

## write the code for print_dice(dice):

This code defines a function named `print_dice` that takes one argument:

- `dice` (list of integers): This represents the current state of the dice, where each integer in the list is the value of a single die.

**What it does:**

1. It defines a dictionary named `dice_symbols` that maps die values (1 to 6) to their corresponding Unicode dice symbol representations.
2. It iterates through the `dice` list. For each die value, it uses the `dice_symbols` dictionary to retrieve the corresponding symbol and prints it using `print(dice_symbols[die], end=" ")`. The `end=" "` argument ensures that there's a space between each die symbol for better visual representation.
3. After iterating through all dice, it adds a newline character (`print()`) to move the cursor to the next line, providing a cleaner output format.

This function doesn't return anything (indicated by `None` as the return type) but directly prints the dice symbols to the console in a visually appealing way.

## write code for print_scorecard(scorecard):

**Arguments taken:**

- `scorecard` (dictionary): This represents the current state of the Yahtzee scorecard, where each key is a category name (e.g., "Aces", "Full House") and the corresponding value is the score earned for that category (or `None` if not scored yet).

**What it does:**

This function prints out the current state of the Yahtzee scorecard in a formatted table. It uses Python's `print` function to display the category names, scores, and table borders to the console.

**Return type:**

- None: This function doesn't return any value. It simply prints the formatted scorecard to the console for visualization purposes.

## write code for yahtzee_score(dice, category):

**Arguments taken:**

- `dice` (list of integers): This represents the values rolled on the dice. It's a list where each integer represents the value of a single die.
- `category` (string): This specifies the scoring category for which the score needs to be calculated. It should be a valid Yahtzee category name like "Aces", "Three of a Kind", "Full House", etc.

**What it does:**

1. It uses `Counter(dice)` to create a dictionary that counts the occurrences of each die value (e.g., {1: 2, 2: 1, 3: 0, 4: 1, 5: 1, 6: 0}).
2. It checks the `category` string:
    - For upper section categories ("Aces", "Twos", ..., "Sixes"): It retrieves the count of the corresponding value from the `counts` dictionary (using `counts.get(int(category[0]), 0)`) and multiplies it by the value itself (e.g., for "Fours", it multiplies the count of 4s by 4).
    - For other categories, it applies the specific scoring rules:
        - Three of a Kind: Checks if there are at least three dice with the same value and returns the sum of all dice if true, otherwise 0.
        - Four of a Kind: Similar to Three of a Kind, but checks for four dice with the same value.
        - Full House: Checks if there's a pair (two of a kind) and a three of a kind using the `counts` dictionary and returns 25 points if true, otherwise 0.
        - Small Straight: Sorts the dice and checks if they form a sequence like [1, 2, 3, 4, 5] or

## **write the code for play():**

Controls the main flow of the game, allowing players to roll dice, select which dice to keep, choose scoring categories, and updates the scorecard accordingly.
It coordinates the execution of all other functions to simulate the gameplay of Yahtzee.

## Give test cases for the code of yahtzee

Here are some test cases for your Yahtzee code:

**Test Case 1: Rolling Dice**

- **Description:** This test case verifies that the `roll_dice` function generates a list of 5 random integers between 1 and 6 (inclusive).
- **Input:** `num_dice=5`
- **Expected Output:** A list of 5 integers where each element is between 1 and 6.

**Test Case 2: Rerolling Dice**

- **Description:** This test case checks if the `reroll_dice` function correctly rerolls the specified dice indices.
- **Input:**
    - `dice = [1, 2, 3, 4, 5]`
    - `dice_to_reroll = [1, 3]`
- **Expected Output:** A new list where dice at indices 1 and 3 are rerolled, and other dice remain the same (e.g., possible output: [1, 6, 3, 4, 5]).

**Test Case 3: Printing Dice**

- **Description:** This test case confirms that the `print_dice` function displays the rolled dice in a user-friendly format.
- **Input:** `dice = [2, 5, 1, 4, 3]`
- **Expected Output:** The output should clearly represent the rolled dice values (e.g., "Dice: 2 5 1 4 3").

**Test Case 4: Printing Scorecard**

- **Description:** This test case ensures the `print_scorecard` function presents the scorecard information in a readable table format.
- **Input:** `scorecard = {"Ones": 3, "Twos": None, "Threes": 0}`
- **Expected Output:** A formatted table showing category names and corresponding scores (e.g.,

`Scorecard:
Ones: 3
Twos: None
Threes: 0`

**Test Case 5: Yahtzee Score Calculation (Ones)**

- **Description:** This test case verifies if the `yahtzee_score` function calculates the score for the "Ones" category correctly.
- **Input:**
    - `dice = [1, 2, 3, 4, 5]`
    - `category = "Ones"`
- **Expected Output:** The score should be 1 (since only one die has a value of 1).

**Test Case 6: Yahtzee Score Calculation (Three of a Kind)**

- **Description:** This test case tests if the `yahtzee_score` function accurately calculates the score for the "Three of a Kind" category.
- **Input:**
    - `dice = [3, 3, 3, 4, 6]`
    - `category = "Three of a Kind"`
- **Expected Output:** The score should be 19 (sum of all dice).

**Test Case 7: Yahtzee Score Calculation (Full House)**

- **Description:** This test case checks if the `yahtzee_score` function correctly determines the score for the "Full House" category.
- **Input:**
    - `dice = [2, 2, 2, 5, 5]`
    - `category = "Full House"`
- **Expected Output:** The score should be 25 (as it fulfills the criteria for a Full House).

**Test Case 8: Yahtzee Score Calculation (Yahtzee)**

- **Description:** This test case verifies if the `yahtzee_score` function recognizes and scores a Yahtzee (all dice with the same value).
- **Input:**
    - `dice = [4, 4, 4, 4, 4]`
    - `category = "Yahtzee"`
- **Expected Output:** The score should be 50 (the maximum score for Yahtzee).

**Test Case 9: Gameplay Flow (Basic Round)**

- **Description:** This test case simulates a basic round of Yahtzee where the player rolls, keeps some dice, and scores in an unused category.
- **Input:** (simulated user input)
    - Keep dice with index 0 and 2 (e.g., "0 2")
    - Choose an unused category (e.g., "Fours")
- **Expected Output:** The game should display the rerolled dice, validate the category selection, calculate the score for the chosen category, and update the scorecard.

**Test Case 10: Gameplay Flow (Invalid Input)**

- **Description:** This test case checks how the game handles invalid user input during the "keep dice"