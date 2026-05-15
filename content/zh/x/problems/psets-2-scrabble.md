---
title: "Scrabble - CS50x 2026"
pset: 2
draft: false
---

![Scrabble Board](scrabble.png)

## 待解决的问题

在 [Scrabble](https://en.wikipedia.org/wiki/Scrabble) 游戏中，玩家通过拼凑单词来得分，分数是单词中每个字母分值的总和。

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q  | R | S | T | U | V | W | X | Y | Z  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|----|---|---|---|---|---|---|---|---|----|
| 1 | 3 | 3 | 2 | 1 | 4 | 2 | 4 | 1 | 8 | 5 | 1 | 3 | 1 | 1 | 3 | 10 | 1 | 1 | 1 | 1 | 4 | 4 | 8 | 4 | 10 |

例如，如果我们想给单词 “CODE” 评分，我们会注意到 ‘C’ 值 3 分，‘O’ 值 1 分，‘D’ 值 2 分，‘E’ 值 1 分。将这些分数相加，我们得到 “CODE” 价值 7 分。

在 `scrabble` 文件夹中一个名为 `scrabble.c` 的文件中，使用 C 语言实现一个程序，来决定一场简短的类 Scrabble 游戏的获胜者。你的程序应该提示输入两次：一次让 “Player 1” 输入他们的单词，一次让 “Player 2” 输入他们的单词。然后，根据哪位玩家得分最高，你的程序应该打印 “Player 1 wins!”、“Player 2 wins!” 或 “Tie!”（如果两位玩家得分相等）。

## 演示

## 建议与提示

编写一些你确定可以编译的代码

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

}
```

请注意，你现在已经包含了几个头文件，它们将允许你访问可能帮助你解决此问题的函数。

在编写更多代码之前先编写一些伪代码

如果不确定如何解决问题本身，请将其分解为较小的问题，你可能可以先解决这些小问题。例如，这个问题实际上只是几个小问题：

1. 提示用户输入两个单词
2. 计算每个单词的分数
3. 打印获胜者

让我们编写一些伪代码作为注释来提醒你这样做：

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt the user for two words

    // Compute the score of each word

    // Print the winner
}
```

习题集中的一些题目（比如这道题）可能会包含剧透（例如接下来的内容），它们最终会引导你完成整个解决方案。虽然允许使用这些代码，但我们非常强烈地鼓励你先自己尝试！习题集中的其他题目将不会有这种引导，通常包含“完整剧透”的题目是你稍后需要解决的更难问题的热身版本。

将伪代码转换为代码

首先，考虑如何提示用户输入两个单词。回想一下，CS50 库中的函数 `get_string` 可以提示用户输入字符串。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word

    // Print the winner
}
```

接下来考虑如何计算每个单词的分数。由于相同的评分算法适用于两个单词，这是一个很好的抽象机会。在这里，我们将定义一个名为 `compute_score` 的函数，它接受一个名为 `word` 的字符串作为输入，然后以 `int` 形式返回 `word` 的分数。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner   
}

int compute_score(string word)
{
    // Compute and return score for word
}
```

现在转向实现 `compute_score`。要计算单词的分数，你需要知道单词中每个字母的分值。你可以使用数组将字母与其分值关联起来。想象一个由 26 个 `int` 组成的数组，名为 `POINTS`，其中第一个数字是 ‘A’ 的分值，第二个数字是 ‘B’ 的分值，依此类推。通过在任何单个函数之外声明并初始化这样一个数组，你可以确保任何函数（包括 `compute_score`）都可以访问该数组。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner   
}

int compute_score(string word)
{
    // Compute and return score for word
}
```

为了实现 `compute_score`，首先尝试找到 `word` 中单个字母的分值。

- 回想一下，要查找字符串 `s` 第 n 个索引处的字符，你可以编写 `s[n]`。因此，例如 `word[0]` 将给出 `word` 的第一个字符。
- 现在，回想一下计算机使用 ASCII 表示字符，这是一种将每个字符表示为数字的标准。
- 还请记住，`POINTS` 的第 0 个索引 `POINTS[0]` 给出了 ‘A’ 的分值。思考一下如何将 ‘A’ 的数字表示转换为其分值的索引。那么 ‘a’ 呢？你需要对大写和小写字母应用不同的转换，因此你可能会发现函数 [`isupper`](https://manual.cs50.io/3/isupper) 和 [`islower`](https://manual.cs50.io/3/islower) 对你很有帮助。
- 请记住，不是字母的字符应该给零分。例如，`!` 值 0 分。

如果你能正确计算 `word` 中一个字符的值，那么你很可能可以使用循环来计算其余字符的分数总和。一旦你自己尝试了上述操作，请考虑下面这个（非常有启发性的！）提示。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner   
}

int compute_score(string word)
{
    // Keep track of score
    int score = 0;

    // Compute score for each character
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

最后，完成伪代码的最后一步：打印获胜者。回想一下，`if` 语句可以用来检查条件是否为真，而额外使用 `else if` 或 `else` 可以检查其他（互斥的）条件。

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

在你尝试了上述操作后，请随时查看下面的提示（或者更确切地说，完整的解决方案！）。

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner   
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
    // Keep track of score
    int score = 0;

    // Compute score for each character
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

## 如何测试

你的程序的行为应该如下例所示。

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

### 正确性

```
check50 cs50/problems/2026/x/scrabble
```

### 代码风格

```
style50 scrabble.c
```

## 如何提交

在你的终端中，执行以下命令提交你的工作，并回答出现的提示。

```
submit50 cs50/problems/2026/x/scrabble
```
