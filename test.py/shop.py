import json
import os

#保村先のファイル名
FILE_NAME = "shop_data.json"


# --- 1. ロード機能（お店を開く準備） ---
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        save_data = json.load(f)
        items_dict = save_data["items"]
        prices = save_data["prices"]

else:
    # データがないときは初期値を用意する
    items_dict = {"1": "りんご", "2": "みかん", "3": "ぶどう"}
    prices = {"りんご": 100, "みかん": 50, "ぶどう": 80}

print("----商品管理システム---- ")
print("1: お買い物をする")
print("2: 新しい商品を追加する（店長モード）")
      
mode = input("モードを選択して下さい（1 or 2）：").strip()

if mode == "1": 
    print("----- いらっしゃいませ！ -----")
    for num, name in items_dict.items():
        print(f"{num}: {name} ({prices[name]}円)")

    num_choice = input("商品番号を入力してください：").strip()

    # ↓ ここから下の段差に注目してください
    if num_choice in items_dict:
        choice = items_dict[num_choice]
        price = prices[choice]
        
        count = int(input(f"{choice}は何個買いますか？：").strip())
        total = price * count
        
        if total >= 2000:
            print("2000円以上なので10%割引！")
            total *= 0.9

        print(f"{choice} {count}個で、合計金額は {int(total)} 円です。")
    else:
        # 正しくない番号のときはここだけが動く
        print("正しい番号を入力してください。")

elif mode == "2":
    print("\n--- 商品登録画面 ---")
    new_name = input("登録する商品名を入力してください：").strip()
    new_price = int(input(f"{new_name}の価格を入力してください：").strip())

    new_num = str(len(items_dict) + 1)
    items_dict[new_num] = new_name
    prices[new_name] = new_price
    print(f"☑️ {new_name}が{new_price}円で登録されました。")

    print("\n--- 更新後の商品一覧 ---")
    for num, name in items_dict.items():
        print(f"{num}: {name} ({prices[name]}円)")

# --- 2. セーブ機能（新商品をノートに書き留める） ---        
    save_data = {"items": items_dict, "prices": prices}
    with open(FILE_NAME, "w", encoding="utf-8") as f:
     json.dump(save_data, f, ensure_ascii=False, indent=2)

    print(f"☑️{new_name} が登録され、ファイルの保存されました！")

    print("\n--- 更新後の商品一覧 ---")
    for num, name in items_dict.items():
     print(f"{num}: {name} ({prices[name]}円)")
    
else:
    print("1か2を選択して下さい。")