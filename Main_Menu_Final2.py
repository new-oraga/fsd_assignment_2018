# -*- coding: UTF-8 -*-
import datetime
import time
import sys

from PersonDetails import PersonDetails

# Ferry[][0]-->bussiness
# Ferry[][1]-->economy
dateFerryc = {}
dateFerry1 = {}
dateFerry2 = {}
BusinessList = []
EconomyList = []
printList = []
timetable = ['1) 10:00 am', '2) 11:00 am', '3) 12:00 am', '4) 1:00 pm', '5) 2:00 pm', '6) 3:00 pm', '7) 4:00 pm',
             '8) 5:00 pm']


# exit
def exit_sys():
    print
    print ' ' * 10, 'You have already exited this system!'
    print
    sys.exit()


##CORE FUNCTIONS##
# list append function
def addition(s, dateFerry, date, ferryId, name, number, trip):
    if s == 'B':
        if len(dateFerry[date][ferryId - 1][0]) < 10:

            # judgement
            nnow = len(dateFerry[date][ferryId - 1][0])
            if number > 10:
                print ' ' * 10, '* Please buy the tickets no more than 10 '
                return
            if (nnow + number) > 10 and number <= 10:
                print ' ' * 10, '* The seat is full now, please buy tickets no more than %d ' % (10 - nnow)
                print ' ' * 10,
                number = raw_input('* Please input the number of tickets you want to buy : ')
                print
            try:
                number = int(number)
            except:
                print ' ' * 10, '=== Invalid input === '
                print
                time.sleep(1.0)
                return

            for n in range(number):
                dateFerry[date][ferryId - 1][0].append(1)

            if trip == 1:
                tripdest = 'From Penang to Langkawi'
            elif trip == 2:
                tripdest = 'From Langkawi to Penang'

            p = PersonDetails(name, 'Bussiness', ferryId, date, number, tripdest)

            flag = 0
            for k in BusinessList:
                if k.name == name and k.type == 'Bussiness' and k.ferryId == ferryId and k.date == date:
                    k.number = k.number + number
                    flag = 1
            if flag == 0:
                BusinessList.append(p)
            return 'success'
        else:
            print
            print ' ' * 10, ('**This ferry 00%d is full now! Please try purchasing on a different date, time or a different seat class.**' % ferryId)
            time.sleep(4.0)
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

            if trip == 1:
                tripdest = 'From Penang to Langkawi'
            elif trip == 2:
                tripdest = 'From Langkawi to Penang'

            p = PersonDetails(name, 'Ecomomy', ferryId, date, number, tripdest)
            flag = 0
            for k in EconomyList:
                if k.name == name and k.type == 'Ecomomy' and k.ferryId == ferryId and k.date == date:
                    k.number = k.number + number
                    flag = 1
            if flag == 0:
                EconomyList.append(p)
            return 'success'
        else:
            print
            print ' ' * 10, ('**This ferry 00%d is full now! Please try purchasing on a different date, time or a different seat class.**' % ferryId)
            time.sleep(4.0)
            return 'fail'


