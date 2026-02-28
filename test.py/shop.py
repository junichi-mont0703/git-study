# 名前を教えてもらう(入力待ち状態になります)
user_name = input("あなたの名前を教えて下さい: ")

#挨拶を表示します
print("こんにちは、" + user_name + "さん！")

#好きなリンゴの数を聞く
# inputで入ってきたものは「文字」なので、int()を使って「数字」に変換します
apple_count = input("りんごは何個買いますか？: " )
apple_count = int(apple_count)

#合計金額を計算する(1個100円とします)
total_price = apple_count * 150

#結果を表示します
print(user_name + "さん、合計は," + str(total_price) + "円ですよ")