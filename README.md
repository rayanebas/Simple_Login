# Secure Authentication System in Python

This Python script implements a simple yet secure login system that validates a user's credentials and limits the number of login attempts to prevent brute-force attacks.

## 🚀 Features

* **Credential Validation**: Verifies if the username and password match the required values.
* **Attempt Limit**: The user has a maximum of **3 attempts**.
* **Dynamic Counter**: Displays the remaining number of attempts after each failure.
* **Security Lock**: Shuts down access after 3 consecutive failed attempts.

## 🛠️ How It Works (Code Logic)

The script relies on a `while` loop combined with conditional statements (`if/else`):

1. **Initialization**: The attempt counter is set to 3.
2. **User Input**: Inside the loop, the program prompts the user for a *username* and a *password* on every turn.
3. **Verification**:
    * If the credentials are correct, a success message is displayed, and the loop stops instantly using a `break` statement.
    * If the credentials are incorrect, the counter decreases by 1, and an error message is shown.
4. **Game Over**: If the counter hits 0, the program prints a final lockout message and terminates.

## 📋 Prerequisites & Installation

To run this script, you need to have **Python 3** installed on your computer.

1. Save the Python script file (e.g., `script.py`) in your project folder.
2. Open your terminal or command prompt.
3. Run the script using the following command:
   ```bash
   python script.py
