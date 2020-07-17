import random
HANGMAN = """
----+
    |
    O
   /|\\ 
   / \\ 
"""

def printHangman(lines,i):
    for line in lines[:i]:
        print(line)

def rand(start,end):
    num = int(random.random()*(end-start+1))+start
    return num


def main():
    newhang = HANGMAN.splitlines()
    newhang.pop(0)
    dead = []
    print(newhang)
    answer = rand(1,100)
    for n in range(1,6):
        #print(n,end='')
        guess = int(input(str(n)+ "번째 추측값 : "))
        if guess == answer:
            print("정답입니다 정답:",answer)
            print("You save the man")
            break
        elif guess > answer:
            print(guess,"보다는 작습니다")
        elif guess < answer:
            print(guess,'보다는 큽니다')
        printHangman(newhang,n)
        #내가만든 행맨그리기
        # dead.append(newhang[n])
        # for _ in range(len(dead)):
        #     print(dead[_])
        
        if n == 5:
            print("죽었습니다")
            print("정답은",answer,"입니다")

main()