---
title: "Credit - CS50x 2026"
pset: 6
draft: false
---

## 待解决的问题

在一个名为 `sentimental-credit` 的文件夹中创建一个名为 `credit.py` 的文件，编写一个程序，提示用户输入信用卡号，然后报告（通过 `print`）它是否是一个有效的 American Express、MasterCard 或 Visa 卡号，就像你在 [Problem Set 1](../../1/) 中所做的那样。这次你的程序应该用 Python 编写！

## 演示

## 规格要求

- 为了我们可以自动测试你的代码，我们要求你程序的最后一行输出是 `AMEX\n`、`MASTERCARD\n`、`VISA\n` 或 `INVALID\n`，不多不少。
- 为简单起见，你可以假设用户的输入将完全是数字（即没有连字符，就像印在实际卡片上的一样）。
- 最好使用 CS50 库中的 `get_int` 或 `get_string` 来获取用户的输入，具体取决于你决定如何实现。

## 提示

- 可以使用正则表达式来验证用户输入。例如，你可以使用 Python 的 [`re`](https://docs.python.org/3/library/re.html) 模块来检查用户的输入是否确实是长度正确的数字序列。

## 如何测试

虽然此题目提供了 `check50`，但我们鼓励你首先自行测试以下各项。

- 运行程序 `python credit.py`，等待输入提示。输入 `378282246310005` 并按回车。你的程序应该输出 `AMEX`。
- 运行程序 `python credit.py`，等待输入提示。输入 `371449635398431` 并按回车。你的程序应该输出 `AMEX`。
- 运行程序 `python credit.py`，等待输入提示。输入 `5555555555554444` 并按回车。你的程序应该输出 `MASTERCARD`。
- 运行程序 `python credit.py`，等待输入提示。输入 `5105105105105100` 并按回车。你的程序应该输出 `MASTERCARD`。
- 运行程序 `python credit.py`，等待输入提示。输入 `4111111111111111` 并按回车。你的程序应该输出 `VISA`。
- 运行程序 `python credit.py`，等待输入提示。输入 `4012888888881881` 并按回车。你的程序应该输出 `VISA`。
- 运行程序 `python credit.py`，等待输入提示。输入 `1234567890` 并按回车。你的程序应该输出 `INVALID`。

### 正确性

```
check50 cs50/problems/2026/x/sentimental/credit
```

### 风格

```
style50 credit.py
```

## 如何提交

在你的终端中，执行以下命令来提交你的作品，并根据提示进行操作。

```
submit50 cs50/problems/2026/x/sentimental/credit
```
