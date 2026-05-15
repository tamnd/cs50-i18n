---
title: "Hello, Again - CS50x 2026"
pset: 6
draft: false
---

## 待解决的问题

在一个名为 `sentimental-hello` 的文件夹中创建一个名为 `hello.py` 的文件，实现一个程序，提示用户输入姓名，然后打印 `hello, so-and-so`，其中 `so-and-so` 是他们提供的姓名，就像你在 [Problem Set 1](../../1/) 中所做的那样。不同的是，这次你的程序应该用 Python 编写！

提示

- 请记住，你可以使用 `get_string` 从用户那里获取一个 `str`，它是在 `cs50` 库中声明的。
- 请记住，你可以使用 `print` 打印 `str`。
- 请记住，在 Python 中，你可以通过在字符串前加上 `f` 来创建格式化字符串。例如，`f"{name}"` 将在你编写 `{name}` 的地方替换（“插值”）变量 `name` 的值。

## 演示

## 如何测试

虽然此题目提供了 `check50`，但我们鼓励你首先自行测试以下各项。

- 运行程序 `python hello.py`，等待输入提示。输入 `David` 并按回车。你的程序应该输出 `hello, David`。
- 运行程序 `python hello.py`，等待输入提示。输入 `Inno` 并按回车。你的程序应该输出 `hello, Inno`。
- 运行程序 `python hello.py`，等待输入提示。输入 `Kamryn` 并按回车。你的程序应该输出 `hello, Kamryn`。

### 正确性

```
check50 cs50/problems/2026/x/sentimental/hello
```

### 风格

```
style50 hello.py
```

## 如何提交

在你的终端中，执行以下命令来提交你的作品，并根据提示进行操作。

```
submit50 cs50/problems/2026/x/sentimental/hello
```
