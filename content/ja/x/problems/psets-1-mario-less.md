---
title: "Mario - CS50x 2026"
pset: 1
draft: false
---

## 解くべき問題

任天堂の [Super Mario Bros.](https://en.wikipedia.org/wiki/Super_Mario_Bros.) のワールド 1-1 の終盤で、マリオは以下のように右揃えのレンガのピラミッドを登らなければなりません。

![screenshot of Mario jumping up a right-aligned pyramid](pyramid.png)

`mario-less` というフォルダの中の `mario.c` というファイルに、ハッシュ記号（`#`）をレンガとして使い、以下のようなピラミッドを再現する C 言語のプログラムを実装してください。

```
       #
      ##
     ###
    ####
   #####
  ######
 #######
########
```

ただし、ピラミッドの実際の高さとして `int` を入力するようユーザーに促し、プログラムが以下のようなより低いピラミッドも出力できるようにしてください。

```
  #
 ##
###
```

ユーザーの入力が 0 より大きい整数でない場合は、必要に応じて何度でもユーザーに再入力を促してください。

ヒント

- `cs50.h` で宣言されている `get_int` を使って、ユーザーから `int` を取得できることを思い出してください。
- `stdio.h` で宣言されている `printf` を使って、`string` を印刷できることを思い出してください。

## デモ

## アドバイス

コンパイルできることがわかっているコードを書く

このプログラムは何もしませんが、少なくとも `make` でコンパイルできるはずです！

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{

}
```

さらにコードを書く前に疑似コードを書く

問題自体の解き方がわからない場合は、まず解決できそうな小さな問題に分解してください。例えば、この問題は実際には 2 つの問題に分けられます。

1. ユーザーにピラミッドの高さを入力させる
2. その高さのピラミッドを印刷する

そこで、それを忘れないようにコメントとして疑似コードを書いておきましょう。

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ユーザーにピラミッドの高さを入力させる

    // その高さのピラミッドを印刷する
}
```

疑似コードをコードに変換する

まず、ユーザーにピラミッドの高さを入力させる方法を考えましょう。以下の例のように、少なくとも 1 回、そして必要に応じて何度も繰り返したい場合には、`do while` ループが役立つことを思い出してください。

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ユーザーにピラミッドの高さを入力させる
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // その高さのピラミッドを印刷する
}
```

次に、その高さのピラミッドを上から下へ印刷する方法を考えましょう。最初の行には 1 つ、2 行目には 2 つというようにレンガを配置する必要があることに注目してください。おそらく、以下の例のように、ループを使いたくなるでしょう（ループの中に何を入れるかまだ決まっていないとしても）。とりあえず、コメントとして疑似コードをさらに追加しておきましょう。

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ユーザーにピラミッドの高さを入力させる
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // その高さのピラミッドを印刷する
    for (int i = 0; i < n; i++)
    {
        // レンガの行を印刷する
    }
}
```

そのレンガの行をどうやって印刷しましょうか？ そうですね、それを行う `print_row` という関数があれば便利だと思いませんか？ あると仮定してみましょう。

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // ユーザーにピラミッドの高さを入力させる
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // その高さのピラミッドを印刷する
    for (int i = 0; i < n; i++)
    {
        // レンガの行を印刷する
    }
}

void print_row(int bricks)
{
    // レンガの行を印刷する
}
```

そうすれば、以下の例のように `main` からその関数を呼び出すことができます。

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // ユーザーにピラミッドの高さを入力させる
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // その高さのピラミッドを印刷する
    for (int i = 0; i < n; i++)
    {
        // レンガの行を印刷する
        print_row(i + 1);
    }
}

void print_row(int bricks)
{
    // レンガの行を印刷する
}
```

なぜ `i + 1` なのでしょうか？

では、`print_row` を実装しましょう。

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // ユーザーにピラミッドの高さを入力させる
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // その高さのピラミッドを印刷する
    for (int i = 0; i < n; i++)
    {
        // レンガの行を印刷する
        print_row(i + 1);
    }
}

void print_row(int bricks)
{
    for (int i = 0; i < bricks; i++)
    {
        printf("#");
    }
    printf("\n");
}
```

なぜ最後に `\n` があるのでしょうか？

残念ながら、このコードは左揃えのピラミッドを出力しますが、必要なのは右揃えのものです！ おそらく、レンガの前にいくつか空白を印刷して、レンガを右に移動させる必要があるのではないでしょうか？ `print_row` を次のように変更して、両方を印刷できるようにしましょう。

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    // ユーザーにピラミッドの高さを入力させる
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // その高さ의 ピラミッドを印刷する
    for (int i = 0; i < n; i++)
    {
        // レンガの行を印刷する
    }
}

void print_row(int spaces, int bricks)
{
    // 空白を印刷する

    // レンガを印刷する
}
```

これで、`main` と `print_row` の両方に疑似コードが残りました。あとは皆さんにお任せします！

また、`main` のコードの一部を、必要な `int` を返す `get_height` 関数に抽出できるかどうかも検討してみてください！

## ウォークスルー

このウォークスルーでは、プログラムがピラミッドの高さを入力させ、入力値が 1 未満または 8 より大きい場合に *再* 入力を促すように指定されています。仕様では、入力値が 1 未満の場合にのみ再入力を促すことが求められています。

## テスト方法

以下のように入力したとき、コードは規定通りに動作しますか？

- `-1` やその他の負の数？
- `0`？
- `1` やその他の正の数？
- 文字や単語？
- 何も入力せずに Enter キーだけを押した場合？

### 正確性

```
check50 cs50/problems/2026/x/mario/less
```

### スタイル

```
style50 mario.c
```

## 提出方法

ターミナルで以下を実行して、表示される指示に従って課題を提出してください。

```
submit50 cs50/problems/2026/x/mario/less
```
