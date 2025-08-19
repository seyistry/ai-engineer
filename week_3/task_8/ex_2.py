"""Task2
- Comment the code below appropriately, and using doctring, explain what the code is doing.
-  Adapt the code to the case below.

- Federal Government Scholarship Key Eligibility Requirements:
- Citizenship:
- Applicant must be a citizen of Nigeria. 
- Enrollment:
- Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
- Other Scholarships:
- Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
- Academic Qualification:
- For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.
"""

name = input("Enter your name: ")

# Check citizenship
citizen = input("Are you a Nigerian citizen? (yes/no): ").strip().lower() == "yes"
# Check enrollment status
enrolled = input("Are you a registered, full-time undergraduate in a recognized Nigerian university? (yes/no): ").strip().lower() == "yes"
# Check for other scholarships
other_scholarship = input("Are you currently receiving any Oil & Gas industry scholarship? (yes/no): ").strip().lower() == "no"
# Academic qualification: number of distinctions
distinctions = int(input("How many distinctions (A/B grades) do you have in WAEC/WASSCE (including English and Mathematics)?: "))

# Eligibility check based on all requirements
eligible = all([
	citizen,                # Must be Nigerian
	enrolled,               # Must be full-time undergraduate
	other_scholarship,      # Must not be receiving other Oil & Gas scholarship
	distinctions >= 5       # Must have at least 5 distinctions
])

# Print candidate details and eligibility result
print(f"\nCandidate: {name}")
print(f"Nigerian Citizen: {'Yes' if citizen else 'No'}")
print(f"Full-time Undergraduate: {'Yes' if enrolled else 'No'}")
print(f"No Other Oil & Gas Scholarship: {'Yes' if other_scholarship else 'No'}")
print(f"Distinctions in WAEC/WASSCE: {distinctions}")
print(f"Eligible for Scholarship: {'Yes' if eligible else 'No'}")