# select purchase date function
def selectdate(s):
    while(1):
        print ' ' * 10, '*',
        date = raw_input('Please input a date (e.g.: \'YYYY-MM-DD\') : ')
        print
        # check date
        datel = date.split('-')
        comdate = ''
        for i in datel:
            comdate += i
        try:
            comdate = int(comdate)
            break
        except:
            print ' ' * 10, '=== Invalid Input, please try again === '
            print
            time.sleep(1.0)
            continue
    # select trip
    while (1):
        print ' ' * 10,     '************************************************************'
        print ' ' * 10, '*', '1) From Penang to Langkawi.  2) From Langkawi to Penang.', '*'
        print ' ' * 10,     '************************************************************'
        print ' ' * 10, '*',
        trip = raw_input(' Please select the trip destination (e.g. \'1 or 2\'): ')
        try:
            trip = int(trip)
            if trip < 1 or trip > 2:
                raise ValueError
            else:
                break
        except ValueError:
            print
            print ' ' * 10, '=== Invalid Input, please try again === '
            print
            time.sleep(1.0)
            continue
    print
    # select ferryId
    while (1):
        ptimetable()
        print ' ' * 10, '*',
        try:
            ferryId = raw_input(' Please select a time (e.g. \'1, 2, 3\') : ')
            ferryId = int(ferryId)
            if ferryId > 8 or ferryId < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print
            print ' ' * 10, '=== Invalid Input, please try again === '
            print
            time.sleep(1.0)
            continue
    print
    while (1):
        try:
            print ' ' * 10, '*',
            name = raw_input(' Please input your name : ')
            if name.isalpha():
                break
            else:
                raise ValueError
        except ValueError:
            print
            print ' ' * 10, '=== Invalid Input, please try again === '
            print
            time.sleep(1.0)
            continue
    print
    while (1):
        try:
            if s == 'B':
                print ' ' * 10, '*',
                number = raw_input(' Please input the number of tickets you want to buy (Maximum amount is 10): ')
                number = int(number)
                if number > 10 or number < 1:
                    raise ValueError
                else:
                    break
            elif s == 'E':
                print ' ' * 10, '*',
                number = raw_input(' Please input the number of tickets you want to buy (Maximum amount is 40): ')
                number = int(number)
                if number > 40 or number < 1:
                    raise ValueError
                else:
                    break
        except ValueError:
            print
            print ' ' * 10, '=== Invalid Input, please try again === '
            print
            time.sleep(1.0)
            continue
    print
    while(1):
        pconfirmation(name, s, date, timetable, ferryId, number, trip)
        print ' ' * 10, '*',
        print 'Confirm purchase?'
        print ' ' * 10, '*',
        print 'Y = Yes', ' ' * 6, 'N = No'
        print ' ' * 10, '*',
        a = raw_input('Please select option Y or N: ')
        a = a.upper()
        if a == 'Y':
            # same date same ferry id addition problem // solved
            sdate = ''
            if trip==1:
                for k in dateFerry1:
                    if date == k:
                        sdate = date
            elif trip==2:
                for k in dateFerry2:
                    if date == k:
                        sdate = date
            else:
                print ' ' * 10,'invalid input!'
                return
            dest = 0
            if trip == 2:
                dest = 1
            if sdate == date:
                if dest == 0:
                    add = addition(s, dateFerry1, date, ferryId, name, number, trip)
                    break
                elif dest == 1:
                    add = addition(s, dateFerry2, date, ferryId, name, number, trip)
                    break
            else:
                if dest == 0:
                    dateFerry1[date] = (([], []), ([], []), ([], []), ([], []), ([], []), ([], []),
                                        ([], []), ([], []))
                    add = addition(s, dateFerry1, date, ferryId, name, number, trip)
                    break
                elif dest == 1:
                    dateFerry2[date] = (([], []), ([], []), ([], []), ([], []), ([], []), ([], []),
                                        ([], []), ([], []))
                    add = addition(s, dateFerry2, date, ferryId, name, number, trip)
                    break
        elif a == 'N':
            purchase(BusinessList, EconomyList)
        else:
            print
            print ' ' * 10, '=== Invalid Input, please try again ==='
            print
            time.sleep(1.0)
            continue
    return add

# purchase confirmation function
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


# Submenu Purchase Ticket function
def purchase(BusinessList, EconomyList):
    print
    ppurchase()
    print ' ' * 10,
    s = raw_input('* Please select your option : ')
    print
    s = s.upper()
    # select date
    if s == 'B' or s == 'E':
        r = selectdate(s)
        if r == 'success':
            while (1):
                print
                s = consequ()
                if s == 'M':
                    return 'continue'
                elif s == 'Q':
                    exit_sys()
                    break
                else:
                    print ' ' * 10, '=== Invalid Input, please try again ==='
                    print
                    time.sleep(1.0)
                    continue
        if r == 'fail':
            purchase(BusinessList, EconomyList)
    elif s == 'M':
        return 'continue'
    else:
        print ' ' * 10, '=== Invalid Input, please try again ==='
        time.sleep(1.0)
        purchase(BusinessList, EconomyList)


