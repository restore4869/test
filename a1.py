#These are modules.
from enum import Enum 
from abc import ABC
from datetime import date


# ------------------------
# Custom Enums
# ------------------------

class EmploymentLevel(Enum):

    ENTRY = 'entry level'
    INTERMEDIATE = 'intermediate level'
    MID = 'mid level'
    SENIOR = 'senior level'
    EXECUTIVE = 'executive level'

class EducationLevel(Enum):

    HIGH_SCHOOL = 'highschool diploma'
    SOME_COLLEGE = 'some college'
    ASSOCIATE = 'associates degree'
    BACHELOR = 'bachelors degree'
    MASTER = 'masters degree'
    DOCTORAL = 'doctoral degree'


# ------------------------
# Helper class
# ------------------------

class Name:
    def __init__(self, first: str, last: str):
# Initialize Name attributes
        self.first = first
        self.last = last

    def __str__(self):
# Return a readable string representation
        return f"{self.first} {self.last}"


#HW 03/01/26: add the __str__ method to both the class Name and class ContactInfo.

#HW 02/24/26: Finish the contactinfo class code just like the Name class.
#Google:

'''class ContactInfo(Name):
    def __init__(self, first: str, last: str, address: str, phone: str, email: str, emergency_contact: Name):
        # Initialize the Name class attributes
        super().__init__(first, last)
        
        self.address = address
        self.phone_number = phone
        self.email_address = email
        self.emergency_contact = emergency_contact'''

class ContactInfo:
    def __init__(self,name: Name, address: str, phone: str, email: str, emergency_contact: Name):
    
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.emergency_contact = emergency_contact
        
    def __str__(self):
        return f"ID:{self.name},zip:{self.address},dial:{self.phone}, mail:{self.email}, alert:{self.emergency_contact}"

# ------------------------
# Base Employee class
# ------------------------

class Employee(ABC):
    INTERMEDIATE_BOOST = 1.4    #This is a class variable.
    def __init__(
        self,
        employee_id: str,
        contact: ContactInfo,
        employment_date: date,
        education: EducationLevel,
        level: EmploymentLevel,
        last_year_earnings: float
        ):
        self.employee_id = employee_id
        self.education = education
        self.contact = contact
        self.employment_date = employment_date
        self.level = level
        self.last_year_earnings = last_year_earnings

    def estimateProductivity(self):
        productivity = 0.0
        
        #HW: 03/03/26
        #Apply the employment level bonus into this method between this line.
        #Find what attributes to use and how to check if is equal to intermediate level in the enum.
        '''If an employee is hired into the intermediate level role, they get a bonus boost,
            where 1.4 is added to their current productivity estimate.'''
        #Google:--- Apply the employment level bonus ---
        #Check if the employee's level is equal to Intermediate
        if self.level == EmploymentLevel.INTERMEDIATE: 

            productivity += self.INTERMEDIATE_BOOST

        return productivity

#03/08/26
#HW: Figure out what rules apply to class FullTimeEmployee.
#HW:Figure out how and where to calculate the productivity method.
#HW: Read the 4. Productivity Estimation Rules.

'''Base productivity estimate for full-time employees: Base productivity of full-
time employees is calculated as a ratio between an employee's last year's earnings, and their base pay.'''

'''Number of projects bonus: Every full-time employee involved in more than 2
projects gets a bonus boost where 1.5 is added to their base productivity estimate.'''

'''Last promotion penalty: For every full-time employee, if more than three years
have passed since their last promotion, they get a penalty, where 0.8 is subtracted
from their current productivity estimate.'''


# ------------------------
# Full-Time Employees
# ------------------------

