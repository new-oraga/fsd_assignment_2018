# -*- coding: UTF-8 -*-
import datetime
import time

from PersonDetails import PersonDetails

# Ferry[][0]-->bussiness
# Ferry[][1]-->economy
dateFerry = {}
BussinessList = []
EconomyList = []
printList = []
timetable = ['* 1) 10:00 am', '2) 11:00 am', '3) 12:00 am', '4) 1:00 pm', '5) 2:00 pm', '6) 3:00 pm', '7) 4:00 pm',
             '8) 5:00 pm']


# exit
def exit_sys():
    print ' ' * 10, 'You have already exited this system!'


def consequ():
    print  ' ' * 10, '*' * 40
    print  ' ' * 10, '* Ticket is purchased. Have a nice day *'
    print  ' ' * 10, '* ==================================== *'
    print ' ' * 10, '* Do you still want to continue?       *'
    print ' ' * 10, '* M - to Main Menu                     *'
    print ' ' * 10, '* Q - to Quit the system               *'
    print  ' ' * 10, '*' * 40
    print ' ' * 10,
    s = raw_input('Please select your option : ')
    print
    s = s.upper()
    return s


def addition(s, dateFerry, date, ferryId, name, number):
    if s == 'B':
        if len(dateFerry[date][ferryId - 1][0]) < 10:

            # judgement
            nnow = len(dateFerry[date][ferryId - 1][0])
            if number > 10:
                print ' ' * 10, '* please buy the tickets no more than 10 '
                return
            if (nnow + number) > 10 and number <= 10:
                print ' ' * 10, '* the seat is full now, please buy tickets no more than %d ' % (10 - nnow)
                print ' ' * 10,
                number = raw_input('* please input the number of tickets you want to buy : ')
                print
            try:
                number = int(number)
            except:
                print ' ' * 10, '=== Invalid input === '
                print
                return

            for n in range(number):
                dateFerry[date][ferryId - 1][0].append(1)

            p = PersonDetails(name, 'Bussiness', ferryId, date, number)

            flag = 0
            for k in BussinessList:
                if k.name == name and k.type == 'Bussiness' and k.ferryId == ferryId and k.date == date:
                    k.number = k.number + number
                    flag = 1
            if flag == 0:
                BussinessList.append(p)

            return 'success'

        else:

            print ' ' * 10, ('This ferry 00%d is full now!' % ferryId)

            return 'fail'
    elif s == 'E':
        if len(dateFerry[date][ferryId - 1][1]) < 40:

            # judgement
            nnow = len(dateFerry[date][ferryId - 1][1])
            if number > 40:
                print ' ' * 10, '* please buy the tickets no more than 40 '
                return
            if (nnow + number) > 40 and number <= 40:
                print ' ' * 10, '* the seat is full now, please buy tickets no more than %d ' % (40 - nnow)
                print ' ' * 10,
                number = raw_input('* please input the number of tickets you want to buy : ')
                print

            try:
                number = int(number)
            except:
                print ' ' * 10, '=== Invalid input === '
                print
                return

            for i in range(number):
                dateFerry[date][ferryId - 1][1].append(1)

            p = PersonDetails(name, 'Ecomomy', ferryId, date, number)

            flag = 0
            for k in EconomyList:
                if k.name == name and k.type == 'Ecomomy' and k.ferryId == ferryId and k.date == date:
                    k.number = k.number + number
                    flag = 1
            if flag == 0:
                EconomyList.append(p)

            return 'success'

        else:

            print ' ' * 10, 'This ferry 00%d is full now!' % ferryId
            return 'fail'


