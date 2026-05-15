title: "Sắp xếp - CS50x 2026"
pset: 3
draft: "false"
---

## Vấn đề cần giải quyết

Nhớ lại từ bài giảng, chúng ta đã thấy một vài thuật toán để sắp xếp một dãy số: sắp xếp chọn (selection sort), sắp xếp nổi bọt (bubble sort), và sắp xếp hợp nhất (merge sort).

- Sắp xếp chọn lặp qua các phần chưa được sắp xếp của danh sách, chọn phần tử nhỏ nhất mỗi lần và di chuyển nó đến đúng vị trí.
- Sắp xếp nổi bọt so sánh từng cặp giá trị liền kề và hoán đổi chúng nếu chúng không theo đúng thứ tự. Việc này tiếp tục cho đến khi danh sách được sắp xếp.
- Sắp xếp hợp nhất đệ quy chia danh sách thành hai phần lặp đi lặp lại và sau đó hợp nhất các danh sách nhỏ hơn lại thành một danh sách lớn hơn theo đúng thứ tự.

Trong bài toán này, bạn sẽ phân tích ba chương trình sắp xếp (đã được biên dịch!) để xác định thuật toán mà chúng sử dụng. Trong một tệp có tên `answers.txt` trong thư mục `sort`, hãy ghi lại các câu trả lời của bạn, cùng với phần giải thích cho từng chương trình, bằng cách điền vào các ô trống được đánh dấu `TODO`.

## Mã nguồn phân phối

Đối với bài toán này, bạn sẽ cần một số “mã nguồn phân phối” — đó là mã nguồn được viết bởi đội ngũ CS50. Bạn được cung cấp ba chương trình C đã được biên dịch sẵn, `sort1`, `sort2`, và `sort3`, cũng như một số tệp `.txt` để nhập dữ liệu và một tệp khác, `answers.txt`, để viết câu trả lời của bạn. Mỗi chương trình `sort1`, `sort2`, và `sort3` thực thi một thuật toán sắp xếp khác nhau: sắp xếp chọn, sắp xếp nổi bọt, hoặc sắp xếp hợp nhất (mặc dù không nhất thiết theo thứ tự đó!). Nhiệm vụ của bạn là xác định thuật toán sắp xếp nào được sử dụng bởi mỗi tệp. Hãy bắt đầu bằng cách tải xuống các tệp này.

Tải xuống các tệp phân phối

Mở [cs50.dev](https://cs50.dev/).

Bắt đầu bằng cách nhấp vào bên trong cửa sổ terminal, sau đó thực hiện lệnh `cd`. Bạn sẽ thấy “dấu nhắc” (prompt) của nó giống như dưới đây.

```
$
```

Nhấp vào bên trong cửa sổ terminal đó và thực hiện lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/3/sort.zip
```

sau đó nhấn Enter để tải xuống một tệp ZIP có tên `sort.zip` trong codespace của bạn. Hãy cẩn thận không bỏ sót khoảng trắng giữa `wget` và URL theo sau, hoặc bất kỳ ký tự nào khác!

Bây giờ hãy thực hiện lệnh

```
unzip sort.zip
```

để tạo một thư mục có tên `sort`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện lệnh

```
rm sort.zip
```

và trả lời với “y” sau đó nhấn Enter tại dấu nhắc để xóa tệp ZIP mà bạn đã tải xuống.

## Gợi ý

Khám phá các tệp `.txt`

- Nhiều tệp `.txt` được cung cấp cho bạn. Các tệp này chứa `n` dòng giá trị, có thể là đảo ngược, xáo trộn hoặc đã sắp xếp.
  
  - Ví dụ, `reversed10000.txt` chứa 10.000 dòng số được đảo ngược từ `10000`, trong khi `random50000.txt` chứa 50.000 dòng số ở thứ tự ngẫu nhiên.
- Các loại tệp `.txt` khác nhau có thể giúp bạn xác định chương trình sắp xếp nào là thuật toán nào. Hãy cân nhắc xem mỗi thuật toán hoạt động như thế nào với một danh sách đã được sắp xếp. Còn một danh sách đảo ngược thì sao? Hay một danh sách bị xáo trộn? Có thể sẽ hữu ích nếu bạn thử với một danh sách nhỏ hơn của mỗi loại và đi qua từng quy trình sắp xếp.

Đo thời gian mỗi thuật toán sắp xếp với các đầu vào khác nhau

- Để chạy các chương trình sắp xếp trên các tệp văn bản, trong terminal, hãy chạy `./[tên_chương_trình] [tên_tệp_văn_bản.txt]`. Đảm bảo rằng bạn đã sử dụng lệnh `cd` để di chuyển vào thư mục `sort`!
  
  - Ví dụ, để sắp xếp `reversed10000.txt` với `sort1`, hãy chạy `./sort1 reversed10000.txt`.
- Bạn có thể thấy hữu ích khi đo thời gian các chương trình sắp xếp của mình. Để làm như vậy, hãy chạy `time ./[tệp_sắp_xếp] [tên_tệp_văn_bản.txt]`.
  
  - Ví dụ, bạn có thể chạy `time ./sort1 reversed10000.txt` để chạy `sort1` trên 10.000 số đảo ngược. Ở cuối đầu ra của terminal, bạn có thể xem thời gian `real` để biết thực tế đã mất bao lâu khi chạy chương trình.

## Hướng dẫn chi tiết

Bạn không chắc cách giải quyết?

## Cách kiểm tra

### Độ chính xác

```
check50 cs50/problems/2026/x/sort
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/sort
```