# Submenu View Seating Arrangement function
def view(BusinessList, EconomyList):
    print
    pview()
    print ' ' * 10,
    s = raw_input('Please select your choice : ')
    print
    s = s.upper()

    if s == 'M':
        return 'continue'

    elif s == 'T':
        while (1):
            print ' ' * 10,     '************************************************************'
            print ' ' * 10, '*', '1) From Penang to Langkawi.  2) From Langkawi to Penang.', '*'
            print ' ' * 10,     '************************************************************'
            print ' ' * 10, '*',
            trip = raw_input(' Please select the trip destination (e.g. \'1 or 2\'): ')
            try:
                trip = int(trip)
                if trip < 1 or trip > 2:
                    raise ValueError
                else:
                    break
            except ValueError:
                print
                print ' ' * 10, '=== Invalid Input, please try again === '
                print
                time.sleep(1.0)
                continue

        if trip == 1:
            dateFerryc = dateFerry1
            tripdest = 'From Penang to Langkawi'
        elif trip == 2:
            dateFerryc = dateFerry2
            tripdest = 'From Langkawi to Penang'
        else:
            print ' ' * 10,'invalid input! '
            return

        try:
            if dateFerryc == {}:
                raise KeyError
        except KeyError:
            print
            print ' ' * 10, '*',
            print 'No purchases have been made yet, will return to main menu in 3 seconds.'
            print
            time.sleep(3.0)
            return 'continue'

        while (1):
            print
            print  ' ' * 10, '*' * 108
            print ' ' * 10, '* The Date List : ',
            for k in dateFerryc:
                print '*', k
            print  ' ' * 10, '*' * 108
            print ' ' * 10, '*',
            date = raw_input(' Please input the date (e.g. \'YYYY-MM-DD\') : ')
            datel = date.split('-')
            comdate = ''
            for i in datel:
                comdate += i
            try:
                comdate = int(comdate)
                if date not in dateFerryc:
                    print
                    print ' ' * 10, '=== Invalid Input, please select a date from the date list === '
                    time.sleep(1.0)
                    continue
                else:
                    break
            except:
                print
                print ' ' * 10, '=== Invalid Input, please try again === '
                time.sleep(1.0)
                continue

        while (1):
            print
            ptimetable()
            print ' ' * 10, '*',
            try:
                ferryId = raw_input(' Please select a time (e.g. \'1, 2, 3\') : ')
                ferryId = int(ferryId)
                if ferryId > 8 or ferryId < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print
                print ' ' * 10, '=== Invalid Input, please try again === '
                print
                time.sleep(1.0)
                continue

    else:
        print ' ' * 10, '=== Invalid input, please try again ==='
        print
        time.sleep(1.0)
        view(BusinessList, EconomyList)

    # print
    print
    print ' ' * 10,
    print ('*******************************')
    print ' ' * 10,
    print ('*   %s   *') % (tripdest)
    print ' ' * 10,
    print ('*      Ferry ID : 00%d         *' % (ferryId))
    print ' ' * 10,
    print ('*      Date : %s               *' % (date))
    print ' ' * 10,
    print ('*******************************')
    print ' ' * 10,
    print ('*        Bussiness CLASS      *')
    # Algorithm 1 : bussiness seat
    if s == 'T':
        busnum = len(dateFerryc[date][ferryId - 1][0])

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
    print ('*        Economy CLASS        *')

    # Algorithm 2 economy seat
    if s == 'T':
        econum = len(dateFerryc[date][ferryId - 1][1])

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

    del printList[:]

    print  ' ' * 10, '*' * 31
    print
    print  ' ' * 10, '* ', 'M - Go back to main menu'
    print  ' ' * 10, '* ', 'Q - Quit system'
    print
    print  ' ' * 10, '*' * 31
    print  ' ' * 10, '* ',
    while (1):
        s = raw_input('Please select option: ')
        s = s.upper()
        if s == 'M':
            # return 'continue'
            return
        elif s == 'Q':
            exit_sys()
        else:
            print ' ' * 10, '=== Invalid Input, please try again ==='
            print
            print ' ' * 10, '* ',
            continue

    dateFerryc.clear()


#####################################################################################################################
##PRINT FUNCTIONS##
# print main menu trapezium
def ptrapezium():
    l = [1, 3, 5]
    for i in l:
        print ' ' * 25, '*' * i
        time.sleep(0.1)
    l1 = [2, 2]
    for i in l1:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), '*' * i
        time.sleep(0.1)
    l3 = [10, 12, 14]
    for i in l3:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), '*' * i
        time.sleep(0.1)
    l4 = [38, 36, 34, 32]
    for i in l4:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), '*' * i
        time.sleep(0.1)
    print
    print ' ' * 3,
    print('=Welcome to Local Malaysian Ferry Admiral Operations=')
    print
    time.sleep(1.0)


# print main menu
def pmain():
    print  ' ' * 10, '*' * 37
    print  ' ' * 10, '* LMFAO FERRY TICKETING SYSTEM      *'
    print  ' ' * 10, '*' * 37
    print  ' ' * 10, '* P = to Purchase Ticket            *'
    print  ' ' * 10, '* V = to View Seating Arrangement   *'
    print  ' ' * 10, '* Q = to Quit the system            *'
    print  ' ' * 10, '*' * 37


