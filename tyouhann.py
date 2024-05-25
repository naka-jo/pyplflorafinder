#丁半博打
#プレイヤー4人
from audioop import reverse
import random
import copy

def game(point):
    #持ち点15点
    player_point = copy.copy(point)
    a_point = copy.copy(point)
    b_point = copy.copy(point)
    c_point = copy.copy(point)
    while player_point > 0 and a_point > 0 and b_point > 0 and c_point > 0:
        print("さあ、はった！はった！")
        print("(丁は偶数、半は奇数です。どちらを選びますか？)")
        you = input()
        cpu_choice = ["丁","半"]
        a_choice = random.choice(cpu_choice)
        b_choice = random.choice(cpu_choice)
        c_choice = random.choice(cpu_choice)
        print("あなたは"+you+"を選んだ！")
        print("aは"+a_choice+"を選んだ！")
        print("bは"+b_choice+"を選んだ！")
        print("cは"+c_choice+"を選んだ！")
        print("持ち点は"+str(player_point)+"点です。いくら賭けますか？")
        your_bet = int(input())
        a_bet = random.randint(1,a_point)
        b_bet = random.randint(1,b_point)
        c_bet = random.randint(1,c_point)
        print("あなたは"+str(your_bet)+"点賭けた")
        print("aは"+str(a_bet)+"点賭けた")
        print("bは"+str(b_bet)+"点賭けた")
        print("cは"+str(c_bet)+"点賭けた")
        dice_1 = random.randint(1,6)
        dice_2 = random.randint(1,6)
        sum_dice = dice_1 + dice_2
        if sum_dice % 2 == 0:
            print("はい、コマ揃いました。入りました！丁！")
            if you == "丁":
                player_point += your_bet
            else:
                player_point -= your_bet
            if a_choice == "丁":
                a_point += a_bet
            else:
                a_point -= a_bet
            if b_choice == "丁":
                b_point += b_bet
            else:
                b_point -= b_bet
            if c_choice == "丁":
                c_point += c_bet
            else:
                c_point -= c_bet
        if sum_dice % 2 == 1:
            print("はい、コマ揃いました。入りました！半！")
            if you == "半":
                player_point += your_bet
            else:
                player_point -= your_bet
            if a_choice == "半":
                a_point += a_bet
            else:
                a_point -= a_bet
            if b_choice == "半":
                b_point += b_bet
            else:
                b_point -= b_bet
            if c_choice == "半":
                c_point += c_bet
            else:
                c_point -= c_bet
        print("あなたの持ち点は"+str(player_point)+"です")
        print("aの持ち点は"+str(a_point)+"です")
        print("bの持ち点は"+str(b_point)+"です")
        print("cの持ち点は"+str(c_point)+"です")
    print("終了！")
    fin_result = {"あなた":player_point, "a":a_point, "b":b_point, "c":c_point}
    fin_result_2 = sorted(fin_result.items(), key = lambda x:x[1], reverse = True)
    print("1位は"+fin_result_2[0][0]+"です！おめでとう！")
    print("2位は"+fin_result_2[1][0]+"です！")
    print("3位は"+fin_result_2[2][0]+"です！")
    print("4位は"+fin_result_2[3][0]+"です。運が悪かったね。")