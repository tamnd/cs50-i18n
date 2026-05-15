---
title: "Plurality - CS50x 2026"
pset: 3
draft: false
---

## 解くべき問題

選挙にはさまざまな形や規模があります。イギリスでは、[首相](https://www.parliament.uk/education/about-your-parliament/general-elections/)は公式には君主によって任命されますが、通常は庶民院（下院）で最も多くの議席を獲得した政党のリーダーが選ばれます。アメリカでは、多段階の[選挙人団](https://www.archives.gov/federal-register/electoral-college/about.html)プロセスが採用されており、市民は各州がどのように選挙人を割り当てるかに投票し、その選挙人が大統領を選出します。

おそらく、選挙を行う最も単純な方法は、「複数投票制（plurality vote）」（「最多得票者当選制」や「一人勝ち」とも呼ばれる）として一般に知られている方法です。複数投票制では、すべての有権者が1人の候補者に投票します。選挙の最後に、最も多くの票を獲得した候補者が選挙の勝者として宣言されます。

この問題では、以下に従って、複数投票制の選挙を実行するプログラムを実装します。

## デモ

## 配布コード

この問題では、CS50のスタッフから提供された「配布コード」の機能を拡張します。

配布コードをダウンロードする

[cs50.dev](https://cs50.dev/)にログインし、ターミナルウィンドウをクリックして、`cd`を単独で実行します。ターミナルウィンドウのプロンプトが以下のようになっていることを確認してください。

```
$
```

次に、以下のコマンドを実行します。

```python
wget https://cdn.cs50.net/2026/x/psets/3/plurality.zip
```

これにより、`plurality.zip`というZIPファイルがコードスペースにダウンロードされます。

次に、以下を実行します。

```
unzip plurality.zip
```

`plurality`というフォルダが作成されます。ZIPファイルはもう必要ないので、以下を実行します。

```
rm plurality.zip
```

プロンプトが表示されたら「y」に続いてEnterを押し、ダウンロードしたZIPファイルを削除します。

次に、以下を入力します。

```bash
cd plurality
```

Enterを押して、そのディレクトリに移動（開く）します。プロンプトは以下のようになっているはずです。

```
plurality/ $
```

すべてが成功していれば、以下を実行します。

```bash
ls
```

`plurality.c`という名前のファイルが表示されるはずです。`code plurality.c`を実行すると、この問題セットのコードを入力するファイルが開きます。もしそうならない場合は、手順を振り返って、どこで間違えたかを確認してください。

`plurality.c`のコードを理解する

既存のコードの機能を拡張する場合は、まず現在の状態を理解しておくことが最善です。

まず、ファイルの先頭を見てください。`#define MAX 9`という行は、`MAX`がプログラム全体で使用できる定数（`9`に等しい）であることを意味する構文です。ここでは、選挙が持つことができる候補者の最大数を表しています。

```
// Max number of candidates
#define MAX 9
```

`plurality.c`がこの定数を使用してグローバル配列（すべての関数がアクセスできる配列）を定義していることに注目してください。

```
// Array of candidates
candidate candidates[MAX];
```

しかし、この場合の`candidate`とは何でしょうか？`plurality.c`では、`candidate`は`struct`（構造体）です。各`candidate`には2つのフィールドがあります。候補者の名前を表す`name`という`string`と、候補者の得票数を表す`votes`という`int`です。

```
// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;
```

次に、`main`関数自体を見てください。プログラムが選挙の候補者数を表すグローバル変数`candidate_count`を設定している場所を見つけられるか確認してください。

```
// Number of candidates
int candidate_count;
```

コマンドライン引数を配列`candidates`にコピーしている場所はどうでしょうか？

```c
// Populate array of candidates
candidate_count = argc - 1;
if (candidate_count > MAX)
{
    printf("Maximum number of candidates is %i\n", MAX);
    return 2;
}
for (int i = 0; i < candidate_count; i++)
{
    candidates[i].name = argv[i + 1];
    candidates[i].votes = 0;
}
```

ユーザーに有権者数を入力するように求めている場所はどこでしょうか？

```
int voter_count = get_int("Number of voters: ");
```

その後、プログラムはすべての有権者に投票を入力させ、投票された各候補者に対して`vote`関数を呼び出します。最後に、`main`は`print_winner`関数を呼び出して、選挙の勝者（または勝者たち）を出力します。この機能を実装しているコードを特定するのは、皆さんにお任せします。

ファイルのさらに下の方を見ると、`vote`関数と`print_winner`関数が空のままになっていることに気づくでしょう。

```c
// Update vote totals given a new vote
bool vote(string name)
{
    // TODO
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO
    return;
}
```

この部分を完成させるのはあなたです！**`vote`関数と`print_winner`関数の実装（および必要に応じて追加のヘッダーファイルのインクルード）以外は、`plurality.c`の他の部分を変更しないでください。**

## ヒント

以下を切り替えて、アドバイスを読んでください！

`vote`関数を完成させる

次に、`vote`関数を完成させます。

- `vote`のシグネチャである`bool vote(string name)`は、投票された候補者の名前を表す`name`という`string`を引数として1つ取ることを示しています。
- `vote`は`bool`を返す必要があり、`true`は投票が正常に行われたことを示し、`false`は行われなかったことを示します。

この問題にアプローチする1つの方法は、次の通りです。

1. 各候補者をループで確認する
   
   1. 候補者の名前が入力された`name`と一致するか確認する
      
      1. 一致する場合、その候補者の得票数（votes）をインクリメントし、`true`を返す
      2. 一致しない場合、確認を続ける
2. すべての候補者を確認しても一致が見つからない場合は、`false`を返す

そのためのリマインダーとして、疑似コードを書いてみましょう。

```sql
// Update vote totals given a new vote
bool vote(string name)
{
    // 各候補者をループで確認する
        // 候補者の名前が指定された名前と一致するか確認する
            // 一致する場合、候補者の得票数をインクリメントし、trueを返す

    // 一致が見つからない場合は、falseを返す
}
```

コードでの実装は、皆さんにお任せします！

`print_winner`関数を完成させる

最後に、`print_winner`関数を完成させます。

- この関数は、選挙で最も多くの票を獲得した候補者の名前を出力し、その後に改行を出力する必要があります。
- 複数の候補者がそれぞれ最大得票数を獲得した場合、選挙はタイ（同点）で終了する可能性があります。その場合、勝利した候補者全員の名前を、それぞれ別の行に出力する必要があります。

この問題を解決するにはソートアルゴリズムが最適だと考えるかもしれません。候補者を得票数でソートし、トップの候補者（または候補者たち）を出力することを想像してみてください。しかし、ソートにはコストがかかることを思い出してください。最も高速なソートアルゴリズムの1つであるマージソートであっても、\\(O(N \\space log(N))\\)で実行されます。

この問題を解決するために必要な情報は、次の2つだけであることを考慮してください。

1. 最大得票数
2. その得票数を持つ候補者（または候補者たち）

そのため、優れた解決策は2回の検索だけで済むかもしれません。そのための疑似コードを書いてみましょう。

```c
// Print the winner (or winners) of the election
void print_winner(void)
{
    // 最大得票数を見つける

    // 最大得票数を持つ候補者（または候補者たち）を出力する

}
```

コードの実装は、皆さんにお任せします！

## ウォークスルー

## テスト方法

コードをテストして、以下を処理できることを確認してください。

- 任意の数の候補者（最大`MAX`の`9`まで）がいる選挙
- 名前による候補者への投票
- 投票用紙に記載されていない候補者への無効な投票
- 勝者が1人だけの場合の選挙勝者の出力
- 複数の勝者がいる場合の選挙勝者の出力

### 正確性

```
check50 cs50/problems/2026/x/plurality
```

### スタイル

```
style50 plurality.c
```

## 提出方法

ターミナルで以下を実行して、表示されるプロンプトに答えながら課題を提出してください。

```
submit50 cs50/problems/2026/x/plurality
```
