# ACME_schedule
## Folder structure
The following programming is composed of 4 files:
- test -> folder that contains all the file for the texts
- constants.py -> contains a class with all the static string
- functions.py -> contains a class with all the logic for get schedule
- main.py -> for manual run, run the following command 
>  python main.py 0


The second parameter show if the program will ignore string with bad format

- test.py -> contains a text for each file in the test folder, to run test.py
> python test.py

## Structures
The full program was constructed using oriented programming objects, furthermore for the analysis of schedule, it used sets and dictionaries. 

#### Considerations: 
The program only match exact schedule for employees, it ignores or raise error if a string do not follow the correct format. It depends of the console parameter in the main.py file. If a employee has the same name that other employee, the first user will be replace for the last one in the file.
We assume that the schedule time per employee in day occurs once.
