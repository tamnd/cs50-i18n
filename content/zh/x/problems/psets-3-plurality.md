---
title: "多数票制 - CS50x 2026"
pset: 3
draft: false
---

## 待解决的问题

选举形式多种多样。在英国，[首相](https://www.parliament.uk/education/about-your-parliament/general-elections/)由君主任命，通常选择在下议院获得席位最多的政党的领袖。美国则使用多步骤的[选举人团](https://www.archives.gov/federal-register/electoral-college/about.html)程序，由公民投票决定各州如何分配选举人票，再由选举人选出总统。

然而，最简单的选举方式或许是通常被称为“多数票制”（plurality vote）的方法（也称为“简单多数制”或“胜者全得”）。在多数票制中，每位选民只能投给一位候选人。在选举结束时，获得票数最多的候选人即被宣布为选举获胜者。

在本项目中，你将实现一个运行多数票制选举的程序，如下所述。

## 演示

## 分发代码

在本项目中，你将扩展由 CS50 工作人员提供的“分发代码”的功能。

下载分发代码

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，并执行 `cd` 命令。你应该会发现终端窗口的提示符如下所示：

```
$
```

接下来执行

```python
wget https://cdn.cs50.net/2026/x/psets/3/plurality.zip
```

以便将名为 `plurality.zip` 的压缩包下载到你的 codespace。

然后执行

```
unzip plurality.zip
```

创建一个名为 `plurality` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm plurality.zip
```

并在提示符处输入 “y” 后按 Enter 键，以删除你下载的 ZIP 文件。

现在输入

```bash
cd plurality
```

后按 Enter 键进入（即打开）该目录。你的提示符现在应如下所示。

```
plurality/ $
```

如果一切顺利，执行

```bash
ls
```

你应该看到一个名为 `plurality.c` 的文件。执行 `code plurality.c` 应打开该文件，你将在此文件中编写本问题集的代码。如果没有，请回顾你的步骤，看看能否确定哪里出了问题！

理解 `plurality.c` 中的代码

每当你扩展现有代码的功能时，最好先确保你理解它当前的状态。

首先看文件顶部。`#define MAX 9` 这行语法表示 `MAX` 是一个常量（等于 `9`），可以在整个程序中使用。在这里，它代表选举可以拥有的最大候选人数量。

```
// Max number of candidates
#define MAX 9
```

注意 `plurality.c` 随后使用该常量定义了一个全局数组——也就是说，任何函数都可以访问的数组。

```
// Array of candidates
candidate candidates[MAX];
```

但是，在这种情况下，什么是 `candidate` 呢？在 `plurality.c` 中，`candidate` 是一个结构体（`struct`）。每个 `candidate` 有两个字段：一个名为 `name` 的 `string`，代表候选人的姓名；一个名为 `votes` 的 `int`，代表候选人获得的票数。

```
// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;
```

现在，看看 `main` 函数本身。看看你是否能找到程序设置全局变量 `candidate_count` 的位置，它代表选举中的候选人人数。

```
// Number of candidates
int candidate_count;
```

那么，在哪里将命令行参数复制到 `candidates` 数组中呢？

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

又是在哪里要求用户输入选民人数的呢？

```
int voter_count = get_int("Number of voters: ");
```

然后，程序让每位选民输入一张选票，并为每位被投票的候选人调用 `vote` 函数。最后，`main` 调用 `print_winner` 函数来打印选举的获胜者（或多位获胜者）。我们将把识别实现这些功能的代码的任务留给你。

但是，如果你进一步查看文件下方，你会注意到 `vote` 和 `print_winner` 函数留空了。

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

这部分由你来完成！**除了 `vote` 和 `print_winner` 函数的实现（以及根据需要包含额外的头文件）之外，你不应修改 `plurality.c` 中的任何其他内容。**

## 提示

点击下面的切换按钮阅读一些建议！

完成 `vote` 函数

接下来，完成 `vote` 函数。

- 考虑 `vote` 的函数签名 `bool vote(string name)`，显示它接受一个名为 `name` 的 `string` 参数，代表被投票的候选人姓名。
- `vote` 应返回一个 `bool` 值，其中 `true` 表示投票成功，`false` 表示投票失败。

解决这个问题的一种方法是执行以下操作：

1. 遍历每位候选人
   
   1. 检查候选人的姓名是否与输入 `name` 匹配
      
      1. 如果是，增加该候选人的票数并返回 `true`
      2. 如果否，继续检查
2. 如果检查完每位候选人后都没有匹配项，返回 `false`

让我们写一些伪代码来提醒你这样做：

```sql
// Update vote totals given a new vote
bool vote(string name)
{
    // 遍历每位候选人
        // 检查候选人姓名是否与给定姓名匹配
            // 如果是，增加候选人的票数并返回 true

    // 如果没有匹配项，返回 false
}
```

不过，代码实现将留给你来完成！

完成 `print_winner` 函数

最后，完成 `print_winner` 函数。

- 该函数应打印出在选举中获得最多票数的候选人的姓名，然后打印一个换行符。
- 如果多位候选人各自拥有最高票数，选举可能会以平局告终。在这种情况下，你应该输出每位获胜候选人的姓名，每人占一行。

你可能会认为排序算法是解决这个问题的最佳方案：想象一下按票数总计对候选人进行排序，并打印排在首位的候选人（或多位候选人）。但请记住，排序可能开销很大：即使是 Merge Sort（最快的排序算法之一），运行时间也需要 \\(O(N \\space log(N))\\)。

考虑一下，你只需要两条信息就能解决这个问题：

1. 最高票数
2. 获得该票数的候选人（或多位候选人）

因此，一个好的解决方案可能只需要两次搜索。写一些伪代码来提醒自己这样做：

```c
// Print the winner (or winners) of the election
void print_winner(void)
{
    // 找到最高票数

    // 打印获得最高票数的候选人（或多位候选人）

}
```

不过，代码将留给你来完成！

## 视频讲解

## 如何测试

确保测试你的代码，以确保它可以处理……

- 包含任意数量候选人的选举（最多为 `MAX` 值 `9`）
- 按姓名投票给候选人
- 对不在选票上的候选人进行无效投票
- 如果只有一名获胜者，打印选举的获胜者
- 如果有多名获胜者，打印选举的获胜者

### 正确性

```
check50 cs50/problems/2026/x/plurality
```

### 风格

```
style50 plurality.c
```

## 如何提交

在你的终端中，执行以下命令来提交你的作品，并回答出现的提示。

```
submit50 cs50/problems/2026/x/plurality
```
