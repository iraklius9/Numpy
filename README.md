# Student Table Generator

The Student Table Generator is a Python program that generates a table of student scores for various subjects. It allows users to calculate statistics such as the highest average score, best and worst scores in specific subjects, and students with scores higher than the average in a particular subject.


## Usage

1. Open the `main.py` file.

2. Customize the input data:
   - Modify the `first_names`, `last_names`, and `subjects` lists to include the names of your students and subjects.
   
3. Run the `main.py` file:

    ```bash
    python main.py
    ```

4. View the generated student table with scores and statistics printed to the console.

## Example

```python
from student_table import StudentTable

# Georgian first names and last names of students
first_names = ['ვენერა', 'თინა', 'თეა']
last_names = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე']
# Subjects
subjects = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ისტორია', 'კომპიუტერული მეცნიერება']

# Creating instance of StudentTable
student_table = StudentTable(first_names, last_names, subjects)

# Printing table
student_table.print_table()

# Finding student with highest average score
student_table.find_student_with_highest_average_score()

# Finding best and worst in Mathematics
student_table.find_best_and_worst_in_mathematics()

# Finding students with higher English scores
student_table.find_students_with_higher_english_scores()
