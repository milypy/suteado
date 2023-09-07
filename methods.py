import Suteado as suteado

#インスタンスの作成 セッションハッシュは指定しなくても一応通るけど非推奨
mail = suteado.SuteAddress("SHASH%3ABCDEFGHIJK1234567890")

#メールの作成(アドレス名の指定無し)
print(mail.create_Mail("eay.jp"))

#メールの作成(アドレス名の指定あり) 下の場合:abcdefg@eay.jpが作成される
print(mail.create_Mail("eay.jp","abcdefg1234"))

#指定したセッションハッシュのアカウントに登録されているすべてのメールの取得
print(mail.get_AllAddress())

#メールボックスの確認 整数で因数を指定して最新のものから数個取得も出来る
print(mail.get_mailbox(3))
