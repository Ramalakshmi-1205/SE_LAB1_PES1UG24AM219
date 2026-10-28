\# LAB 5: STATIC CODE ANALYSIS



\*\*Subject:\*\* Software Engineering Laboratory  

\*\*Experiment:\*\* Static Code Analysis of a To-Do List and Task Manager



\## 1. Objective



The objective of this experiment was to analyze a Python task management program using Pylint, Bandit, and Flake8, identify code quality, style, and security issues, and improve the code while maintaining its functionality.



\## 2. Tools Used



\- \*\*Pylint:\*\* Used to identify programming errors, code quality issues, and style problems.

\- \*\*Bandit:\*\* Used to identify potential security vulnerabilities in the Python code.

\- \*\*Flake8:\*\* Used to detect style violations and formatting issues.



\## 3. Issues Identified and Fixes Applied



The following issues were identified and addressed during the experiment:



1\. \*\*Unsafe shell command execution:\*\* Removed the unsafe shell-command approach.

2\. \*\*Unsafe deserialization:\*\* Replaced pickle-based storage and loading with JSON.

3\. \*\*Mutable default argument:\*\* Replaced the mutable default list with `None` and initialized a new list inside the function.

4\. \*\*Inconsistent return behavior:\*\* Updated the task search function to return the task ID when found and `None` otherwise.

5\. \*\*Naming convention violations:\*\* Renamed functions, variables, and parameters to follow Python's snake\_case convention.

6\. \*\*Missing documentation:\*\* Added a module docstring and function docstrings.

7\. \*\*File encoding:\*\* Specified UTF-8 encoding when opening files.

8\. \*\*Formatting issues:\*\* Corrected spacing and formatting to follow PEP 8 conventions.



The detailed issue descriptions and corresponding fixes are documented in `issues.md`.



\## 4. Analysis Results



The program was analyzed before and after making the changes. The final results were as follows:



| Tool | Before Fixes | After Fixes |

|---|---|---|

| Pylint | Score: 5.09/10 | Score: 10.00/10 |

| Bandit | Potential issues reported | No issues identified |

| Flake8 | Style violations reported | No violations reported |



The final reports are saved in the `Lab5` folder as separate before-and-after files for each tool.



\## 5. Verification



After applying the fixes, the program was checked to ensure that its task management functionality was maintained. The updated program supports adding tasks, completing tasks, listing pending tasks according to priority, searching by keyword, saving and loading tasks using JSON, and exporting tasks to a JSON file.



The final static analysis results indicate improved code quality, formatting, and security.



\## 6. Conclusion



This experiment demonstrated the importance of static code analysis in improving software quality and identifying potential security risks. Pylint, Bandit, and Flake8 helped identify different categories of problems. After fixing the identified issues, the program achieved a Pylint score of 10.00/10, and the final Bandit and Flake8 reports showed no reported issues or violations.



The experiment highlighted the importance of following coding standards, documenting code, using safe data handling practices, and verifying software after making changes.



