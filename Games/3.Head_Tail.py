# Give head or tail radomly
from random import random
from user_decision import get_user_decision

'''
    random give == [0,1)    ,eg: 0.23657895
    round(a,b) == round a upto b decimal palces
    # 0.2589631 * 1000 = 258.9631
    # rounding upto 0 decimal = 258
'''

def random_num():
        return round(random()*1000,0)

def decision(n):        # head when even else tail
        return 'HEAD' if n%2 == 0 else 'TAIL'
    
while True:
    num = random_num()
    print(f"------{decision(num)}------")

    if not get_user_decision("Do you want to toss again? (y/n): "):
        break

print("-----Program ended-----")