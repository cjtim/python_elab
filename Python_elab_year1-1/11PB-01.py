	
#|         *         |9 1(
#|        ***        |8 3
#|       *****       |7 5
#|      *******      |6 7
#|     *********     |5 9
#|    ***********    |4 11
#|   *************   |3 13
#|  ***************  |2 15
#| ***************** |1 17
#|*******************|0 19
n = int(input())
star = 1
space = n-1
i = 0
while i < n:
    print('|',end='')
    print(' '*(space),end='')
    print('*'*((star*2)-1),end='')
    print(' '*(space),end='')
    print('|')
    i += 1
    star += 1
    space -= 1