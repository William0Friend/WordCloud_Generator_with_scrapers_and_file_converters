import pandas as pd
import xlsxwriter
with open("authors.txt", encoding='utf-8') as f:
    x = f.readlines()
    s = []

    for i in x:
        s.append(i)
        #clean_file.write(j)
        print(s)

    data = pd.DataFrame(s)

    data2excel = pd.ExcelWriter("wordcloud_user_count.xlsx", engine='xlsxwriter')
    data.to_excel(data2excel, sheet_name='Sheet1')
    data2excel.save()