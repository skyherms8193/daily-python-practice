"""
Kata: Get the Grade

Description:
Create a function that calculates the average of three scores
and returns the corresponding letter grade.

Grading scale:
90–100 -> A
80–89  -> B
70–79  -> C
60–69  -> D
0–59   -> F

Concepts practiced:
- Arithmetic operations (averages)
- Conditional logic (if/elif/else)
- Function structure
- Return values

Notes:
Practicing how to map numerical ranges to categorical outputs.
Reinforces clean conditional branching and readable logic.

"""

def get_grade(s1, s2, s3):
    grade = ""
    
    result = (s1 + s2 + s3)/3
    
    if result <= 100 and result >= 90:
        grade = 'A'
    elif result < 90 and result >= 80:
        grade = 'B'
    elif result < 80 and result >= 70:
        grade = 'C'
    elif result < 70 and result >= 60:
        grade = 'D'
    elif result < 60 and result >= 0:
        grade = 'F'
    else:
        grade = "Error"
    
    return grade

# Example usage
if __name__ == "__main__":
    print(get_grade(95, 90, 93))  # A
