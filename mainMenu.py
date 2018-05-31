# -*- coding: UTF-8 -*-
import datetime

from PersonDetails import PersonDetails

# Ferry[][0]-->bussiness
# Ferry[][1]-->economy
Ferry = (([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []))
dateFerry = {}
BussinessList = []
EconomyList = []
printList = []
timetable = ['1) 10:00 am', '2) 11:00 am', '3) 12:00 am', '4) 1:00 pm', '5) 2:00 pm', '6) 3:00 pm', '7) 4:00 pm',
             '8) 5:00 pm']


# exit
def exit_sys():
    print('You have already exited this system!')


def consequ():
    print ('Ticket is purchased. Have a nice day.')
    print ('=====================================')
    print('Do you still want to continue?')
    print('M - to Main Menu')
    print('Q - to Quit the system')
    s = input('Please select your option : ')
    s = s.upper()
    return s

def selectdate(s):
    ans = input(' Would you like to select time?? please enter Y / N (default date is today) : ').upper()
    if ans=='Y':
        date = input(' please input the date(format must like this \'2018-5-30\') : ')
        # check date
        datel = date.split('-')
        comdate = ''
        for i in datel:
            comdate += i
        try:
            comdate = int(comdate)
        except:
            print('=== Invalidinput == = ')
            date = input('please input the date(format must like this \'2018-5-30\') : ')
        # select ferryId
        for t in timetable:
            print t,
        print
        ferryId = int(input(' please select the timetable (select the number: 1, 2, 3 so on..) : '))
        dateFerry[date] = (([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []))
        if s=='B':
            if len(dateFerry[date][ferryId - 1][0]) < 10:

                dateFerry[date][ferryId - 1][0].append(1)

                return 'success'

            else:

                print ('This ferry 00 % d is full now!' % ferryId)

                return 'fail'
        elif s=='E':
            if len(dateFerry[date][ferryId - 1][1]) < 40:

                dateFerry[date][ferryId - 1][1].append(1)

                return 'success'

            else:

                print ('This ferry 00%d is full now!' % ferryId)
                return 'fail'
    else:
        return 'fail'

# Submenu purchase ticket
def purchase(Ferry, BussinessList, EconomyList):
    print('PURCHASING MODULE')
    print('B – to purchase ticket for Business class')
    print('E – to purchase ticket for Economy class')
    print('M – to return to Main Menu')
    s = input('Please select your option : ')
    s = s.upper()
    # select date
    r = selectdate(s)
    if r=='success':
        s = consequ()


        if s == 'M':
            return 'continue'
        elif s == 'Q':
            print('You have already exited this system!')
            exit()
    else:

        # default date is now
        # Assigning Seats
        # Busseness
        if s == 'B':
            name = input("Please enter your name : ")
            try:
                ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
            except:
                print('=== Invalid input ===')
                ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

            if ferryId == '' or ferryId == None:
                try:
                    ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
                except:
                    print('=== Invalid input ===')
                    ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))


            if len(Ferry[ferryId - 1][0]) < 10:

                Ferry[ferryId - 1][0].append(1)

                personDetails = PersonDetails(name, 'bussiness', ferryId)

                BussinessList.append(personDetails)
            else:

                print ('This ferry 00%d is full now!' % ferryId)
                return 'continue'

            s = consequ()

            if s == 'M':
                return 'continue'
            elif s == 'Q':
                print('You have already exited this system!')
                exit()

        # Economy
        elif s == 'E':

            name = input("Please enter your name : ")

            try:
                ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
            except:
                print('=== Invalid input ===')
                ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

            if ferryId == '' or ferryId == None:

                try:
                    ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
                except:
                    print('=== Invalid input ===')
                    ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

            if len(Ferry[ferryId - 1][1]) < 40:

                Ferry[ferryId - 1][1].append(1)

                personDetails = PersonDetails(name, 'economy', ferryId)

                EconomyList.append(personDetails)

            else:

                print ('This ferry 00%d is full now!' % ferryId)
                return 'continue'

            s = consequ()

            if s == 'M':
                return 'continue'
            elif s == 'Q':
                print('You have already exited this system!')
                exit()


# Submenu View Seating Arrangement
def view(Ferry, BussinessList, EconomyList):
    print('SEATING ARRANGEMENT MODULE')
    print('F - to select Ferry ID ')
    print('T - to select Trip Time')
    print('M - to Main Menu')
    s = input('Please select your choice : ')
    s = s.upper()
    if s == 'F':
        try:

            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
            date = datetime.datetime.now().strftime('%Y-%m-%d')

        except:

            print('=== Invalid input ===')
            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

    elif s == 'M':
        return 'continue'

    elif s == 'T':
        try:

            print 'the date list : ',
            for k in dateFerry:
                print k,
            print
            date = input('please input the date you want to select (the format must be the same as given) : ')

            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

        except:

            print('=== Invalid input ===')
            return

    else:
        print('=== Invalid input ===')
        s = input('Please select your choice : ')
        return


    print ('********************************************************************')
    print ('*         Ferry ID : 00%d           Date : %s                *' % (ferryId, date))
    print ('********************************************************************')
    print ('*         Bussiness CLASS                                          *')
    # Algorithm 1 : bussiness seat
    if s=='T':
        busnum = len(dateFerry[date][ferryId - 1][0])
    else:
        busnum = len(Ferry[ferryId - 1][0])

    if busnum <= 10:
        for i in range(1, busnum + 1):
            printList.append(1)
        cha = 10 - busnum
        for i in range(1, cha + 1):
            printList.append(0)

    print '* ',
    for i in range(10):
        if i == 5:
            print
            print '* ',
        print printList[i], ' * ',
    print

    del printList[:]

    print ('*         Economy CLASS                                            *')

    # Algorithm 2 economy seat
    if s=='T':
        econum = len(dateFerry[date][ferryId - 1][1])
    else:
        econum = len(Ferry[ferryId - 1][1])

    if econum <= 40:
        for i in range(1, econum + 1):
            printList.append(1)
        cha = 40 - econum
        for i in range(1, cha + 1):
            printList.append(0)

    print '* ',
    for i in range(40):
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35:
            print
            print '* ',
        print printList[i], ' * ',
    print

    del printList[:]


# main function
if __name__ == '__main__':
    while (1):
        print ('FERRY TICKETING SYSTEM')
        print ('P – to Purchase Ticket')
        print ('V – to View Seating Arrangement')
        print ('Q – to Quit the system')
        s = input('Please select your option : ')
        s = s.upper()
        if s == 'P':
            purchase(Ferry, BussinessList, EconomyList)
        elif s == 'V':
            view(Ferry, BussinessList, EconomyList)
        elif s == 'Q':
            exit_sys()
            break
        else:
            print('=== Invalid input ===')
            s = input('Please select your option : ')
            s = s.upper()
            if s == 'P':
                purchase(Ferry, BussinessList, EconomyList)
            elif s == 'V':
                view(Ferry, BussinessList, EconomyList)
            elif s == 'Q':
                exit_sys()
                break
            else:
                pass
