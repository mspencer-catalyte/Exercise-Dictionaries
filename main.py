
status = ['Applied', 'Accepted', 'Active', 'Completed', 'Dismissed', 'Rejected']

#applicant = {
#    "name": "",
#    "age" : 0,
#    "address": "",
#    "street": "",
#    "city": "",
#    "state": "",
#    "zip": "",
#    "status": ""
#}

applicants = [ 
{"name": "Abigail Fontane", "age" : 44, "address" : "123", "street" : "Gibby St", "city" : "Havalina", "state" : "NY", "zip" : "94949", "status" : status[2]},
{"name": "Bruce Lee", "age" : 52, "address" : "1343 ", "street" : "IDK Ave", "city" : "Greer", "state" : "MO", "zip" : "96969", "status" : status[1]},
{"name": "Charlie Murphy", "age" : 13, "address" : "3343 ", "street" : "Hall Ln", "city" : "Nantucket", "state" : "NC", "zip" : "84549", "status" : status[2]},
{"name": "Dean Wilson", "age" : 16, "address" : "984 ", "street" : "Pace Ave", "city" : "Franklin", "state" : "IL", "zip" : "07552", "status" : status[3]},
{"name": "Esteban Ortega", "age" : 18, "address" : "777", "street" : "Luck St", "city" : "Foster", "state" : "NY", "zip" : "20209", "status" : status[4]},
{"name": "Florence Macine","age" : 19, "address" : "656", "street" : "Calumm Dr", "city" : "Newark", "state" : "DE", "zip" : "08312", "status" : status[5]},
{"name": "Giana Wallace", "age" : 99, "address" : "7535", "street" : "Not Way", "city" : "Wheaton", "state" : "MD", "zip" : "02265", "status" : status[2]},
{"name": "Henderson Pak", "age" : 73, "address" : "244", "street" : "Heart St", "city" : "Kensington", "state" : "CA", "zip" : "84521", "status" : status[3]},
{"name": "Imogen Heap", "age" : 21, "address" : "782", "street" : "Boop Pl", "city" : "Haplern", "state" : "FL", "zip" : "59643", "status" : status[4]},
{"name": "Jackie Warner ", "age" : 32, "address" : "789", "street" : "Funt Dr", "city" : "Greenbelt", "state" : "GA", "zip" : "12548", "status" : status[1]}
]

#print(applicants[0]["age"]) 

def is_eligble_applicant(applicant):
    """ Takes an applicant as a parameter and returns a boolean that indicates whether or not the applicant's 
        age is greater than 18."""
    age_var = applicant["age"]
   
    if age_var >= 18:
        return True
    else:
        return False

if is_eligble_applicant(applicants[0]):
    print("This applicant is eligble.")
else:
    print("This applicant is ineligble.")

def is_active_applicant(applicant):
    """Takes an applicant as a parameter and returns
        a boolean that indicates whether or not the applicant's 
        program status is "Active""""
    status_var = applicant["status"]
    if status_var == "Active":
        return True
    else:
        return False

if is_active_applicant(applicants[0]):
    print("This applicant is active.")
else:
    print("This applicant is inactive.") 

def filter_applicants_by_eligibility(applicant_list):
    """Takes a list of applicants 
        and returns a list of eligible applicants."""
    eligible_list = []
    for applicant in applicant_list:
        if applicant["age"] >= 18:
            eligible_list.append(applicant["name"])
        else:
            pass

    print("Applicants that are eligble for the program.")
    for name in eligible_list:
        print(name)
    print("\n")

filter_applicants_by_eligibility(applicants)

#Define a function "filter_active_applicants" which 

def filter_active_applicants(applicant_list):
    """Takes a list of applicants 
         and returns a list of applicants with an active program status."""
    active_list = []
    for applicant in applicant_list:
        if applicant["status"] == "Active":
            active_list.append(applicant["name"])
        else:
            pass

    print("Applicants that are active in the program.")
    for name in active_list:
        print(name)
    print("\n")

filter_active_applicants(applicants)

#Define a function "report_completed_applicants" which 

def report_completed_applicants(applicant_list):
    """"Takes a list of applicants 
            and returns the number of applicants with the program status of "Completed"."""
    completed_list = []
    for applicant in applicant_list:
        if applicant["status"] == "Completed":
            completed_list.append(applicant["name"])
        else:
            pass

    print("Applicants that have completed the program.")
    for name in completed_list:
        print(name)
    print("\n")

report_completed_applicants(applicants)