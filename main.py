from date import *

def main():
    objDate = Date()
    print(objDate.heure())
    print(objDate.minute())
    print(objDate.second())
    print(objDate.jour())
    print(objDate.jourSimple())
    print(objDate.nbMois())
    print(objDate.nbMoisSimple())
    print(objDate.mois())
    print(objDate.annes())
    print(objDate.getDateToday())
    print(objDate.getDateToday())
    print(objDate.dateTowmoro())
    print(objDate.otherPastDate(2))
    print(objDate.otherAfterDate(2))

if __name__ == '__main__':
    main()