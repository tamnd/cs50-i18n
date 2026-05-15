---
title: "Readability - CS50x 2026"
pset: 2
draft: false
---

![Charlotte's Web Cover](charlottes_web.jpg)

## 解決すべき問題

[Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html) によれば、E.B. ホワイトの『シャーロットのおくりもの（Charlotte’s Web）』は小学2年生から4年生の読書レベルであり、ロイス・ローリーの『ギヴァー 記憶を注ぐ者（The Giver）』は中学2年生から高校3年生（8年生から12年生）の読書レベルであるとされています。しかし、本が特定の読書レベルにあるというのは、一体どういう意味なのでしょうか。

多くの場合、人間の専門家が本を読み、その本がどの学年（つまり学校の年次）に最も適しているかを判断します。しかし、アルゴリズムによってもそれを判断できるはずです！

`readability` というフォルダ内の `readability.c` というファイルに、あるテキストを理解するために必要な、おおよその学年レベルを計算するプログラムを実装してください。プログラムは、計算された学年レベルを四捨五入して「Grade X」（Xは学年）として出力する必要があります。学年レベルが16以上の場合は（大学4年生以上の読書レベルに相当）、正確な指数を出す代わりに「Grade 16+」と出力してください。学年レベルが1未満の場合は、「Before Grade 1」と出力してください。

## デモ

## 背景

では、読書レベルが高いテキストにはどのような特徴があるのでしょうか。おそらく、長い単語は高い読書レベルと相関があるでしょう。同様に、長い文章も高い読書レベルと相関があるはずです。

長年にわたり、テキストの読書レベルを計算するための公式を定義した「読解力テスト（readability tests）」が数多く開発されてきました。その一つが *Coleman-Liau インデックス* です。Coleman-Liau インデックスは、あるテキストを理解するために必要な（米国の）学年レベルを出力するように設計されています。その公式は以下の通りです。

```
index = 0.0588 * L - 0.296 * S - 15.8
```

ここで、`L` はテキスト内の単語100個あたりの平均文字数、`S` はテキスト内の単語100個あたりの平均文章数です。

## アドバイス

まず、コンパイルできることがわかっているコードを書きます。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

}
```

この問題の解決に役立つ可能性のある関数にアクセスできるように、いくつかのヘッダーファイルが既にインクルードされていることに注目してください。

さらにコードを書く前に、疑似コードを書きます。

問題自体の解き方がわからない場合は、まず解決できそうな小さな問題に分解してみましょう。例えば、この問題は実質的に数個の小さな問題に分けられます。

1. ユーザーにテキストの入力を促す
2. テキスト内の文字数、単語数、文章数を数える
3. Coleman-Liau インデックスを計算する
4. 学年レベルを出力する

これらを忘れないように、コメントとして疑似コードを書いてみましょう。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // ユーザーにテキストの入力を促す

    // テキスト内の文字数、単語数、文章数を数える

    // Coleman-Liau インデックスを計算する

    // 学年レベルを出力する
}
```

疑似コードをコードに変換します。

まず、ユーザーにテキストの入力を促す方法を考えます。CS50 ライブラリの関数である `get_string` を使えば、ユーザーに文字列の入力を促すことができることを思い出してください。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // ユーザーにテキストの入力を促す
    string text = get_string("Text: ");

    // テキスト内の文字数、単語数、文章数を数える

    // Coleman-Liau インデックスを計算する

    // 学年レベルを出力する
}
```

ユーザーから入力を受け取ったら、その入力の分析を開始できます。まず、テキスト内の文字数を数えてみましょう。文字とは、句読点、数字、その他の記号ではなく、大文字または小文字のアルファベット文字であると見なします。

この問題へのアプローチの一つとして、文字列 `text` を入力として受け取り、そのテキスト内の文字数を `int` として返す `count_letters` という関数を作成することが考えられます。

```
int count_letters(string text)
{
    // text 内の文字数を返す
}
```

テキスト内の文字数を数えるための独自のコードを書く必要があります。しかし、文字がアルファベットかどうかを判断する関数を、誰か他の経験豊富な人が既に書いているかもしれません。これは、C標準ライブラリの一般的な関数の解説を集めた [CS50 マニュアル](https://manual.cs50.io/) を活用する絶好の機会です。

`count_letters` を既に書いたコードに組み込むと、次のようになります。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);

int main(void)
{
    // ユーザーにテキストの入力を促す
    string text = get_string("Text: ");

    // テキスト内の文字数、単語数、文章数を数える
    int letters = count_letters(text);

    // Coleman-Liau インデックスを計算する

    // 学年レベルを出力する
}

int count_letters(string text)
{
    // text 内の文字数を返す
}
```

