def solvepart1():
    #format data
    data = fileRead("input.txt")
    data[0] = " ".join(data[0].split()).split(":")[1].strip().split(" ")
    data[1] = " ".join(data[1].split()).split(":")[1].strip().split(" ")
    data[0] = [ int(i) for i in data[0] ]
    data[1] = [ int(i) for i in data[1] ]
    races = []
    for i in range(len(data[0])):
        races.append([data[0][i],data[1][i]])

    #solve races
    sum = 1
    for race in races:
        time = race[0]
        record = race[1]
        numWins = 0
        for currentTime in range(race[0]):
            distance = (time-currentTime)*currentTime
            if (distance > record):
                numWins = numWins + 1
        sum = sum * numWins
    print(sum)



def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()