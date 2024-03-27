import numpy as np


class StudentTable:
    def __init__(self, first_names, last_names, subjects):
        self.first_names = first_names
        self.last_names = last_names
        self.subjects = subjects
        self.full_names = self.generate_full_names()
        self.table_data = self.generate_table_data()
        self.table_data_with_names = self.generate_full_table()

    def generate_full_names(self):
        full_names = []
        min_length = min(len(self.first_names), len(self.last_names))
        for i in range(min_length):
            full_name = self.first_names[i] + ' ' + self.last_names[i]
            full_names.append(full_name)
        return full_names

    def generate_table_data(self):
        return np.random.randint(1, 101, size=(len(self.full_names), len(self.subjects)))

    def generate_full_table(self):
        subjects_table = np.array(self.subjects).reshape(1, len(self.subjects))
        full_names_table = np.array(self.full_names).reshape(len(self.full_names), 1)
        table_header = np.hstack(([['']], subjects_table))
        return np.vstack((table_header, np.hstack((full_names_table, self.table_data))))

    def print_table(self):
        for row in self.table_data_with_names:
            first_col = f'{row[0]:25}'
            other_cols = '  '.join(f'{cell:15}' for cell in row[1:])
            print(first_col + other_cols)

    def find_student_with_highest_average_score(self):
        average_scores = np.mean(self.table_data, axis=1)
        max_average_score = np.max(average_scores)
        print(f"\nStudent with the highest average score: "
              f"{self.full_names[np.argmax(average_scores)]} with an average score of"
              f" {max_average_score}")

    def find_best_and_worst_in_mathematics(self):
        max_score = np.max(self.table_data[:, 1])
        min_score = np.min(self.table_data[:, 1])
        print(f"\nStudent with the highest score in Mathematics: "
              f"{self.full_names[np.argmax(self.table_data[:, 1])]} with a score of {max_score}")
        print(f"Student with the lowest score in Mathematics: "
              f"{self.full_names[np.argmin(self.table_data[:, 1])]} with a score of {min_score}")

    def find_students_with_higher_english_scores(self):
        english_average_score = np.mean(self.table_data[:, 2])
        good_student_indices = np.where(self.table_data[:, 2] > english_average_score)
        good_students = [self.full_names[i] for i in good_student_indices[0]]
        print("\nStudents with a higher score in English than the average English score:")
        print(", ".join(good_students))
