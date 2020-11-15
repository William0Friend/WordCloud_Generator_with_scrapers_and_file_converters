import re
with open("wordcloud.txt", encoding='utf-8') as f:
    with open("clean_full.txt", 'w', encoding='utf-8') as clean_file:
        x = f.readlines()
        s = []

        for i in x:
            i = i.replace(","," ")
            i = i.replace('.', " ")
            i = i.replace('!', " ")
            i = i.replace('?', " ")
            i = i.replace('  ', ' ')
            #i = i.replace('   ', ' ')    
            i = re.sub(r'[^a-zA-Z0-9_]', ' ', i)
            j = i.replace("\t"," ")
            s.append(j)
            clean_file.write(j)
            print(j)

        
            #for row in s:
            #    clean_file.write(row)