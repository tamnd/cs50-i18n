---
title: "生日记录 - CS50x 2026"
pset: 9
draft: false
---

![生日记录网站截图](birthdays.png)

## 待解决的问题

创建一个 Web 应用程序来记录朋友们的生日。

## 从这里开始

下载发行代码

打开 [cs50.dev](https://cs50.dev/)。

首先点击终端窗口，然后单独执行 `cd` 命令。你会发现其“提示符”类似于下方所示。

```
$
```

点击终端窗口并执行

```python
wget https://cdn.cs50.net/2026/x/psets/9/birthdays.zip
```

然后按回车键，以便在你的 codespace 中下载名为 `birthdays.zip` 的压缩文件。注意不要漏掉 `wget` 与后面 URL 之间的空格，也不要漏掉任何其他字符！

现在执行

```
unzip birthdays.zip
```

以创建一个名为 `birthdays` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm birthdays.zip
```

并在提示处输入 “y” 后按回车，以删除你下载的 ZIP 文件。

现在输入

```bash
cd birthdays
```

然后按回车键将自己移动到（即打开）该目录。你的提示符现在应该类似于下方所示。

```
birthdays/ $
```

如果一切顺利，你应该执行

```bash
ls
```

并且你应该会看到以下文件和文件夹：

```
app.py  birthdays.db  static/  templates/
```

如果你遇到任何麻烦，请再次执行这些相同的步骤，看看你是否能找出哪里出了问题！

## 理解代码

在 `app.py` 中，你会看到一个 Flask Web 应用程序的起始代码。该应用程序有一个路由（`/`），它同时接受 `POST` 请求（在 `if` 之后）和 `GET` 请求（在 `else` 之后）。目前，当通过 `GET` 请求 `/` 路由时，会渲染 `index.html` 模板。当通过 `POST` 请求 `/` 路由时，用户会通过 `GET` 重定向回 `/`。

`birthdays.db` 是一个 SQLite 数据库，其中有一个表 `birthdays`，包含四列：`id`、`name`、`month` 和 `day`。该表中已经有几行数据，但最终你的 Web 应用程序将支持向该表中插入行的功能！

在 `static` 目录中是一个 `styles.css` 文件，包含此 Web 应用程序的 CSS 代码。无需编辑此文件，但如果你愿意，也可以自行修改！

在 `templates` 目录中是一个 `index.html` 文件，当用户查看你的 Web 应用程序时，该文件将被渲染。

## 实现细节

完成 Web 应用程序的实现，让用户能够存储并记录生日。

- 当通过 `GET` 请求 `/` 路由时，你的 Web 应用程序应该在一个表格中显示数据库中所有的人及其生日。
  
  - 首先，在 `app.py` 中，在 `GET` 请求处理逻辑中添加代码，查询 `birthdays.db` 数据库以获取所有生日。将所有这些数据传递给你的 `index.html` 模板。
  - 然后，在 `index.html` 中，添加逻辑将每个生日渲染为表格中的一行。每行应该有两列：一列显示人的姓名，另一列显示人的生日。
- 当通过 `POST` 请求 `/` 路由时，你的 Web 应用程序应该向数据库中添加一个新的生日，然后重新渲染索引页面。
  
  - 首先，在 `index.html` 中添加一个 HTML 表单。该表单应允许用户输入姓名、生日月份和生日日期。确保表单提交到 `/`（其 “action”），并且方法为 `post`。
  - 然后，在 `app.py` 中，在 `POST` 请求处理逻辑中添加代码，根据用户提供的数据向 `birthdays` 表中 `INSERT`（插入）一个新行。

可选地，你还可以：

- 添加删除和/或编辑生日条目的功能。
- 添加你选择的任何其他功能！

## 提示

创建一个表单供用户提交生日

在 `index.html` 中，注意以下 TODO：

```python
<!-- TODO: Create a form for users to submit a name, a month, and a day -->
```

回想一下，要创建一个表单，你可以使用 `form` HTML 元素。你可以使用以下开始和结束标签创建一个 `form` HTML 元素：

```
<form>
</form>
```

当然，表单仍然需要输入字段（以及一个供用户提交表单的按钮！）。回想一下，HTML `input` 元素可以在表单中创建输入框等内容。你可以指定它们的 `type` 属性，使其接受 `text`（文本）或 `number`（数字）。同时为 `input` 元素提供 `name` 属性，以便区分它们。

```
<form>
    <input name="name" type="text">
    <input name="month" type="number">
    <input name="day" type="number">
</form>
```

你的表单可能会从一个供用户点击以提交数据的按钮中受益。添加一个 `type` 为 `submit` 的 `input` 元素，这将允许用户执行该操作。如果你希望按钮本身带有解释性文本，请尝试设置 `value` 属性。

```
<form>
    <input name="name" type="text">
    <input name="month" type="number">
    <input name="day" type="number">
    <input type="submit" value="Add Birthday">
</form>
```

用户的资料将提交到哪里？目前，哪里都不会提交！回想一下，你可以指定表单的 `action` 属性，以决定提交表单后应请求哪个路由。表单数据将随生成的请求一起提交。`method` 属性指定提交表单时使用的 HTTP 请求方法。

```
<form action="/" method="post">
    <input name="name" type="text">
    <input name="month" type="number">
    <input name="day" type="number">
    <input type="submit" value="Add Birthday">
</form>
```

到此为止，你的表单应该已经可以正常工作了，但仍有改进空间！考虑添加 `placeholder`（占位符）值来修饰一下：

```
<form action="/" method="post">
    <input name="name" placeholder="Name" type="text">
    <input name="month" placeholder="Month" type="number">
    <input name="day" placeholder="Day" type="number">
    <input type="submit" value="Add Birthday">
</form>
```

此外，考虑添加一些 *客户端验证*，以确保用户配合你表单的设计意图。例如，一个 `type` 为 `number` 的 `input` 字段还可以指定 `min` 和 `max` 属性，这决定了用户可以输入的最小值和最大值。

```
<form action="/" method="post">
    <input name="name" placeholder="Name" type="text">
    <input name="month" placeholder="Month" type="number" min="1" max="12">
    <input name="day" placeholder="Day" type="number" min="1" max="31">
    <input type="submit" value="Add Birthday">
</form>
```

将用户的表单提交添加到数据库中

在 `app.py` 中，注意以下 TODO：

```
# TODO: Add the user's entry into the database
```

回想一下，Flask 有一些方便的方法来访问通过 `POST` 提交的表单数据！特别是：

```
# Access form data
request.form.get(NAME)
```

其中 `NAME` 指的是带有提交数据的特定 `input` 元素的 `name` 属性。如果你的 `input` 元素被命名为 `name`、`month` 和 `day`，你可以分别通过以下方式访问（并存储！）它们的值：

```
# Access form data
name = request.form.get("name")
month = request.form.get("month")
day = request.form.get("day")
```

现在，用户在 `name`、`month` 和 `day` 输入元素中提交的值就可以作为 Python 变量使用了。

下一步是将这些值添加到你的数据库中！多亏了这一行

```
db = SQL("sqlite:///birthdays.db")
```

`app.py` 已经建立了与 `birthdays.db` 的连接，名为 `db`。你现在可以通过调用 `db.execute` 并传入有效的 SQL 查询来执行 SQL 查询。如果你想添加 Carter 在 1 月 1 日的生日，你可能会运行以下 SQL 语句：

```sql
INSERT INTO birthdays (name, month, day) VALUES('Carter', 1, 1);
```

配置 `app.py` 来运行相同的查询，但使用占位符来表示要插入的值，如下所示：

```sql
# Access form data
name = request.form.get("name")
month = request.form.get("month")
day = request.form.get("day")

# Insert data into database
db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
```

这样就可以了！尝试提交表单，打开 `birthdays.db`，并使用 `SELECT` 查询来查看 `birthdays` 表的内容。你应该能看到你提交的表单数据。

当你创建更高级的应用程序时，你还需要添加 *服务器端验证*：也就是说，在执行任何其他操作 *之前* 检查用户的数据是否有效的方法！你可能进行的第一个验证是用户是否提交了任何数据！如果你在用户未提交任何数据的情况下尝试通过 `request.form.get` 获取表单数据，`request.form.get` 将返回一个空字符串。你可以在 Python 中按如下方式检查此值：

```sql
# Access form data
name = request.form.get("name")
if not name:
    return redirect("/")

month = request.form.get("month")
if not month:
    return redirect("/")

day = request.form.get("day")
if not day:
    return redirect("/")

# Insert data into database
db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
```

现在，除非你确定用户已经提供了你所需的所有数据，否则你不会插入行。

还有一些事情可能会出错！如果用户实际上没有为 `month` 或 `day` 提供数字值怎么办？一种检查方法是 `try`（尝试）使用 `int` 将值转换为整数，如果转换失败，则将用户重定向回主页。

```sql
# Access form data
name = request.form.get("name")
if not name:
    return redirect("/")

month = request.form.get("month")
if not month:
    return redirect("/")
try:
    month = int(month)
except ValueError:
    return redirect("/")

day = request.form.get("day")
if not day:
    return redirect("/")
try:
    day = int(day)
except ValueError:
    return redirect("/")

# Insert data into database
db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
```

而且，即使用户输入了数字，最好也检查它是否在正确的范围内！

```sql
# Access form data
name = request.form.get("name")
if not name:
    return redirect("/")

month = request.form.get("month")
if not month:
    return redirect("/")
try:
    month = int(month)
except ValueError:
    return redirect("/")
if month < 1 or month > 12:
    return redirect("/")

day = request.form.get("day")
if not day:
    return redirect("/")
try:
    day = int(day)
except ValueError:
    return redirect("/")
if day < 1 or day > 31:
    return redirect("/")

# Insert data into database
db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
```

渲染 `birthdays.db` 中的生日

一旦用户可以提交生日并将其存储在 `birthdays.db` 中，你的下一个任务就是确保这些生日在 `index.html` 中被渲染出来。

首先，你需要从 `birthdays.db` 中检索所有生日。你可以使用以下 SQL 查询来实现：

```sql
SELECT * FROM birthdays;
```

在 `app.py` 中看到以下 TODO：

```
# TODO: Display the entries in the database on index.html
```

考虑配置 `app.py`，以便在每次通过 `GET` 请求加载页面时运行此 SQL 查询：

```sql
# Query for all birthdays
birthdays = db.execute("SELECT * FROM birthdays")
```

现在，`birthdays.db` 的 `birthdays` 表中的所有生日都保存在名为 `birthdays` 的 Python 变量中。具体来说，SQL 查询的结果以字典列表的形式存储。每个字典代表查询返回的一行，字典中的每个键对应 `birthdays` 表的一个列名（即 “name”、“month” 和 “day”）。

要在 `index.html` 中渲染这些生日，你可以依靠 Flask 的 `render_template` 函数。你可以通过指定一个也叫 `birthdays` 的关键字参数，并将其设置为你刚刚创建的 `birthdays` 变量，来指定应使用 `birthdays` 变量来渲染 `index.html`。

```sql
# Query for all birthdays
birthdays = db.execute("SELECT * FROM birthdays")

# Render birthdays page
return render_template("index.html", birthdays=birthdays)
```

需要说明的是，`=` 左侧的名字 `birthdays` 是你在 `index.html` 内部访问生日数据时所使用的名字。

现在 `index.html` 在渲染时可以访问生日数据了，你可以使用 Jinja 来正确渲染数据。Jinja 和 Python 一样，可以循环遍历列表中的元素。而且 Jinja 和 Python 一样，可以通过键访问字典中的元素。在这种情况下，执行此操作的 Jinja 语法是字典名，后跟一个 `.`，然后是要访问的键名。

```
{% for birthday in birthdays %}
    <tr>
        <td>{{ birthday.name }}</td>
        <td>{{ birthday.month }}/{{ birthday.day }}</td>
    </tr>
{% endfor %}
```

就是这样！尝试重新加载页面以查看渲染出的生日。

### 视频演示

此视频是在课程仍使用 CS50 IDE 编写代码时录制的。虽然界面可能与你的 codespace 不同，但这两个环境的行为应该是基本相似的！

不知道如何解决？

### 测试

本题集没有 `check50`！但请务必通过添加一些生日并确保数据如预期出现在表格中来测试你的 Web 应用程序。

在你的 `birthdays` 目录中，在终端运行 `flask run` 来启动一个为你的 Flask 应用程序提供服务的 Web 服务器。

## 如何提交

在你的终端中，执行以下命令来提交你的工作，并回答出现的提示。

```
submit50 cs50/problems/2026/x/birthdays
```