次に、単語を数える関数を書きます。

```
int count_words(string text)
{
    // text 内の単語数を返す
}
```

この問題では、スペースで区切られた一連の文字を単語と見なします（したがって、「sister-in-law」のようなハイフンでつながれた単語は、3つではなく1つの単語と見なされます）。文章については、以下のことを前提として構いません。

- 少なくとも1つの単語が含まれている。
- スペースで始まったり終わったりしない。
- 複数のスペースが連続することはない。

これらの前提条件の下では、単語数とスペースの数の間に関係が見つかるかもしれません。もちろん、単語間の複数のスペースや、あるいは単語が全くない場合にも対応できるような解決策を試みることも歓迎します。

これで、`count_words` を次のようにプログラムに組み込むことができます。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);

int main(void)
{
    // ユーザーにテキストの入力を促す
    string text = get_string("Text: ");

    // テキスト内の文字数、単語数、文章数を数える
    int letters = count_letters(text);
    int words = count_words(text);

    // Coleman-Liau インデックスを計算する

    // 学年レベルを出力する
}

int count_letters(string text)
{
    // text 内の文字数を返す
}

int count_words(string text)
{
    // text 内の単語数を返す
}
```

最後に、文章を数える関数を書きます。`.` または `!` または `?` で終わる一連の文字を文章と見なすことができます。

```
int count_sentences(string text)
{
    // text 内の文章数を返す
}
```

`count_sentences` を次のようにプログラムに組み込みます。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // ユーザーにテキストの入力を促す
    string text = get_string("Text: ");

    // テキスト内の文字数、単語数、文章数を数える
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Coleman-Liau インデックスを計算する

    // 学年レベルを出力する
}

int count_letters(string text)
{
    // text 内の文字数を返す
}

int count_words(string text)
{
    // text 内の単語数を返す
}

int count_sentences(string text)
{
    // text 内の文章数を返す
}
```

最後に、Coleman-Liau インデックスを計算し、結果の学年レベルを出力します。

- Coleman-Liau インデックスは、`index = 0.0588 * L - 0.296 * S - 15.8` で計算されることを思い出してください。
- `L` はテキスト内の単語100個あたりの平均文字数です。つまり、文字数を単語数で割り、それに100を掛けたものです。
- `S` はテキスト内の単語100個あたりの平均文章数です。つまり、文章数を単語数で割り、それに100を掛けたものです。
- 結果を最も近い整数に四捨五入する必要があります。[manual.cs50.io](https://manual.cs50.io/) にあるように、`round` 関数は `math.h` で宣言されています。
- C言語で `int` 型の値を割る場合、結果も `int` となり、余り（つまり小数点以下の桁）は切り捨てられることを思い出してください。言い換えれば、結果は「切り捨て（truncated）」られます。`L` や `S` を計算するときに除算を行う前に、1つ以上の値を `float` にキャストしたいかもしれません！

計算された指数が16以上の場合（大学4年生以上の読書レベルに相当）、正確な指数を出力する代わりに「Grade 16+」と出力する必要があります。指数が1未満の場合は、「Before Grade 1」と出力してください。

## ウォークスルー

## テスト方法

以下のテキストでプログラムを実行し、指定された学年レベルが表示されることを確認してください。余分なスペースを含めず、テキストのみをコピーするようにしてください。

- `One fish. Two fish. Red fish. Blue fish.` (Before Grade 1)
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (Grade 2)
- `Congratulations! Today is your day. You're off to Great Places! You're off and away!` (Grade 3)
- `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` (Grade 5)
- `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` (Grade 7)
- `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` (Grade 8)
- `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` (Grade 8)
- `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` (Grade 9)
- `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` (Grade 10)
- `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` (Grade 16+)

### 正確性

```
check50 cs50/problems/2026/x/readability
```

### スタイル

```
style50 readability.c
```

## 提出方法

ターミナルで以下を実行して、表示されるプロンプトに従って回答し、課題を提出してください。

```
submit50 cs50/problems/2026/x/readability
```
