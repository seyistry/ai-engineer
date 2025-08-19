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

# Get O'Level results for English and Mathematics explicitly
candidate['english'] = int(input("Enter your English score: "))
candidate['math'] = int(input("Enter your Mathematics score: "))

# Get scores for three other subjects
other_subjects = [int(x) for x in input(
    "Enter your other three O'Level subject scores (comma-separated): ").split(",")]
candidate['other_subjects'] = other_subjects

# Check admission eligibility
eligible = True
if candidate['age'] < 16:
    eligible = False
elif candidate['utme_score'] < 200:
    eligible = False
elif candidate['english'] < 50 or candidate['math'] < 50:
    eligible = False
elif len(candidate['other_subjects']) < 3 or any(x < 50 for x in candidate['other_subjects']):
    eligible = False

if eligible:
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")
