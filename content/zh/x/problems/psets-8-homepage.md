---
title: "个人主页 - CS50x 2026"
pset: 8
draft: false
---

使用 HTML、CSS 和 JavaScript 构建一个简单的个人主页。

## 背景

互联网实现了许多不可思议的事情：我们可以使用搜索引擎研究任何可以想象到的事物，与全球的朋友和家人交流，玩游戏，参加课程等等。但事实证明，我们访问的几乎所有页面都是基于三种核心语言构建的，每种语言都有略微不同的用途：

1. HTML，即 *超文本标记语言*（HyperText Markup Language），用于描述网站的内容；
2. CSS，即 *层叠样式表*（Cascading Style Sheets），用于描述网站的美学样式；以及
3. JavaScript，用于使网站具有交互性和动态性。

创建一个简单的个人主页，介绍你自己、你最喜欢的爱好或课外活动，或者你感兴趣的其他任何内容。

## 入门

登录 [cs50.dev](https://cs50.dev/)，点击你的终端窗口，然后单独执行 `cd` 命令。你应该会发现终端窗口的提示符类似于下方所示：

```
$
```

接下来执行

```python
wget https://cdn.cs50.net/2026/x/psets/8/homepage.zip
```

以便将名为 `homepage.zip` 的 ZIP 文件下载到你的 codespace 中。

然后执行

```
unzip homepage.zip
```

以创建一个名为 `homepage` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm homepage.zip
```

并在提示符处输入 “y” 后按回车键，以删除你下载的 ZIP 文件。

现在输入

```bash
cd homepage
```

后按回车键以进入（即打开）该目录。你的提示符现在应该类似于下方所示。

```
homepage/ $
```

单独执行 `ls`，你应该会看到几个文件：

```
index.html  styles.css
```

如果你遇到任何问题，请再次按照这些步骤操作，看看能否找出出错的地方！你可以通过在终端窗口中运行以下命令来立即启动服务器以查看你的站点

```
http-server
```

在终端窗口中执行。然后，在出现的第一个链接上点击 `Command`+点击（如果是 Mac）或 `Control`+点击（如果是 PC）：

```
http-server running on LINK
```

其中 LINK 是你服务器的地址。

## 规范

在你的 `homepage` 目录中实现一个网站，该网站必须：

- 包含至少四个不同的 `.html` 页面，其中至少一个是 `index.html`（你网站的主页），并且应该可以通过点击一个或多个超链接从网站的任何页面跳转到其他任何页面。
- 使用至少十（10）个不同的 HTML 标签，除了 `<html>`、`<head>`、`<body>` 和 `<title>` 之外。多次使用某个标签（例如 `<p>`）仍仅计为这十个标签中的一（1）个！
- 将 Bootstrap 的一个或多个功能集成到你的站点中。Bootstrap 是一个流行的库（带有许多 CSS 类等），你可以通过它来美化你的站点。请参阅 [Bootstrap 的文档](https://getbootstrap.com/docs/5.2/) 开始使用。特别是，你可能会发现一些 [Bootstrap 的组件](https://getbootstrap.com/docs/5.2/components/) 很有趣。要将 Bootstrap 添加到你的站点，只需在页面的 `<head>` 中包含以下内容：
  
  ```
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ho+j7jyWK8fNQe+A12Hb8AhRq26LrZ/JpcUGGOn+Y7RsweNrtN/tE3MoK7ZeZDyx" crossorigin="anonymous"></script>
  ```
  
  在此之下你还可以包含
  
  ```
  <link href="styles.css" rel="stylesheet">
  ```
  
  以链接你自己的 CSS。
- 拥有至少一个由你自己创建的样式表文件 `styles.css`，其中至少使用五（5）个不同的 CSS 选择器（例如：标签 (`example`)、类 (`.example`) 或 ID (`#example`)），并且在其中总共使用至少五（5）种不同的 CSS 属性，例如 `font-size` 或 `margin`；以及
- 将 JavaScript 的一个或多个功能集成到你的站点中，使你的站点更具交互性。例如，你可以使用 JavaScript 添加警报、在循环间隔内产生效果，或者为按钮、下拉菜单或表单添加交互性。请随意发挥创意！
- 确保你的站点在移动设备以及笔记本电脑和台式机的浏览器上看起来都很美观。

你还应该创建一个文本文件 `specification.txt`，列出你使用的 10 个 HTML 标签和 5 个 CSS 属性，以及关于你如何选择使用 JavaScript 和 Bootstrap 的简短（一句话）描述。

## 测试

如果你想在工作时查看站点的外观，可以运行 `http-server`。点击 `http-server` 提供的第一个链接（Mac 请按 `Command`，PC 请按 `Control`），这应该会在新标签页中打开你的网页。然后，你应该能够刷新包含网页的标签页以查看最新的更改。

另请记住，通过打开 Google Chrome 中的开发者工具，你可以通过点击开发者工具窗口中 **Elements** 左侧的手机形状图标来 *模拟* 在移动设备上访问页面，或者在已打开开发者工具标签页的情况下，在 PC 上按 `Ctrl`+`Shift`+`M` 或在 Mac 上按 `Cmd`+`Shift`+`M`，而无需单独在移动设备上访问你的站点！

## 评估

本次作业没有 `check50`！相反，你的站点正确性将根据你是否符合上述规范要求，以及你的 HTML 是否格式良好且有效来进行评估。为了确保你的页面符合要求，你可以使用这个 [标记验证服务](https://validator.w3.org/#validate_by_input)，将你的 HTML 直接复制并粘贴到提供的文本框中。请务必在提交之前消除验证器建议的所有警告或错误！

另请考虑：

- 网站的美学设计是否直观且易于用户导航；
- 你的 CSS 是否已提取到单独的 CSS 文件中；以及
- 你是否通过从父标签“层叠”样式属性来避免了重复和冗余。

遗憾的是 `style50` 不支持 HTML 文件，因此你有责任整齐地缩进和对齐你的 HTML 标签。另请注意，你可以使用以下方式创建 HTML 注释：

```
<!-- 注释内容写在这里 -->
```

但在 HTML 代码中编写注释并不像在 C 或 Python 等语言中那样紧迫。你也可以在 CSS 文件中使用以下方式为 CSS 编写注释：

```
/* 注释内容写在这里 */
```

## 提示

有关本次问题中介绍的语言的相当全面的指南，请查看这些教程：

- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [JavaScript](https://www.w3schools.com/js/)

## 如何提交

在终端中执行以下命令来提交你的工作，并回答出现的提示。

```
submit50 cs50/problems/2026/x/homepage
```
