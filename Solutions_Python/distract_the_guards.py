from fractions import gcd

def loops(x, y):
    res = (x+y)/gcd(x,y)
    return bool(res & (res - 1))

def remove(guards, ref):
    for i in range(len(guards)):
        j = 0 
        while j < len(guards[i]):
            if(guards[i][j]==ref):
                guards[i].pop(j)
            j+=1 
    guards[ref]=[-1]

def solution(banana_list):
    guards= [[] for i in range(len(banana_list))]
    bad=0
    
    for i in range(len(guards)):
        for j in range(len(guards)):
            if(loops(banana_list[i], banana_list[j])):
                guards[i].append(j)

    to_process=len(banana_list)
    while(to_process>0):

        min_num=0
        for i in range(len(guards)):
            if(i!=0 and (len(guards[i])<len(guards[min_num]) or guards[min_num]
                == [-1]) and guards[i]!=[-1]):
                min_num=i

        if((len(guards[min_num])) == 0 or (len(guards[min_num])==1 and
                guards[min_num][0] == guards[min_num]) and guards[min_num] !=
                [-1]):
            remove(guards, min_num)
            to_process-=1
            bad+=1
        else:
            min_node=guards[min_num][0]
            for i in range(len(guards[min_num])):
                if(i!=0 and guards[min_num][i]!=min_num and len(guards[guards[min_num][i]])<len(guards[min_node])):
                    min_node=guards[min_num][i]
            if(guards[min_node]!=[-1]):
                remove(guards, min_num)
                remove(guards, min_node)
                to_process-=2

    return bad 