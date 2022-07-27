# '''pre-defined Function'''
# ...sorted()....    (new list containing all item form the iterable ascending order)
# a=[1,6,3,8,2]
# a.sort()
# print(a)            #[1, 2, 3, 6, 8]
# print(sorted([12,3,120,9]))       #[3, 9, 12, 120]
# print(sorted([12,3,4,56]))           #[3, 4, 12, 56]


# ....all()....
# print(all([True,1,2]))              ##True
# print(all([True,'',1,2]))          # False
# print(all([True,' ',1,2]))          #True
# print(all([True,False,1,2]))        #False
# print(all([True,True,1,2,0]))      # False
# print(all([True,True,1,2,None]))   # False

# ...any()...
# print(any([True,False,False,23]))    #True
# print(any([False,False,0]))          #False
# print(any([True,True,None,0]))       #True
  
# ...bool()...
# print(bool(False))   # False
# print(bool(1))       #True
# print(bool(0))       #False
# print(bool(None))     #False
# print(bool('bool'))   #True


# eval()
# print('eval=',eval('5+6.8-1'))
# a=eval('5+6-1')
# b=eval('4+3.8-1')  #eval= 10.8
# print(a,type(a))   #10 <class 'int'>
# print(b,type(b))   #6.8 <class 'float'>

# sum()
# print('sum=',sum([1,2,3,4,5]))      #sum= 15
# print('sum=',sum((10.5,20,30)))     #sum= 60.5

# reversed()-list
# for i in reversed([1,2,3,4,5]):        5
#     print(i)                           4
#                                        3
#                                        2
#                                        1

# reversed() -tuple
# for i in reversed((10,20,30,40)):      40
#     print(i)                           30
#                                        20
#                                        10

# enumerate()
# a=['bread','milk','python']
# b=enumerate(a)
# print(type(b))     <class 'enumerate'>
# print(dict(b))     {0: 'bread', 1: 'milk', 2: 'python'}
# print(list(b))      []
# print(tuple(b))     ()

# a=['bread','milk','python']
# c=enumerate(a,6)
# print(list(c))          # [(6, 'bread'), (7, 'milk'), (8, 'python')]





