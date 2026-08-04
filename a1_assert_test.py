
"""
====================================================
A1 TEST FILE (STUDENT VERSION)
====================================================

INSTRUCTIONS:

1. Instantiate objects using the test data below
2. Call the appropriate methods
3. Print the results in the format shown

DO NOT change the expected values.
Your output should match (or be very close after rounding to two decimal places).

----------------------------------------------------
HINTS:
- Use f-strings when rounding decimals
- Follow the order exactly
- Read each section carefully
====================================================
"""
'''Window Powershell:pip install pytest coverage
coverage run -m pytest a1_assert_test.py
coverage html'''
# TODO: import date class from datetime module
# write the line of code here
from datetime import date

# TODO: import everything from your implementation file
from a1 import *
import pytest

#HW 03/31/26
#Keep making the assert cases for all the other classes and change the contact into contactinfo.
#Put in the approx for the other classes. Also review 2 links for AI.
#Find any articles or videos relating to AI that you find interesting. Just 1 topic is fine. 


# ------------------------
# 1. Create Shared Contact Info
# ------------------------
'''
Create the following objects:

Name:
- First name: "John"
- Last name: "Doe"

Emergency Contact:
- First name: "Jane"
- Last name: "Doe"

ContactInfo:
- name: John Doe
- address: "123 Main St"
- phone: "555-5555"
- email: "john@example.com"
- emergency_contact: Jane Doe

Expected:
- No output yet, just object creation
'''

@pytest.fixture
def contact_info():
    
    n = Name("John", "Doe")

    ec = Name("Jane", "Doe")

    contact = ContactInfo(n, "123 Main Street", "555-5555", "john@example.com", ec)

    return contact

# ------------------------
# 2. Test Name Class
# ------------------------
'''
Call the __str__ method using print()

Expected Output:
John Doe'''

def test_name_class():
    n = Name("John", "Doe")
    assert str(n) == "John Doe", "Name Class __str__ fail"

# ------------------------
# 3. Test Employee (Base Class)
# ------------------------
'''Employee Case 1: INTERMEDIATE level (boost applies)
- employee_id = "E001"
- employment_date = date(2020, 1, 1)
- education = BACHELOR
- level = INTERMEDIATE
- last_year_earnings = 50000

Call estimateProductivity()

Expected Output:
1.40'''

"""
Employee Case 2: ENTRY level (no boost)
- employee_id = "E002"
- employment_date = date(2020, 1, 1)
- education = BACHELOR
- level = ENTRY
- last_year_earnings = 50000

Call estimateProductivity()

Expected Output:
0.00
"""

def test_employee_intermediate(contact_info):

    employee_intermediate = Employee("E001",
                        contact_info,
                        date(2020, 1, 1),
                        EducationLevel.BACHELOR,
                        EmploymentLevel.INTERMEDIATE,
                        50000)
    assert employee_intermediate.estimateProductivity() == pytest.approx(1.4), "employee_intermediate fail"

    employee_entry = Employee("E002",
                contact_info,
                date(2020, 1, 1),
                EducationLevel.BACHELOR,
                EmploymentLevel.ENTRY,
                50000)
    assert employee_entry.estimateProductivity() == pytest.approx(0.0), "employee_entry fail"

# ------------------------
# 4. Test FullTimeEmployee
# ------------------------
"""
FullTimeEmployee Case 1: project bonus + promotion penalty
- employee_id = "FT001"
- employment_date = date(2018, 1, 1)
- education = BACHELOR
- level = SENIOR
- last_year_earnings = 80000
- base_pay = 70000
- bonuses = 5000
- overtime = 2000
- last_promotion_date = date(2019, 1, 1)
- num_projects = 3

Steps:
1. base productivity: 80000 / 70000 ≈ 1.14
2. num_projects > 2 → add bonus 1.5 → ≈ 2.64
3. years since promotion > 3 → subtract 0.8 → ≈ 1.84

Expected Output:
1.84
"""

"""
FullTimeEmployee Case 2: project bonus, no penalty
- employee_id = "FT003"
- employment_date = date(2021, 1, 1)
- education = BACHELOR
- level = SENIOR
- last_year_earnings = 80000
- base_pay = 70000
- bonuses = 5000
- overtime = 2000
- last_promotion_date = date.today()  # recent promotion, no penalty
- num_projects = 3  # >2 → bonus applies

Steps:
1. base productivity: 80000 / 70000 ≈ 1.14
2. project bonus: +1.5 → ≈ 2.64
3. promotion penalty does NOT apply

Expected Output:
2.64
"""

"""
FullTimeEmployee Case 3: no project bonus, promotion penalty
- employee_id = "FT004"
- employment_date = date(2018, 1, 1)
- education = BACHELOR
- level = SENIOR
- last_year_earnings = 70000
- base_pay = 70000
- bonuses = 5000
- overtime = 2000
- last_promotion_date = date(2019, 1, 1)
- num_projects = 2  # ≤2 → no bonus

Steps:
1. base productivity: 70000 / 70000 = 1.0
2. project bonus: none
3. years since promotion > 3 → apply penalty -0.8 → 0.2

Expected Output:
0.20
"""

