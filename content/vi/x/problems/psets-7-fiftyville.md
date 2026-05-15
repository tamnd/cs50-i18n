---
title: "Fiftyville - CS50x 2026"
pset: 7
draft: false
---

## Vấn đề cần giải quyết

Chú vịt CS50 Duck đã bị đánh cắp! Thị trấn Fiftyville đã nhờ bạn giải quyết bí ẩn về chú vịt bị đánh cắp. Chính quyền tin rằng tên trộm đã lấy cắp chú vịt và sau đó, ngay sau đó, đã lên một chuyến bay rời khỏi thị trấn với sự giúp đỡ của một đồng phạm. Mục tiêu của bạn là xác định:

- Tên trộm là ai,
- Thành phố mà tên trộm đã trốn đến, và
- Đồng phạm đã giúp tên trộm trốn thoát là ai

Tất cả những gì bạn biết là vụ trộm **diễn ra vào ngày 28 tháng 7 năm 2025** và **diễn ra trên đường Humphrey Street**.

Bạn sẽ giải quyết bí ẩn này như thế nào? Chính quyền Fiftyville đã thu thập một số hồ sơ của thị trấn từ khoảng thời gian xảy ra vụ trộm và chuẩn bị một cơ sở dữ liệu SQLite cho bạn, `fiftyville.db`, chứa các bảng dữ liệu từ khắp thị trấn. Bạn có thể truy vấn bảng đó bằng các câu lệnh SQL `SELECT` để truy cập dữ liệu mà bạn quan tâm. Chỉ sử dụng thông tin trong cơ sở dữ liệu, nhiệm vụ của bạn là giải quyết bí ẩn.

## Bản demo

## Bắt đầu

Đối với bài toán này, bạn sẽ sử dụng cơ sở dữ liệu do đội ngũ CS50 cung cấp.

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực hiện lệnh `cd`. Bạn sẽ thấy dấu nhắc lệnh của terminal trông giống như bên dưới:

```
$
```

Tiếp theo hãy thực thi

```python
wget https://cdn.cs50.net/2026/x/psets/7/fiftyville.zip
```

để tải xuống tệp ZIP có tên `fiftyville.zip` vào codespace của bạn.

Sau đó thực thi

```
unzip fiftyville.zip
```

để tạo một thư mục có tên `fiftyville`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi

```
rm fiftyville.zip
```

và trả lời “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy nhập

```bash
cd fiftyville
```

rồi nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc lệnh của bạn bây giờ sẽ giống như bên dưới.

```
fiftyville/ $
```

Thực thi lệnh `ls`, và bạn sẽ thấy một vài tệp:

```
answers.txt  fiftyville.db  log.sql
```

Nếu bạn gặp bất kỳ rắc rối nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Yêu cầu chi tiết

Đối với bài toán này, quá trình bạn sử dụng để giải quyết bí ẩn cũng quan trọng không kém việc giải quyết chính bí ẩn đó. Trong `log.sql`, hãy lưu lại nhật ký của tất cả các truy vấn SQL mà bạn thực hiện trên cơ sở dữ liệu. Phía trên mỗi truy vấn, hãy dán nhãn cho từng truy vấn bằng một chú thích (trong SQL, chú thích là bất kỳ dòng nào bắt đầu bằng `--`) mô tả lý do bạn chạy truy vấn và/hoặc thông tin bạn hy vọng nhận được từ truy vấn cụ thể đó. Bạn có thể sử dụng các chú thích trong tệp nhật ký để thêm các ghi chú bổ sung về quá trình suy nghĩ của mình khi giải quyết bí ẩn: cuối cùng, tệp này sẽ đóng vai trò là bằng chứng về quá trình bạn đã sử dụng để xác định tên trộm!

Khi viết các truy vấn, bạn có thể nhận thấy một số truy vấn có thể trở nên khá phức tạp. Để giúp các truy vấn của bạn dễ đọc hơn, hãy xem các nguyên tắc về phong cách trình bày tốt tại [sqlstyle.guide](https://www.sqlstyle.guide). Phần [thụt lề (indentation)](https://www.sqlstyle.guide/#indentation) có thể đặc biệt hữu ích!

Sau khi giải quyết xong bí ẩn, hãy hoàn thành từng dòng trong `answers.txt` bằng cách điền tên của tên trộm, thành phố mà tên trộm đã trốn đến và tên của đồng phạm đã giúp họ trốn khỏi thị trấn. (Hãy chắc chắn không thay đổi bất kỳ văn bản hiện có nào trong tệp hoặc thêm bất kỳ dòng nào khác vào tệp!)

Cuối cùng, bạn nên nộp cả hai tệp `log.sql` và `answers.txt`.

## Hướng dẫn từng bước

## Gợi ý

- Thực thi `sqlite3 fiftyville.db` để bắt đầu chạy các truy vấn trên cơ sở dữ liệu.
  
  - Trong khi chạy `sqlite3`, thực thi `.tables` sẽ liệt kê tất cả các bảng trong cơ sở dữ liệu.
  - Trong khi chạy `sqlite3`, thực thi `.schema TABLE_NAME`, trong đó `TABLE_NAME` là tên của một bảng trong cơ sở dữ liệu, sẽ hiển thị lệnh `CREATE TABLE` được sử dụng để tạo bảng đó. Điều này có thể hữu ích để biết cột nào cần truy vấn!
- Bạn có thể thấy hữu ích khi bắt đầu với bảng `crime_scene_reports`. Hãy bắt đầu bằng cách tìm một báo cáo hiện trường vụ án khớp với ngày và địa điểm xảy ra tội ác.
- Xem [tham khảo từ khóa SQL này](https://www.w3schools.com/sql/sql_ref_keywords.asp) để biết một số cú pháp SQL có thể hữu ích!

## Cách kiểm tra

### Độ chính xác

```
check50 cs50/problems/2026/x/fiftyville
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh bên dưới để nộp bài làm của mình, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/fiftyville
```
