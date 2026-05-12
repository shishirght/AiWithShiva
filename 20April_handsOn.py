import numpy as np;
# list0 = np.array([10,20,30,40]);
# list1 = np.arange(6);
# list2 = list1.reshape(2,3)
# print(list2);
#list1 = np.arange(6);
list1=np.array([1,2]);
list2=np.array([3,4]);
print(np.vstack((list1,list2)))

list4 = np.arange(6);
print(np.split(list4 ,2))
print(np.split(list4 ,3))
print(np.split(list4 ,4)) // err: ValueError: array split does not result in an equal division