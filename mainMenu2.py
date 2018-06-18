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
timetable = ['1) 10:00 am', '2) 11:00 am', '3) 12:00 am', '4) 1:00 pm', '5) 2:00 pm', '6) 3:00 pm', '7) 4:00 pm',
             '8) 5:00 pm']

# exit
def exit_sys():
    print ' ' * 10, 'You have already exited this system!'

#####################################################################################################################
##TRY AGAIN FUNCTIONS##
#select ferry Id/time try again function
# def selectfIdTA(ferryId):
#     while(1):
#         print ' ' * 10, '*',
#         try:
#             ferryId = raw_input(' Please select a time (e.g. \'1, 2, 3\') : ')
#             ferryId = int(ferryId)
#             if ferryId > 8 or ferryId < 1:
#                 raise ValueError
#             else:
#                 return (ferryId)
#                 break
#         except ValueError:
#             print ' ' * 10, '=== Invalid Input, please try again === '
#             print
#             continue

#select number of tickets try again function
# def selectnumticketTA(number):
#     while(1):
#         print ' ' * 10,
#         try:
#             number = raw_input(' Please input the number of tickets you want to buy : ')
#             number = int(number)
#             if number > 10 or number < 1:
#                 raise ValueError
#             else:
#                 return (number)
#                 break
#         except ValueError:
#             print ' ' * 10, '=== Invalid Input, please try again === '
#             print
#             continue

#confirmation to buy ticket try again function
# def confirmticketTA(s, date, ferryId, name, number):
#     while(1):
#         print ' ' * 10,
#         s = raw_input(' Confirm purchase? Y/N: ')
#         s = s.upper()
#         if s == 'Y':
#             # same date same ferry id addition problem // solved
#             sdate = ''
#             for k in dateFerry:
#                 if date == k:
#                     sdate = date
#                     continue
#                 else:
#                     pass
#             if sdate == date:
#                 r = addition(s, dateFerry, date, ferryId, name, number)
#                 break
#             else:
#                 dateFerry[date] = (([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []))
#                 r = addition(s, dateFerry, date, ferryId, name, number)
#                 break
#         elif s == 'N':
#             purchase(BussinessList, EconomyList)
#         else:
#             print ' ' * 10,'=== Invalid Input, please try again ==='
#             continue
#     return r

#main menu invalid input try again function
# def invinpTA():
#     while(1):
#         print
#         print ' ' * 10, '=== Invalid Input, please try again ==='
#         print ' ' * 10,
#         s = raw_input('Please select your option : ')
#         s = s.upper()
#         if s == 'P':
#             purchase(BussinessList, EconomyList)
#             break
#         elif s == 'V':
#             view(BussinessList, EconomyList)
#             break
#         elif s == 'Q':
#             exit_sys()
#             break
#         elif s == 'ADMIN':
#             pAllpersondetails(s, BussinessList, EconomyList)
#             break
#         else:
#             continue

#####################################################################################################################
##CORE FUNCTIONS##
#list append function
def addition(s, dateFerry, date, ferryId, name, number):
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

