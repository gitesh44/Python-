a=(34,54,233,454,"GItesh")
a[5]="jak"
print(a)
# Output: 

# here we cannot change beacuse tuple is immutable.  
# we cannot add,remove,update the elements of tuple.
# we can only access the elements of tuple. 
# we can use count and index function in tuple.
# we can convert tuple into list and then we can perform all the operations of list.
b=list(a)
b[0]="Gitesh"   
print(b)
# Output: ['Gitesh', 54, 233, 454, 'GItesh']

