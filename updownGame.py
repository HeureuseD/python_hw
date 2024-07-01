import random

# random_number = random.randint(1, 100)

num = int(input("숫자를 입력하세요: "))

def updown(num):
    random_number = random.randint(1, 100)

    while True:
        # num = int(input("숫자를 입력하세요: "))

        # count += 1

        if 0 < num <= 100:
            count = 0
            if random_number > num:
                count += 1
                print("업")
                num = int(input("숫자를 입력하세요: "))
            elif random_number < num:
                count += 1
                print("다운")
                num = int(input("숫자를 입력하세요: "))
            elif random_number == num:
                print("맞았습니다")
                print(f"시도한 횟수: {count}")
                count = 0
                break
                # retry = input("다시 하시겠습니까? (y/n): ")
                # if retry == 'y':
                #     # random_number = random.randint(1, 100)
                #     updown(num)
                #     count = 0
                # elif retry == 'n':
                #     print("게임을 종료합니다")
                #     break
                # else:
                #     print("y 또는 n을 입력하세요")
                #     retry = input("다시 하시겠습니까? (y/n): ")
        else:
            print("유효한 범위 내의 숫자를 입력하세요")
            num = int(input("숫자를 입력하세요: "))

updown(num)
retry = input("다시 하시겠습니까? (y/n): ")
while retry != 'n':
    if retry == 'y':
        # random_number = random.randint(1, 100)
        updown(num)
        retry = input("다시 하시겠습니까? (y/n): ")
        count = 0
    elif retry == 'n':
        print("게임을 종료합니다")
    else:
        print("y 또는 n을 입력하세요")
        retry = input("다시 하시겠습니까? (y/n): ")