"""
FullTimeEmployee Case 3: no project bonus, promotion penalty
- employee_id = "FT004"
- employment_date = date(2018, 1, 1)
- education = BACHELOR
- level = SENIOR
- last_year_earnings = 70000
- base_pay = 70000
- bonuses = 5000
- overtime = 2000
- last_promotion_date = date(2019, 1, 1)
- num_projects = 2  # ≤2 → no bonus

Steps:
1. base productivity: 70000 / 70000 = 1.0
2. project bonus: none
3. years since promotion > 3 → apply penalty -0.8 → 0.2

Expected Output:
0.20
"""

"""
FullTimeEmployee Case 4: no project bonus, no penalty
- employee_id = "FT002"
- employment_date = date(2021, 1, 1)
- education = BACHELOR
- level = SENIOR
- last_year_earnings = 70000
- base_pay = 70000
- bonuses = 5000
- overtime = 2000
- last_promotion_date = date.today()
- num_projects = 2  # ≤2 → no bonus

Steps:
1. base productivity: 70000 / 70000 = 1.0
2. project bonus: none
3. promotion penalty: none

Expected Output:
1.00
"""

def test_fte(contact_info):

    fte_case1 = FullTimeEmployee("FT001",
                contact_info,
                date(2018, 1, 1),
                EducationLevel.BACHELOR,
                EmploymentLevel.SENIOR,
                80000,
                70000,
                5000,
                2000,
                date(2019, 1, 1),
                num_projects=3)
    assert fte_case1.estimateProductivity() == 1.84, "fte case 1 fail"

    fte_case2 = FullTimeEmployee("FT003",
                contact_info,
                date(2021, 1, 1),
                EducationLevel.BACHELOR,
                EmploymentLevel.SENIOR,
                80000,
                70000,
                5000,
                2000,
                date.today(),
                num_projects=3
                )
    assert fte_case2.estimateProductivity() == 2.64, "fte case 2 fail"

    fte_case3 = FullTimeEmployee("FT004",
                contact_info,
                date(2018, 1, 1),
                EducationLevel.BACHELOR,
                EmploymentLevel.SENIOR,
                70000,
                70000,
                5000,
                2000,
                date(2019, 1, 1),
                num_projects=2)
    assert fte_case3.estimateProductivity() == 0.2, "fte case 3 fail"

    fte_case4 = FullTimeEmployee("FT002",
                contact_info,
                date(2021, 1, 1),
                EducationLevel.BACHELOR,
                EmploymentLevel.SENIOR,
                70000,
                70000,
                5000,
                2000,
                date.today(),
                num_projects=2)
    assert fte_case4.estimateProductivity() == 1.00, "fte case 4 fail"

# ------------------------
# 5. Test Manager
# ------------------------
"""
Manager Case 1: management bonus applies
- employee_id = "M001"
- employment_date = date(2017, 1, 1)
- education = MASTER
- level = INTERMEDIATE
- last_year_earnings = 90000
- base_pay = 80000
- bonuses = 6000
- overtime = 3000
- last_promotion_date = date(2018, 1, 1)
- num_projects = 4
- num_employees_managed = 10

Expected Output:
≈ 3.62
"""

"""
Manager Case 2: management bonus does not apply
- num_employees_managed = 7
- other data same as Case 1

Expected Output:
≈ 1.82
"""

def test_manager(contact_info):

    manager_case1 = Manager("M001",
                contact_info,
                date(2017, 1, 1),
                EducationLevel.MASTER,
                EmploymentLevel.INTERMEDIATE,
                90000,
                80000,
                6000,
                3000,
                date(2018, 1, 1),
                num_projects=4,
                num_employees_managed=10)
    assert manager_case1.estimateProductivity() == pytest.approx(3.62), "manager_case 1 fail"

    manager_case2 = Manager("M001",
                contact_info,
                date(2017, 1, 1),
                EducationLevel.MASTER,
                EmploymentLevel.INTERMEDIATE,
                90000,
                80000,
                6000,
                3000,
                date(2018, 1, 1),
                num_projects=4,
                num_employees_managed=7)
    assert manager_case2.estimateProductivity() == pytest.approx(1.82), "manager_case2 fail"

# ------------------------
# 6. Test IndividualContributor
# ------------------------
"""
IndividualContributor Case 1: publication bonus
- employee_id = "IC001"
- employment_date = date(2019, 1, 1)
- education = DOCTORAL
- level = SENIOR
- last_year_earnings = 85000
- base_pay = 75000
- bonuses = 4000
- overtime = 1000
- last_promotion_date = date(2020, 1, 1)
- num_projects = 2
- num_patents = 2
- num_publications = 5
- num_external_collab = 1

Expected Output:
≈ 1.63
"""

