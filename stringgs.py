# def func(str):
# 	max=[str[0],str.count(str[0])]
# 	for i in str:
# 		if str.count(i)>max[1]:
# 			max[0]=i 
# 			max[1]=str.count(i)
# 	return(max)		 
# str="Darshan"
# print(func(str))

# to get unique values from list
def unique(list1):
    unique_list = []

    for x in list1:
        if x not in unique_list:
            unique_list.append(x)

def func(str):
    listt = list(str)
    print(listt)

func("darshan")    