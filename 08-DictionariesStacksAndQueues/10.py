from re import A


arr=[
    {'country':'Poland', 'population': 39000000},
    {'country':'France', 'population': 12000000},
    {'country':'Spain', 'population': 18000000},
    {'country':'Italy', 'population': 21000000},
    {'country':'Norvay', 'population': 1000000},
]
i=0
while i<len(arr):
    for k,v in arr[i].items():
        print(v, end=" ")
    print()
    i+=1
