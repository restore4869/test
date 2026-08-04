'''3. Employee Productivity Tracking System
You are part of a company developing automated tools for tracking, predicting, and opti-
mizing employee productivity. Employees' productivity is a function of many complex
parameters, but at this stage, your company models and estimates productivity as follows.
The system distinguishes between two kinds of employees:

• Full-time employees
• Part-time employees

A full-time employee can be:
• Individual contributor
• Manager

A part-time employee can be:
• Benefits-eligible employee
• Hourly employee

3.1 Employee Information
For every employee, the productivity tracking system keeps track of:

• Employee ID, a unique employee identifier, represented as a str.
• Contact info, represented as a ContactInfo, a custom class that you will have to develop.

Class ContactInfo contains the following fields:

-Name, employee's first and last name, represented as a class Name, that you will also have to develop.
-Address, an employee's address, represented as a str.
-Phone number, the employee's phone number, represented as a str.
-Email address, the employee's email address, represented as a str.
-Emergency contact, the employee's emergency contact, represented as a Name.

• Employment date, the date the employee started working at their current company,
represented using datetime.date from the datetime module.
• Education level, represented as an EducationLevel, a custom enum (using Enum
from the enum module) that you will have to develop, with possible values: Highschool diploma,
Some college, Associate's degree, Bachelor's degree, Master's degree, Doctoral or professional degree.
• Employment level, represented as an EmploymentLevel, a custom enum (using Enum
from the enum module) that you will have to develop, with possible values: Entry level,
Intermediate level, Mid-level, Senior level, Executive level.
• Last year's earnings, represented as a float.

3.2 Full-Time Employees
Additionally, for every full-time employee, the system keeps track of:

• Base pay, the employee's base pay, as defined by the contract, represented as a float.
• Bonuses, the employee's last year earned bonuses, represented as a float.
• Overtime, the employee's last year's earnings due to overtime payments, represented as a float.
• Date of the last promotion, the date of the employee's last promotion, represented 
using datetime.date from the datetime module.
• Number of projects, the number of projects an employee is working on, represented as an int.

3.3 Part-Time Employees
Further, for every part-time employee, the system keeps track of:

• The contractual number of worked hours, denoting the number of hours an
employee is contractually expected to work per week, represented as a float.
• The actual number of worked hours, denoting the actual number of hours an
employee worked last week, represented as a float.
• Bonus and overtime earnings, denoting the combined bonus and overtime earnings, represented as a float.

3.4 Specialized Roles
Further, for every manager, the system keeps track of the number of employees they manage, represented as an int.
Additionally, for every individual contributor, the system keeps track of:

• The number of patents, denoting the number of patents awarded to the employee
while with the company, represented as an int.
• The number of publications, denoting the number of publications that the employee
published /presented last year, represented as an int.
• The number of external collaborations, denoting the number of external projects
that the employee is involved in, represented as an int.

Finally, for every hourly employee, the system keeps track of:

• Hourly earnings, denoting the contractual hourly earnings, and represented as a float.



4. Productivity Estimation Rules
The system estimates an employee's productivity according to the following rules:

• Base productivity estimate for full-time employees: Base productivity of full-
time employees is calculated as a ratio between an employee's last year's earnings, and their base pay.
• Base productivity estimate for part-time employees: Base productivity of part-
time employees is calculated as a ratio between an employee's actual number of worked
hours, and their contractual number of worked hours, and the result is multiplied by 3.7.
• Number of projects bonus: Every full-time employee involved in more than 2
projects gets a bonus boost where 1.5 is added to their base productivity estimate.
• Manager bonus: Every manager who manages more than 8 employees gets a bonus
boost, where 1.8 is added to their current productivity estimate.
• Individual contributor bonus: Every individual contributor who published more
than 4 publications last year, gets a bonus boost, where 1.3 is added to their current productivity estimate.
• Employment level bonus: If an employee is hired into the intermediate level role,
they get a bonus boost, where 1.4 is added to their current productivity estimate.
• Last promotion penalty: For every full-time employee, if more than three years
have passed since their last promotion, they get a penalty, where 0.8 is subtracted
from their current productivity estimate.
• Hourly earnings bonus: If an hourly employee's hourly rate is less than $14, they
get a bonus boost, where 3 is added to their current productivity estimate.'''



