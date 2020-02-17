def triangle(row):
    modrow = ''
    colours = 'GBR'
    for i in range(len(row)):

        if len(row) == 1:
                return row
        
        for j in range(len(row)-1):
            
            if row[j] == row[j+1]:
                modrow += row[j]
            else:
                modrow += colours.replace(row[j],'').replace(row[j+1],'')
        row = modrow
        modrow = ''


print(triangle('RBRGBRBGGRRRBGBBBGG'))

