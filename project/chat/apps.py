from django.apps import AppConfig
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

class ChatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat'

def draw_mat(M,N):
    endline = M/2
    rev=2
    odd_numbers = [num for num in range(1,101,2)]
    ary = []
    for i in range(1,M+1):
        scount = 1
        tcount = N-3/2
        sline = N/2
        if i <= endline: 
            pattern = '-'*(tcount)+('.|.'*odd_numbers[i])+'-'*(tcount)
        elif i == endline+1:
            pattern = '-'*(N-7)/2+('WELCOME')+'-'*(N-7)/2
        elif i > endline:
            cnt = 1
            pattern = ary[endline-1-cnt]
            cnt+=1

        print(pattern)
        ary.append(pattern)


    
    
  
# M = int(input())
# N= int(input())
# draw_mat(M,N)