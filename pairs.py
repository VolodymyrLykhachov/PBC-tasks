sum=10
def find_pair (cur, *list_elem):
    for ele in list_elem:
        if ele+cur=sum:
            return (ele, cur)
def pair (*list_elem):
    for ele in list_elem:
        print(find_pair(ele,*list_elem))
pair([1,2,3,4,5,6,7,8,9])