class FullTimeEmployee(Employee):
    PROJECT_THRESHOLD = 2
    PROJECT_BONUS = 1.5
    PROMOTION_PENALTY = 0.8
    def __init__(
            self,
            employee_id: str,
            contact: ContactInfo,
            employment_date: date,
            education: EducationLevel,
            level: EmploymentLevel,
            last_year_earnings: float,
            base_pay: float,
            bonuses: float,
            overtime: float,
            last_promotion_date: date,
            num_projects: int):
        
        super().__init__(employee_id,
        contact,
        employment_date,
        education, level,
        last_year_earnings)
        self.base_pay = base_pay
        self.bonuses = bonuses
        self.overtime = overtime
        self.last_promotion_date = last_promotion_date
        self.num_projects = num_projects

    def estimateProductivity(self):

        productivity = self.last_year_earnings / self.base_pay

        if self.num_projects > self.PROJECT_THRESHOLD:
            productivity += self.PROJECT_BONUS

        '''years_since_promotion = (date.today() - self.last_promotion_date).days / 365
        if self.last_promotion_date > years_since_promotion:
            productivity -= self.PROMOTION_PENALTY'''

        years_since_promotion = (date.today() - self.last_promotion_date).days / 365
        if years_since_promotion > 3:
            productivity -= self.PROMOTION_PENALTY

        return productivity

#Google:
#Base Calculation: Divides self.last_year_earnings by self.base_pay.
#Project Bonus: Checks self.num_projects > 2 and adds 1.5.
'''Promotion Penalty: Calculates three_years_ago using timedelta to check
if self.last_promotion_date is older than 3 years, subtracting 0.8.'''
#Safety check: Added a check for base_pay > 0 to prevent division by zero errors.



#HW 03/10/26:
#Implement the manager and Individual Contributor as child classes and what attributes it needs.
#What methods it goes into.
#key question: in the child class, how do we access certain attributes/methods that are defined in the parent class?

'''Manager bonus: Every manager who manages more than 8 employees gets a bonus
boost, where 1.8 is added to their current productivity estimate.'''

# ------------------------
# Manager
# ------------------------

class Manager(FullTimeEmployee):
    MANAGE_EMPLOYEES_THRESHOLD = 8
    MANAGE_BONUS = 1.8
    def __init__(
            self,
            employee_id: str,
            contact: ContactInfo,
            employment_date: date,
            education: EducationLevel,
            level: EmploymentLevel,
            last_year_earnings: float,
            base_pay: float,
            bonuses: float,
            overtime: float,
            last_promotion_date: date,
            num_projects: int,
            num_employees_managed: int):
        
        
        super().__init__(employee_id,
        contact,
        employment_date,
        education,
        level,
        last_year_earnings,
        base_pay,
        bonuses,
        overtime,
        last_promotion_date,
        num_projects)
        self.num_employees_managed = num_employees_managed

    def estimateProductivity(self):    
        
        productivity = super().estimateProductivity()

        if self.num_employees_managed > self.MANAGE_EMPLOYEES_THRESHOLD:
            productivity += self.MANAGE_BONUS

        return productivity


'''class Manager(FullTimeEmployee):
    MANAGE_EMPLOYEES = 8
    MANAGE_BONUS = 1.8
    def __init__(
            self,
            employee_id: str,
            contact: ContactInfo,
            employment_date: date,
            education: EducationLevel,
            level: EmploymentLevel,
            last_year_earnings: float,
            base_pay: float,
            bonuses: float,
            overtime: float,
            last_promotion_date: date,
            num_projects: int,
            num_employees_managed: int):
        
        super().__init__(employee_id,
        contact,
        employment_date,
        education,
        level,
        last_year_earnings,
        base_pay,
        bonuses,
        overtime,
        last_promotion_date,
        num_projects)
        self.num_employees_managed = num_employees_managed

    def estimateProductivity(self):    
        
        productivity = self.num_employees_managed + self.MANAGE_BONUS

        if self.num_employees_managed > self.MANAGE_EMPLOYEES:
            productivity += self.MANAGE_BONUS

        return productivity'''


'''Individual contributor bonus: Every individual contributor who published more than 4 publications last year,
    gets a bonus boost, where 1.3 is added to their current productivity estimate.'''