#We'll need the from abc and import ABC abstract method.
#For an abstraction, it will be called class Employees:.
#There will be 2 child classes and both will be inherited by the Employees class.
#For full time employees it will be called Class FullTimeEmployee(Employees) as a child class.
#For part time employees it will be called Class PartTimeEmployee(Employees) as a child class.
#The full time employees attributes will have Base Pay, Bonuses, Overtime, Date of the last promotion,
#and Number of projects.
#The part time employees attributes will have contractual_hours, actual_hours, and bonus_overtime.
#Both the child classes will have an instance variable(self).
#The child class for FullTimeEmployee will have 2 child classes called Individual_contributor and Manager.
#The child class for PartTimeEmployee will have 2 child classes called Benefits_eligible_employee and Hourly_employee.

#3. Employee Productivity Tracking System is the attributes.
#4. Productivity Estimation Rules is the methods.

#The new child class called Contact_Info and will have 5 attributes called Name, Address, Phone Number, Email Address,
#and Emergency Contact.
#The 2 attributes for the child class for Contact_Info for Name will be first and last.
#It will instantiate as contact = Name(Emergency_contact).

'''@startuml
' --------------------
' Employee Base Class
' --------------------

abstract class Employee {

+ employee_id : str
+ contact : ContactInfo
+ employment_date : date
+ education : EducationLevel
+ level : EmploymentLevel
+ last_year_earnings : float
}


' --------------------
' Full-Time Employees
' --------------------

estimateProductivity() :
class FullTimeEmployee {
+ base_pay : float
+ estimateProductivity() : float
+ bonuses : float
+ overtime : float
+ last_promotion_date : date
+ num_projects : int
+ estimateProductivity() : float
}


class Manager {
estimateProductivity() :
+ num_employees_managed : int
+ estimateProductivity() : float
}


class IndividualContributor {
estimateProductivity() :
+ num_patents : int
+ num_publications : int
+ num_external_collab : int
+ estimateProductivity() : float
}


' --------------------
' Part-Time Employees
' --------------------

class PartTimeEmployee {
estimateProductivity() :
+ contractual_hours : float
+ actual_hours : float
+ bonus_overtime : float
+ estimateProductivity() : float
}


class HourlyEmployee {
+ hourly_earnings : float
+ estimateProductivity() : float
}


class BenefitsEligibleEmployee {
}


' -------------------------
' Contact Support Classes
' -------------------------

class ContactInfo {
+ name : Name
+ address : str
+ phone : str
+ email : str
+ emergency_contact : Name
}


class Name {
+ first : str
+ last : str
}


enum EducationLevel {
}


enum EmploymentLevel {
}


' -------------------------
' Relationships
' -------------------------

Employee <|-- FullTimeEmployee
Employee <|-- PartTimeEmployee


FullTimeEmployee <|-- Manager
FullTimeEmployee <|-- IndividualContributor


PartTimeEmployee <|-- HourlyEmployee
PartTimeEmployee <|-- BenefitsEligibleEmployee


' Object associations
Employee --> ContactInfo
ContactInfo --> Name
@enduml'''

#The 2 pillars of O.O.P. for this assignment is Encapsulation and Abstraction.

#HW 02/22/26: Read through 3 and 4 sections of the OOP Assignment 1 HW.py.
# HW 02/22/26: Find what constants to have for enums for employment level and education level enums.

#For the employment level constants, it will be a custom enum which will have Entry level,
#Intermediate level, Mid-level, Senior level, Executive level.

#For the education level constants, it will also be a custom enum which will have  Highschool diploma,
#Some college, Associate's degree, Bachelor's degree, Master's degree, Doctoral or professional degree.

#Example: 

from enum import Enum 

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
