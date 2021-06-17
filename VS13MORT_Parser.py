# ------------------------------------------------------------------
# Converts the 2013 Mortality file located here:
#   http://www.cdc.gov/nchs/data_access/vitalstatsonline.htm
# to a CSV, based on data file documentation here:
#   http://www.cdc.gov/nchs/data/dvs/Record_Layout_2013.pdf
#
# Originally derived from https://github.com/tommaho/VS13MORT.DUSMCPUB-Parser

# Directions
#  1. Have Python installed.
#  2. Get & unzip mortality file
#  3. Change `infile_name` and `outfile_name` to point to the source and
#     destination of your choosing.
#
# How Python handles indexing:
#  1. indices count from zero
#  2. indices count up to, but not including, the second position
#
#  Example: 'Resident_Status' is at position 20, which in Python is indexed as [19:20]
# ------------------------------------------------------------------

import collections
import csv

# Define your input and output files
#
# If you need to process many files, you can put them in a directory and
# automatically generate a list of file names. Read the documentation for
# pathlib.Path for more info on how to do this.

infile_name = 'VS11MORT.DUSMCPUB'
outfile_name = 'VS11MORT.csv'

# When `test_flag` is True, the program will process 10 lines and quit. To process the
# entire file, set this to False

test_flag = True

# Create an ordered collection of key:value pairs
fields = collections.OrderedDict([('Resident_Status', (19, 20)),
                                  ('Education', (60, 62)),
                                  ('Month_Of_Death', (63, 67)),
                                  ('Sex', (68, 69)),
                                  ('Age_Key', (69, 70)),
                                  ('Age_Value', (70, 73)),
                                  ('Age_Sub_Flag', (73, 74)),
                                  ('Age_Recode_52', (74, 76)),
                                  ('Age_Recode_27', (76, 78)),
                                  ('Age_Recode_12', (78, 80)),
                                  ('Infant_Age_Recode_22', (80, 82)),
                                  ('Place_Of_Death', (82, 83)),
                                  ('Marital_Status', (83, 84)),
                                  ('DOW_of_Death', (84, 85)),
                                  ('Data_Year', (101, 105)),
                                  ('Injured_At_Work', (105, 106)),
                                  ('Manner_Of_Death', (106, 107)),
                                  ('Method_Of_Disposition', (107, 108)),
                                  ('Autopsy', (108, 109)),
                                  ('Activity_Code', (143, 144)),
                                  ('Place_Of_Causal_Injury', (144, 145)),
                                  ('ICD10', (145, 149)),
                                  ('Cause_Recode_358', (149, 152)),
                                  ('Cause_Recode_113', (153, 156)),
                                  ('Infant_Cause_Recode_130', (156, 159)),
                                  ('Cause_Recode_39', (159, 161)),
                                  ('Entity_Axis_Conditions', (162, 164)),
                                  ('EAC1', (164, 171)),
                                  ('EAC2', (171, 178)),
                                  ('EAC3', (178, 185)),
                                  ('EAC4', (185, 192)),
                                  ('EAC5', (192, 199)),
                                  ('EAC6', (199, 206)),
                                  ('EAC7', (206, 213)),
                                  ('EAC8', (213, 220)),
                                  ('EAC9', (220, 227)),
                                  ('EAC10', (227, 234)),
                                  ('EAC11', (234, 241)),
                                  ('EAC12', (241, 248)),
                                  ('EAC13', (248, 255)),
                                  ('EAC14', (255, 262)),
                                  ('EAC15', (262, 269)),
                                  ('EAC16', (269, 276)),
                                  ('EAC17', (276, 283)),
                                  ('EAC18', (283, 290)),
                                  ('EAC19', (290, 297)),
                                  ('EAC20', (297, 304)),
                                  ('Record_Axis_Conditions', (340, 342)),
                                  ('RA1', (343, 348)),
                                  ('RA2', (348, 353)),
                                  ('RA3', (353, 358)),
                                  ('RA4', (358, 363)),
                                  ('RA5', (363, 368)),
                                  ('RA6', (368, 373)),
                                  ('RA7', (373, 378)),
                                  ('RA8', (378, 383)),
                                  ('RA9', (383, 388)),
                                  ('RA10', (388, 393)),
                                  ('RA11', (393, 398)),
                                  ('RA12', (398, 403)),
                                  ('RA13', (403, 408)),
                                  ('RA14', (408, 413)),
                                  ('RA15', (413, 418)),
                                  ('RA16', (418, 423)),
                                  ('RA17', (423, 428)),
                                  ('RA18', (428, 433)),
                                  ('RA19', (433, 438)),
                                  ('RA20', (438, 443)),
                                  ('Race', (444, 446)),
                                  ('Race_Bridged', (446, 447)),
                                  ('Race_Imputation', (447, 448)),
                                  ('Race_Recode_3', (448, 449)),
                                  ('Race_Recode_5', (449, 450)),
                                  ('Hispanic_Origin', (483, 486)),
                                  ('Hispanic_Origin_Recode', (487, 488))])

# Sanity check for field positions; crash the program if they don't make sense
for key, val in fields.items():
    assert len(val) == 2
    assert val[0] <= val[1]

# Open files using a context manager (the "with" statement)
#
# Note that the output file has more parameters specified, because we are
# handling it with the csv module instead of treating it as a generic file

with open(infile_name, 'r') as infile, open(outfile_name, 'w', newline='') as outfile:

    # Create a CSV writer object
    writer = csv.writer(outfile)

    # Write headers
    writer.writerow(fields.keys())

    indices = fields.values()

    for row_num, line in enumerate(infile):
        # Generate list of line slices (this is a "list comprehension")
        out_list = [line[i[0]:i[1]].strip() for i in indices]
        writer.writerow(out_list)

        # If testing, quit after 10 rows
        if test_flag and row_num > 10:
            break

print("Parse complete")
