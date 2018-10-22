#! python3

import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
for i in range(1,11):
	sheet['A' + str(i)] = i

referenceObject = openpyxl.chart.Reference(sheet,min_col=1, min_row=1, max_col=1, max_row=10)
chartObject = openpyxl.chart.BarChart()
chartObject.add_data(referenceObject)

#set the position of chart
#chartObject.drawing.top = 50
#chartObject.drawing.left = 100
#chartObject.drawing.width = 300
#chartObject.drawing.height = 200

sheet.add_chart(chartObject)
wb.save('D:\\Scripts\\sampleChart.xlsx')
