# 商品リストと価格
items = {"りんご": 100, "みかん": 50, "ぶどう": 80}

print("-----いらっしゃいませ！商品一覧-----")
for name, price in items.items():
    print(f"{name}: {price}円")

# 商品を選ぶ
choice = input("何を買いますか？（りんご、みかん、ぶどう）：").strip() # .strip()を入れると前後の余計な空白を消せます

if choice in items:
    # --- 商品があった場合の処理（ここからインデントを下げる） ---
    price = items[choice]
    count = int(input(f"{choice}は何個買いますか？："))
    
    total = price * count
    
    # 2000円以上なら割引
    if total >= 2000:
        print("2000円以上なので10%割引になります！")
        total = total * 0.9  # priceではなくtotalにかける
    
    print(f"合計金額は {int(total)} 円です。毎度あり！")
    # ----------------------------------------------------
else:
    # 商品リストに名前がなかった場合
    print("申し訳ありません、その商品は置いていません。")

