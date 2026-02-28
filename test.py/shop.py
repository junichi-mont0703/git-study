# 商品データ
items_dict = {"1": "りんご", "2": "みかん", "3": "ぶどう"}
prices = {"りんご": 100, "みかん": 50, "ぶどう": 80}

print("----- いらっしゃいませ！ -----")
# .items()を使って、番号(num)と商品名(name)をセットで取り出して表示
for num, name in items_dict.items():
    print(f"{num}: {name} ({prices[name]}円)")

# ① strip()で空白対策、② 番号選択式
num_choice = input("商品番号を入力してください：").strip()

if num_choice in items_dict:
    choice = items_dict[num_choice]
    price = prices[choice]
    
    # int()で文字を計算可能な数字に変換
    count = int(input(f"{choice}は何個買いますか？：").strip())
    
    total = price * count
    
    if total >= 2000:
        print("2000円以上なので10%割引！")
        total *= 0.9

    # f-stringsでスッキリ表示
    print(f"{choice} {count}個で、合計金額は {int(total)} 円です。")
else:
    print("正しい番号を入力してください。")
