#! python3

import openpyxl, pprint
print('Opening workbook...');
wb = openpyxl.load_workbook('D:\\Scripts\\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')

countyData = {}

print('Reading rows...')
for row in range(2,sheet.max_row):
	state = sheet['B'+ str(row)].value
	county = sheet['C' + str(row)].value
	pop = sheet['D' + str(row)].value
	
	countyData.setdefault(state,{})
	countyData[state].setdefault(county,{'pop':0,'tracts':0})
	countyData[state][county]['pop'] += int(pop)
	countyData[state][county]['tracts'] += 1
	
print('Writing results...')
resultFile = open('D:\\Scripts\\census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')	
