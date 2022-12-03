from pathlib import Path
import re

path = 'c:/Users/wojda/OneDrive/Dokumenty/GitHub/skryptowe_jezyki_LAB/skryptowe_jezyki_programowania/LAB5/l4z2.txt'
txt = Path(path).read_text('utf-8')

#wykrycie konta bankowego prostym regexem
bankAccRegex = re.compile(r'[0-9]{2}(?:[ ]?[0-9]{4}){6}')
print(re.findall(bankAccRegex, txt))

#prosty regex na potrzeby zadania, nie będę rozbudowywał bo regexy na datę muszą być bardzo skomplikowane
dateRegex = re.compile(r'[0-3][0-9][.][0-1][0-9][.][0-9][0-9]') 
dates = re.findall(dateRegex, txt)
for i in dates:
    print(re.sub(r'[.]', '-', i))

ammRegex = re.compile(r"[0-9]{4}[,][0-9]{2}[z][ł]")
amm = re.findall(ammRegex, txt)
for i in amm:
    print(re.sub(ammRegex, '.........', i))
#zamiana podwójnych spacji na pojedyncze
spaceRegex = re.compile(r"[ ]{2}")
re.sub(ammRegex, '.........',txt)
#wykrycie wszystkich znaków dopóki nie zostanie napotkany newline
newlineRegex = re.compile(r".*")
newline = re.findall(newlineRegex, txt)


