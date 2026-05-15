---
title: "找零 - CS50x 2026"
pset: 1
draft: false
---

![US coins](coins.jpg)

## 要解决的问题

假设你在一家商店工作，一位顾客为了购买价格为 $0.50（50 美分）的糖果，给了你 $1.00（100 美分）。你需要找给顾客“零钱”，也就是支付糖果费用后剩下的金额。找零时，你通常会希望给出的硬币数量尽可能少，以免硬币用完（或让顾客不耐烦！）。请在名为 `cash` 的文件夹中，在一个名为 `cash.c` 的文件里，用 C 实现一个程序：给定应找的零钱金额（以美分为单位），打印所需的最少硬币数，如下所示：

```python
Change owed: 25
1
```

不过，你的程序应提示用户输入一个大于 0 的 `int`，使程序能处理任意金额的找零：

```python
Change owed: 70
4
```

如果用户输入的值不大于或等于 0（或者输入根本不是 `int`），就根据需要一次又一次地重新提示用户。

## 演示

## 贪心算法

幸运的是，计算机科学为各地的收银员提供了减少应付硬币数量的方法：贪心算法。

根据美国国家标准与技术研究院（National Institute of Standards and Technology，NIST）的说法，贪心算法是一种“在寻找答案的过程中，总是选择当前最优，也就是局部最优解”的算法。贪心算法能为某些优化问题找到整体最优解，也就是全局最优解，但在另一些问题的某些情形下，可能只能得到次优解。

这到底是什么意思？假设一名收银员需要给顾客找零，而收银抽屉里有 25 美分硬币、10 美分硬币、5 美分硬币和 1 美分硬币。要解决的问题是：应该给顾客哪些硬币，以及每种硬币各给多少枚。你可以把“贪心”的收银员想象成这样一个人：每次从抽屉中拿出一枚硬币时，都想尽可能多地减少剩余问题。例如，如果某位顾客应得 41 美分，第一次能拿走的最大一口（也就是当前最优、局部最优的一步）就是 25 美分。（这一口之所以“最优”，是因为它比任何其他硬币都能更快让我们接近 0 美分。）请注意，这样一口会把原本 41 美分的问题削减为 16 美分的问题，因为 41 - 25 = 16。也就是说，剩余部分是一个相似但更小的问题。不用说，再拿一枚 25 美分硬币就太多了（假设收银员不想亏钱），于是我们的贪心收银员会转向 10 美分硬币，留下 6 美分的问题。此时，贪心策略会选择一枚 5 美分硬币，然后再选择一枚 1 美分硬币，问题就解决了。顾客会收到一枚 25 美分硬币、一枚 10 美分硬币、一枚 5 美分硬币和一枚 1 美分硬币：总共四枚硬币。

事实证明，对于美国货币（以及欧盟货币）来说，这种贪心方法（也就是算法）不仅局部最优，而且全局最优。也就是说，只要收银员每种硬币都有足够数量，按从大到小选择硬币就会得到可能的最少硬币数。到底有多少？这就由你来告诉我们了！

## 建议

先写一些你知道能编译的代码

即使这个程序还不会做任何事情，它至少应该能用 `make` 编译！

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{

}
```

请注意，你现在已经包含了 `cs50.h` 和 `stdio.h` 这两个“头文件”，它们会让你能够使用一些可能有助于解决这个问题的函数。

在写更多代码之前，先写一些伪代码

如果你不确定如何解决问题本身，可以把它拆成一些你大概能先解决的小问题。例如，这个问题其实只有少数几个步骤：

1. 提示用户输入应找零钱，单位为美分。
2. 计算应该给顾客多少枚 *quarters*。从 cents 中减去这些 quarters 的价值。
3. 计算应该给顾客多少枚 *dimes*。从剩余 cents 中减去这些 dimes 的价值。
4. 计算应该给顾客多少枚 *nickels*。从剩余 cents 中减去这些 nickels 的价值。
5. 计算应该给顾客多少枚 *pennies*。从剩余 cents 中减去这些 pennies 的价值。
6. 将用到的 quarters、dimes、nickels 和 pennies 的数量相加。
7. 打印这个总数。

这就是你可以用来解决此问题的贪心算法，所以我们把一些伪代码写成注释，提醒自己按这个思路完成：

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for change owed, in cents

    // Calculate how many quarters you should give customer
    // Subtract the value of those quarters from cents

    // Calculate how many dimes you should give customer
    // Subtract the value of those dimes from remaining cents

    // Calculate how many nickels you should give customer
    // Subtract the value of those nickels from remaining cents

    // Calculate how many pennies you should give customer
    // Subtract the value of those pennies from remaining cents

    // Sum the number of quarters, dimes, nickels, and pennies used
    // Print that sum
}
```

