\# Lab 5: Static Code Analysis — Issues and Fixes



\## Identified Issues



| Issue | Type | Line(s) Before Fix | Description | Fix Approach |

|---|---|---:|---|---|

| Shell command execution using `os.system()` | Security — High | 57 | Constructing a shell command by concatenating an email address can allow command injection if the input is untrusted. | Removed the unsafe shell-command approach so the program does not execute a command through the shell. |

| Unsafe deserialization using `pickle.load()` | Security — Medium | 47 | Loading an untrusted pickle file can execute malicious code during deserialization. | Replaced unsafe pickle loading with JSON-based data storage and loading. |

| Mutable default argument `labels=\[]` | Code quality / potential bug | 11 | A mutable default list can be shared between function calls, causing unexpected changes to task labels. | Changed the default to `None` and initialized a new list inside the function. |

| Inconsistent return statements in `findTask()` | Code quality | 33–38 | The function did not return an expression consistently when a task was not found. | Made the return behavior consistent by returning the task ID when found and `None` otherwise. |

| Non-compliant function and variable names | Style | Multiple | Names such as `addTask`, `taskId`, and `fileName` did not follow Python's snake\_case naming convention. | Renamed functions, variables, and parameters to use snake\_case consistently. |

| Missing docstrings | Code quality | Multiple | The module and functions lacked documentation explaining their purpose. | Added a module docstring and descriptive function docstrings. |

| Missing explicit file encoding | Code quality | 51 | Opening a text file without specifying its encoding can lead to platform-dependent behavior. | Specified UTF-8 when opening text files. |

| Inconsistent spacing and formatting | Style | Multiple | Flake8 reported whitespace and formatting violations. | Corrected spacing and formatting to follow PEP 8 conventions. |

| Use of `random.choice()` | Security review | 70 | Bandit flagged pseudo-random selection, which is unsuitable when security-sensitive randomness is required. | Replaced random selection with the first pending task; cryptographic randomness is not needed for this feature. | Security review | 70 | Bandit flagged the use of a pseudo-random generator. This is not necessarily a vulnerability for ordinary task suggestions, but it is unsuitable for security-sensitive randomness. | Kept the task suggestion feature for non-security-sensitive use; cryptographic randomness is not required for this feature. |



\## Verification



\- Original Pylint score: 5.09/10.

\- Final Pylint score: 10.00/10.

\- Final Bandit report: no reported issues.

\- Final Flake8 report: no reported violations.



The updated program was checked to ensure that its task-management features continued to work after the changes.



