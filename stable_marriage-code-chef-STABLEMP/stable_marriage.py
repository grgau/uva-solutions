from collections import defaultdict

input_matrix = int(input())

for  each_case in range(input_matrix):
    n = int(input())
    women = {}
    men = {}
    match = {}
    pri = {}
    
    for woman in range(1,n+1):
        women[woman] = list(map(int,input().split()))[1:]

    for man in range(1,n+1):
        men[man] = list(map(int,input().split()))[1:]
        pri[man] = 0

    while(len(match) < n):
        proposals = defaultdict(list)
        for man in range(1,n+1):
            if(man not in list(match.values())):
                proposals[men[man][pri[man]]].append(man)
                pri[man]+=1

        for woman in proposals:
            lists = [women[woman].index(man) for man in proposals[woman]]
            
            if(woman not in list(match.keys())):
                match[woman] = women[woman][min(lists)]
            
            else:
                match[woman] = women[woman][min(lists+[women[woman].index(match[woman])])]

    for woman,man in sorted(list(match.items()), key = lambda w_m:(w_m[1],w_m[0])):
        print(man,woman)