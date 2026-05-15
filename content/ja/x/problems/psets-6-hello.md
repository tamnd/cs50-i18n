---
title: "Hello, Again - CS50x 2026"
pset: 6
draft: false
---

## 解くべき問題

`sentimental-hello`というフォルダの中の`hello.py`というファイルに、ユーザーに名前を尋ね、`hello, so-and-so`（`so-and-so`は入力された名前）と表示するプログラムを実装してください。[問題セット1](../../1/)で行ったことと全く同じですが、今回はプログラムをPythonで書いてください！

ヒント

- CS50ライブラリで宣言されている`get_string`を使用して、ユーザーから`str`を取得できることを思い出してください。
- `print`を使用して`str`を出力できることを思い出してください。
- Pythonでは、文字列の直前に`f`を付けることで、フォーマット済み文字列（f-string）を作成できることを思い出してください。例えば、`f"{name}"`は、`{name}`と書いた場所に変数`name`の値を代入（「補完」）します。

## デモ

## テスト方法

`check50`はこの問題で利用可能ですが、まずは自分自身で以下のそれぞれについてコードをテストすることをお勧めします。

- `python hello.py`としてプログラムを実行し、入力プロンプトを待ちます。`David`と入力してEnterキーを押します。プログラムは`hello, David`と出力するはずです。
- `python hello.py`としてプログラムを実行し、入力プロンプトを待ちます。`Inno`と入力してEnterキーを押します。プログラムは`hello, Inno`と出力するはずです。
- `python hello.py`としてプログラムを実行し、入力プロンプトを待ちます。`Kamryn`と入力してEnterキーを押します。プログラムは`hello, Kamryn`と出力するはずです。

### 正確性

```
check50 cs50/problems/2026/x/sentimental/hello
```

### スタイル

```
style50 hello.py
```

## 提出方法

ターミナルで以下を実行して、表示されるプロンプトに答えながら課題を提出してください。

```
submit50 cs50/problems/2026/x/sentimental/hello
```
