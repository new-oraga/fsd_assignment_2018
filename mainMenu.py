# -*- coding: UTF-8 -*-
from PersonDetails import PersonDetails

# Ferry[][0]-->bussiness
# Ferry[][1]-->economy
Ferry = (([],[]),([],[]),([],[]),([],[]),([],[]),([],[]),([],[]),([],[]))
BussinessList=[]
EconomyList=[]
printList=[]

# exit
def exit_sys():
    print('You have already exited this system!')


# Submenu purchase ticket
def purchase(Ferry,BussinessList,EconomyList):
    print('PURCHASING MODULE')
    print('B – to purchase ticket for Business class')
    print('E – to purchase ticket for Economy class')
    print('M – to return to Main Menu')
    s = input('Please select your option : ')
    s = s.upper()
    # Assigning Seats
    # Busseness
    if s == 'B':
        name = input("Please enter your name : ")
        try:
            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
        except:
            print('=== Invalid input ===')
            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
            


        if ferryId=='' or ferryId==None:
            try:
                ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
            except:
                pass

        # a lot to do
        if len(Ferry[ferryId-1][0])<10:

            Ferry[ferryId-1][0].append(1)

            personDetails = PersonDetails(name,'bussiness',ferryId)

            BussinessList.append(personDetails)
        else:
            
            print ('This ferry 00%d is full now!' %ferryId)
            
            return 'continue'
        
        print ('Ticket is purchased. Have a nice day.')
        print ('=====================================')
        print('Do you still want to continue?')
        print('M - to Main Menu')
        print('Q - to Quit the system')
        s = input('Please select your option : ')
        s = s.upper()
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

        if ferryId=='' or ferryId==None:
            
            try:
                
                ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))
            except:
                
                pass

        # a lot to do
        if len(Ferry[ferryId - 1][1]) < 40:

            Ferry[ferryId - 1][1].append(1)

            personDetails = PersonDetails(name, 'economy', ferryId)

            EconomyList.append(personDetails)

        else:
            
            print ('This ferry 00%d is full now!' %ferryId)
            
            return 'continue'

        print ('Ticket is purchased. Have a nice day.')
        print ('=====================================')
        print('Do you still want to continue?')
        print('M - to Main Menu')
        print('Q - to Quit the system')
        s = input('Please select your option : ')
        s = s.upper()
        if s == 'M':
            return 'continue'
        elif s == 'Q':
            print('You have already exited this system!')
            exit()

##    # Return Main manu
##    elif s == 'M':
##        return 'continue'
##    else:
##        print('=== Invalid input ===')
##        return 'continue'

# Submenu View Seating Arrangement
def view(Ferry,BussinessList,EconomyList):
    print('SEATING ARRANGEMENT MODULE')
    print('F - to select Ferry ID ')
    print('T - to select Trip Time')
    print('M - to Main Menu')
    s = input('Please select your choice : ')
    s = s.upper()
    if s == 'F':
        try:

            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

        except:

            print('=== Invalid input ===')
            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

    elif s == 'M':
        return 'continue'

    else:
        print('=== Invalid input ===')
        s = input('Please select your choice : ')
        s = s.upper()
    if s == 'M':
        return 'continue'
    
    elif s == 'F':
        try:

            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

        except:

            print('=== Invalid input ===')
            ferryId = int(input("Please select your FerryId (range from 1 to 8) : "))

    else:
        return 'continue'



    # TIME problem remained
    print ('********************************************************************')
    print ('*         Ferry ID : 00%d           Date : 29 Apr 2018             *' %(ferryId))
    print ('********************************************************************')
    print ('*         Bussiness CLASS                                          *')
    # Algorithm 1 : bussiness seat
    busnum = len(Ferry[ferryId-1][0])

    if busnum<=10:
        for i in range(1,busnum+1):
            printList.append(1)
        cha = 10-busnum
        for i in range(1,cha+1):
            printList.append(0)
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (
    printList[0], printList[1], printList[2], printList[3], printList[4]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (
    printList[5], printList[6], printList[7], printList[8], printList[9]))
    
    del printList[:]

    print ('*         Economy CLASS                                            *')
    # Algorithm 2 economy seat
    econum = len(Ferry[ferryId - 1][1])

    if econum<=40:
        for i in range(1,econum+1):
            printList.append(1)
        cha = 40 - econum
        for i in range(1,cha+1):
            printList.append(0)
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *'%(printList[0],printList[1],printList[2],printList[3],printList[4]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (printList[5], printList[6], printList[7], printList[8], printList[9]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (printList[10], printList[11], printList[12], printList[13], printList[14]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (printList[15], printList[16], printList[17], printList[18], printList[19]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (printList[20], printList[21], printList[22], printList[23], printList[24]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (printList[25], printList[26], printList[27], printList[28], printList[29]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (printList[30], printList[31], printList[32], printList[33], printList[34]))
    print ('*  %d  *  %d  *  %d  *  %d  *  %d  *' % (printList[35], printList[36], printList[37], printList[38], printList[39]))

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
