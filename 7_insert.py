from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

ws.insert_rows(8) #8번째 줄이 비원짐
ws.insert_rows(8, 5) #8번째줄 위체에 5줄을 추가

wb.save("sample_insert_rows.xlsx")