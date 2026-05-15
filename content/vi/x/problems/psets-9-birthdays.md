title: "Ngày sinh nhật (Birthdays) - CS50x 2026"
pset: 9
draft: "false"
---

![ảnh chụp màn hình trang web birthdays](birthdays.png)

## Bài toán cần giải quyết

Tạo một ứng dụng web để theo dõi ngày sinh nhật của bạn bè.

## Bắt đầu

Tải mã nguồn phân phối (distribution code)

Mở [cs50.dev](https://cs50.dev/).

Bắt đầu bằng cách nhấp chuột vào bên trong cửa sổ terminal, sau đó thực thi lệnh `cd`. Bạn sẽ thấy "dấu nhắc" (prompt) của nó tương tự như dưới đây.

```
$
```

Nhấp vào bên trong cửa sổ terminal đó và thực thi lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/9/birthdays.zip
```

theo sau là phím Enter để tải xuống tệp ZIP có tên `birthdays.zip` vào codespace của bạn. Hãy cẩn thận đừng bỏ sót khoảng trắng giữa `wget` và URL theo sau, hoặc bất kỳ ký tự nào khác!

Bây giờ hãy thực thi lệnh

```
unzip birthdays.zip
```

để tạo một thư mục có tên `birthdays`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi lệnh

```
rm birthdays.zip
```

và trả lời "y" rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy gõ

```bash
cd birthdays
```

theo sau là phím Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ tương tự như dưới đây.

```
birthdays/ $
```

Nếu mọi thứ thành công, bạn nên thực thi lệnh

```bash
ls
```

và bạn sẽ thấy các tệp và thư mục sau:

```
app.py  birthdays.db  static/  templates/
```

Nếu bạn gặp bất kỳ khó khăn nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã làm sai ở đâu không!

## Tìm hiểu

Trong `app.py`, bạn sẽ tìm thấy phần bắt đầu của một ứng dụng web Flask. Ứng dụng có một đường dẫn (route) (`/`) chấp nhận cả yêu cầu `POST` (sau `if`) và yêu cầu `GET` (sau `else`). Hiện tại, khi đường dẫn `/` được yêu cầu qua `GET`, bản mẫu (template) `index.html` sẽ được hiển thị (render). Khi đường dẫn `/` được yêu cầu qua `POST`, người dùng sẽ được chuyển hướng ngược lại `/` qua `GET`.

`birthdays.db` là một cơ sở dữ liệu SQLite với một bảng, `birthdays`, có bốn cột: `id`, `name`, `month`, và `day`. Đã có một vài hàng trong bảng này, mặc dù cuối cùng ứng dụng web của bạn sẽ hỗ trợ khả năng chèn thêm các hàng mới vào bảng này!

Trong thư mục `static` là tệp `styles.css` chứa mã CSS cho ứng dụng web này. Không cần phải chỉnh sửa tệp này, tuy nhiên bạn có thể làm vậy nếu muốn!

Trong thư mục `templates` là tệp `index.html` sẽ được hiển thị khi người dùng xem ứng dụng web của bạn.

## Chi tiết triển khai

Hoàn thành việc triển khai ứng dụng web để cho phép người dùng lưu trữ và theo dõi ngày sinh nhật.

- Khi đường dẫn `/` được yêu cầu qua `GET`, ứng dụng web của bạn sẽ hiển thị, trong một bảng, tất cả những người trong cơ sở dữ liệu cùng với ngày sinh của họ.
  
  - Đầu tiên, trong `app.py`, thêm logic trong phần xử lý yêu cầu `GET` để truy vấn cơ sở dữ liệu `birthdays.db` cho tất cả các ngày sinh nhật. Truyền tất cả dữ liệu đó vào bản mẫu `index.html` của bạn.
  - Sau đó, trong `index.html`, thêm logic để hiển thị mỗi ngày sinh nhật như một hàng trong bảng. Mỗi hàng nên có hai cột: một cột cho tên của người đó và một cột khác cho ngày sinh của họ.
- Khi đường dẫn `/` được yêu cầu qua `POST`, ứng dụng web của bạn sẽ thêm một ngày sinh nhật mới vào cơ sở dữ liệu và sau đó hiển thị lại trang chủ.
  
  - Đầu tiên, trong `index.html`, thêm một biểu mẫu (form) HTML. Biểu mẫu này nên cho phép người dùng nhập tên, tháng sinh và ngày sinh. Đảm bảo biểu mẫu gửi dữ liệu đến `/` (thuộc tính "action" của nó) với phương thức (method) là `post`.
  - Sau đó, trong `app.py`, thêm logic trong phần xử lý yêu cầu `POST` để `INSERT` một hàng mới vào bảng `birthdays` dựa trên dữ liệu do người dùng cung cấp.

Tùy chọn, bạn cũng có thể:

- Thêm khả năng xóa và/hoặc chỉnh sửa các mục ngày sinh nhật.
- Thêm bất kỳ tính năng bổ sung nào tùy chọn!

## Gợi ý

Tạo một biểu mẫu để người dùng có thể gửi ngày sinh nhật

Trong `index.html`, hãy chú ý phần TODO sau:

```python
<!-- TODO: Create a form for users to submit a name, a month, and a day -->
```

Hãy nhớ rằng, để tạo một biểu mẫu, bạn có thể sử dụng phần tử HTML `form`. Bạn có thể tạo một phần tử HTML `form` với các thẻ đóng và mở sau:

```
<form>
</form>
```

Tất nhiên, một biểu mẫu vẫn cần các trường nhập dữ liệu (và một nút để người dùng có thể gửi biểu mẫu!). Hãy nhớ rằng các phần tử HTML `input` tạo ra, cùng với những thứ khác, các hộp nhập liệu trong một biểu mẫu. Bạn có thể chỉ định thuộc tính `type` của chúng để cho phép chúng chấp nhận văn bản (`text`) hoặc số (`number`). Đồng thời cung cấp cho các phần tử `input` một thuộc tính `name` để bạn có thể phân biệt chúng.

```
<form>
    <input name="name" type="text">
    <input name="month" type="number">
    <input name="day" type="number">
</form>
```

Biểu mẫu của bạn có thể cần một nút bấm để người dùng có thể nhấp vào nhằm gửi dữ liệu của họ. Thêm một phần tử `input` có loại `submit`, điều này sẽ cho phép người dùng thực hiện việc đó. Nếu bạn muốn bản thân nút bấm có văn bản giải thích, hãy thử thiết lập thuộc tính `value`.

```
<form>
    <input name="name" type="text">
    <input name="month" type="number">
    <input name="day" type="number">
    <input type="submit" value="Add Birthday">
</form>
```

Dữ liệu của người dùng sẽ được gửi đi đâu? Hiện tại thì chưa đi đâu cả! Hãy nhớ rằng bạn có thể chỉ định thuộc tính `action` của biểu mẫu để quyết định đường dẫn nào sẽ được yêu cầu sau khi biểu mẫu được gửi. Dữ liệu biểu mẫu sẽ được gửi cùng với yêu cầu kết quả. Thuộc tính `method` chỉ định phương thức yêu cầu HTTP nào sẽ được sử dụng khi gửi biểu mẫu.

```
<form action="/" method="post">
    <input name="name" type="text">
    <input name="month" type="number">
    <input name="day" type="number">
    <input type="submit" value="Add Birthday">
</form>
```

Với điều đó, biểu mẫu của bạn sẽ hoạt động hoàn hảo, mặc dù nó vẫn có thể được cải thiện! Hãy cân nhắc thêm các giá trị `placeholder` để làm mọi thứ sinh động hơn một chút:

```
<form action="/" method="post">
    <input name="name" placeholder="Name" type="text">
    <input name="month" placeholder="Month" type="number">
    <input name="day" placeholder="Day" type="number">
    <input type="submit" value="Add Birthday">
</form>
```

Và hãy cân nhắc thêm một số *kiểm tra dữ liệu phía máy khách (client-side validation)*, để đảm bảo người dùng hợp tác đúng với mục đích của biểu mẫu. Ví dụ, một trường `input` loại `number` cũng có thể có thuộc tính `min` và `max` được chỉ định, giúp xác định giá trị tối thiểu và tối đa mà người dùng có thể nhập.

```
<form action="/" method="post">
    <input name="name" placeholder="Name" type="text">
    <input name="month" placeholder="Month" type="number" min="1" max="12">
    <input name="day" placeholder="Day" type="number" min="1" max="31">
    <input type="submit" value="Add Birthday">
</form>
```

Thêm dữ liệu gửi từ biểu mẫu của người dùng vào cơ sở dữ liệu

Trong `app.py`, hãy chú ý phần TODO sau:

```
# TODO: Add the user's entry into the database
```

Hãy nhớ rằng Flask có một số phương thức tiện dụng để truy cập dữ liệu biểu mẫu được gửi qua `POST`! Cụ thể là:

```
# Access form data
request.form.get(NAME)
```

trong đó `NAME` đề cập đến thuộc tính `name` của phần tử `input` cụ thể có dữ liệu được gửi. Nếu các phần tử `input` của bạn được đặt tên là `name`, `month`, và `day`, bạn có thể truy cập (và lưu trữ!) các giá trị của chúng tương ứng như sau:

```
# Access form data
name = request.form.get("name")
month = request.form.get("month")
day = request.form.get("day")
```

Bây giờ, các giá trị do người dùng gửi trong các phần tử nhập liệu `name`, `month`, và `day` đã có sẵn cho bạn dưới dạng các biến Python.

Bước tiếp theo là thêm các giá trị này vào cơ sở dữ liệu của bạn! Nhờ dòng lệnh cụ thể này

```
db = SQL("sqlite:///birthdays.db")
```

`app.py` đã thiết lập kết nối tới `birthdays.db` dưới tên gọi `db`. Bây giờ bạn có thể thực thi các truy vấn SQL bằng cách gọi `db.execute` với một truy vấn SQL hợp lệ. Nếu bạn muốn thêm ngày sinh của Carter vào ngày 1 tháng 1, bạn có thể chạy câu lệnh SQL sau:

```sql
INSERT INTO birthdays (name, month, day) VALUES('Carter', 1, 1);
```

Cấu hình `app.py` để chạy cùng truy vấn đó, nhưng sử dụng các trình giữ chỗ (placeholder) cho các giá trị cần chèn, như sau:

```sql
# Access form data
name = request.form.get("name")
month = request.form.get("month")
day = request.form.get("day")

# Insert data into database
db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
```

Và như vậy là xong! Hãy thử gửi biểu mẫu, mở `birthdays.db` và sử dụng truy vấn `SELECT` để xem nội dung của bảng `birthdays`. Bạn sẽ thấy dữ liệu biểu mẫu đã gửi có sẵn cho bạn.

Khi bạn tạo các ứng dụng nâng cao hơn, bạn cũng sẽ muốn thêm *kiểm tra dữ liệu phía máy chủ (server-side validation)*: nghĩa là một cách để kiểm tra xem dữ liệu của người dùng có hợp lệ hay không *trước khi* thực hiện bất kỳ việc gì khác! Một trong những bước kiểm tra đầu tiên bạn có thể thực hiện là liệu người dùng có gửi bất kỳ dữ liệu nào hay không! Nếu bạn cố gắng lấy dữ liệu biểu mẫu bằng `request.form.get` khi người dùng không gửi gì, `request.form.get` sẽ trả về một chuỗi trống. Bạn có thể kiểm tra giá trị này trong Python như sau:

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

Giờ đây, bạn sẽ không chèn một hàng mới cho đến khi chắc chắn rằng người dùng đã cung cấp tất cả dữ liệu bạn cần.

Vẫn còn một vài điều có thể sai sót! Điều gì sẽ xảy ra nếu người dùng thực tế không cung cấp giá trị số cho `month` hoặc `day`? Một cách để kiểm tra là `try` (thử) chuyển đổi giá trị sang kiểu số nguyên với `int` và nếu quá trình chuyển đổi thất bại, hãy chuyển hướng người dùng quay lại trang chủ.

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

Và ngay cả khi người dùng đã nhập một con số, tốt nhất là hãy kiểm tra xem nó có nằm trong phạm vi chính xác hay không!

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

Hiển thị ngày sinh nhật từ `birthdays.db`

Sau khi người dùng có thể gửi ngày sinh nhật và lưu trữ chúng trong `birthdays.db`, nhiệm vụ tiếp theo của bạn là đảm bảo những ngày sinh nhật đó được hiển thị trong `index.html`.

Đầu tiên, bạn cần lấy tất cả các ngày sinh nhật từ `birthdays.db`. Bạn có thể làm vậy với truy vấn SQL:

```sql
SELECT * FROM birthdays;
```

Xem phần TODO sau trong `app.py`:

```
# TODO: Display the entries in the database on index.html
```

Hãy cân nhắc cấu hình `app.py` để chạy truy vấn SQL này mỗi khi trang được tải bằng yêu cầu `GET`:

```sql
# Query for all birthdays
birthdays = db.execute("SELECT * FROM birthdays")
```

Bây giờ, tất cả các ngày sinh trong bảng `birthdays` của `birthdays.db` đều có sẵn cho bạn trong một biến Python tên là `birthdays`. Cụ thể, kết quả của truy vấn SQL được lưu trữ dưới dạng một danh sách các từ điển (dictionaries). Mỗi từ điển đại diện cho một hàng được trả về bởi truy vấn và mỗi khóa (key) trong từ điển tương ứng với tên cột của bảng `birthdays` (tức là "name", "month", và "day").

Để hiển thị các ngày sinh nhật này trong `index.html`, bạn có thể dựa vào hàm `render_template` của Flask. Bạn có thể chỉ định rằng `index.html` nên được hiển thị với biến `birthdays` bằng cách chỉ định một đối số từ khóa, cũng được gọi là `birthdays`, và đặt nó bằng biến `birthdays` bạn vừa tạo.

```sql
# Query for all birthdays
birthdays = db.execute("SELECT * FROM birthdays")

# Render birthdays page
return render_template("index.html", birthdays=birthdays)
```

Để làm rõ, cái tên ở phía bên trái của dấu `=`, `birthdays`, là cái tên mà bạn có thể sử dụng để truy cập dữ liệu ngày sinh nhật ngay bên trong chính tệp `index.html`.

Bây giờ `index.html` đang được hiển thị với quyền truy cập vào dữ liệu ngày sinh nhật, bạn có thể sử dụng Jinja để hiển thị dữ liệu một cách hợp lý. Jinja, giống như Python, có thể lặp qua các phần tử của một danh sách. Và Jinja, giống như Python, có thể truy cập các phần tử của một từ điển thông qua các khóa của chúng. Trong trường hợp này, cú pháp Jinja để thực hiện việc đó là tên của từ điển, theo sau là dấu `.`, rồi đến tên của khóa cần truy cập.

```
{% for birthday in birthdays %}
    <tr>
        <td>{{ birthday.name }}</td>
        <td>{{ birthday.month }}/{{ birthday.day }}</td>
    </tr>
{% endfor %}
```

Và thế là xong! Hãy thử tải lại trang để xem các ngày sinh nhật được hiển thị.

### Hướng dẫn chi tiết

Video này được ghi lại khi khóa học vẫn còn sử dụng CS50 IDE để viết mã. Mặc dù giao diện có thể trông khác so với codespace của bạn, nhưng hành vi của hai môi trường này về cơ bản là tương tự nhau!

Bạn không chắc chắn cách giải quyết?

### Kiểm tra

Không có `check50` cho bài tập này! Nhưng hãy chắc chắn kiểm tra ứng dụng web của bạn bằng cách thêm một số ngày sinh nhật và đảm bảo rằng dữ liệu xuất hiện trong bảng của bạn như mong đợi.

Chạy lệnh `flask run` trong terminal khi đang ở thư mục `birthdays` để khởi động máy chủ web phục vụ ứng dụng Flask của bạn.

## Cách nộp bài

Trong terminal của bạn, thực thi lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/birthdays
```
