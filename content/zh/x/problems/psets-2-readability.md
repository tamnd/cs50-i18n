---
title: "可读性 - CS50x 2026"
pset: 2
draft: false
---

![Charlotte's Web Cover](charlottes_web.jpg)

## 待解决的问题

根据 [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html) 的说法，E.B. White 的《夏洛特的网》（*Charlotte’s Web*）介于二到四年级的阅读水平之间，而 Lois Lowry 的《记忆传授人》（*The Giver*）则介于八到十二年级的阅读水平之间。但是，一本书处于特定的阅读水平到底意味着什么呢？

通常情况下，人类专家会阅读一本书，并根据他们认为该书最适合的年级（即在校年数）做出决定。但算法可能也能计算出这一点！

在名为 `readability` 的文件夹中一个名为 `readability.c` 的文件中，你将实现一个程序，用于计算理解某些文本所需的近似年级水平。你的程序应打印输出 “Grade X”，其中 “X” 是计算出的年级水平，四舍五入到最接近的整数。如果年级水平为 16 或更高（相当于或高于高级本科阅读水平），你的程序应输出 “Grade 16+”，而不是给出确切的指数数字。如果年级水平小于 1，你的程序应输出 “Before Grade 1”。

## 演示

## 背景知识

那么，高阅读水平具有哪些特征呢？嗯，较长的单词可能与较高的阅读水平相关。同样，较长的句子也可能与较高的阅读水平相关。

多年来，人们开发了许多“可读性测试”，定义了计算文本阅读水平的公式。其中一种可读性测试是 *Coleman-Liau 指数*。文本的 Coleman-Liau 指数旨在输出理解某些文本所需的（美国）年级水平。公式为：

```
index = 0.0588 * L - 0.296 * S - 15.8
```

其中 `L` 是文本中每 100 个单词的平均字母数，而 `S` 是文本中每 100 个单词的平均句子数。

## 建议

编写一些你确定可以编译的代码

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

请注意，你现在已经包含了几个头文件，这些文件将允许你访问可能帮助你解决此问题的函数。

在编写更多代码之前先编写一些伪代码

如果不确定如何解决问题本身，请将其分解为可能首先解决的小问题。例如，这个问题实际上只是几个小问题：

1. 提示用户输入一些文本
2. 统计文本中的字母、单词和句子数量
3. 计算 Coleman-Liau 指数
4. 打印年级水平

让我们将一些伪代码写成注释，以提醒你这样做：

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // 提示用户输入一些文本

    // 统计文本中的字母、单词和句子数量

    // 计算 Coleman-Liau 指数

    // 打印年级水平
}
```

将伪代码转换为代码

首先，考虑如何提示用户输入一些文本。回想一下，CS50 库中的函数 `get_string` 可以提示用户输入一个字符串。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // 提示用户输入一些文本
    string text = get_string("Text: ");

    // 统计文本中的字母、单词和句子数量

    // 计算 Coleman-Liau 指数

    // 打印年级水平
}
```

现在你已经收集了用户的输入，你可以开始分析该输入。首先，尝试统计文本中的字母数量。将字母视为大写或小写字母字符，而不是标点符号、数字或其他符号。

解决此问题的一种方法是创建一个名为 `count_letters` 的函数，该函数将字符串 `text` 作为输入，然后将该文本中的字母数量作为 `int` 返回。

```
int count_letters(string text)
{
    // 返回 text 中的字母数量
}
```

你需要编写自己的代码来统计文本中的字母数量。但比你更有经验的人可能已经编写了一个函数来确定字符是否为字母。这是一个使用 [CS50 手册](https://manual.cs50.io/)（C 标准库中常用函数的说明集）的好机会。

你可以将 `count_letters` 集成到你已经编写的代码中，如下所示。

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);

int main(void)
{
    // 提示用户输入一些文本
    string text = get_string("Text: ");

    // 统计文本中的字母、单词和句子数量
    int letters = count_letters(text);

    // 计算 Coleman-Liau 指数

    // 打印年级水平
}

int count_letters(string text)
{
    // 返回 text 中的字母数量
}
```

接下来，编写一个统计单词的函数。

```
int count_words(string text)
{
    // 返回 text 中的单词数量
}
```

为了解决这个问题，我们将任何由空格分隔的字符序列视为一个单词（因此，像 “sister-in-law” 这样的连字符单词应被视为一个单词，而不是三个）。你可以假设一个句子：

- 将包含至少一个单词；
- 不会以空格开头或结尾；且
- 不会连续出现多个空格。

在这些假设下，你可能会发现单词数量和空格数量之间的关系。当然，我们也欢迎你尝试能够容忍单词之间有多个空格甚至没有单词的解决方案！

你现在可以将 `count_words` 集成到你的程序中，如下所示：

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
    // 提示用户输入一些文本
    string text = get_string("Text: ");

    // 统计文本中的字母、单词和句子数量
    int letters = count_letters(text);
    int words = count_words(text);

    // 计算 Coleman-Liau 指数

    // 打印年级水平
}

int count_letters(string text)
{
    // 返回 text 中的字母数量
}

int count_words(string text)
{
    // 返回 text 中的单词数量
}
```

最后，编写一个统计句子的函数。你可以将任何以 `.`、`!` 或 `?` 结尾的字符序列视为一个句子。

```
int count_sentences(string text)
{
    // 返回 text 中的句子数量
}
```

你可以将 `count_sentences` 集成到你的程序中，如下所示：

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
    // 提示用户输入一些文本
    string text = get_string("Text: ");

    // 统计文本中的字母、单词和句子数量
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // 计算 Coleman-Liau 指数

    // 打印年级水平
}

int count_letters(string text)
{
    // 返回 text 中的字母数量
}

int count_words(string text)
{
    // 返回 text 中的单词数量
}

int count_sentences(string text)
{
    // 返回 text 中的句子数量
}
```

最后，计算 Coleman-Liau 指数并打印生成的年级水平。

- 回想一下，Coleman-Liau 指数的计算公式为 `index = 0.0588 * L - 0.296 * S - 15.8`
- `L` 是文本中每 100 个单词的平均字母数：即字母数量除以单词数量，再乘以 100。
- `S` 是文本中每 100 个单词的平均句子数：即句子数量除以单词数量，再乘以 100。
- 你需要将结果四舍五入到最接近的整数，因此请回想一下，`round` 是在 `math.h` 中声明的，参见 [manual.cs50.io](https://manual.cs50.io/)。
- 回想一下，在 C 中对 `int` 类型的值进行除法运算时，结果也将是一个 `int`，任何余数（即小数点后的数字）都将被丢弃。换句话说，结果将被“截断”。在计算 `L` 和 `S` 时进行除法之前，你可能需要将一个或多个值强制转换为 `float`！

如果生成的指数数字为 16 或更高（相当于或高于高级本科阅读水平），你的程序应输出 “Grade 16+”，而不是输出确切的指数数字。如果指数数字小于 1，你的程序应输出 “Before Grade 1”。

## 视频演示

## 如何测试

尝试在以下文本上运行你的程序，确保你看到指定的年级水平。务必仅复制文本，不要多余的空格。

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

### 正确性

```
check50 cs50/problems/2026/x/readability
```

### 风格

```
style50 readability.c
```

## 如何提交

在你的终端中，执行以下命令以提交你的作品，并根据提示进行回答。

```
submit50 cs50/problems/2026/x/readability
```
