# Repository Testing

## What runs automatically

GitHub Actions uses Python 3.12 and performs three checks:

1. Compiles every Python source file in the six numbered practice folders and `07_Beginner_Projects`, plus the test scripts.
2. Runs all 110 numbered practice programs with a representative input (where needed) and checks for an expected output fragment.
3. Runs one sample-input smoke test for each of the 15 beginner projects.

The workflow runs on relevant pushes and pull requests. It can also be started manually from the repository's **Actions** tab using **Python Repository Checks**.

## Run the checks locally

From the repository root:

```bash
python -m compileall -q 01_Basics 02_Control_Flow_and_Loops 03_Data_Structures_and_Problem_Solving 04_Functions_OOP_Files 05_Modules_and_Standard_Library 06_Advanced_Practice 07_Beginner_Projects .github/scripts
python .github/scripts/test_practice_programs.py
python .github/scripts/smoke_test_projects.py
```

Use `python3` instead of `python` if that is how Python is installed on your system.

## Important limitation

These are repeatable smoke tests, not exhaustive proofs that every code path is correct. Each numbered practice program gets at least one representative run and expected-output check; edge cases and alternate paths may need additional tests. The project checks likewise use one scripted user journey per project. A passing workflow means all checks above passed for that commit, not that every possible input has been tested.
