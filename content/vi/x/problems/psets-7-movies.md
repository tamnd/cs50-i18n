---
title: "Movies - CS50x 2026"
pset: 7
draft: false
---

**Thay đổi cho năm 2026:** `5.sql` hiện yêu cầu khớp các bộ phim bắt đầu bằng “Harry Potter and the “ (không chỉ là “Harry Potter”). `9.sql` hiện yêu cầu xuất **hai cột** (ID và tên của mỗi người), không chỉ là tên. Nếu bạn đã bắt đầu bài toán này trước năm 2026, hãy đảm bảo cập nhật các truy vấn của mình cho phù hợp!

![IMDb Logo](imdb.png)

## Bài toán cần giải quyết

Bạn được cung cấp một tệp tên là `movies.db`, một cơ sở dữ liệu SQLite lưu trữ dữ liệu từ [IMDb](https://www.imdb.com/) về các bộ phim, những người đạo diễn và đóng vai chính trong đó, cùng với xếp hạng của họ. Hãy viết các truy vấn SQL để trả lời các câu hỏi về cơ sở dữ liệu phim này.

## Demo

## Bắt đầu

Đối với bài toán này, bạn sẽ sử dụng một cơ sở dữ liệu được cung cấp bởi đội ngũ CS50.

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực thi `cd` một mình. Bạn sẽ thấy dấu nhắc của cửa sổ terminal giống như dưới đây:

```
$
```

Tiếp theo, hãy thực thi

```python
wget https://cdn.cs50.net/2026/x/psets/7/movies.zip
```

để tải một tệp ZIP tên là `movies.zip` vào codespace của bạn.

Sau đó thực thi

```
unzip movies.zip
```

để tạo một thư mục tên là `movies`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi

```
rm movies.zip
```

và trả lời bằng “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ gõ

```bash
cd movies
```

rồi nhấn Enter để di chuyển bản thân vào (tức là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ giống như dưới đây.

```
movies/ $
```

Thực thi `ls` một mình, và bạn sẽ thấy 13 tệp .sql, cũng như `movies.db`.

Nếu bạn gặp bất kỳ rắc rối nào, hãy làm lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Yêu cầu

Đối với mỗi bài toán sau đây, bạn nên viết một truy vấn SQL duy nhất để xuất ra kết quả được chỉ định bởi từng bài toán. Câu trả lời của bạn phải ở dạng một truy vấn SQL duy nhất, mặc dù bạn có thể lồng các truy vấn khác bên trong truy vấn của mình. Bạn **không nên** giả định bất cứ điều gì về `id` của bất kỳ bộ phim hoặc con người cụ thể nào: các truy vấn của bạn phải chính xác ngay cả khi `id` của bất kỳ bộ phim hoặc con người cụ thể nào khác đi. Cuối cùng, mỗi truy vấn chỉ nên trả về dữ liệu cần thiết để trả lời câu hỏi: ví dụ, nếu bài toán chỉ yêu cầu bạn xuất tên phim, thì truy vấn của bạn không nên xuất thêm năm phát hành của mỗi bộ phim.

Bạn có thể kiểm tra kết quả truy vấn của mình so với chính [IMDb](https://www.imdb.com/), nhưng hãy nhận ra rằng xếp hạng trên trang web có thể khác với xếp hạng trong `movies.db`, vì có thể đã có nhiều phiếu bầu hơn được thực hiện kể từ khi chúng tôi tải dữ liệu xuống!

01. Trong `1.sql`, hãy viết một truy vấn SQL để liệt kê tiêu đề của tất cả các bộ phim được phát hành vào năm 2008.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tiêu đề của mỗi bộ phim.
02. Trong `2.sql`, hãy viết một truy vấn SQL để xác định năm sinh của Emma Stone.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất và một hàng duy nhất (không tính tiêu đề cột) chứa năm sinh của Emma Stone.
    - Bạn có thể giả định rằng chỉ có một người trong cơ sở dữ liệu có tên là Emma Stone.
03. Trong `3.sql`, hãy viết một truy vấn SQL để liệt kê tiêu đề của tất cả các bộ phim có ngày phát hành vào hoặc sau năm 2018, theo thứ tự bảng chữ cái.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tiêu đề của mỗi bộ phim.
    - Các bộ phim phát hành năm 2018 nên được bao gồm, cũng như các bộ phim có ngày phát hành trong tương lai.
04. Trong `4.sql`, hãy viết một truy vấn SQL để xác định số lượng phim có xếp hạng IMDb là 10.0.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất và một hàng duy nhất (không tính tiêu đề cột) chứa số lượng phim có xếp hạng 10.0.
05. Trong `5.sql`, hãy viết một truy vấn SQL để liệt kê tiêu đề và năm phát hành của tất cả các bộ phim Harry Potter, theo thứ tự thời gian.
    
    - Truy vấn của bạn nên xuất ra một bảng có hai cột, một cho tiêu đề của mỗi bộ phim và một cho năm phát hành của mỗi bộ phim.
    - Bạn có thể giả định rằng tiêu đề của tất cả các bộ phim Harry Potter sẽ bắt đầu bằng các từ “Harry Potter and the “, và nếu một tiêu đề phim bắt đầu bằng các từ “Harry Potter and the “, thì đó là một bộ phim Harry Potter.
06. Trong `6.sql`, hãy viết một truy vấn SQL để xác định xếp hạng trung bình của tất cả các bộ phim được phát hành vào năm 2012.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất và một hàng duy nhất (không tính tiêu đề cột) chứa xếp hạng trung bình.
07. Trong `7.sql`, hãy viết một truy vấn SQL để liệt kê tất cả các bộ phim được phát hành vào năm 2010 và xếp hạng của chúng, theo thứ tự giảm dần theo xếp hạng. Đối với những bộ phim có cùng xếp hạng, hãy sắp xếp chúng theo thứ tự bảng chữ cái theo tiêu đề.
    
    - Truy vấn của bạn nên xuất ra một bảng có hai cột, một cho tiêu đề của mỗi bộ phim và một cho xếp hạng của mỗi bộ phim.
    - Các bộ phim không có xếp hạng không nên được bao gồm trong kết quả.
08. Trong `8.sql`, hãy viết một truy vấn SQL để liệt kê tên của tất cả những người đã đóng vai chính trong Toy Story.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi người.
    - Bạn có thể giả định rằng chỉ có một bộ phim trong cơ sở dữ liệu có tiêu đề Toy Story.
09. Trong `9.sql`, hãy viết một truy vấn SQL để liệt kê ID và tên của tất cả những người đã đóng vai chính trong một bộ phim phát hành vào năm 2004, được sắp xếp theo năm sinh.
    
    - Truy vấn của bạn nên xuất ra một bảng có hai cột: một cho ID và một cho tên của mỗi người.
    - Những người có cùng năm sinh có thể được liệt kê theo bất kỳ thứ tự nào.
    - Không cần lo lắng về những người không có năm sinh được liệt kê, miễn là những người có năm sinh được liệt kê theo thứ tự.
    - Nếu một người xuất hiện trong nhiều hơn một bộ phim vào năm 2004, họ chỉ nên xuất hiện trong kết quả của bạn một lần.
10. Trong `10.sql`, hãy viết một truy vấn SQL để liệt kê tên của tất cả những người đã đạo diễn một bộ phim nhận được xếp hạng ít nhất là 9.0.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi người.
    - Nếu một người đạo diễn nhiều hơn một bộ phim nhận được xếp hạng ít nhất là 9.0, họ chỉ nên xuất hiện trong kết quả của bạn một lần.
11. Trong `11.sql`, hãy viết một truy vấn SQL để liệt kê tiêu đề của năm bộ phim được xếp hạng cao nhất (theo thứ tự) mà Chadwick Boseman đã đóng vai chính, bắt đầu từ bộ phim được xếp hạng cao nhất.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tiêu đề của mỗi bộ phim.
    - Bạn có thể giả định rằng chỉ có một người trong cơ sở dữ liệu có tên là Chadwick Boseman.
12. Trong `12.sql`, hãy viết một truy vấn SQL để liệt kê tiêu đề của tất cả các bộ phim mà cả Bradley Cooper và Jennifer Lawrence đều đóng vai chính.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tiêu đề của mỗi bộ phim.
    - Bạn có thể giả định rằng chỉ có một người trong cơ sở dữ liệu có tên là Bradley Cooper.
    - Bạn có thể giả định rằng chỉ có một người trong cơ sở dữ liệu có tên là Jennifer Lawrence.
13. Trong `13.sql`, hãy viết một truy vấn SQL để liệt kê tên của tất cả những người đã đóng vai chính trong một bộ phim mà Kevin Bacon cũng đóng vai chính.
    
    - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi người.
    - Có thể có nhiều người tên là Kevin Bacon trong cơ sở dữ liệu. Hãy chắc chắn chỉ chọn Kevin Bacon sinh năm 1958.
    - Bản thân Kevin Bacon không nên được bao gồm trong danh sách kết quả.

## Gợi ý

Hiểu sơ đồ (schema) của `movies.db`

Bất cứ khi nào bạn làm việc với một cơ sở dữ liệu mới, tốt nhất là trước tiên hãy hiểu *sơ đồ* (schema) của nó. Trong một cửa sổ terminal, hãy chạy `sqlite3 movies.db` để bạn có thể bắt đầu thực thi các truy vấn trên cơ sở dữ liệu.

Đầu tiên, khi `sqlite3` nhắc bạn cung cấp một truy vấn, hãy gõ `.schema` và nhấn enter. Điều này sẽ xuất ra các câu lệnh `CREATE TABLE` đã được sử dụng để tạo từng bảng trong cơ sở dữ liệu. Bằng cách xem xét các câu lệnh đó, bạn có thể xác định các cột có mặt trong mỗi bảng.

Lưu ý rằng bảng `movies` có cột `id` xác định duy nhất mỗi bộ phim, cũng như các cột cho `title` (tiêu đề) của phim và `year` (năm) mà bộ phim được phát hành. Bảng `people` cũng có một cột `id`, và cũng có các cột cho `name` (tên) và `birth` (năm sinh) của mỗi người.

Trong khi đó, xếp hạng phim được lưu trữ trong bảng `ratings`. Cột đầu tiên trong bảng là `movie_id`: một khóa ngoại tham chiếu đến `id` của bảng `movies`. Phần còn lại của hàng chứa dữ liệu về `rating` (xếp hạng) cho mỗi bộ phim và số lượng `votes` (phiếu bầu) mà bộ phim đã nhận được trên IMDb.

Cuối cùng, các bảng `stars` và `directors` khớp con người với các bộ phim mà họ đã tham gia diễn xuất hoặc đạo diễn. (Chỉ bao gồm các diễn viên chính [principal](https://www.imdb.com/interfaces/) và đạo diễn.) Mỗi bảng chỉ có hai cột: `movie_id` và `person_id`, lần lượt tham chiếu đến một bộ phim và một người cụ thể.

Thách thức dành cho bạn là viết các truy vấn SQL để trả lời nhiều câu hỏi khác nhau bằng cách chọn dữ liệu từ một hoặc nhiều bảng này.

Trình bày các truy vấn của bạn một cách nhất quán

Xem [sqlstyle.guide](https://www.sqlstyle.guide/) để biết các hướng dẫn về phong cách trình bày tốt trong SQL, đặc biệt khi các truy vấn của bạn trở nên phức tạp hơn!

Liệt kê tiêu đề của tất cả các bộ phim phát hành năm 2008

Hãy nhớ rằng bạn có thể chọn một (hoặc nhiều) cột từ cơ sở dữ liệu bằng cách sử dụng `SELECT`, theo ví dụ dưới đây,

```sql
SELECT column0, column1 FROM table;
```

trong đó `column0` là tên của một cột, và `column1` là tên của một cột khác.

Và hãy nhớ rằng bạn có thể lọc các hàng được trả về trong một truy vấn bằng từ khóa `WHERE`, theo sau là một điều kiện. Bạn cũng có thể sử dụng `=`, `>`, `<`, và [các toán tử khác](https://www.w3schools.com/sql/sql_operators.asp).

```sql
SELECT column FROM table
WHERE condition;
```

Xem [tham chiếu từ khóa SQL này](https://www.w3schools.com/sql/sql_ref_keywords.asp) để biết một số cú pháp SQL có thể hữu ích!

Xác định năm sinh của Emma Stone

Hãy nhớ rằng một mệnh đề `WHERE` có thể đánh giá các điều kiện không chỉ với các con số, mà còn với các chuỗi ký tự.

Liệt kê tiêu đề của tất cả các bộ phim có ngày phát hành vào hoặc sau năm 2018, theo thứ tự bảng chữ cái

Hãy thử chia truy vấn này thành hai bước. Đầu tiên, hãy tìm các bộ phim có ngày phát hành vào hoặc sau năm 2018. Sau đó, hãy sắp xếp tiêu đề của những bộ phim đó theo thứ tự bảng chữ cái.

Để tìm các bộ phim có ngày phát hành vào hoặc sau năm 2018, hãy nhớ rằng một điều kiện trong SQL hỗ trợ việc sử dụng nhiều [toán tử so sánh](https://www.w3schools.com/sql/sql_operators.asp) phổ biến, bao gồm `>=` cho “lớn hơn hoặc bằng.” Kiểm tra xem truy vấn của bạn có trả về đúng số lượng phim hay không, theo [Cách kiểm tra](#how-to-test).

Cuối cùng, sắp xếp kết quả của truy vấn theo thứ tự bảng chữ cái theo tiêu đề. Hãy nhớ rằng `ORDER BY` có thể sắp xếp dữ liệu theo một cột trong kết quả của bạn, theo ví dụ dưới đây.

```
...
ORDER BY column;
```

Xác định số lượng phim có xếp hạng IMDb là 10.0

Lưu ý rằng câu hỏi này không yêu cầu bạn tìm các bộ phim *riêng lẻ* có xếp hạng 10.0, mà yêu cầu tìm *số lượng* phim có xếp hạng như vậy. Nói cách khác, bạn nên thu thập (“tổng hợp”) các kết quả truy vấn của mình thành một con số duy nhất (số lượng hàng). Hãy nhớ rằng SQL hỗ trợ một “hàm tổng hợp” gọi là `COUNT`, bạn có thể sử dụng hàm này trên một cột theo ví dụ dưới đây.

```sql
SELECT COUNT(column)
FROM table;
```

Liệt kê tiêu đề và năm phát hành của tất cả các bộ phim Harry Potter, theo thứ tự thời gian

Đối với truy vấn này, có thể bạn sẽ muốn sử dụng từ khóa `LIKE` của SQL. Hãy nhớ rằng `LIKE` có thể sử dụng các ký tự gọi là “ký tự đại diện” (wildcard characters), chẳng hạn như `%`, ký tự này sẽ khớp với bất kỳ ký tự nào (hoặc một chuỗi ký tự).

```sql
SELECT column0, column1
FROM table
WHERE column1 LIKE pattern;
```

Xác định xếp hạng trung bình của tất cả các bộ phim phát hành năm 2012

Đây là một ví dụ khác về một truy vấn mà bạn sẽ cần tổng hợp dữ liệu. Hãy cân nhắc hàm tổng hợp `AVG` của SQL để tính giá trị trung bình.

Cũng nên cân nhắc rằng truy vấn này sử dụng dữ liệu được lưu trữ trong hai bảng riêng biệt: `ratings` và `movies`. Hãy nhớ rằng—miễn là một bảng có khóa ngoại khớp với một cột trong bảng khác—bạn có thể kết hợp hai bảng bằng cách sử dụng từ khóa `JOIN` của SQL. Để sử dụng từ khóa `JOIN`, bạn nên chỉ định bảng bạn muốn kết nối và cột dùng để kết nối.

```sql
SELECT column0
FROM table0
JOIN table1 ON table0.column1 = table1.column2
```

Liệt kê tất cả các bộ phim phát hành năm 2010 và xếp hạng của chúng, theo thứ tự giảm dần theo xếp hạng

Hãy nhớ rằng `ORDER BY` không phải lúc nào cũng sắp xếp theo thứ tự tăng dần. Bạn có thể chỉ định kết quả của mình được sắp xếp theo thứ tự *giảm dần* bằng cách thêm `DESC`.

```
...
ORDER BY column DESC;
```

Liệt kê tên của tất cả những người đã đóng vai chính trong Toy Story

Khi bạn thấy một truy vấn phức tạp hơn như thế này, tốt nhất là hãy chia nhỏ nó thành các phần nhỏ hơn. Cuối cùng, truy vấn của bạn nên trả về một danh sách các tên, theo như dưới đây.

```sql
-- Chọn tên
SELECT name
FROM people
WHERE ...
```

But làm thế nào là tốt nhất để có được tên của những người đã đóng vai chính trong Toy Story? Hãy cân nhắc rằng bảng `people` không có thông tin này (nhưng bảng `stars` thì có thể!). Thực tế, bảng `stars` kết hợp hai cột, `person_id` và `movie_id`: bất kỳ người nào có `person_id` liên quan đến `movie_id` của Toy Story đều đã đóng vai chính trong Toy Story.

```sql
-- Chọn tên
SELECT name
FROM people
WHERE ...

-- Chọn ID người
SELECT person_id
FROM stars
WHERE movie_id = ...
```

Một bước tiếp theo tự nhiên, khi đó, là tìm ID phim của Toy Story.

```sql
-- Chọn tên
SELECT name
FROM people
WHERE ...

-- Chọn ID người
SELECT person_id
FROM stars
WHERE movie_id = ...

-- Tìm ID của Toy Story
SELECT id
FROM movies
WHERE title = 'Toy Story';
```

Tất nhiên, hiện tại bạn đã viết ba truy vấn *riêng biệt*. Nhưng lưu ý rằng một số truy vấn (hai truy vấn đầu tiên) sẽ hoàn chỉnh bằng cách đưa vào kết quả của truy vấn ngay bên dưới chúng. Quá trình tạo một truy vấn phụ thuộc vào kết quả của một “truy vấn con” (subquery) được gọi là “lồng” các truy vấn. Đó là một gợi ý khá lớn, nhưng đây là một cách để lồng các truy vấn trên!

```sql
-- Chọn tên
SELECT name
FROM people
WHERE id IN
(
    -- Chọn ID người
    SELECT person_id
    FROM stars
    WHERE movie_id = (

        -- Chọn ID của Toy Story
        SELECT id
        FROM movies
        WHERE title = 'Toy Story'
    )
);
```

Liệt kê ID và tên của tất cả những người đã đóng vai chính trong một bộ phim phát hành năm 2004, được sắp xếp theo năm sinh

Lưu ý rằng truy vấn này, giống như truy vấn trước, yêu cầu bạn sử dụng dữ liệu từ nhiều bảng. Hãy nhớ rằng bạn có thể “lồng” các truy vấn trong SQL, điều này cho phép bạn chia một truy vấn lớn thành các truy vấn nhỏ hơn. Có lẽ bạn có thể viết các truy vấn để…

1. Tìm ID của các bộ phim phát hành năm 2004
2. Tìm ID của những người đóng vai chính trong những bộ phim đó
3. Tìm ID và tên của những người có các ID người đó

Sau đó, hãy thử lồng các truy vấn đó để đi đến một truy vấn duy nhất trả về tất cả ID và tên của những người đã đóng vai chính trong một bộ phim phát hành năm 2004. Cân nhắc xem sau đó bạn có thể sắp xếp kết quả truy vấn của mình như thế nào.

Như một lưu ý cuối cùng, hãy nhớ rằng nhiều người có thể có cùng tên. Mặc dù mỗi người chỉ nên xuất hiện trong kết quả của bạn một lần, việc hai ngôi sao có cùng tên không nhất thiết có nghĩa họ là cùng một người.

Liệt kê tên của tất cả những người đã đạo diễn một bộ phim nhận được xếp hạng ít nhất là 9.0

Lưu ý rằng truy vấn này, giống như truy vấn trước, yêu cầu bạn sử dụng dữ liệu từ nhiều bảng. Hãy nhớ rằng bạn có thể “lồng” các truy vấn trong SQL, điều này cho phép bạn chia một truy vấn lớn thành các truy vấn nhỏ hơn. Có lẽ bạn có thể viết các truy vấn để…

1. Tìm ID của các bộ phim có xếp hạng ít nhất 9.0
2. Tìm ID của những người đã đạo diễn những bộ phim đó
3. Tìm tên của những người có các ID người đó

Sau đó, hãy thử lồng các truy vấn đó để đi đến một truy vấn duy nhất trả về tên của tất cả những người đã đạo diễn một bộ phim nhận được xếp hạng ít nhất 9.0.

Liệt kê tiêu đề của năm bộ phim được xếp hạng cao nhất (theo thứ tự) mà Chadwick Boseman đã đóng vai chính, bắt đầu từ bộ phim được xếp hạng cao nhất

Lưu ý rằng truy vấn này, giống như truy vấn trước, yêu cầu bạn sử dụng dữ liệu từ nhiều bảng. Hãy nhớ rằng bạn có thể “lồng” các truy vấn trong SQL, điều này cho phép bạn chia một truy vấn lớn thành các truy vấn nhỏ hơn. Có lẽ bạn có thể viết các truy vấn để…

1. Tìm ID của Chadwick Boseman
2. Tìm ID của các bộ phim liên quan đến ID của Chadwick Boseman
3. Tìm tiêu đề phim với các ID phim đó

Sau đó, hãy thử lồng các truy vấn đó để đi đến một truy vấn duy nhất trả về tiêu đề các bộ phim của Chadwick Boseman.

Từ đó, bạn sẽ cần xác định xếp hạng của các tiêu đề đó và sắp xếp các tiêu đề đó theo xếp hạng, theo thứ tự giảm dần. Cân nhắc cách bạn có thể kết hợp một bảng liên quan (có thể là `ratings`!) và sắp xếp kết quả theo một cột liên quan.

Cuối cùng, hãy tìm hiểu về từ khóa [`LIMIT`](https://www.sqlitetutorial.net/sqlite-limit/) của SQL, từ khóa này sẽ trả về \\(n\\) hàng đầu tiên trong một truy vấn.

Liệt kê tiêu đề của tất cả các bộ phim mà cả Bradley Cooper và Jennifer Lawrence đều đóng vai chính

Lưu ý rằng truy vấn này, giống như truy vấn trước, yêu cầu bạn sử dụng dữ liệu từ nhiều bảng. Hãy nhớ rằng bạn có thể “lồng” các truy vấn trong SQL, điều này cho phép bạn chia một truy vấn lớn thành các truy vấn nhỏ hơn. Có lẽ bạn có thể viết các truy vấn để…

1. Tìm ID của Bradley Cooper
2. Tìm ID của Jennifer Lawrence
3. Tìm ID của các bộ phim liên quan đến ID của Bradley Cooper
4. Tìm ID của các bộ phim liên quan đến ID của Jennifer Lawrence
5. Tìm tiêu đề phim từ các ID phim liên quan đến *cả* Bradley Cooper và Jennifer Lawrence

Sau đó, hãy thử lồng các truy vấn đó để đi đến một truy vấn duy nhất trả về các bộ phim mà cả Bradley Cooper và Jennifer Lawrence đều đóng vai chính.

Hãy nhớ rằng bạn có thể xây dựng các điều kiện kết hợp trong SQL bằng cách sử dụng `AND` hoặc `OR`.

Liệt kê tên của tất cả những người đã đóng vai chính trong một bộ phim mà Kevin Bacon cũng đóng vai chính

Lưu ý rằng truy vấn này, giống như truy vấn trước, yêu cầu bạn sử dụng dữ liệu từ nhiều bảng. Hãy nhớ rằng bạn có thể “lồng” các truy vấn trong SQL, điều này cho phép bạn chia một truy vấn lớn thành các truy vấn nhỏ hơn. Có lẽ bạn có thể viết các truy vấn để…

1. Tìm ID của Kevin Bacon (người sinh năm 1958!)
2. Tìm ID của các bộ phim liên quan đến ID của Kevin Bacon
3. Tìm ID của những người liên quan đến các ID phim đó
4. Tìm tên của những người có các ID người đó

Sau đó, hãy thử lồng các truy vấn đó để đi đến một truy vấn duy nhất trả về tên của tất cả những người đã đóng vai chính trong một bộ phim mà Kevin Bacon cũng đóng vai chính. **Hãy lưu ý rằng bạn sẽ muốn loại bản thân Kevin Bacon ra khỏi kết quả!**

## Video hướng dẫn

## Cách sử dụng

Để kiểm tra các truy vấn của bạn trong VS Code, bạn có thể truy vấn cơ sở dữ liệu bằng cách chạy

```bash
$ cat filename.sql | sqlite3 movies.db
```

trong đó `filename.sql` là tệp chứa truy vấn SQL của bạn.

Bạn cũng có thể chạy

```bash
$ cat filename.sql | sqlite3 movies.db > output.txt
```

để chuyển hướng đầu ra của truy vấn sang một tệp văn bản tên là `output.txt`. (Điều này có thể hữu ích để kiểm tra xem có bao nhiêu hàng được trả về bởi truy vấn của bạn!)

## Cách kiểm tra

Mặc dù `check50` có sẵn cho bài toán này, nhưng bạn được khuyến khích tự kiểm tra mã của mình cho từng bài tập sau. Bạn có thể chạy `sqlite3 movies.db` để thực hiện các truy vấn bổ sung trên cơ sở dữ liệu nhằm đảm bảo kết quả của bạn là chính xác.

Nếu bạn đang sử dụng cơ sở dữ liệu `movies.db` được cung cấp trong bộ mã nguồn phân phối của bài tập này, bạn sẽ thấy rằng

- Việc thực thi `1.sql` mang lại một bảng có 1 cột và 10.647 hàng.
- Việc thực thi `2.sql` mang lại một bảng có 1 cột và 1 hàng.
- Việc thực thi `3.sql` mang lại một bảng có 1 cột và 154.665 hàng.
- Việc thực thi `4.sql` mang lại một bảng có 1 cột và 1 hàng.
- Việc thực thi `5.sql` mang lại một bảng có 2 cột và 18 hàng.
- Việc thực thi `6.sql` mang lại một bảng có 1 cột và 1 hàng.
- Việc thực thi `7.sql` mang lại một bảng có 2 cột và 7.386 hàng.
- Việc thực thi `8.sql` mang lại một bảng có 1 cột và 10 hàng.
- Việc thực thi `9.sql` mang lại một bảng có 2 cột và 36.219 hàng.
- Việc thực thi `10.sql` mang lại một bảng có 1 cột và 4.675 hàng.
- Việc thực thi `11.sql` mang lại một bảng có 1 cột và 5 hàng.
- Việc thực thi `12.sql` mang lại một bảng có 1 cột và 4 hàng.
- Việc thực thi `13.sql` mang lại một bảng có 1 cột và 550 hàng.

Lưu ý rằng số lượng hàng không bao gồm các hàng tiêu đề chỉ hiển thị tên cột.

Nếu truy vấn của bạn trả về số lượng hàng hơi khác so với đầu ra mong đợi, hãy đảm bảo rằng bạn đang xử lý các giá trị trùng lặp một cách chính xác! Đối với các truy vấn yêu cầu danh sách tên, không một người nào nên được liệt kê hai lần, nhưng hai người khác nhau có cùng tên thì mỗi người nên được liệt kê.

### Độ chính xác

```
check50 cs50/problems/2026/x/movies
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài làm của mình, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/movies
```

## Lời cảm ơn

Thông tin được cung cấp bởi IMDb ([imdb.com](https://www.imdb.com)). Được sử dụng với sự cho phép.