# ------------------------
# IndividualContributor
# ------------------------

class IndividualContributor(FullTimeEmployee):
    PUBLICATION_THRESHOLD = 4
    PUBLISH_BONUSES = 1.3
    def __init__(self,
            employee_id: str,
            contact: ContactInfo,
            employment_date: date,
            education: EducationLevel,
            level: EmploymentLevel,
            last_year_earnings: float,
            base_pay: float,
            bonuses: float,
            overtime: float,
            last_promotion_date: date,
            num_projects: int,
            num_patents: int,
            num_publications : int,
            num_external_collab : int):
    
        super().__init__(
        employee_id,
        contact,
        employment_date,
        education,
        level,
        last_year_earnings,
        base_pay,
        bonuses,
        overtime,
        last_promotion_date,
        num_projects)    
        self.num_patents = num_patents
        self.num_publications = num_publications
        self.num_external_collab = num_external_collab

    def estimateProductivity(self):    

        productivity = super().estimateProductivity()
        if self.num_publications > self.PUBLICATION_THRESHOLD:
            productivity += self.PUBLISH_BONUSES
        return productivity
    
'''HW 03/15/26: Code out the partimeemployee class and the child classes.
Put attributes, methods, and see if there are no magic numbers.'''


'''Base productivity estimate for part-time employees: Base productivity of part-
time employees is calculated as a ratio between an employee's actual number of worked
hours, and their contractual number of worked hours, and the result is multiplied by 3.7.'''

# ------------------------
# PartTimeEmployee
# ------------------------

class PartTimeEmployee(Employee):
    PRODUCTIVITY_MULTIPLIER = 3.7
    def __init__(
            self,
            employee_id: str,
            contact: ContactInfo,
            employment_date: date,
            education: EducationLevel,
            level: EmploymentLevel,
            last_year_earnings: float,
            contractual_hours: float,
            actual_hours: float,
            bonus_overtime: float):
        
        super().__init__(employee_id, contact, employment_date, education, level, last_year_earnings)
        self.contractual_hours = contractual_hours
        self.actual_hours = actual_hours
        self.bonus_overtime = bonus_overtime

    def estimateProductivity(self):

        productivity = (self.actual_hours / self.contractual_hours) * self.PRODUCTIVITY_MULTIPLIER

        return productivity

'''Hourly earnings bonus: If an hourly employee's hourly rate is less than $14, they
get a bonus boost, where 3 is added to their current productivity estimate.'''

# ------------------------
# HourlyEmployee
# ------------------------

class HourlyEmployee(PartTimeEmployee):
    HOURLY_RATE = 14
    HOURLY_BONUSES = 3
    def __init__(
            self,
            employee_id: str,
            contact: ContactInfo,
            employment_date: date,
            education: EducationLevel,
            level: EmploymentLevel,
            last_year_earnings: float,
            contractual_hours: float,
            actual_hours: float,
            bonus_overtime: float,
            hourly_earnings: float):

        super().__init__(
        employee_id,
        contact,
        employment_date,
        education, level,
        last_year_earnings,
        contractual_hours,
        actual_hours,
        bonus_overtime)
        self.hourly_earnings = hourly_earnings

    def estimateProductivity(self):
        
        productivity = super().estimateProductivity()

        if self.hourly_earnings < self.HOURLY_RATE:
            productivity += self.HOURLY_BONUSES

        return productivity


# ------------------------
# BenefitsEligibleEmployee
# ------------------------

class BenefitsEligibleEmployee(PartTimeEmployee):

    def __init__(
            self,
            employee_id: str,
            contact: ContactInfo,
            employment_date: date,
            education: EducationLevel,
            level: EmploymentLevel,
            last_year_earnings: float,
            contractual_hours: float,
            actual_hours: float,
            bonus_overtime: float):
        
        super().__init__(
        employee_id,
        contact,
        employment_date,
        education, level,
        last_year_earnings,
        contractual_hours,
        actual_hours,
        bonus_overtime)