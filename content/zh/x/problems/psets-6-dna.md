---
title: "DNA - CS50x 2026"
pset: 6
draft: false
---

## 待解决的问题

DNA 是生物体内遗传信息的载体，几十年来一直被用于刑事司法。但是，DNA 分型（DNA profiling）到底是如何运作的呢？给定一段 DNA 序列，法医调查员如何确定它属于谁？

在名为 `dna` 的文件夹中，创建一个名为 `dna.py` 的文件，实现一个能够识别 DNA 序列归属者的程序。

## 演示

## 基础代码

对于这个问题，你将扩展 CS50 工作人员为你提供的代码功能。

下载基础代码

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，执行 `cd` 命令。你应该会发现终端提示符如下所示：

```
$
```

接下来执行

```python
wget https://cdn.cs50.net/2026/x/psets/6/dna.zip
```

以便将名为 `dna.zip` 的 ZIP 文件下载到你的 codespace 中。

然后执行

```
unzip dna.zip
```

来创建一个名为 `dna` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm dna.zip
```

并在提示符处输入 “y” 后按回车键，删除下载的 ZIP 文件。

现在输入

```bash
cd dna
```

并按回车键进入（即打开）该目录。你的提示符现在应该如下所示：

```
dna/ $
```

单独执行 `ls`，你应该会看到一些文件和文件夹：

```
databases/ dna.py sequences/
```

如果你遇到任何困难，请重新按照这些步骤操作，看看能否找出出错的地方！

## 背景知识

DNA 实际上是由被称为核苷酸（nucleotides）的分子组成的序列，排列成特定的形状（双螺旋）。每个人的细胞都有数以十亿计的按顺序排列的核苷酸。每个 DNA 核苷酸包含四种不同的碱基之一：腺嘌呤 (A)、胞嘧啶 (C)、鸟嘌呤 (G) 或胸腺嘧啶 (T)。这段序列（即基因组）的某些部分在几乎所有人中都是相同或非常相似的，但序列的其他部分具有较高的遗传多样性，因此在人群中的差异较大。

DNA 遗传多样性较高的一个地方是短串联重复序列（Short Tandem Repeats，简称 STR）。STR 是一段短的 DNA 碱基序列，往往在人的 DNA 内部特定位置连续重复多次。任何特定 STR 的重复次数在不同个体之间差异很大。例如，在下面的 DNA 样本中，Alice 的 DNA 中有 STR `AGAT` 重复了四次，而 Bob 的同一 STR 重复了五次。

![样本 STR](strs.png)

使用多个 STR 而不是一个，可以提高 DNA 分型的准确性。如果两个人对单个 STR 具有相同重复次数的概率是 5%，而分析人员观察 10 个不同的 STR，那么两个 DNA 样本纯粹巧合匹配的概率大约是千万亿分之一（假设所有 STR 相互独立）。因此，如果两个 DNA 样本在每个 STR 的重复次数上都匹配，分析人员就可以非常有把握地认为它们来自同一个人。FBI 的 [DNA 数据库](https://www.fbi.gov/services/laboratory/biometric-analysis/codis/codis-and-ndis-fact-sheet) CODIS 在其 DNA 分型过程中使用了 20 个不同的 STR。

这样的 DNA 数据库可能是什么样的？在最简单的形式下，你可以想象将 DNA 数据库格式化为一个 CSV 文件，其中每一行对应一个体，每一列对应一个特定的 STR。

```
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

上述文件中的数据表明，Alice 在其 DNA 的某个位置有连续重复 28 次的序列 `AGAT`，序列 `AATG` 重复 42 次，序列 `TATC` 重复 14 次。与此同时，Bob 的这三个 STR 分别重复了 17 次、22 次和 19 次。而 Charlie 的这三个 STR 分别重复了 36、18 和 25 次。

那么，给定一段 DNA 序列，你该如何识别它属于谁呢？想象一下，你在 DNA 序列中寻找 `AGAT` 重复的最长连续序列，发现最长的序列有 17 个重复。如果你随后发现 `AATG` 的最长重复序列是 22 个，`TATC` 的最长重复序列是 19 个，那将提供非常有力的证据证明这段 DNA 是 Bob 的。当然，也有可能在你统计了每个 STR 的计数后，它与 DNA 数据库中的任何人都不匹配，在这种情况下，你就没有匹配项。

在实践中，由于分析人员知道 STR 会出现在哪条染色体以及 DNA 的哪个位置，他们可以将搜索范围锁定在 DNA 的一小部分。但在这个问题中，我们将忽略这个细节。

你的任务是编写一个程序，该程序将接收一段 DNA 序列和一个包含个体列表 STR 计数的 CSV 文件，然后输出这段 DNA（最有可能）属于谁。

## 具体要求

- 程序应要求将包含个体列表 STR 计数的 CSV 文件名作为第一个命令行参数，并要求将待识别 DNA 序列的文本文件名作为第二个命令行参数。
  
  - 如果程序执行时的命令行参数数量不正确，你的程序应该打印一条你选择的错误消息（使用 `print`）。如果提供了正确数量的参数，你可以假设第一个参数确实是一个有效的 CSV 文件的文件名，第二个参数是一个有效的文本文件的文件名。
