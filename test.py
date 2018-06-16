# -*- coding: UTF-8 -*-
from Person import Person
from PersonDetails import PersonDetails

# p1 = Person('aaaaa')
# p2 = Person('aaaaa')
# p3 = Person('aaaaa')
# p4 = Person('aaaaa')
#
#
#
# i = 1
# S = []
# if __name__ == '__main__':
#     while (1):
#         ss = raw_input(' do sth  :')
#         S.append(i)
#         i = 1+i
#         print S
#         if ss == '999':
#             print len(S)
#             print S
#             break

# for i in range(1,11):
#     print('0%d'%(i))
#
# print '\n\n'
#
# l = [1,1,1,1,1]
# del l[:]
# print l
# l.append(1)
# l.append(1)
# l.append(1)
# print(l)


# ferryid = FerryId('001')
# print ferryid.id
# person = Person('name','bussiness')
# print person.name,person.type

# print 'aaaaaaaa',
# print
# print 'aaaaaaaaaaa'
#
#
# l = [1,2,3]
# print len(l)+1
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC


CRED = '\033[91m'
CEND = '\033[0m'
print(CRED + "Error, does not compute!" + CEND)

#! /usr/bin/python                                                          
# -*- coding: utf-8
 
STYLE = {
        'fore': {
                'black': 30, 'red': 31, 'green': 32, 'yellow': 33,
                'blue': 34, 'purple': 35, 'cyan': 36, 'white': 37,
        },
        'back': {
                'black': 40, 'red': 41, 'green': 42, 'yellow': 43,
                'blue': 44, 'purple': 45, 'cyan': 46, 'white': 47,
        },
        'mode': {
                'bold': 1, 'underline': 4, 'blink': 5, 'invert': 7,
        },
        'default': {
                'end': 0,
        }
}
 
def use_style(string, mode='', fore='', back=''):
    mode = '%s' % STYLE['mode'][mode] if STYLE['mode'].has_key(mode) else ''
    fore = '%s' % STYLE['fore'][fore] if STYLE['fore'].has_key(fore) else ''
    back = '%s' % STYLE['back'][back] if STYLE['back'].has_key(back) else ''
    style = ';'.join([s for s in [mode, fore, back] if s])
    style = '\033[%sm' % style if style else ''
    end = '\033[%sm' % STYLE['default']['end'] if style else ''
    return '%s%s%s' % (style, string, end)
 
def test():
    print use_style('Normal')
    print use_style('Bold', mode='bold')
    print use_style('Underline & red text', mode='underline', fore='red')
    print use_style('Invert & green back', mode='reverse', back='green')
    print use_style('Black text & White back', fore='black', back='white')
 
if __name__ == '__main__':
    test()
