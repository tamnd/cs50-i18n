---
title: "Mario - CS50x 2026"
pset: 1
draft: false
---

## 要解决的问题

在 Nintendo 的 [Super Mario Bros.](https://en.wikipedia.org/wiki/Super_Mario_Bros.) 中，接近 1-1 世界的结尾时，Mario 必须爬上一座右对齐的砖块金字塔，如下所示。

![Mario 跳上一座右对齐金字塔的截图](pyramid.png)

请在名为 `mario-less` 的文件夹中，在一个名为 `mario.c` 的文件里，用 C 实现一个程序，用井号（`#`）表示砖块，重现这座金字塔，如下所示：

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

不过，你的程序应提示用户输入一个 `int` 作为金字塔的实际高度，这样程序也能输出更矮的金字塔，例如：

```
  #
 ##
###
```

如果用户输入的值不大于 0（或者输入根本不是 `int`），就根据需要一次又一次地重新提示用户。

提示

- 回忆一下，你可以用 `get_int` 从用户那里获取一个 `int`，这个函数声明在 `cs50.h` 中。
- 回忆一下，你可以用 `printf` 打印一个 `string`，这个函数声明在 `stdio.h` 中。

## 演示

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

在写更多代码之前，先写一些伪代码

如果你不确定如何解决问题本身，可以把它拆成一些你大概能先解决的小问题。例如，这个问题其实可以分成两个部分：

1. 提示用户输入金字塔的高度
2. 打印一个对应高度的金字塔

因此，可以把一些伪代码写成注释，提醒自己按这个思路完成：

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for the pyramid's height

    // Print a pyramid of that height
}
```

把伪代码转换为代码

首先，想想如何提示用户输入金字塔的高度。回忆一下，当你希望某件事至少执行一次，并且可能反复执行时，`do while` 循环会很有用，如下所示：

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
}
```

接下来，考虑如何从上到下打印出这个高度的金字塔。注意，第一行应该有一块砖，第二行应该有两块砖，依此类推。即使你暂时还不确定循环里该写什么，大概率也会需要一个循环，如下所示。因此，现在先再添加一些伪代码作为注释：

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
    }
}
```

如何打印某一行砖块呢？如果有一个叫做 `print_row` 的函数能完成这件事，岂不是很方便？我们先假设有这样一个函数：

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
    }
}

void print_row(int bricks)
{
    // Print row of bricks
}
```

然后，我们就可以在 `main` 中调用这个函数，如下所示：

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
        print_row(i + 1);
    }
}

void print_row(int bricks)
{
    // Print row of bricks
}
```

不过，为什么是 `i + 1` 呢？

现在来实现 `print_row`：

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int bricks);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
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

不过，为什么最后要有 `\n` 呢？

遗憾的是，这段代码打印的是左对齐的金字塔，而你需要的是右对齐的！也许我们应该在某些砖块前打印一些空格，把它们向右推？让我们把 `print_row` 改成下面这样，使它既能打印空格，也能打印砖块：

```c
#include <cs50.h>
#include <stdio.h>

void print_row(int spaces, int bricks);

int main(void)
{
    // Prompt the user for the pyramid's height
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1);

    // Print a pyramid of that height
    for (int i = 0; i < n; i++)
    {
        // Print row of bricks
    }
}

void print_row(int spaces, int bricks)
{
    // Print spaces

    // Print bricks
}
```

现在，`main` 和 `print_row` 中都还留有一些伪代码，这部分就留给你完成了！

也请思考一下，是否可以把 `main` 中的一部分代码提取到一个 `get_height` 函数中，让它返回你需要的那个 `int`！

## 讲解视频

请注意，这个讲解视频中说明：程序应提示用户输入金字塔高度，并在用户输入小于 1 或大于 8 的值时*重新*提示。当前规范只要求你在用户输入小于 1 的值时重新提示。

## 如何测试

当你输入以下内容时，你的代码是否能按要求运行？

- `-1` 或其他负数？
- `0`？
- `1` 或其他正数？
- 字母或单词？
- 什么都不输入，只按 Enter？

### 正确性

```
check50 cs50/problems/2026/x/mario/less
```

### 风格

```
style50 mario.c
```

## 如何提交

在终端中执行以下命令来提交你的作业，并回答随后出现的提示。

```
submit50 cs50/problems/2026/x/mario/less
```
