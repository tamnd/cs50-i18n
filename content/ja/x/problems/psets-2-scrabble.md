---
title: "Scrabble - CS50x 2026"
pset: 2
draft: false
---

![Scrabble Board](scrabble.png)

## 解決すべき問題

[Scrabble](https://en.wikipedia.org/wiki/Scrabble)というゲームでは、プレイヤーは単語を作成してポイントを獲得します。ポイントは、単語内の各文字のポイント値の合計です。

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q  | R | S | T | U | V | W | X | Y | Z  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|----|---|---|---|---|---|---|---|---|----|
| 1 | 3 | 3 | 2 | 1 | 4 | 2 | 4 | 1 | 8 | 5 | 1 | 3 | 1 | 1 | 3 | 10 | 1 | 1 | 1 | 1 | 4 | 4 | 8 | 4 | 10 |

例えば、「CODE」という単語のスコアを計算する場合、「C」は3点、「O」は1点、「D」は2点、「E」は1点であることを確認します。これらを合計すると、「CODE」は7点になります。

`scrabble`というフォルダ内の`scrabble.c`というファイルに、短いScrabbleのようなゲームの勝者を決定するCのプログラムを実装してください。プログラムは入力を2回促す必要があります。1回目は「Player 1」が単語を入力するため、2回目は「Player 2」が単語を入力するためです。次に、どちらのプレイヤーがより多くのポイントを獲得したかに応じて、プログラムは「Player 1 wins!」、「Player 2 wins!」、または「Tie!」（2人のプレイヤーのポイントが同じ場合）のいずれかを表示する必要があります。

## デモ

## アドバイスとヒント

コンパイルできることがわかっているコードをいくつか書く

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

}
```

この問題を解決するのに役立つ関数にアクセスできるようにする、いくつかのヘッダーファイルが含まれていることに注意してください。

さらにコードを書く前に疑似コードを書く

問題自体の解決方法がわからない場合は、まず解決できそうな小さな問題に分解してください。例えば、この問題は実際にはほんの数個の問題にすぎません：

1. ユーザーに2つの単語を促す
2. 各単語のスコアを計算する
3. 勝者を表示する

それを忘れないように、コメントとして疑似コードを書いてみましょう：

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // ユーザーに2つの単語を促す

    // 各単語のスコアを計算する

    // 勝者を表示する
}
```

この問題のように、問題セットの中には、最終的に完全な解決策を案内するスポイラー（次のものなど）が含まれている場合があります。このコードを使用することは許可されていますが、まずは自分で試してみることを強くお勧めします！問題セットの他の問題には、このようなウォークスルーはありません。通常、「完全なスポイラー」が含まれている問題は、後で取り組む必要があるより大きな問題の準備のためのバージョンです。

疑似コードをコードに変換する

まず、ユーザーに2つの単語をどのように促すかを検討してください。CS50ライブラリの関数である`get_string`は、ユーザーに文字列を促すことができることを思い出してください。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // ユーザーに2つの単語を促す
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // 各単語のスコアを計算する

    // 勝者を表示する
}
```

次に、各単語のスコアを計算する方法を検討します。両方の単語に同じスコア計算アルゴリズムが適用されるため、これは「抽象化」の良い機会です。ここでは、`word`という文字列を入力として受け取り、その`word`のスコアを`int`として返す`compute_score`という関数を定義します。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int compute_score(string word);

int main(void)
{
    // ユーザーに2つの単語を促す
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // 各単語のスコアを計算する
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // 勝者を表示する   
}

int compute_score(string word)
{
    // 単語のスコアを計算して返す
}
```

次に、`compute_score`の実装に移ります。単語のスコアを計算するには、その単語の各文字のポイント値を知る必要があります。文字とそのポイント値を「配列」に関連付けることができます。`POINTS`という26個の`int`の配列を想像してください。最初の数値は「A」のポイント値、2番目の数値は「B」のポイント値、というようになります。このような配列を単一の関数の外側で宣言して初期化することで、`compute_score`を含むすべての関数からこの配列にアクセスできるようにすることができます。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// アルファベットの各文字に割り当てられたポイント
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // ユーザーに2つの単語を促す
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // 各単語のスコアを計算する
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // 勝者を表示する   
}

int compute_score(string word)
{
    // 単語のスコアを計算して返す
}
```

`compute_score`を実装するには、まず`word`内の1文字のポイント値を見つけてみてください。

- 文字列`s`のn番目のインデックスにある文字を見つけるには、`s[n]`と書くことができることを思い出してください。したがって、例えば`word[0]`は、`word`の最初の文字を返します。
- 次に、コンピュータは各文字を数値として表す標準であるASCIIを使用して文字を表すことを思い出してください。
- また、`POINTS`の0番目のインデックスである`POINTS[0]`が「A」のポイント値を返すことも思い出してください。「A」の数値表現をそのポイント値のインデックスにどのように変換できるか考えてみてください。では、「a」はどうでしょうか？大文字と小文字で異なる変換を適用する必要があるため、関数[`isupper`](https://manual.cs50.io/3/isupper)と[`islower`](https://manual.cs50.io/3/islower)が役立つかもしれません。
- 文字「ではない」文字には0ポイントが与えられる必要があることに注意してください。例えば、`!`は0ポイントです。

`word`内の1文字の値を正しく計算できれば、ループを使用して残りの文字のポイントを合計できる可能性があります。自分で上記を試したら、以下の（かなり明らかな！）ヒントを検討してください。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// アルファベットの各文字に割り当てられたポイント
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // ユーザーに2つの単語を促す
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // 各単語のスコアを計算する
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // 勝者を表示する   
}

int compute_score(string word)
{
    // スコアを追跡
    int score = 0;

    // 各文字のスコアを計算
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
    }

    return score;
}
```

最後に、疑似コードの最後のステップである勝者の表示を完了します。`if`文を使用して条件が真かどうかを確認できること、および`else if`または`else`を追加で使用して他の（排他的な）条件を確認できることを思い出してください。

```
if (/* Player 1 wins */)
{
    // ...
}
else if (/* Player 2 wins */)
{
    // ...
}
else
{
    // ...
}
```

そして、上記を試したら、以下のヒント（というか、完全な解決策！）をのぞいてみてください。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// アルファベットの各文字に割り当てられたポイント
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // ユーザーに2つの単語を促す
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // 各単語のスコアを計算する
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // 勝者を表示する   
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // スコアを追跡
    int score = 0;

    // 各文字のスコアを計算
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
    }

    return score;
}
```

## テスト方法

プログラムは以下の例のように動作する必要があります。

```bash
$ ./scrabble
Player 1: Question?
Player 2: Question!
Tie!
```

```bash
$ ./scrabble
Player 1: red
Player 2: wheelbarrow
Player 2 wins!
```

```bash
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

```bash
$ ./scrabble
Player 1: Scrabble
Player 2: wiNNeR
Player 1 wins!
```

### 正確性

```
check50 cs50/problems/2026/x/scrabble
```

### スタイル

```
style50 scrabble.c
```

## 提出方法

ターミナルで以下を実行して、表示されるプロンプトに従って課題を提出してください。

```
submit50 cs50/problems/2026/x/scrabble
```
