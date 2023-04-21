##############################################################################
###    ~~~~~~~~~~~~    THIS IS A SKILLSTORM ASSIGNMENT!    ~~~~~~~~~~~~    ### 
##############################################################################




import csv

# Defines the Expenditure class with attributes for department, BCL, program, and actual 2012 expense
class Expenditure:
    Department: str
    BCL: str
    Program: str
    actual_2012: float

    def __init__(self, Department, BCL, Program, actual_2012):
        self.department = Department
        self.bcl = BCL
        self.program = Program
        self.actual_2012 = actual_2012


# Opens the CSV file with expenditure data
with open("city-of-seattle-2012-expenditures-dollars.csv") as file:
    # Creates a CSV reader object
    reader = csv.reader(file, delimiter=",")
    # Creates an empty dictionary to store the total expenses for each department
    expenditure_dict = {}
    # Initializes a row number counter
    row_number = 1
    # Iterates through each row of the file
    for row in reader:
        # Skip the first row
        if row_number != 1:
            # Extracts the department and the actual 2012 expense converted to a float
            department = row[0]
            actual_2012 = float(row[3]) if row[3] != '' else 0
            # Checks if the department is already in the expenditure_dict, if it is 
            # add the actual 2012 expense to the existing total. If it is not in the expenditure_dict, 
            # add it with the actual 2012 expense as the total.
            if department in expenditure_dict:
                expenditure_dict[department] += actual_2012
            else:
                expenditure_dict[department] = actual_2012
        # Increments the row number counter
        row_number += 1
    # Prints column headers
print("Department\t\t\tTotal 2012 Actual")
print("----------------------------------------------------")
# Formats output
for department, total in expenditure_dict.items():
    print(f"{department.ljust(30)}\t\t${total:,.2f}")



#                 .                                            .
#      *   .                  .              .        .   *          .
#   .         .                     .       .           .      .        .
#         o                             .                   .
#          .              .                  .           .
#           0     .
#                  .          .                 ,                ,    ,
#  .          \          .                         .
#       .      \   ,
#    .          o     .                 .                   .            .
#      .         \                 ,             .                .
#                #\##\#      .                              .        .
#              #  #O##\###                .                        .
#    .        #*#  #\##\###                       .                     ,
#         .   ##*#  #\##\##               .                     .
#       .      ##*#  #o##\#         .                             ,       .
#           .     *#  #\#     .                    .             .          ,
#                       \          .                         .
# ____^/\___^--____/\____O______________/\/\---/\___________---______________
#    /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
#          --           -            --  -      -         ---  __       ^
#    --  __                      ___--  ^  ^                         --  __