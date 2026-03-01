import json
import os

# 保存先のファイル名
FILE_NAME = "shop_data.json"

# --- 1. ロード機能 ---
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        save_data = json.load(f)
        items_dict = save_data["items"]
        prices = save_data["prices"]
        # 名前を stocks に統一します
        stocks = save_data.get("stocks", {})
else:
    items_dict = {"1": "りんご", "2": "みかん", "3": "ぶどう"}
    prices = {"りんご": 100, "みかん": 50, "ぶどう": 80}
    stocks = {"りんご": 10, "みかん": 10, "ぶどう": 10}

print("----商品管理システム---- ")
print("1: お買い物をする")
print("2: 新しい商品を追加する（店長モード）")
      
mode = input("モードを選択して下さい（1 or 2）：").strip()

if mode == "1": 
    print("----- いらっしゃいませ！ -----")
    for num, name in items_dict.items():
        # 在庫も表示
        print(f"{num}: {name} ({prices[name]}円) [在庫: {stocks.get(name, 0)}個]")

    num_choice = input("\n商品番号を入力してください：").strip()

    if num_choice in items_dict:
        choice = items_dict[num_choice]
        price = prices[choice]
        current_stock = stocks.get(choice, 0) # 名前を修正
        
        count_input = input(f"{choice}は何個買いますか？（現在の在庫: {current_stock}個）：").strip()
        if count_input.isdigit():
            count = int(count_input)

            # --- 在庫チェック ---
            if count > current_stock:
                print(f"❌ 申し訳ありませんが、{choice}の在庫は{current_stock}個しかありません。")
            else:
                # 在庫がある場合のみ、以下の計算を行う
                stocks[choice] -= count
                total = price * count

                if total >= 2000:
                    print("✨ 2000円以上なので10%割引！")
                    total *= 0.9

                print(f"✅ {choice} {count}個で、合計金額は {int(total)} 円です。")
                print(f"（残りの{choice}の在庫は {stocks[choice]} 個になりました）")

                # 購入後にセーブする
                save_data = {"items": items_dict, "prices": prices, "stocks": stocks}
                with open(FILE_NAME, "w", encoding="utf-8") as f:
                    json.dump(save_data, f, ensure_ascii=False, indent=2)
        else:
            print("数字を入力してください。")
    else:
        print("正しい番号を入力してください。")

elif mode == "2":
    print("\n--- 商品登録・入荷画面 ---")
    new_name = input("商品名を入力してください：").strip()
    
    # --- すでに商品が存在するかチェック ---
    found_num = None
    for num, name in items_dict.items():
        if name == new_name:
            found_num = num
            break

    if found_num:
        # 【既存商品の入荷】
        print(f"💡 {new_name}はすでに登録されています（商品番号: {found_num}）。")
        add_stock = int(input(f"何個入荷しますか？：").strip())
        stocks[new_name] = stocks.get(new_name, 0) + add_stock
        print(f"✅ {new_name}を{add_stock}個入荷しました。現在の在庫は{stocks[new_name]}個です。")
    else:
        # 【新規商品の登録】
        new_price = int(input(f"{new_name}の価格を入力してください：").strip())
        new_stock = int(input(f"{new_name}の初期在庫を入力してください：").strip())

        new_num = str(len(items_dict) + 1)
        items_dict[new_num] = new_name
        prices[new_name] = new_price
        stocks[new_name] = new_stock
        print(f"✨ 新規商品 {new_name}（{new_price}円）を{new_stock}個で登録しました！")

    # --- 共通のセーブ処理 ---        
    save_data = {"items": items_dict, "prices": prices, "stocks": stocks}
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(save_data, f, ensure_ascii=False, indent=2)

    print("\n--- ✨ 最新の全商品リスト ---")
    for num, name in items_dict.items():
        print(f"{num}: {name} ({prices[name]}円) [在庫: {stocks.get(name, 0)}個]")
    
else:
    print("1か2を選択して下さい。")