import tabulate
table = [['','' ,'' ], ['', '', ''], ['', '', '']]
print(tabulate.tabulate(table, tablefmt="grid"))
print "Enter cordinates"
cordinates = input()
rowindex =1
columnindex=1
for row in table:
    #print(count)
    if rowindex == cordinates[0]:
      for column in row:
        if columnindex == cordinates[1]:
          table[rowindex][columnindex] = 0
      columnindex += 1
    rowindex +=1

print(tabulate.tabulate(table, tablefmt="grid"))
