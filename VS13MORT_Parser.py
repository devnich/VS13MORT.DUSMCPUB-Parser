# VS13MORT Parser.py
# Author tommaho
# Hosted at https://github.com/tommaho/VS13MORT.DUSMCPUB-Parser
#
# About
#   Converts the 2013 Mortality file located here: http://www.cdc.gov/nchs/data_access/vitalstatsonline.htm
#   to a CSV, based on data file documentation here: http://www.cdc.gov/nchs/data/dvs/Record_Layout_2013.pdf
# Edits
#
# Directions
#
# 1. Have Python installed.
# 2. Get & unzip mortality file
# 3. Tweak fileObj and FileOutObj to point to the source and destination of your choosing.


fileObj = open('VS11MORT.DUSMCPUB','r')
fileOutObj = open('VS11MORT.csv','w')

fileOutObj.write('Resident_Status, Education, Month_Of_Death, Sex, Age_Key, Age_Value, Age_Sub_Flag, Age_Recode_52, Age_Recode_27, ' + \
                 'Age_Recode_12, Infant_Age_Recode_22, Place_Of_Death, Marital_Status, DOW_of_Death, Data_Year, Injured_At_Work, ' + \
                 'Manner_Of_Death, Method_Of_Disposition, Autopsy, Activity_Code, Place_Of_Causal_Injury,  ICD10, Cause_Recode_358, ' + \
                 'Cause_Recode_113, Infant_Cause_Recode_130, Cause_Recode_39, Entity_Axis_Conditions, EAC1, EAC2, EAC3, EAC4, EAC5, ' + \
                 'EAC6, EAC7, EAC8, EAC9, EAC10, EAC11, EAC12, EAC13, EAC14, EAC15, EAC16, EAC17, EAC18, EAC19, EAC20, ' + \
                 'Record_Axis_Conditions, RA1, RA2, RA3, RA4, RA5, RA6, RA7, RA8, RA9, RA10, RA11, RA12, RA13, RA14, ' + \
                 'RA15, RA16, RA17, RA18, RA19, RA20, Race, Race_Bridged, Race_Imputation, Race_Recode_3, Race_Recode_5, ' + \
                 'Hispanic_Origin, Hispanic_Origin_Recode\n')

outStr = ""

for line in fileObj:
    outList = [line[19].strip()
               , line[60:62].strip()
               , line[63:67].strip()
               , line[68].strip()
               , line[69].strip()
               , line[70:73].strip()
               , line[73].strip()
               , line[74:76].strip()
               , line[76:78].strip()
               , line[78:80].strip()
               , line[80:82].strip()
               , line[82].strip()
               , line[83].strip()
               , line[84].strip()
               , line[101:105].strip()
               , line[105].strip()
               , line[106].strip()
               , line[107].strip()
               , line[108].strip()
               , line[143].strip()
               , line[144].strip()
               , line[145:149].strip()
               , line[149:152].strip()
               , line[153:156].strip()
               , line[156:159].strip()
               , line[159:161].strip()
               , line[162:164].strip()
               , line[164:171].strip()
               , line[171:178].strip()
               , line[178:185].strip()
               , line[185:192].strip()
               , line[192:199].strip()
               , line[199:206].strip()
               , line[206:213].strip()
               , line[213:220].strip()
               , line[220:227].strip()
               , line[227:234].strip()
               , line[234:241].strip()
               , line[241:248].strip()
               , line[248:255].strip()
               , line[255:262].strip()
               , line[262:269].strip()
               , line[269:276].strip()
               , line[276:283].strip()
               , line[283:290].strip()
               , line[290:297].strip()
               , line[297:304].strip()
               , line[340:342].strip()
               , line[343:348].strip()
               , line[348:353].strip()
               , line[353:358].strip()
               , line[358:363].strip()
               , line[363:368].strip()
               , line[368:373].strip()
               , line[373:378].strip()
               , line[378:383].strip()
               , line[383:388].strip()
               , line[388:393].strip()
               , line[393:398].strip()
               , line[398:403].strip()
               , line[403:408].strip()
               , line[408:413].strip()
               , line[413:418].strip()
               , line[418:423].strip()
               , line[423:428].strip()
               , line[428:433].strip()
               , line[433:438].strip()
               , line[438:443].strip()
               , line[444:446].strip()
               , line[446].strip()
               , line[447].strip()
               , line[448].strip()
               , line[449].strip()
               , line[483:486].strip()
               , line[487].strip()
               ]

    outStr = ', '.join(outList)
    fileOutObj.write(''.join([outStr, '\n']))

print("Parse complete.")
fileOutObj.close()
fileObj.close()
