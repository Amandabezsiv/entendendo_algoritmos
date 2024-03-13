def quicksort(_list):
    if len(_list) < 2:
        return _list
    else:
        pivot = _list[0]
        greater = []
        lesser = []

        for i in _list[1:]:
            if i > pivot:                
                greater.append(i)
            else:
                lesser.append(i)
        return quicksort(lesser) + [pivot] + quicksort(greater)

#print(quicksort([5,4,3,2,1]))

def merge_sort(_list):
    if len(_list) <= 1:
        return _list

    middle = len(_list)//2
    left = _list[:middle]
    right = _list[middle:]

    left = merge_sort(left)
    print('left', left)
    right = merge_sort(right)
    print('right', right)
    
    return merge(left,right)

def merge(_list1,_list2):
    order =[]
    i = 0
    j = 0

    while i < len(_list1) and j < len(_list2):
            
        if _list1[i] < _list2[j]:
            order.append(_list1[i])
            print('imprimir se esquerdo for maior que direito',order)
            i += 1

        else:
            order.append(_list2[j])
            print('imprimir se direito for maior que esquerdo', order)            
            j += 1
    
    while i < len(_list1):
        order.append(_list1[i])
        print('adicionando oq restou da lista esquerda', order)
        i+= 1

    while j < len(_list2):
        order.append(_list2[j])
        print('adicionando oq restou da lista direita', order)
        j += 1
        
    return(order)
            
    

print(merge_sort([4,2,0,9, 20, 90, 66, 3, 8, 7]))
