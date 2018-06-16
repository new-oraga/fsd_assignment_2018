#-*- coding: UTF-8 -*-
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


class fontcolors:
    BULE = '\033[1;34m'
    PINK = '\033[95m'
    RED = '\033[1;31m'
    GREEN = '\033[1;32m'
    YELLOW = '\033[1;33m'
    YRED = '\033[1;35m'
    QGREEN = '\033[1;36m'
    ENDC = '\033[0m'


# exit
def exit_sys():
    print ' ' * 10, fontcolors.BULE + 'You have already exited this system!' + fontcolors.ENDC


def consequ():
    print  ' ' * 10, fontcolors.YELLOW + '*' * 40 + fontcolors.YELLOW
    print  ' ' * 10, fontcolors.YELLOW + '* Ticket is purchased. Have a nice day *' + fontcolors.YELLOW
    print  ' ' * 10, fontcolors.YELLOW + '* ==================================== *' + fontcolors.YELLOW
    print ' ' * 10, fontcolors.YELLOW + '* Do you still want to continue?       *' + fontcolors.YELLOW
    print ' ' * 10, fontcolors.YELLOW + '* M - to Main Menu                     *' + fontcolors.YELLOW
    print ' ' * 10, fontcolors.YELLOW + '* Q - to Quit the system               *' + fontcolors.YELLOW
    print  ' ' * 10, fontcolors.YELLOW + '*' * 40
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
                print ' ' * 10, fontcolors.PINK, '* please buy the tickets no more than 10 '
                print
                return
            if (nnow + number) > 10 and number <= 10:
                print ' ' * 10, fontcolors.PINK, '* the seat is full now, please buy tickets no more than %d ' % (
                            10 - nnow)
                print ' ' * 10, fontcolors.PINK,
                number = raw_input('* please input the number of tickets you want to buy : ')
                print
            try:
                number = int(number)
            except:
                print ' ' * 10, fontcolors.RED, '=== Invalid input === '
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

            print ' ' * 10, fontcolors.PINK, ('This ferry 00%d is full now!' % ferryId)

            return 'fail'
    elif s == 'E':
        if len(dateFerry[date][ferryId - 1][1]) < 40:

            # judgement
            nnow = len(dateFerry[date][ferryId - 1][1])
            if number > 40:
                print ' ' * 10, fontcolors.PINK, '* please buy the tickets no more than 40 '
                print
                return
            if (nnow + number) > 40 and number <= 40:
                print ' ' * 10, fontcolors.PINK, '* the seat is full now, please buy tickets no more than %d ' % (
                            40 - nnow)
                print ' ' * 10, fontcolors.PINK,
                number = raw_input('* please input the number of tickets you want to buy : ')
                print

            try:
                number = int(number)
            except:
                print ' ' * 10, fontcolors.RED, '=== Invalid input === '
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

            print ' ' * 10, fontcolors.PINK, 'This ferry 00%d is full now!' % ferryId
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
        print ' ' * 10, fontcolors.RED, '=== Invalid input === '
        print
        print ' ' * 10,
        date = raw_input(' Please input the date (format must like this : \'2018-5-30\') : ')
        print
    # select ferryId
    ptimetable()
    print ' ' * 10, fontcolors.PINK,
    ferryId = int(raw_input(' please select the timetable (select the number: 1, 2, 3 so on..) : '))
    print
    print ' ' * 10, fontcolors.PINK,
    name = raw_input(' please input your name : ')
    print
    print ' ' * 10, fontcolors.PINK,
    number = raw_input(' please input the number of tickets you want to buy : ')
    print
    try:
        number = int(number)
    except:
        print ' ' * 10, fontcolors.RED, '=== Invalid input === '
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
    print ' ' * 10, fontcolors.GREEN,
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
                print ' ' * 10, fontcolors.RED, '=== Invalid input ==='
                print
                return
    elif s == 'M':
        return 'continue'
    else:
        print ' ' * 10, fontcolors.RED, '=== Invalid input ==='
        print
        return


# Submenu View Seating Arrangement
def view(BussinessList, EconomyList):
    pview()
    print ' ' * 10, fontcolors.YELLOW,
    s = raw_input('Please select your choice : ')
    print
    s = s.upper()

    if s == 'M':
        return 'continue'

    elif s == 'T':
        try:
            print  ' ' * 10, '*' * 108
            print ' ' * 10, '* the date list : ',
            # print date list
            cout = 0
            for k in dateFerry:
                cout += 1
                if cout % 6 == 0:
                    print
                    print ' ' * 10,
                    print fontcolors.YELLOW + '*', fontcolors.YELLOW + k,
                else:
                    print fontcolors.YELLOW + '*', fontcolors.YELLOW + k,
            print
            print  ' ' * 10, '*' * 108
            print ' ' * 10, '*', fontcolors.YELLOW,
            date = raw_input(' Please input the date you want to select (the format must be the same as given) : ')
            print

            print ' ' * 10, fontcolors.YELLOW,
            ferryId = int(raw_input("Please select your FerryId (range from 1 to 8) : "))
            print

        except:

            print ' ' * 10, fontcolors.RED, '=== Invalid input ==='
            print
            return

    else:
        print ' ' * 10, fontcolors.RED, '=== Invalid input ==='
        print
        return

    # printing part
    print ' ' * 10, fontcolors.PINK,
    print ('********************************************************************')
    print ' ' * 10, fontcolors.PINK,
    print ('*         Ferry ID : 00%d           Date : %s                *' % (ferryId, date))
    print ' ' * 10, fontcolors.PINK,
    print ('********************************************************************')
    print ' ' * 10, fontcolors.PINK,
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
    print fontcolors.PINK, '* ',
    for i in range(10):
        if i == 5:
            print
            print ' ' * 10, fontcolors.PINK, '* ',
        print fontcolors.PINK, printList[i], fontcolors.PINK, ' * ',
    print

    del printList[:]

    print ' ' * 10, fontcolors.PINK,
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
    print fontcolors.PINK, '* ',
    for i in range(40):
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35:
            print
            print ' ' * 10, fontcolors.PINK, '* ',
        print fontcolors.PINK, printList[i], fontcolors.PINK, ' * ',
    print
    print

    del printList[:]