# print purchase module
def ppurchase():
    print
    print  ' ' * 10, '*' * 47
    print ' ' * 10, '* PURCHASING MODULE                           *'
    print  ' ' * 10, '*' * 47
    print ' ' * 10, '* B = to purchase ticket for Business class   *'
    print ' ' * 10, '* E = to purchase ticket for Economy class    *'
    print ' ' * 10, '* M = to return to Main Menu                  *'
    print  ' ' * 10, '*' * 47

# print purchase confirmation
def pconfirmation(name, s, date, timetable, ferryId, number, trip):
    print ' ' * 10, '*' * 48
    print ' ' * 10, '*', 'PURCHASE DETAILS', ' ' * 27
    print ' ' * 10, '*' * 48
    print ' ' * 10, '*', 'Name: ', name
    if trip==1:
        t = 'From Penang to Langkawi'
        pass
    else:
        t= 'From Langkawi to Penang'
    print ' ' * 10, '*', 'Trip destination: ', t
    print ' ' * 10, '*', 'SeatType: ', s, 'Class'
    print ' ' * 10, '*', 'Date: ', date
    print ' ' * 10, '*', 'Ferry Time: ', timetable[ferryId - 1]
    print ' ' * 10, '*', 'Number of ticket(s): ', number
    print ' ' * 10, '*' * 48

# print view seat module
def pview():
    print  ' ' * 10, '*' * 30
    print ' ' * 10, '* SEATING ARRANGEMENT MODULE *'
    print ' ' * 10, '* T = to select Trip Date    *'
    print ' ' * 10, '* M = to Main Menu           *'
    print  ' ' * 10, '*' * 30


# print timetable
def ptimetable():
    print  ' ' * 10, '*' * 108
    print ' ' * 10,
    for t in timetable:
        print '*', t,
    print '*'
    print  ' ' * 10, '*' * 108


# print all person details (admin)
def pAllpersondetails(s, BusinessList, EconomyList):
    print
    print  ' ' * 10, '*' * 48
    # if s == 'B':
    for b in BusinessList:
        print  ' ' * 10, '* ', 'Name: ', b.name
        print  ' ' * 10, '* ', 'Trip Destination: ', b.tripdest
        print  ' ' * 10, '* ', 'SeatType: ', b.type
        print  ' ' * 10, '* ', 'FerryId: ', b.ferryId
        print  ' ' * 10, '* ', 'Date: ', b.date
        print  ' ' * 10, '* ', 'Number of ticket(s): ', b.number
        print ' ' * 10, '*' * 48
    # elif s == 'E':
    for e in EconomyList:
        print  ' ' * 10, '* ', 'Name: ', e.name
        print  ' ' * 10, '* ', 'Trip Destination: ', e.tripdest
        print  ' ' * 10, '* ', 'SeatType: ', e.type
        print  ' ' * 10, '* ', 'FerryId: ', e.ferryId
        print  ' ' * 10, '* ', 'Date: ', e.date
        print  ' ' * 10, '* ', 'Number of ticket(s): ', e.number
        print  ' ' * 10, '*' * 48
    print
    print  ' ' * 10, '* ', 'M - Go back to main menu'
    print  ' ' * 10, '* ', 'Q - Quit system'
    print  ' ' * 10, '* ',
    while (1):
        s = raw_input('Please select option: ')
        s = s.upper()
        if s == 'M':
            return 'continue'
        elif s == 'Q':
            exit_sys()
            break
        else:
            print ' ' * 10, '=== Invalid Input, please try again ==='
            print
            print ' ' * 10, '* ',
            continue


#####################################################################################################################
##MAIN FUNCTION##
if __name__ == '__main__':
    while (1):
        print
        ptrapezium()
        print
        pmain()
        print ' ' * 10,
        s = raw_input('* Please select your option : ')
        s = s.upper()
        if s == 'P':
            purchase(BusinessList, EconomyList)
        elif s == 'V':
            view(BusinessList, EconomyList)
        elif s == 'Q':
            exit_sys()
            break
        elif s == 'ADMIN':
            pAllpersondetails(s, BusinessList, EconomyList)
        else:
            print
            print ' ' * 10, '=== Invalid Input, please try again ==='
            print
            time.sleep(1.0)
            continue

############################################END######################################################################
