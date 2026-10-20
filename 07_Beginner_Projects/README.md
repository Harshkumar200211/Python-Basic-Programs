# Beginner Python Projects — Console Edition

A hands-on project collection for BCA students, designed to demonstrate how small Python programs grow from simple syntax into useful applications.

**15 projects • Console/terminal only • Standard library only • Beginner-friendly code**

These projects intentionally have **no HTML, CSS, JavaScript frontend, no GUI and no screenshot/output images**. Students interact through text menus in a terminal.

## Getting started

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Download or clone the repository.
3. Open the chosen project folder in a terminal.
4. Run the main file using Python. Example:

```bash
python main.py
```

On some systems, use `python3 main.py`. For multi-file module/package projects, run the command **from that project's folder** so imports work.

## Project index

| No. | Project | What it does | Main concepts | Guide |
|---:|---|---|---|---|
| 01 | [Menu-Driven Calculator](01_Menu_Driven_Calculator/main.py) | Add, subtract, multiply and divide using a repeating menu. | Variables, input, functions, loops, conditions | [Build guide](01_Menu_Driven_Calculator/README.md) |
| 02 | [Student Grade Calculator](02_Student_Grade_Calculator/main.py) | Calculate subject totals, percentage, pass/fail and grade. | Lists, loops, validation, arithmetic, conditions | [Build guide](02_Student_Grade_Calculator/README.md) |
| 03 | [MCQ Quiz App](03_MCQ_Quiz_App/main.py) | Ask MCQs, check answers and calculate score. | Lists, dictionaries, loops, score counter | [Build guide](03_MCQ_Quiz_App/README.md) |
| 04 | [Number Guessing Game](04_Number_Guessing_Game/main.py) | Guess a random number with limited attempts. | random, loops, conditions, try-except | [Build guide](04_Number_Guessing_Game/README.md) |
| 05 | [Unit Converter](05_Unit_Converter/main.py) | Convert distance, temperature and weight units. | Functions, arithmetic, menu loops | [Build guide](05_Unit_Converter/README.md) |
| 06 | [Student Record Manager](06_Student_Record_Manager/main.py) | Add, view, search and delete student records. | Dictionaries, functions, JSON, files | [Build guide](06_Student_Record_Manager/README.md) |
| 07 | [Daily Attendance Manager](07_Attendance_Manager/main.py) | Record daily P/A/L attendance and summarize attendance. | Dates, dictionaries, JSON, percentages | [Build guide](07_Attendance_Manager/README.md) |
| 08 | [Contact Book](08_Contact_Book/main.py) | Add/update, view, search and delete contacts. | Dictionaries, functions, JSON, CRUD | [Build guide](08_Contact_Book/README.md) |
| 09 | [Expense Tracker](09_Expense_Tracker/main.py) | Save expenses and show category totals. | Lists, dictionaries, dates, JSON, aggregation | [Build guide](09_Expense_Tracker/README.md) |
| 10 | [Library Management System](10_Library_Management_System/main.py) | Add books, issue and return books, track availability. | Dictionaries, JSON, loops, conditions | [Build guide](10_Library_Management_System/README.md) |
| 11 | [Inventory and Billing System](11_Inventory_Billing_System/main.py) | Build a cart, calculate bill and tax, update demo stock. | Nested dictionaries, loops, totals, validation | [Build guide](11_Inventory_Billing_System/README.md) |
| 12 | [Calculator Using Custom Modules](12_Custom_Modules_Calculator/main.py) | Split arithmetic and geometry into reusable modules. | import, modules, functions, exceptions | [Build guide](12_Custom_Modules_Calculator/README.md) |
| 13 | [Student Manager Using a Custom Package](13_Custom_Package_Student_Manager/main.py) | Organize student details and marks logic inside a package. | Package structure, `__init__.py`, class, functions | [Build guide](13_Custom_Package_Student_Manager/README.md) |
| 14 | [Calendar and Attendance Planner](14_Calendar_Attendance_Planner/main.py) | Show monthly calendar and store dated notes. | calendar, datetime, JSON, dictionaries | [Build guide](14_Calendar_Attendance_Planner/README.md) |
| 15 | [Text File Analyzer](15_Text_File_Analyzer/main.py) | Count lines, words, characters and frequent words in a file. | File handling, pathlib, re, Counter | [Build guide](15_Text_File_Analyzer/README.md) |

## Suggested learning sequence

### Stage 1 — Learn the basic syntax (Projects 01–05)
Start with input/output, variables, operators, conditions, loops and functions. Change values and test invalid inputs.

### Stage 2 — Store and manage data (Projects 06–10)
Understand dictionaries, lists, dates and JSON. These projects save their records into local JSON files beside `main.py`; students can inspect the generated files after running them.

### Stage 3 — Billing and reusable code (Projects 11–13)
Practise nested data, bills and tax calculations, then split one application into custom modules and a custom package.

### Stage 4 — Standard-library practice (Projects 14–15)
Use calendar/date modules and learn to read and analyze text files with built-in Python tools.

## How the projects are built

Most projects follow the same beginner-friendly design:

1. **Input:** ask the user for values or a menu selection.
2. **Validation:** check missing, non-numeric or out-of-range values.
3. **Logic:** use conditions, loops, functions, lists or dictionaries.
4. **Persistence (where needed):** use JSON files so records survive a restart.
5. **Output:** display a clear text report in the terminal.
6. **Practice:** change one feature, run multiple cases and explain the logic.

Projects 12 and 13 deliberately use more than one source file to demonstrate imports, modules and packages. Each project has its own README with the purpose, concepts, step-by-step logic, file structure and run instructions.

## Important notes

- No third-party package installation is needed.
- Persistent projects create their JSON data file automatically when the first record is saved.
- Inventory in Project 11 is an in-memory demonstration and resets after exit.
- Attendance, contact, student and expense examples are for learning; they are not secure production systems.
- No project has a graphical or web frontend. All interaction is through the terminal.
