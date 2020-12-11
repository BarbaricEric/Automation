#! python3
# readCensusEcel.py - Tabulates population and number of census tracts for each county

import openxl, pprint
print('Opening workbook...')
wb = openpyxl.loada_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1);
 state = sheet['B' + str(row)].value
 county = sheet['C' + str(row)].value
 pop = sheet['D' + str(row)].value