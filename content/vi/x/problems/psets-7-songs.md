title: "Songs - CS50x 2026"
pset: 7
draft: "false"
---

![Spotify Wrapped '22 Logo](wrapped.png)

## Bài toán cần giải quyết

Viết các câu truy vấn SQL để trả lời các câu hỏi về một cơ sở dữ liệu gồm 100 bài hát được nghe nhiều nhất trên [Spotify](https://en.wikipedia.org/wiki/Spotify) vào năm 2018.

## Demo

## Bắt đầu

Đối với bài toán này, bạn sẽ sử dụng một cơ sở dữ liệu được cung cấp bởi đội ngũ CS50.

Tải mã nguồn phân phối

Mở [VS Code](https://cs50.dev/).

Bắt đầu bằng cách nhấp vào bên trong cửa sổ terminal của bạn, sau đó thực hiện lệnh `cd`. Bạn sẽ thấy "dấu nhắc" (prompt) của nó giống như dưới đây.

```
$
```

Nhấp vào bên trong cửa sổ terminal đó và thực hiện lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/7/songs.zip
```

sau đó nhấn Enter để tải xuống tệp ZIP có tên `songs.zip` vào codespace của bạn. Hãy cẩn thận đừng bỏ sót khoảng trắng giữa `wget` và URL đi kèm, cũng như bất kỳ ký tự nào khác!

Bây giờ hãy thực hiện lệnh

```
unzip songs.zip
```

để tạo một thư mục có tên `songs`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện

```
rm songs.zip
```

và trả lời bằng "y" rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy nhập

```bash
cd songs
```

rồi nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ giống như dưới đây.

```
songs/ $
```

Nếu mọi việc thành công, bạn nên thực hiện

```bash
ls
```

và bạn sẽ thấy 8 tệp .sql, `songs.db` và `answers.txt`.

Nếu bạn gặp bất kỳ rắc rối nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Tìm hiểu

Bạn được cung cấp một tệp tên là `songs.db`, một cơ sở dữ liệu SQLite lưu trữ dữ liệu từ [Spotify](https://developer.spotify.com/documentation/web-api/) về các bài hát và nghệ sĩ của chúng. Tập dữ liệu này chứa 100 bài hát được nghe nhiều nhất trên Spotify vào năm 2018. Trong cửa sổ terminal, hãy chạy lệnh `sqlite3 songs.db` để bạn có thể bắt đầu thực hiện các câu truy vấn trên cơ sở dữ liệu.

Đầu tiên, khi `sqlite3` yêu cầu bạn cung cấp một câu truy vấn, hãy nhập `.schema` và nhấn Enter. Lệnh này sẽ xuất ra các câu lệnh `CREATE TABLE` đã được sử dụng để tạo từng bảng trong cơ sở dữ liệu. Bằng cách kiểm tra các câu lệnh đó, bạn có thể xác định các cột có trong mỗi bảng.

Lưu ý rằng mỗi `artist` (nghệ sĩ) đều có một `id` và một `name` (tên). Hãy lưu ý thêm rằng mỗi bài hát đều có một `name`, một `artist_id` (tương ứng với `id` của nghệ sĩ trình bày bài hát), cũng như các giá trị về danceability (khả năng nhảy), energy (năng lượng), key (khóa nhạc), loudness (độ to), speechiness (sự xuất hiện của lời nói trong bản nhạc), valence (độ tích cực), tempo (nhịp độ) và duration (thời lượng) của bài hát (được tính bằng mili giây).

Thử thách dành cho bạn là viết các câu truy vấn SQL để trả lời nhiều câu hỏi khác nhau bằng cách chọn dữ liệu từ một hoặc nhiều bảng này. Sau khi thực hiện xong, bạn sẽ suy ngẫm về những cách mà Spotify có thể sử dụng cùng dữ liệu này trong chiến dịch [Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) hàng năm của họ để đặc tả thói quen của người nghe.

## Chi tiết triển khai

Đối với mỗi bài toán sau đây, bạn nên viết một câu truy vấn SQL duy nhất để xuất ra các kết quả được chỉ định bởi từng bài toán. Câu trả lời của bạn phải ở dạng một câu truy vấn SQL duy nhất, mặc dù bạn có thể lồng các truy vấn khác bên trong câu truy vấn của mình. Bạn **không nên** giả định bất cứ điều gì về `id` của bất kỳ bài hát hoặc nghệ sĩ cụ thể nào: các truy vấn của bạn phải chính xác ngay cả khi `id` của bất kỳ bài hát hoặc nghệ sĩ cụ thể nào khác đi. Cuối cùng, mỗi truy vấn chỉ nên trả về dữ liệu cần thiết để trả lời câu hỏi: ví dụ: nếu bài toán chỉ yêu cầu bạn xuất ra tên của các bài hát, thì truy vấn của bạn không nên xuất ra nhịp độ của từng bài hát.

1. Trong `1.sql`, hãy viết một câu truy vấn SQL để liệt kê tên của tất cả các bài hát trong cơ sở dữ liệu.
   
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi bài hát.
2. Trong `2.sql`, hãy viết một câu truy vấn SQL để liệt kê tên của tất cả các bài hát theo thứ tự nhịp độ (tempo) tăng dần.
   
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi bài hát.
3. Trong `3.sql`, hãy viết một câu truy vấn SQL để liệt kê tên của 5 bài hát dài nhất, theo thứ tự thời lượng giảm dần.
   
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi bài hát.
4. Trong `4.sql`, hãy viết một câu truy vấn SQL liệt kê tên của bất kỳ bài hát nào có danceability, energy và valence lớn hơn 0.75.
   
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi bài hát.
5. Trong `5.sql`, hãy viết một câu truy vấn SQL trả về năng lượng trung bình (average energy) của tất cả các bài hát.
   
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất và một hàng duy nhất chứa năng lượng trung bình.
6. Trong `6.sql`, hãy viết một câu truy vấn SQL liệt kê tên của các bài hát của Post Malone.
   
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi bài hát.
   - Bạn không nên đưa ra bất kỳ giả định nào về `artist_id` của Post Malone.
7. Trong `7.sql`, hãy viết một câu truy vấn SQL trả về năng lượng trung bình của các bài hát của Drake.
   
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất và một hàng duy nhất chứa năng lượng trung bình.
   - Bạn không nên đưa ra bất kỳ giả định nào về `artist_id` của Drake.
8. Trong `8.sql`, hãy viết một câu truy vấn SQL liệt kê tên của các bài hát có sự góp mặt của các nghệ sĩ khác.
   
   - Các bài hát có sự góp mặt của các nghệ sĩ khác sẽ bao gồm "feat." trong tên bài hát.
   - Truy vấn của bạn nên xuất ra một bảng với một cột duy nhất cho tên của mỗi bài hát.

## Gợi ý

Xem [tài liệu tham khảo từ khóa SQL này](https://www.w3schools.com/sql/sql_ref_keywords.asp) để biết một số cú pháp SQL có thể hữu ích!

Liệt kê tên của tất cả các bài hát trong cơ sở dữ liệu

Hãy nhớ rằng, để chọn tất cả các giá trị trong một cột của bảng, bạn có thể sử dụng từ khóa `SELECT` của SQL. Theo sau `SELECT` là cột (hoặc các cột) bạn muốn chọn, sau đó là `FROM table` trong đó `table` là tên của bảng bạn muốn chọn dữ liệu.

Trong `1.sql`, hãy thử viết như sau:

```sql
-- All songs in the database.
SELECT name
FROM songs;
```

Liệt kê tên của tất cả các bài hát theo thứ tự nhịp độ (tempo) tăng dần

Hãy nhớ rằng SQL có từ khóa `ORDER BY`, nhờ đó bạn có thể sắp xếp các kết quả của truy vấn theo giá trị trong một cột nhất định. Ví dụ: `ORDER BY tempo` sẽ sắp xếp kết quả theo cột `tempo`.

Trong `2.sql`, hãy thử viết như sau:

```sql
-- All songs in increasing order of tempo.
SELECT name
FROM songs
ORDER BY tempo;
```

Liệt kê tên của 5 bài hát dài nhất, theo thứ tự thời lượng giảm dần

Hãy nhớ rằng `ORDER BY` không phải lúc nào cũng sắp xếp theo thứ tự tăng dần. Bạn có thể chỉ định kết quả của mình được sắp xếp theo thứ tự *giảm dần* bằng cách thêm `DESC`. Ví dụ: `ORDER BY duration_ms DESC` sẽ liệt kê kết quả theo thứ tự giảm dần, theo thời lượng.

Và cũng hãy nhớ rằng, `LIMIT n` có thể chỉ định rằng bạn chỉ muốn lấy n hàng đầu tiên khớp với một truy vấn cụ thể. Ví dụ: `LIMIT 5` sẽ chỉ trả về năm kết quả đầu tiên của truy vấn.

Trong `3.sql`, hãy thử viết như sau:

```sql
-- The names of the top 5 longest songs, in descending order of length.
SELECT name
FROM songs
ORDER BY duration_ms DESC
LIMIT 5;
```

Liệt kê tên của bất kỳ bài hát nào có danceability, energy và valence lớn hơn 0.75

Hãy nhớ rằng bạn có thể lọc kết quả trong SQL bằng các mệnh đề `WHERE`, theo sau là một số điều kiện thường dùng để kiểm tra các giá trị trong các cột của một hàng.

Cũng hãy nhớ rằng, các toán tử của SQL hoạt động giống như của C. Ví dụ: `>` được đánh giá là "true" khi giá trị bên trái lớn hơn giá trị bên phải. Bạn có thể chuỗi các biểu thức này lại với nhau, sử dụng `AND` hoặc `OR`, để tạo thành một điều kiện lớn hơn.

Trong `4.sql`, hãy thử viết như sau:

```sql
-- The names of any songs that have danceability, energy, and valence greater than 0.75.
SELECT name
FROM songs
WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;
```

Tìm năng lượng trung bình của tất cả các bài hát

Hãy nhớ rằng SQL hỗ trợ các từ khóa không chỉ để chọn các hàng cụ thể mà còn để *tổng hợp* (aggregate) dữ liệu trong các hàng đó. Cụ thể, bạn có thể thấy từ khóa `AVG` (để tính trung bình) hữu ích. Để tổng hợp các kết quả của một cột, chỉ cần áp dụng hàm tổng hợp cho cột đó. Ví dụ: `SELECT AVG(energy)` sẽ tìm trung bình cộng của các giá trị trong cột energy cho truy vấn đã cho.

Trong `5.sql`, hãy thử viết như sau:

```sql
-- The average energy of all the songs.
SELECT AVG(energy)
FROM songs;
```

Liệt kê tên của các bài hát của Post Malone

Lưu ý rằng, nếu bạn thực hiện lệnh `.schema songs` trong dấu nhắc sqlite của mình, bảng `songs` có tên bài hát nhưng không có tên nghệ sĩ! Thay vào đó, `songs` có một cột `artist_id`. Để liệt kê tên của các bài hát của Post Malone, trước tiên bạn cần xác định ID nghệ sĩ của Post Malone.

```sql
-- Identify Post Malone's artist id
SELECT id
FROM artists
WHERE name = 'Post Malone';
```

Truy vấn này trả về 54. Bây giờ, bạn có thể truy vấn bảng `songs` cho bất kỳ bài hát nào có ID của Post Malone.

```sql
SELECT name
FROM songs
WHERE artist_id = 54;
```

Nhưng, theo yêu cầu đề bài, bạn nên lưu ý không giả định rằng mình đã biết bất kỳ ID nào. Bạn có thể cải thiện thiết kế của truy vấn này bằng cách *lồng* hai truy vấn của mình.

Trong `6.sql`, hãy thử viết như sau:

```sql
-- The names of songs that are by Post Malone.
SELECT name
FROM songs
WHERE artist_id =
(
    SELECT id
    FROM artists
    WHERE name = 'Post Malone'
);
```

Tìm năng lượng trung bình của các bài hát của Drake

Lưu ý rằng, tương tự như truy vấn trước, bạn sẽ cần kết hợp nhiều bảng để chạy thành công truy vấn này. Bạn có thể một lần nữa sử dụng các truy vấn con lồng nhau, nhưng cũng hãy cân nhắc một cách tiếp cận khác!

Hãy nhớ rằng bạn có thể sử dụng từ khóa `JOIN` của SQL để kết hợp nhiều bảng thành một, miễn là bạn chỉ định các cột nào giữa các bảng đó cuối cùng phải khớp nhau. Ví dụ: truy vấn sau đây tham gia (join) bảng `songs` và `artists`, cho biết rằng cột `artist_id` trong bảng `songs` và cột `id` trong bảng `artists` phải khớp nhau:

```sql
SELECT *
FROM songs
JOIN artists ON songs.artist_id = artists.id
```

Với hai bảng này được kết hợp, vấn đề chỉ còn là lọc lựa chọn của bạn để tìm năng lượng trung bình của các bài hát của Drake.

Trong `7.sql`, hãy thử viết như sau:

```sql
-- The average energy of songs that are by Drake
SELECT AVG(energy)
FROM songs
JOIN artists ON songs.artist_id = artists.id
WHERE artists.name = 'Drake';
```

Liệt kê tên của các bài hát có sự góp mặt của các nghệ sĩ khác

Đối với truy vấn này, hãy lưu ý rằng các bài hát có sự góp mặt của các nghệ sĩ khác thường có đề cập đến "feat." trong tiêu đề của chúng. Hãy nhớ rằng từ khóa `LIKE` của SQL có thể được sử dụng để khớp các chuỗi với một số cụm từ nhất định (như "feat."!). Để làm như vậy, bạn có thể sử dụng `%`: một ký tự đại diện (wildcard) khớp với bất kỳ chuỗi ký tự nào.

Trong `8.sql`, hãy thử viết như sau:

```sql
-- The names of songs that feature other artists.
SELECT name
FROM songs
WHERE name LIKE '%feat.%';
```

## Hướng dẫn chi tiết

Bạn chưa biết cách giải quyết?

## Spotify Wrapped

[Spotify Wrapped](https://en.wikipedia.org/wiki/Spotify_Wrapped) là một tính năng trình bày 100 bài hát được nghe nhiều nhất của người dùng Spotify trong năm qua. Vào năm 2021, Spotify Wrapped đã tính toán một ["Audio Aura"](https://newsroom.spotify.com/2021-12-01/learn-more-about-the-audio-aura-in-your-spotify-2021-wrapped-with-aura-reader-mystic-michaela/) cho mỗi người dùng, một "phân tích về hai tâm trạng nổi bật nhất của họ được quy định bởi các bài hát và nghệ sĩ hàng đầu của họ trong năm". Giả sử Spotify xác định một audio aura bằng cách xem xét năng lượng (energy), độ tích cực (valence) và khả năng nhảy (danceability) trung bình trong 100 bài hát hàng đầu của một người từ năm qua. Trong `answers.txt`, hãy suy ngẫm về các câu hỏi sau:

- Nếu `songs.db` chứa 100 bài hát hàng đầu của một người nghe từ năm 2018, bạn sẽ đặc tả audio aura của họ như thế nào?
- Hãy đưa ra giả thuyết về lý do tại sao cách bạn tính toán aura này có thể *không* đại diện chính xác cho người nghe. Bạn sẽ đề xuất những cách tính toán aura này tốt hơn như thế nào?

Hãy nhớ nộp `answers.txt` cùng với từng tệp `.sql` của bạn!

## Cách kiểm tra

### Độ chính xác

```
check50 cs50/problems/2026/x/songs
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện lên.

```
submit50 cs50/problems/2026/x/songs
```