- 你的程序应该打开 CSV 文件并将其内容读取到内存中。
  
  - 你可以假设 CSV 文件的第一行是列名。第一列将是单词 `name`，其余列将是 STR 序列本身。
- 你的程序应该打开 DNA 序列并将其内容读取到内存中。
- 对于每个 STR（来自 CSV 文件的第一行），你的程序应该计算待识别 DNA 序列中该 STR 的最长连续重复次数。请注意，我们已经为你定义了一个助手函数 `longest_match`，它可以完成这项工作！
- 如果 STR 计数与 CSV 文件中的任何个体完全匹配，你的程序应该打印出该匹配个体的姓名。
  
  - 你可以假设 STR 计数不会匹配多个个体。
  - 如果 STR 计数与 CSV 文件中的任何个体都不完全匹配，你的程序应该打印 `No match`。

## 提示

- 你可能会发现 Python 的 [`csv`](https://docs.python.org/3/library/csv.html) 模块对于将 CSV 文件读取到内存中很有帮助。其中 [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader) 可能特别有用。
  
  - 例如，如果像 `foo.csv` 这样的文件有一行标题行，其中每个字符串是某个字段的名称，那么以下是打印这些 `fieldnames`（字段名）为 `list`（列表）的方法：
    
    ```python
    import csv
    
    with open("foo.csv") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)
    ```
  - 这里展示了如何将 CSV 中的所有（其他）行读入一个 `list`，其中每个元素是一个代表该行的 `dict`（字典）：
    
    ```python
    import csv
    
    rows = []
    with open("foo.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    ```
- [`open`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) 和 [`read`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) 函数对于将文本文件读取到内存中也可能有用。
- 考虑哪些数据结构可能有助于在程序中跟踪信息。[`list`](https://docs.python.org/3/tutorial/introduction.html#lists) 或 [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) 可能会派上用场。
- 记住我们定义了一个函数（`longest_match`），给定 DNA 序列和 STR 作为输入，它会返回该 STR 重复的最大次数。然后你可以在程序的其他部分使用该函数！

## 视频讲解

## 如何测试

虽然此问题可以使用 `check50`，但建议你先自行针对以下每种情况测试代码。

- 运行程序：`python dna.py databases/small.csv sequences/1.txt`。你的程序应该输出 `Bob`。
- 运行程序：`python dna.py databases/small.csv sequences/2.txt`。你的程序应该输出 `No match`。
- 运行程序：`python dna.py databases/small.csv sequences/3.txt`。你的程序应该输出 `No match`。
- 运行程序：`python dna.py databases/small.csv sequences/4.txt`。你的程序应该输出 `Alice`。
- 运行程序：`python dna.py databases/large.csv sequences/5.txt`。你的程序应该输出 `Lavender`。
- 运行程序：`python dna.py databases/large.csv sequences/6.txt`。你的程序应该输出 `Luna`。
- 运行程序：`python dna.py databases/large.csv sequences/7.txt`。你的程序应该输出 `Ron`。
- 运行程序：`python dna.py databases/large.csv sequences/8.txt`。你的程序应该输出 `Ginny`。
- 运行程序：`python dna.py databases/large.csv sequences/9.txt`。你的程序应该输出 `Draco`。
- 运行程序：`python dna.py databases/large.csv sequences/10.txt`。你的程序应该输出 `Albus`。
- 运行程序：`python dna.py databases/large.csv sequences/11.txt`。你的程序应该输出 `Hermione`。
- 运行程序：`python dna.py databases/large.csv sequences/12.txt`。你的程序应该输出 `Lily`。
- 运行程序：`python dna.py databases/large.csv sequences/13.txt`。你的程序应该输出 `No match`。
- 运行程序：`python dna.py databases/large.csv sequences/14.txt`。你的程序应该输出 `Severus`。
- 运行程序：`python dna.py databases/large.csv sequences/15.txt`。你的程序应该输出 `Sirius`。
- 运行程序：`python dna.py databases/large.csv sequences/16.txt`。你的程序应该输出 `No match`。
- 运行程序：`python dna.py databases/large.csv sequences/17.txt`。你的程序应该输出 `Harry`。
- 运行程序：`python dna.py databases/large.csv sequences/18.txt`。你的程序应该输出 `No match`。
- 运行程序：`python dna.py databases/large.csv sequences/19.txt`。你的程序应该输出 `Fred`。
- 运行程序：`python dna.py databases/large.csv sequences/20.txt`。你的程序应该输出 `No match`。

### 正确性

```
check50 cs50/problems/2026/x/dna
```

### 代码风格

```
style50 dna.py
```

## 如何提交

在你的终端中，执行以下命令来提交你的工作，并回答出现的提示。

```
submit50 cs50/problems/2026/x/dna
```
```
