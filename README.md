# 2025-ITELEC2-LAB007
Week 02 - Python Variables, Operators and I/O Statements

Laboratory # 07 - Combined Application Exercise in Python

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 07 - Combined Application Exercise in Python**

   **Objective:**
   This exercise combines the concepts of variables, input/output, arithmetic operators, and the math library to create a more comprehensive program.  You will learn to:
   - Get numerical input from the user.
   - Perform arithmetic operations on the input.
   - Use the math library for more advanced calculations (square root and sine).
   - Display the results in a clear and formatted way.
   - Handle a potential error (negative input for square root).

   **Desired Output:**
   ```bash
   Enter a number to perform operations on: 
   Arithmetic Operations:
   User number + 10 = 35.00
   User number - 5  = 20.00
   User number * 2  = 50.00
   User number / 3  = 8.33

   Math Library Functions:
   Square root of 25.00 is: 5.0
   Sine of 25.00 degrees is: 0.4226
   ```
      
   **Notable Observations (to be discussed after completing the exercise):**
   - This exercise demonstrates how to combine different programming concepts to build a more functional program.
   - It reinforces the importance of data type conversion (using float() in this case).
   - It shows how to use the math library for more advanced mathematical operations.
   - It introduces basic error handling (checking for negative input before calculating the square root).
   - It emphasizes the importance of clear and formatted output.
   - It uses f-strings for cleaner and more readable formatting.

   **Python Best Practices**
   - Input is String, Convert It: input() gives you text. Use float() (or int()) to make it a number before math.
   - Math Module Still Needed: import math if you're using math functions like sqrt() or sin().
   - Radians for Trig: math.sin(), math.cos(), math.tan() need radians. Convert from degrees with math.radians().
   - Handle Errors: Check for potential problems (like a negative square root) and do something sensible. Don't let your program crash!
   - Format Output: Make your results easy to read. F-strings (e.g., f"{variable:.2f}") are great for this.
   - Combine Skills: This exercise shows how to put everything together: input, math, output, and error handling. That's how you build real programs!

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `exercise_05.py`
      
   2.  Get numerical input:
      - Use the input() function to prompt the user to enter a number. Store the input in a variable named user_number.
      - Crucially, convert the input string to a float using the float() function. This allows you to work with decimal numbers.
```python
user_number = float(input("Enter a number to perform operations on: "))
```
      
   3.  Perform arithmetic operations:
      - Perform addition, subtraction, multiplication, and division operations on user_number. Store the results in appropriately named variables (e.g., addition, subtraction, multiplication, division).
```python
addition = user_number + 10
subtraction = user_number - 5
multiplication = user_number * 2
division = user_number / 3
```

   4. Use math library functions:
      - Import the math module if you haven't already done so at the top of your file.
      - Calculate the square root of user_number. However, check if user_number is negative. The square root of a negative number is undefined in the real number system. If it's negative, store an appropriate message (e.g., "Undefined for negative numbers") in the sqrt_value variable. Otherwise, calculate and store the square root.
      - Calculate the sine of user_number. Assume the user is entering the angle in degrees. Use math.radians() to convert it to radians before using math.sin().
```python
import math # Import math module (only need to do this once at the top in a real script)
sqrt_value = math.sqrt(user_number) if user_number >= 0 else "Undefined for negative numbers"
sine_value = math.sin(math.radians(user_number))  # Assuming user enters an angle in degrees
```

   5. Display the results with formatted output (using f-strings):
      - Use print() and f-strings to display the results of the arithmetic operations and the math functions. Format the output to two decimal places using .2f.
```python
print("\nArithmetic Operations:")
print(f"User number + 10 = {addition:.2f}")
print(f"User number - 5  = {subtraction:.2f}")
print(f"User number * 2  = {multiplication:.2f}")
print(f"User number / 3  = {division:.2f}")

print("\nMath Library Functions:")
print(f"Square root of {user_number:.2f} is: {sqrt_value}")
print(f"Sine of {user_number:.2f} degrees is: {sine_value:.4f}") # Sine formatted to 4 decimal places
```

   6. Run the code: Execute your Python code.
   7. Observe the output: Compare your output with the "Desired Output" shown above.
   8. Discussion (Notable Observations):
      - How does this exercise combine the concepts you've learned in previous exercises?
      - Why is it important to convert the user input to a float?
      - Explain how the conditional expression (if user_number >= 0 else ...) is used to handle the error when calculating the square root of a negative number.
      - Why is it important to format the output? How do f-strings make formatting easier?
      - What other error handling techniques could you use? (Hint: try-except blocks)

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 02 - Session 01 - Exercise 05"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
