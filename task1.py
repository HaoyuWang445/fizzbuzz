import csv
def task1():
    good=[]
    marginal=[]
    poor=[]
    after_2000=[]
    active=[]
    lighting=[]
    walkHike=[]
    tuple_list=[]
    with open('Trails.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            if(row[9]=='good'):
                good.append(row)

            elif(row[9]=='marginal'):
                marginal.append(row)

            else:
                poor.append(row)

            if(row[10].startswith('2')):
                after_2000.append(row)
            else:
                pass

            if(row[15].startswith('A')):
                active.append(row)
            else:
                pass

            #walking & hiking
            if(row[23].startswith('Y') and row[24].startswith('Y')):
                walkHike.append(row)
            else:
                pass
            
            tuple_list.append((row[0],row[9],row[23],row[24],row[25]))
            
    print('How many trails are currently Active? [Use "Status" to find 
this]'+'\n \t'+str(len(active))) 
    print('How many have lighting? [Use "Lighting" to do this].'+'\n \t 
'+str(0) ) 
    print('How many are both "Walking" and have "Biking"?'+'\n \t 
'+str(len(walkHike)))
    return after_2000,tuple_list
        


