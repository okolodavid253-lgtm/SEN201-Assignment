# Student Result Management System (SRMS)

def add_student():
    name = input("Enter student name: ")
    score1 = int(input("Enter score for Subject 1: "))
    score2 = int(input("Enter score for Subject 2: "))
    score3 = int(input("Enter score for Subject 3: "))
    
    student = {
        "name": name,
        "scores": [score1, score2, score3]
    }
    return student


def calculate_result(student):
    total = sum(student["scores"])
    average = total / len(student["scores"])
    return total, average


def display_result(student, total, average):
    print("\n--- Student Result ---")
    print("Name:", student["name"])
    print("Scores:", student["scores"])
    print("Total Score:", total)
    print("Average Score:", average)


def main():
    student = add_student()
    total, average = calculate_result(student)
    display_result(student, total, average)


main()
