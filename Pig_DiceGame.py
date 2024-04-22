import random

# 주사위를 굴립니다.
def roll_dice():
    return random.randint(1, 6)


# 플레이어를 설정합니다.
def player(name, total_score):
    turn_score = 0
    while True:
        roll = roll_dice()  # 수정된 부분
        print(f"{name} rolled: {roll}")

        # 만약 주사위 눈이 1일 경우 멈춥니다.
        if roll == 1:
            turn_score = 0
            break
        # 만약 주사위 눈이 2 ~ 6일 경우 스코어를 저장하고 턴을 계속합니다.
        else:
            turn_score += roll
            print(f"Turn score: {turn_score}")

        # 플레이어에게 턴을 계속 진행할건지, 멈출 것인지 물어봅니다.
        choice = input("턴을 계속 진행할거면 (1), 홀드할거면 (2)를 입력해주세요")
        if choice != '1':
            break

    return turn_score

# pig_game을 구현합니다.
def pig_game():
    # 목표 점수를 고릅니다.
    target_score = int(input("목표 점수를 입력하세요: "))

    player1_name = input("플레이어1의 이름을 입력하세요: ")
    player2_name = input("플레이어2의 이름을 입력하세요: ")
    player1_score = 0
    player2_score = 0

    while player1_score < target_score and player2_score < target_score:
        # 플레이어1턴일 때
        player1_score += player(player1_name, player1_score)
        print(f"{player1_name}의 점수는 {player1_score}입니다.")

        if player1_score >= target_score:
            print(f"{player1_name}이 우승하셨습니다!")
            break

        # 플레이어2턴일 때
        player2_score += player(player2_name, player2_score)
        print(f"{player2_name}의 점수는 {player2_score}입니다.")

        if player2_score >= target_score:
            print(f"{player2_name}이 우승하셨습니다!")
            break

pig_game()