def pmian():
    print  ' ' * 10, fontcolors.GREEN + '*' * 36 + fontcolors.ENDC
    print  ' ' * 10, fontcolors.GREEN + '* FERRY TICKETING SYSTEM           *' + fontcolors.ENDC
    print  ' ' * 10, fontcolors.GREEN + '* P – to Purchase Ticket           *' + fontcolors.ENDC
    print  ' ' * 10, fontcolors.GREEN + '* V – to View Seating Arrangement  *' + fontcolors.ENDC
    print  ' ' * 10, fontcolors.GREEN + '* Q – to Quit the system           *' + fontcolors.ENDC
    print  ' ' * 10, fontcolors.GREEN + '* please select your option        *' + fontcolors.ENDC
    print  ' ' * 10, fontcolors.GREEN + '*' * 36 + fontcolors.ENDC


def ppurchase():
    print  ' ' * 10, fontcolors.GREEN + '*' * 45 + fontcolors.ENDC
    print ' ' * 10, fontcolors.GREEN + '* PURCHASING MODULE                         *' + fontcolors.ENDC
    print ' ' * 10, fontcolors.GREEN + '* B – to purchase ticket for Business class *' + fontcolors.ENDC
    print ' ' * 10, fontcolors.GREEN + '* E – to purchase ticket for Economy class  *' + fontcolors.ENDC
    print ' ' * 10, fontcolors.GREEN + '* M – to return to Main Menu                *' + fontcolors.ENDC
    print  ' ' * 10, fontcolors.GREEN + '*' * 45 + fontcolors.ENDC


def pview():
    print  ' ' * 10, fontcolors.YELLOW + '*' * 30 + fontcolors.ENDC
    print ' ' * 10, fontcolors.YELLOW + '* SEATING ARRANGEMENT MODULE *' + fontcolors.ENDC
    print ' ' * 10, fontcolors.YELLOW + '* T - to select Trip Time    *' + fontcolors.ENDC
    print ' ' * 10, fontcolors.YELLOW + '* M - to Main Menu           *' + fontcolors.ENDC
    print  ' ' * 10, fontcolors.YELLOW + '*' * 30 + fontcolors.ENDC


def ptrapezium():
    l = [10, 12, 14]
    for i in l:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), fontcolors.BULE + '*' * i + fontcolors.ENDC
        # time.sleep(0.3)
    l1 = [28, 26, 24, 22]
    for i in l1:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), fontcolors.BULE + '*' * i + fontcolors.ENDC
        time.sleep(0.3)


def ptimetable():
    print  ' ' * 10, fontcolors.PINK + '*' * 108 + fontcolors.ENDC
    print ' ' * 10,
    for t in timetable:
        print fontcolors.PINK + t, fontcolors.PINK + '*' + fontcolors.ENDC,
    print
    print  ' ' * 10, fontcolors.PINK + '*' * 108 + fontcolors.ENDC
    print


def pAllpersondetails(s, BussinessList, EconomyList):
    print
    print  ' ' * 10, fontcolors.PINK + '*' * 52 + fontcolors.ENDC
    if s == 'B':
        for b in BussinessList:
            print  ' ' * 10, fontcolors.PINK + '* ', 'Name: ', b.name + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'SeatType: ', b.type + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'FerryId: ', str(b.ferryId) + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'Fate: ', b.date + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'TicketsNumber: ', str(b.number) + fontcolors.ENDC
            print
    elif s == 'E':
        for e in EconomyList:
            print  ' ' * 10, fontcolors.PINK + '* ', 'Name: ', e.name + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'SeatType: ', e.type + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'FerryId: ', str(e.ferryId) + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'Fate: ', e.date + fontcolors.ENDC
            print  ' ' * 10, fontcolors.PINK + '* ', 'TicketsNumber: ', str(e.number) + fontcolors.ENDC
            print
    print  ' ' * 10, fontcolors.PINK + '*' * 52 + fontcolors.ENDC
    print


# main function
if __name__ == '__main__':
    while (1):
        ptrapezium()
        print
        pmian()
        print ' ' * 10, fontcolors.GREEN,
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