#select purchase date function
def selectdate(s):
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
    except:
        print ' ' * 10, '=== Invalid input === '
        print
        selectdate(s)
    # select ferryId
    ptimetable()
    while(1):
        print ' ' * 10, '*',
        try:
            ferryId = raw_input(' Please select a time (e.g. \'1, 2, 3\') : ')
            ferryId = int(ferryId)
            if ferryId > 8 or ferryId < 1:
                raise ValueError
            else:
                break
        except ValueError:
            print ' ' * 10, '=== Invalid Input, please try again === '
            print
            continue
    print
    print ' ' * 10, '*',
    name = raw_input(' Please input your name : ')
    print
    while(1):
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
            print ' ' * 10, '=== Invalid Input, please try again === '
            print
            continue
    print
    print ' ' * 10, '*' * 48
    print ' ' * 10, '*', 'Name: ', name, ' ' * 31, '*'
    print ' ' * 10, '*', 'SeatType: ', s, 'Class', ' ' * 25, '*'
    print ' ' * 10, '*', 'Date: ', date, ' ' * 26, '*'
    print ' ' * 10, '*', 'Ferry Time: ', timetable[ferryId - 1], ' ' * 19, '*'
    print ' ' * 10, '*', 'Number of ticket: ', number, ' ' * 23, '*'
    print ' ' * 10, '*' * 48
    print
    while(1):
        print ' ' * 10, '*',
        print 'Confirm purchase?'
        print ' ' * 10, '*',
        print 'Y = Yes', ' ' * 6, 'N = No'
        print ' ' * 10, '*',        
        a = raw_input('Please select input Y or N: ')
        a = a.upper()
        if a == 'Y':
            # same date same ferry id addition problem // solved
            sdate = ''
            for k in dateFerry:
                if date == k:
                    sdate = date
            if sdate == date:
                add = addition(s, dateFerry, date, ferryId, name, number)
                break
            else:
                dateFerry[date] = (([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []), ([], []))
                add = addition(s, dateFerry, date, ferryId, name, number)
                break
        elif a == 'N':
            purchase(BussinessList, EconomyList)
            break
        else:
            print ' ' * 10,'=== Invalid Input, please try again ==='
            continue
    return add

#purchase confirmation function
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

#Submenu Purchase Ticket function
def purchase(BussinessList, EconomyList):
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
            while(1):
                print
                s = consequ()
                if s == 'M':
                    return 'continue'
                elif s == 'Q':
                    print(' ' * 10, 'You have already exited this system!')
                    exit_sys()
                    break
                else:
                    print ' ' * 10, '=== Invalid input ==='
                    print
                    continue
    elif s == 'M':
        return 'continue'
    else:
        print ' ' * 10, '=== Invalid Input, please try again ==='
        time.sleep(0.5)
        purchase(BussinessList, EconomyList)


#Submenu View Seating Arrangement function
def view(BussinessList, EconomyList):
    print
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
            print ' ' * 10, '* The Date List : ',
            for k in dateFerry:
                print '*', k,
            print
            print  ' ' * 10, '*' * 108
            while(1):
                print ' ' * 10, '*',
                date = raw_input(' Please input the date (e.g. \'YYYY-MM-DD\') : ')
                datel = date.split('-')
                comdate = ''
                for i in datel:
                    comdate += i
                try:
                    comdate = int(comdate)
                    break
                except ValueError:
                    print ' ' * 10, '=== Invalid Input, please try again === '
                    print
                    continue
            try:
                if dateFerry == {}:
                    raise KeyError
            except KeyError:
                print
                print ' ' * 10, '*',
                print 'No purchases have been made yet, will return to main menu in 3 seconds.'
                time.sleep(3.0)
                return

            print
            ptimetable()
            print ' ' * 10,
            ferryId = int(raw_input(' Please select a time (e.g. \'1, 2, 3\') : '))
            print
            #print ' ' * 10,

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
    print ('********************************')
    print ' ' * 10,
    print ('*         Ferry ID : 00%d      *' % (ferryId))
    print ' ' * 10,
    print ('*         Date : %s            *' % (date))
    print ' ' * 10,

    print ('********************************')
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
    print  ' ' * 10, '*' * 52
    print
    print  ' ' * 10, '* ','M - Go back to main menu'
    print  ' ' * 10, '* ','Q - Quit system'
    print
    print  ' ' * 10, '*' * 52
    print  ' ' * 10, '* ',
    while(1):
        s=raw_input('Please select option: ')
        s=s.upper()
        if s == 'M':
            # return 'continue'
            del printList[:]
            break
        elif s == 'Q':
            del printList[:]
            exit_sys()
            break
        else:
            print ' ' * 10, '=== Invalid Input, please try again ==='
            print
            print ' ' * 10, '* ',
            continue

    # del printList[:]

#####################################################################################################################
##PRINT FUNCTIONS##
#print main menu trapezium
def ptrapezium():
    l = [10, 12, 14]
    for i in l:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), '*' * i
        time.sleep(0.3)
    l1 = [28, 26, 24, 22]
    for i in l1:
        print ' ' * 10, ' ' * (10 - (i - 10) / 2), '*' * i
        time.sleep(0.2)

