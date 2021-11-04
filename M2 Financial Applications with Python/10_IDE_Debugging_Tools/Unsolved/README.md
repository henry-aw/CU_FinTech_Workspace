# Activity: IDE Debugging Tools

In this activity, you'll run tests and debug code for your loan qualifier application.

## Instructions

Use the files in the Unsolved folder to complete the following steps.

1. In VS Code, right-click on `test_qualifier.py` in the file tree and select "Run All Tests." Configure VS Code to use PyTest.

2. Open `test_qualifier.py` in VS Code and activate a breakpoint in line 11, inside `test_calculate_monthly_debt_ratio`.

3. Change the value of the `assert` statement inside `test_calculate_monthly_debt_ratio` from `== 0.375` to `== 0.378`.

4. Click the debug button. When the code execution pauses, click the "Step Into" button to see the variables in memory.
