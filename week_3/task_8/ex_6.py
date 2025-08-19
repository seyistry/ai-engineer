"""**Task6**

- The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement. 

- For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 

Breakdown of the Admission Process:
1. UTME:
Candidates must score 200 or above in the UTME and choose UNILAG as their first choice. 
2. O'Level Requirements:
Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
3. Post-UTME:
Eligible candidates participate in the university's online Post-UTME screening. 
4. Departmental Cut-off Marks:
After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
(This can range from 200 to 320). 
5. Final Admission:
Candidates who meet the departmental cut-off marks are offered admission. 

- Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.
"""

# Create an empty dictionary to store candidate information
candidate = {}


# Get candidate details
candidate['name'] = input("Enter your name: ")
candidate['age'] = int(input("Enter your age: "))
candidate['utme_score'] = int(input("Enter your UTME score: "))
candidate['first_choice'] = input(
    "Is UNILAG your first choice institution? (yes/no): ").strip().lower() == "yes"


# Define valid credit pass grades
passed_grades = ("A1", "B2", "B3", "C4", "C5", "C6")
# Define fail grades (less than 50)
fail_grades = ("E8", "F9")

#Grades
grade_list = "e.g., A1, B2, B3, C4, C5, C6, E8, F9"

# Get O'Level results for English and Mathematics explicitly
candidate['english'] = input(
    f"Enter your English grade ({grade_list}): ").strip().upper()
candidate['math'] = input(
    f"Enter your Mathematics grade ({grade_list}): ").strip().upper()

# Get grades for other subjects (any number)
other_subjects = [x.strip().upper() for x in input(
    "Enter your other O'Level subject grades (comma-separated, e.g., B3, C5, A1, E8, F9): ").split(",")]
candidate['other_subjects'] = other_subjects

# Combine all O'Level grades
all_grades = [candidate['english'], candidate['math']] + \
    candidate['other_subjects']

# Check admission eligibility
eligible = True
if candidate['age'] < 16:
    eligible = False
elif candidate['utme_score'] < 200:
    eligible = False
elif not candidate['first_choice']:
    eligible = False
elif candidate['english'] not in passed_grades or candidate['math'] not in passed_grades:
    eligible = False
elif len(all_grades) < 5 or sum(1 for x in all_grades if x in passed_grades) < 5:
    eligible = False
elif any(x in fail_grades for x in all_grades):
    eligible = False

if eligible:
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")
