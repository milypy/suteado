# suteado
捨てアドぽいぽい(m.kuku.lu)の非公式API
```
pip install suteado
```

サンプルコード

```
from suteado import suteado as st

#インスタンスの作成 セッションハッシュは指定しなくても一応通るけどその度に新しいアカウントになる
mail = st.SuteAddress("SHASH%3ABCDEFGHIJK1234567890")

#メールの作成(アドレス名の指定無し)
print(mail.create_Mail("eay.jp"))

#メールの作成(アドレス名の指定あり) この場合:abcdefg@eay.jpが作成される
print(mail.create_Mail("eay.jp","abcdefg1234"))

#指定したセッションハッシュのアカウントに登録されているすべてのメールの取得
print(mail.get_AllAddress())

#メールボックスの確認 整数で因数を指定して最新のものから数個取得も出来る
print(mail.get_mailbox(3))

#ログイン情報からセッションハッシュを抽出する ログイン情報はあなたのユーザー情報→使用中のアカウント情報
print(mail.login(450569192000,"iawgopisnavoi")

```

セッションハッシュはサイトのcookieのSessionHashみたいな名前のやつです。
chromeだったら使いたいアカウントにログインして右クリック → 検証 → Application → StorageのCookies → https://m.kuku.lu/ のcookie_sessionhashに格納されてる値をコピーすれば使えます。