def selectdate(s):
    print ' ' * 10,
    date = raw_input('please input the date (format must like this \'2018-5-30\') : ')
    print
    # check date
    datel = date.split('-')
    comdate = ''
    for i in datel:
        comdate += i
    try:
        comdate = int(comdate)
    except:
        print ' ' * 10, '=== Invalid input === '
        print
        print ' ' * 10,
        date = raw_input(' Please input the date (format must like this : \'2018-5-30\') : ')
        print
    # select ferryId
    ptimetable()
    print ' ' * 10,
    ferryId = int(raw_input(' please select the timetable (select the number: 1, 2, 3 so on..) : '))
    print
    print ' ' * 10,
    name = raw_input(' please input your name : ')
    print
    print ' ' * 10,
    number = raw_input(' please input the number of tickets you want to buy : ')
    print
    try:
        number = int(number)
    except:
        print ' ' * 10, '=== Invalid input === '
        print
        return

    # same date same ferry id addition problem // solved
    sdate = ''
    for k in dateFerry:
        if date == k:
            sdate = date
    if sdate == date:
        r = addition(s, dateFerry, date, ferryId, name, number)
        return r
    else:
        dateFerry[date] = (([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []))
        r = addition(s, dateFerry, date, ferryId, name, number)
        return r


# Submenu purchase ticket
def purchase(BussinessList, EconomyList):
    ppurchase()
    print ' ' * 10,
    s = raw_input('Please select your option : ')
    print
    s = s.upper()
    # select date
    if s == 'B' or s == 'E':
        r = selectdate(s)
        if r == 'success':
            # print all person details
            pAllpersondetails(s, BussinessList, EconomyList)
            s = consequ()
            if s == 'M':
                return 'continue'
            elif s == 'Q':
                print(' ' * 10, 'You have already exited this system!')
                exit()
            else:
                print ' ' * 10, '=== Invalid input ==='
                print
                return
    elif s == 'M':
        return 'continue'
    else:
        print ' ' * 10, '=== Invalid input ==='
        print
        return


# Submenu View Seating Arrangement
def view(BussinessList, EconomyList):
    pview()
    print ' ' * 10,
    s = raw_input('Please select your choice : ')
    print
    s = s.upper()

    if s == 'M':
        return 'continue'

    elif s == 'T':
        try:
            print  ' ' * 10, '*' * 108
            print ' ' * 10, '* the date list : ',
            for k in dateFerry:
                print '*', k,
            print
            print  ' ' * 10, '*' * 108
            print ' ' * 10, '*',
            date = raw_input(' Please input the date you want to select (the format must be the same as given) : ')
            print

            print ' ' * 10,
            ferryId = int(raw_input("Please select your FerryId (range from 1 to 8) : "))
            print

        except:

            print ' ' * 10, '=== Invalid input ==='
            print
            return

    else:
        print ' ' * 10, '=== Invalid input ==='
        print
        return

    # print
    print ' ' * 10,
    print ('********************************************************************')
    print ' ' * 10,
    print ('*         Ferry ID : 00%d           Date : %s                *' % (ferryId, date))
    print ' ' * 10,
    print ('********************************************************************')
    print ' ' * 10,
    print ('*         Bussiness CLASS                                          *')
    # Algorithm 1 : bussiness seat
    if s == 'T':
        busnum = len(dateFerry[date][ferryId - 1][0])

    if busnum <= 10:
        for i in range(1, busnum + 1):
            printList.append(1)
        cha = 10 - busnum
        for i in range(1, cha + 1):
            printList.append(0)
    print ' ' * 10,
    print '* ',
    for i in range(10):
        if i == 5:
            print
            print ' ' * 10, '* ',
        print printList[i], ' * ',
    print

    del printList[:]

    print ' ' * 10,
    print ('*         Economy CLASS                                            *')

    # Algorithm 2 economy seat
    if s == 'T':
        econum = len(dateFerry[date][ferryId - 1][1])

    if econum <= 40:
        for i in range(1, econum + 1):
            printList.append(1)
        cha = 40 - econum
        for i in range(1, cha + 1):
            printList.append(0)

    print ' ' * 10,
    print '* ',
    for i in range(40):
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35:
            print
            print ' ' * 10, '* ',
        print printList[i], ' * ',
    print
    print

    del printList[:]


def pmian():
    print  ' ' * 10, '*' * 36
    print  ' ' * 10, '* FERRY TICKETING SYSTEM           *'
    print  ' ' * 10, '* P – to Purchase Ticket           *'
    print  ' ' * 10, '* V – to View Seating Arrangement  *'
    print  ' ' * 10, '* Q – to Quit the system           *'
    print  ' ' * 10, '* please select your option        *'
    print  ' ' * 10, '*' * 36


def ppurchase():
    print  ' ' * 10, '*' * 45
    print ' ' * 10, '* PURCHASING MODULE                         *'
    print ' ' * 10, '* B – to purchase ticket for Business class *'
    print ' ' * 10, '* E – to purchase ticket for Economy class  *'
    print ' ' * 10, '* M – to return to Main Menu                *'
    print  ' ' * 10, '*' * 45


def pview():
    print  ' ' * 10, '*' * 30
    print ' ' * 10, '* SEATING ARRANGEMENT MODULE *'
    print ' ' * 10, '* T - to select Trip Time    *'
    print ' ' * 10, '* M - to Main Menu           *'
    print  ' ' * 10, '*' * 30


def ptrapezium():
    l = [10, 12, 14]
    for i in l:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), '*' * i
        # time.sleep(0.3)
    l1 = [28, 26, 24, 22]
    for i in l1:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), '*' * i
        time.sleep(0.3)


def ptimetable():
    print  ' ' * 10, '*' * 108
    print ' ' * 10,
    for t in timetable:
        print t, '*',
    print
    print  ' ' * 10, '*' * 108
    print


def pAllpersondetails(s, BussinessList, EconomyList):
    print
    print  ' ' * 10, '*' * 52
    if s == 'B':
        for b in BussinessList:
            print  ' ' * 10, '* ', 'Name: ', b.name
            print  ' ' * 10, '* ', 'SeatType: ', b.type
            print  ' ' * 10, '* ', 'FerryId: ', b.ferryId
            print  ' ' * 10, '* ', 'Fate: ', b.date
            print  ' ' * 10, '* ', 'TicketsNumber: ', b.number
            print
    elif s == 'E':
        for e in EconomyList:
            print  ' ' * 10, '* ', 'Name: ', e.name
            print  ' ' * 10, '* ', 'SeatType: ', e.type
            print  ' ' * 10, '* ', 'FerryId: ', e.ferryId
            print  ' ' * 10, '* ', 'Fate: ', e.date
            print  ' ' * 10, '* ', 'TicketsNumber: ', e.number
            print
    print  ' ' * 10, '*' * 52
    print


# main function
if __name__ == '__main__':
    while (1):
        ptrapezium()
        print
        pmian()
        print ' ' * 10,
        s = raw_input('* Your option :      ')
        print
        s = s.upper()

        if s == 'P':
            purchase(BussinessList, EconomyList)
        elif s == 'V':
            view(BussinessList, EconomyList)
        elif s == 'Q':
            exit_sys()
            break
        else:
            print ' ' * 10, '=== Invalid raw_input ==='
            print ' ' * 10,
            s = raw_input('Please select your option : ')
            print
            s = s.upper()
            if s == 'P':
                purchase(BussinessList, EconomyList)
            elif s == 'V':
                view(BussinessList, EconomyList)
            elif s == 'Q':
                exit_sys()
                break
            else:
                pass
