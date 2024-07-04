import random

def game():
    win = 0
    lose = 0
    tie = 0

    while True:
        p = input("가위, 바위, 보 중 하나를 선택하세요: ")
        computer = random.choice(['가위', '바위', '보'])

        if p in ['가위', '바위', '보']:
            print(f"사용자: {p}, 컴퓨터: {computer}")

            if (p == '가위' and computer == '보') or (p == '바위' and computer == '가위') or (p == '보' and computer == '바위'):
                print("사용자 승리!")
                win += 1
            elif (p == '가위' and computer == '바위') or (p == '바위' and computer == '보') or (p == '보' and computer == '가위'):
                print("컴퓨터 승리!")
                lose += 1
            else:
                print("무승부!")
                tie += 1

            retry = input("다시 하시겠습니까? (y/n): ")
            if retry.lower() == 'n':
                print("게임을 종료합니다")
                print(f"승: {win} 패: {lose} 무승부: {tie}")
                break
            elif retry.lower() == 'y':
                continue   
        else:
            print("유효한 입력이 아닙니다")

game()
