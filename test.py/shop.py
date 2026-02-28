
# --- 自由入力の割引キャンペーン ---
print("ーーー割引キャンペーン実施中!ーーー")
price = int(input("商品の単価を入力して下さい: ")) 
count = int(input("個数を入力して下さい: "))

total = price * count

# 2000円以上ならさらに割引
if total >= 2000:
    print("2000円以上なので 10% 割引します!")
    total = total * 0.9

print(f"キャンペーン適用後の合計金額は {int(total)} 円です。")