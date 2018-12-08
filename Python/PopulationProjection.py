totalSecondsInYear = 365 * 24 * 60 * 60

def birth():
    return (totalSecondsInYear//7)

def death():
    return (totalSecondsInYear//13)

def newImmigrant():
    return (totalSecondsInYear//45)

def calPopulation(currentPopulation, year):
    for i in range(year):
        currentPopulation += (birth() + newImmigrant() - death()) * i
    return currentPopulation

year = eval(input("Enter how many years? "))
currPop = eval(input("Current Population? "))
print("After {year} years, the population is {pop}".format(year = year, pop = calPopulation(currPop, year)))
