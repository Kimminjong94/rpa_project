from openpyxl import load_workbook
wb = load_workbook("sample.xlsx")
ws = wb.active

ws.delete_rows(8, 3) #8번째 줄에있는 7번학생 삭제


# wb.save("sample_delete_rows.xlsx")

ws.delete_cols(2) #2번째 열 삭제 
wb.save("sample_delete_col.xlsx")