'''
Created on Oct 30, 2017

@author: Orgil Batzaya
ob29
'''
def fileToStringList(filename):
    #filename is a file, 
    #returns a list of strings, each string represents
    #one line from filename
    wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        wordlist.append(line)
    f.close()
    return wordlist

def cancelDict(result):
    '''cancelDict takes in list of strings parameter result 
    and returns the airport code associated with max amount of 
    months with 100 or more cancellations, and the value'''
    cancel = {} #create new dictionary 
    for i in result:#for each string in list 'result
        if int(i.split('$')[3])>=100 and i.split('$')[0] not in cancel:
            cancel[i.split('$')[0]] = 1 #adding new key, airport code, to cancel
        elif int(i.split('$')[3])>=100 and i.split('$')[0] in cancel:
            cancel[i.split('$')[0]] += 1 #if key already exists, add 1 to value
            
    #calculating max value(months)
    m = max(cancel.values())
    cancMo = [k for k,v in cancel.items() if v==m][0]#list comprehension returns key that pairs to highest month
    return cancMo, cancel[cancMo]

def busyMo(result):
    '''busyMo takes a list of string result and prints the busiest month for each airport along
    with avg flights for that month. Uses a dictionary of dictionaries'''
    busy = {}
    for i in result:
        if i.split('$')[0] not in busy:#create new key for every new airport code
            busy[i.split('$')[0]] = {}#initialize dictionary of dictionary
            busy[i.split('$')[0]][i.split('$')[1]] = [i.split('$')[6]]#code:{month: gets total flights as list item 
        else:
            if i.split('$')[1] not in busy[i.split('$')[0]]:#initialize for each new month in a code
                busy[i.split('$')[0]][i.split('$')[1]] =  [i.split('$')[6]]
            else:
                busy[i.split('$')[0]][i.split('$')[1]] += [i.split('$')[6]]#append to list

    for air in sorted(busy.keys()):#for each code key in dictionary of dictionaries busy alphabetized
        for mo in busy[air]:
            numlist = [float(x) for x in busy[air][mo]]#float conversion for items in code:{month:
            busy[air][mo]= sum(numlist)/len(numlist)#reassign value to average for that month
            maxi = max(busy[air], key=busy[air].get)#gets key associated w/ max value
        print "Busiest month for", air,"is", maxi, "with", busy[air][maxi], "average flights that month."
        #iteratively print

def onTime(result): 
    '''uses 3 dictionaries. First organizes by code and total flights. Second is on code and delayed.
    Third combines both by dividing the latter two's values. returns those codes with 0.8 better.'''
    time = {}
    for i in result:
        if i.split('$')[0] not in time:#for new codes
            time[i.split('$')[0]] = float(i.split('$')[6])#immediate float conversion of total flights
        else:
            time[i.split('$')[0]] += float(i.split('$')[6])
    
    delay = {}#new dictionary for total delayed flights
    for i in result:
        if i.split('$')[0] not in delay:
            delay[i.split('$')[0]] = float(i.split('$')[7])
        else:
            delay[i.split('$')[0]] += float(i.split('$')[7])
    
    good = {}#dictionary that gets codes which are 0.8 or better for delayed/total
    for i in time:
        if delay[i]/time[i] >= 0.8:
            good[i] = delay[i]/time[i]
    for k in sorted(good.keys()):
        print k,good[k]
if __name__ == '__main__':
    lines = fileToStringList("airportDataOct2017.txt")
    print "Information about major airports in the United States\n"
    print "Airport with most months with 100 or more cancellations is", cancelDict(lines)[0]
    print "It had", cancelDict(lines)[1], "months with 100 or more cancellations\n"
    print "Busiest month for each airport:"
    busyMo(lines),
    print 
    print "Airports that have >= 80 percent on time flights:"
    onTime(lines)