#print main menu
def pmain():
    print  ' ' * 10, '*' * 37
    print  ' ' * 10, '* FERRY TICKETING SYSTEM            *'
    print  ' ' * 10, '* P – to Purchase Ticket          *'
    print  ' ' * 10, '* V – to View Seating Arrangement *'
    print  ' ' * 10, '* Q – to Quit the system          *'
    print  ' ' * 10, '* Please select your option         *'
    print  ' ' * 10, '*' * 37

#print purchase module
def ppurchase():
    print
    print  ' ' * 10, '*' * 47
    print ' ' * 10, '* PURCHASING MODULE                           *'
    print ' ' * 10, '* B – to purchase ticket for Business class *'
    print ' ' * 10, '* E – to purchase ticket for Economy class  *'
    print ' ' * 10, '* M – to return to Main Menu                *'
    print  ' ' * 10, '*' * 47

#print view seat module
def pview():
    print  ' ' * 10, '*' * 30
    print ' ' * 10, '* SEATING ARRANGEMENT MODULE *'
    print ' ' * 10, '* T - to select Trip Date    *'
    print ' ' * 10, '* M - to Main Menu           *'
    print  ' ' * 10, '*' * 30

#print timetable
def ptimetable():
    print  ' ' * 10, '*' * 108
    print ' ' * 10,
    for t in timetable:
        print '*', t,
    print '*'
    print
    print  ' ' * 10, '*' * 108
    print

#print all person details (admin)
def pAllpersondetails(s, BussinessList, EconomyList):
    print
    print  ' ' * 10, '*' * 52
    # if s == 'B':
    for b in BussinessList:
        print  ' ' * 10, '* ', 'Name: ', b.name, ' ' * 34, '*'
        print  ' ' * 10, '* ', 'SeatType: ' , b.type, ' ' * 26, '*'
        print  ' ' * 10, '* ', 'FerryId: ', b.ferryId, ' ' * 35, '*'
        print  ' ' * 10, '* ', 'Date: ', b.date, ' ' * 29, '*'
        print  ' ' * 10, '* ', 'TicketsNumber: ', b.number, ' ' * 28, '*'
        print ' ' * 10, '*' * 52
        print
    # elif s == 'E':
    for e in EconomyList:
        print  ' ' * 10, '* ', 'Name: ', e.name, ' ' * 34, '*'
        print  ' ' * 10, '* ', 'SeatType: ', e.type, ' ' * 26, '*'
        print  ' ' * 10, '* ', 'FerryId: ', e.ferryId, ' ' * 35, '*'
        print  ' ' * 10, '* ', 'Date: ', e.date, ' ' * 29, '*'
        print  ' ' * 10, '* ', 'TicketsNumber: ', e.number, ' ' * 28, '*'
        print
    print  ' ' * 10, '*' * 52
    print
    print  ' ' * 10, '* ','M - Go back to main menu'
    print  ' ' * 10, '* ','Q - Quit system'
    print  ' ' * 10, '* ',
    while(1):
        s=raw_input('Please select option: ')
        s=s.upper()
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
            purchase(BussinessList, EconomyList)
        elif s == 'V':
            view(BussinessList, EconomyList)
        elif s == 'Q':
            exit_sys()
            break
        elif s == 'ADMIN':
            pAllpersondetails(s, BussinessList, EconomyList)
        else:
            print
            print ' ' * 10, '=== Invalid Input, please try again ==='
            print
            continue

############################################END######################################################################