subjects = []

while True:
    print("1: 授業登録")
    print("2: 一覧表示")
    print("3: 削除")
    print("4: 終了")

    choice = input("選択してください: ")

    if choice == "1":
        subject = input("科目名: ")
        subjects.append(subject)
        print("登録しました")

    elif choice == "2":
        print("時間割一覧")

        for i, s in enumerate(subjects):
            print(i, s)

    elif choice == "3":
        number = int(input("削除番号: "))
        subjects.pop(number)
        print("削除しました")

    elif choice == "4":
        print("終了します")
        break

    else:
        print("もう一度入力してください")