"""
IndividualContributor Case 2: no publication bonus
- num_publications = 4
- other data same as Case 1

Expected Output:
≈ 1.13 + promotion penalty
== 1.13 - 0.8 == 0.33
"""

def test_ic(contact_info):

    ic_case1 = IndividualContributor("IC001",
            contact_info,
            date(2019, 1, 1),
            EducationLevel.DOCTORAL,
            EmploymentLevel.SENIOR,
            85000,
            75000,
            4000,
            1000,
            date(2020, 1, 1),
            num_projects=2,
            num_patents=2,
            num_publications= 5,
            num_external_collab=1)
    assert ic_case1.estimateProductivity() == pytest.approx(1.63), "ic_case 1 fail"

    ic_case2 = IndividualContributor("IC001",
            contact_info,
            date(2019, 1, 1),
            EducationLevel.DOCTORAL,
            EmploymentLevel.SENIOR,
            85000,
            75000,
            4000,
            1000,
            date(2020, 1, 1),
            num_projects=2,
            num_patents=2,
            num_publications= 4,
            num_external_collab=1)
    assert ic_case2.estimateProductivity() == pytest.approx(0.33), "ic_case 2 fail"

# ------------------------
# 7. Test PartTimeEmployee
# ------------------------
"""
PartTimeEmployee Case 1: actual < contractual
- employee_id = "PT001"
- contractual_hours = 40
- actual_hours = 35
- multiplier = 3.7

Expected Output:
3.24
"""

"""
PartTimeEmployee Case 2: actual = contractual
- actual_hours = 40
- other data same as Case 1

Expected Output:
3.70
"""

"""
PartTimeEmployee Case 3: actual = 0
- actual_hours = 0

Expected Output:
0.00
"""

"""
PartTimeEmployee Case 4: actual > contractual
- actual_hours = 45

Expected Output:
≈ 4.16
"""

def test_pte(contact_info):

    pte_case1 = PartTimeEmployee("PT001",
            contact_info,
            date(2022, 1, 1),
            EducationLevel.SOME_COLLEGE,
            EmploymentLevel.ENTRY,
            10000,
            40,
            35,
            200)
    assert pte_case1.estimateProductivity() == pytest.approx(3.24), "pte_case1 fail"

    pte_case2 = PartTimeEmployee("PT001",
            contact_info,
            date(2022, 1, 1),
            EducationLevel.SOME_COLLEGE,
            EmploymentLevel.ENTRY,
            10000,
            40,
            40,
            200)
    assert pte_case2.estimateProductivity() == pytest.approx(3.70), "pte_case2 fail"

    pte_case3 = PartTimeEmployee("PT001",
            contact_info,
            date(2022, 1, 1),
            EducationLevel.SOME_COLLEGE,
            EmploymentLevel.ENTRY,
            10000,
            40,
            0,
            200)
    assert pte_case3.estimateProductivity() == pytest.approx(0.0), "pte_case3 fail"

    pte_case4 = PartTimeEmployee("PT001",
            contact_info,
            date(2022, 1, 1),
            EducationLevel.SOME_COLLEGE,
            EmploymentLevel.ENTRY,
            10000,
            40,
            45,
            200)
    assert pte_case4.estimateProductivity() == pytest.approx(4.16), "pte_case4 fail"

# ------------------------
# 8. Test HourlyEmployee
# ------------------------
"""
HourlyEmployee Case 1: low wage bonus
- hourly_earnings = 10 (<14)
- base productivity: (40/40)*3.7 = 3.7
- bonus: +3

Expected Output:
6.70
"""

"""
HourlyEmployee Case 2: no bonus
- hourly_earnings = 20 (>=14)
- base productivity: 3.7
- bonus: none

Expected Output:
3.70
"""

def test_he(contact_info):

    he_case1 = HourlyEmployee("H001",
                        contact_info,
                        date(2022, 1, 1),
                        EducationLevel.HIGH_SCHOOL,
                        EmploymentLevel.ENTRY,
                        8000,
                        40,
                        40,
                        0,
                        10)
    assert he_case1.estimateProductivity() == pytest.approx(6.70), "he_case1 fail"

    he_case2 = HourlyEmployee("H001",
                        contact_info,
                        date(2022, 1, 1),
                        EducationLevel.HIGH_SCHOOL,
                        EmploymentLevel.ENTRY,
                        8000,
                        40,
                        40,
                        0,
                        20)
    assert he_case2.estimateProductivity() == pytest.approx(3.70), "he_case2 fail"

#Assert

# ------------------------
# FINAL INSTRUCTION
# ------------------------

print("all tests passed")
"""
====================================================
GOAL:
Your output should match all expected values above.
====================================================
"""