
status = ['Applied', 'Accepted', 'Active', 'Completed', 'Dismissed', 'Rejected']

applicant1 = dict(name="Abigail Fontane",age=44,address="123",street="Gibby St",city="Havalina",state="NY",zip="94949",status=status[2])
applicant2 = dict(name="Bruce Lee",age=52,address="1343",street="IDK Ave",city="Greer",state="MO",zip="96969",status=status[1])
applicant3 = dict(name="Charlie Murphy",age=13,address="3343",street="Hall Ln",city="Nantucket",state="NC",zip="84549",status=status[2])
applicant4 = dict(name="Dean Wilson",age=16,address="984",street="Pace Ave",city="Franklin",state="IL",zip="07552",status=status[3])
applicant5 = dict(name="Esteban Ortega",age=18,address="777",street="Luck St",city="Foster",state="NY",zip="20209",status=status[4])
applicant6 = dict(name="Florence Machine",age=19,address="656",street="Calumm Dr",city="Newark",state="DE",zip="08312", status=status[5])
applicant7 = dict(name="Giana Wallace",age=99,address="7535",street="Not Way",city="Wheaton",state="MD",zip="02265",status=status[2])
applicant8 = dict(name="Henderson Pak",age=73,address="244",street="Heart St",city="Kensington",state="CA",zip="84521",status=status[3])
applicant9 = dict(name="Imogen Heap",age=21,address="782",street="Boop Pl",city="Haplern",state="FL",zip="59643",status=status[4])
applicant10 = dict(name="Jackie Warner",age=32,address="789",street="Funt Dr",city="Greenbelt",state="GA",zip="12548",status=status[1])

applicants = [applicant1,applicant2,applicant3,applicant4,applicant5,applicant6,applicant7,applicant8,applicant9,applicant10]

def is_eligble_applicant(applicant):
    """ Takes an applicant as a parameter and returns a boolean that indicates whether or not the applicant's 
        age is greater than 18.
        
      Args:
        applicant(dict): An dictionary of an applicant

    Returns:
        Bool: Indicates whether the applicant is greater than 18.
    
    """
    age_var = applicant["age"]
   
    if age_var > 18:
        return True
    else:
        return False

def is_active_applicant(applicant):
    """Takes an applicant as a parameter and returns
        a boolean that indicates whether or not the applicant's 
        program status is "Active
        Args:
            applicant(dict): An dictionary of an applicant
    
        Returns:
            Bool: Indicates whether the applicant is active in the program.
    
    """
    status_var = applicant["status"]
    if status_var == "Active":
        return True
    else:
        return False

def filter_applicants_by_eligibility(applicant_list):
    """Takes a list of applicants 
        and returns a list of eligible applicants.
        Args:
            applicant_list(list): A list of dictionaries of applicants

        Returns:
            list: List of applicants that meet the filter requirements
 
    """
    eligible_list = []
    for applicant in applicant_list:
        if applicant["age"] >= 18:
            eligible_list.append(applicant["name"])
        else:
            pass
    return eligible_list 

def filter_active_applicants(applicant_list):
    """Takes a list of applicants 
         and returns a list of applicants with an active program status.
        Args:
            applicant_list(list): A list of dictionaries of applicants

        Returns:
            list: List of applicants that meet the filter requirements

    """
    active_list = []
    for applicant in applicant_list:
        if applicant["status"] == "Active":
            active_list.append(applicant["name"])
        else:
            pass
    return active_list

def report_completed_applicants(applicant_list):
    """"Takes a list of applicants 
            and returns the number of applicants with the program status of "Completed".
            
        Args:
            applicant_list(list): A list of dictionaries of applicants

        Returns:
            list: List of applicants that meet the filter requirements

    """
    completed_list = []
    for applicant in applicant_list:
        if applicant["status"] == "Completed":
            completed_list.append(applicant["name"])
        else:
            pass
    return len(completed_list)

list_of_eligibles = filter_applicants_by_eligibility(applicants)
list_of_actives = filter_active_applicants(applicants) 
number_of_completed = report_completed_applicants(applicants)