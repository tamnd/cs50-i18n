title: "Cash - CS50x 2026"
pset: 6
draft: false
---

## Vấn đề cần giải quyết

Trong một tệp có tên là `cash.py` nằm trong thư mục `sentimental-cash`, hãy viết một chương trình hỏi người dùng số tiền thối còn nợ là bao nhiêu, sau đó in ra số lượng đồng xu tối thiểu cần thiết để trả lại số tiền đó. Bạn có thể thực hiện bài này tương tự như cách bạn đã làm trong [Problem Set 1](../../1/), ngoại trừ việc chương trình lần này phải được viết bằng Python và bạn nên giả định rằng người dùng sẽ nhập số tiền thối bằng đô la (ví dụ: 0.50 đô la thay vì 50 cent).

## Demo

## Yêu cầu kỹ thuật

- Sử dụng hàm `get_float` từ Thư viện CS50 để lấy đầu vào của người dùng và hàm `print` để in ra câu trả lời của bạn. Giả định rằng các loại tiền xu có sẵn là quarters (25¢), dimes (10¢), nickels (5¢) và pennies (1¢).
  
  - Chúng tôi yêu cầu bạn sử dụng `get_float` để bạn có thể xử lý cả đô la và cent, mặc dù không có ký hiệu đô la. Nói cách khác, nếu một khách hàng được thối $9.75 (như trong trường hợp một tờ báo có giá 25¢ nhưng khách hàng thanh toán bằng tờ $10), hãy giả định rằng đầu vào của chương trình sẽ là `9.75` chứ không phải `$9.75` hay `975`. Tuy nhiên, nếu khách hàng được thối chính xác $9, hãy giả định rằng đầu vào của chương trình sẽ là `9.00` hoặc chỉ `9` nhưng, nhắc lại, không phải `$9` hay `900`. Tất nhiên, theo bản chất của các giá trị số thực dấu phẩy động, chương trình của bạn cũng có thể hoạt động với các đầu vào như `9.0` và `9.000`; bạn không cần lo lắng về việc kiểm tra xem đầu vào của người dùng có được "định dạng" đúng như tiền tệ hay không.
- Nếu người dùng không nhập một giá trị không âm, chương trình của bạn nên yêu cầu người dùng nhập lại một số tiền hợp lệ cho đến khi người dùng tuân thủ.
- Ngoài ra, để chúng tôi có thể tự động hóa một số thử nghiệm cho mã nguồn của bạn, chúng tôi yêu cầu dòng đầu ra cuối cùng của chương trình chỉ chứa số lượng đồng xu tối thiểu có thể: một số nguyên theo sau bởi một dòng mới.

## Cách kiểm tra

Mặc dù `check50` có sẵn cho bài toán này, bạn nên tự mình kiểm tra mã nguồn trước cho mỗi trường hợp sau đây.

- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `0.41` và nhấn enter. Chương trình của bạn sẽ in ra `4`.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `0.01` và nhấn enter. Chương trình của bạn sẽ in ra `1`.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `0.15` và nhấn enter. Chương trình của bạn sẽ in ra `2`.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `1.60` và nhấn enter. Chương trình của bạn sẽ in ra `7`.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `23` và nhấn enter. Chương trình của bạn sẽ in ra `92`.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `4.2` và nhấn enter. Chương trình của bạn sẽ in ra `18`.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `-1` và nhấn enter. Chương trình của bạn sẽ từ chối đầu vào này vì không hợp lệ và yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Nhập `foo` và nhấn enter. Chương trình của bạn sẽ từ chối đầu vào này vì không hợp lệ và yêu cầu người dùng nhập lại một số khác.
- Chạy chương trình bằng lệnh `python cash.py` và đợi thông báo nhập dữ liệu. Không nhập gì cả và nhấn enter. Chương trình của bạn sẽ từ chối đầu vào này vì không hợp lệ và yêu cầu người dùng nhập lại một số khác.

### Độ chính xác

```
check50 cs50/problems/2026/x/sentimental/cash
```

### Phong cách

```
style50 cash.py
```

## Cách nộp bài

Trong terminal của bạn, thực hiện lệnh dưới đây để nộp bài, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/sentimental/cash
```