把伪代码转换为代码

首先，想想如何提示用户输入应找的美分数。回忆一下，当你希望某件事至少执行一次，并且可能反复执行时，`do while` 循环会很有用，如下所示：

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);
}
```

在这里停下来用 `make` 编译你的程序是明智的。测试一下，确认程序能够编译，并且当你输入小于 0 的美分数（或输入类似 “cat” 的内容）时，会重新提示你。

接下来，考虑如何计算应该给顾客多少枚 quarters。由于我们使用的是贪心算法，这个问题就变成了：“你最多能给他们多少枚 quarters？”你*可以*直接在 `main` 函数中写出这个问题的解法。不过，写一个新函数也许能让思路更清晰：这个函数叫做 `calculate_quarters`。这样你就可以更专注于计算 quarters 的逻辑。之后，你可以再把这个函数整合进更大的解法中。

```
int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
}
```

请注意，这个函数确实名为 `calculate_quarters`。根据括号中的 `int cents`，它接收一个名为 `cents` 的 `int` 作为输入。而根据函数名前面的 `int`，它也应该“返回”一个 `int`。也就是说，这个函数的输出是一个整数：能从 cents 中取出的 quarters 数量。

现在，考虑下面这种实现 `calculate_quarters` 的方式：不断增加 quarters 的数量，直到没有足够的 cents 可以再换成 quarters 为止：

```
int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

当然，至少还有一种更简单的方法可以解决这个 `calculate_quarters` 问题。但我们把它留给你自己去发现！

当 `calculate_quarters` 按预期工作后，你可以把这个函数整合进程序中。注意要在 `main` 函数上方“声明”这个函数的“签名”（也就是 `int calculate_quarters(int cents)`），这样你就能在 `main` 中使用 `calculate_quarters`，并在稍后、`main` 下方再定义它。

```c
#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Calculate how many quarters you should give customer
    int quarters = calculate_quarters(cents);

    // Subtract the value of those quarters from cents
    cents = cents - (quarters * 25);
}

int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

已经解决了几个小问题，还剩下几个！你注意到这里有什么可以复用的模式了吗？

## 如何测试

对于这个程序，请尝试手动测试你的代码。这是很好的练习：

- 如果你输入 `-1`，程序会再次提示你吗？
- 如果你输入 `0`，程序会输出 `0` 吗？
- 如果你输入 `1`，程序会输出 `1` 吗（也就是一枚 penny）？
- 如果你输入 `4`，程序会输出 `4` 吗（也就是四枚 pennies）？
- 如果你输入 `5`，程序会输出 `1` 吗（也就是一枚 nickel）？
- 如果你输入 `24`，程序会输出 `6` 吗（也就是两枚 dimes 和四枚 pennies）？
- 如果你输入 `25`，程序会输出 `1` 吗（也就是一枚 quarter）？
- 如果你输入 `26`，程序会输出 `2` 吗（也就是一枚 quarter 和一枚 penny）？
- 如果你输入 `99`，程序会输出 `9` 吗（也就是三枚 quarters、两枚 dimes 和四枚 pennies）？

### 正确性

```
check50 cs50/problems/2026/x/cash
```

### 风格

```
style50 cash.c
```

在终端中执行以下命令来提交你的作业，并回答随后出现的提示。

```
submit50 cs50/problems/2026/x/cash
```
