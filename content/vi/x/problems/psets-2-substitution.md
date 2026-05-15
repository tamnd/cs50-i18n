title: "Substitution - CS50x 2026"
pset: 2
draft: false
---

## Bài toán cần giải quyết

Trong mật mã thay thế, chúng ta "mã hóa" (tức là che giấu một cách có thể khôi phục) một thông điệp bằng cách thay thế mỗi chữ cái bằng một chữ cái khác. Để làm được điều này, chúng ta sử dụng một *khóa* (key): trong trường hợp này là một bản đồ ánh xạ mỗi chữ cái trong bảng chữ cái với chữ cái tương ứng khi chúng ta mã hóa nó. Để "giải mã" thông điệp, người nhận thông điệp cần biết khóa này để họ có thể đảo ngược quy trình: dịch văn bản đã mã hóa (thường được gọi là *ciphertext*) trở lại thông điệp gốc (thường được gọi là *plaintext*).

Ví dụ, một khóa có thể là chuỗi `NQXPOMAFTRHLZGECYJIUWSKDVB`. Khóa gồm 26 ký tự này có nghĩa là `A` (chữ cái đầu tiên của bảng chữ cái) sẽ được chuyển đổi thành `N` (ký tự đầu tiên của khóa), `B` (chữ cái thứ hai của bảng chữ cái) sẽ được chuyển đổi thành `Q` (ký tự thứ hai của khóa), và cứ tiếp tục như vậy.

Khi đó, một thông điệp như `HELLO` sẽ được mã hóa thành `FOLLE`, thay thế mỗi chữ cái theo sơ đồ ánh xạ được xác định bởi khóa.

Trong tệp tin có tên `substitution.c` tại thư mục `substitution`, hãy tạo một chương trình cho phép bạn mã hóa các thông điệp bằng mật mã thay thế. Tại thời điểm người dùng thực thi chương trình, họ sẽ quyết định khóa cho thông điệp bí mật bằng cách cung cấp một đối số dòng lệnh khi chạy chương trình.

## Demo

## Chi tiết yêu cầu

Thiết kế và triển khai một chương trình, `substitution`, mã hóa các thông điệp bằng mật mã thay thế.

- Triển khai chương trình của bạn trong tệp `substitution.c` trong thư mục `substitution`.
- Chương trình của bạn phải chấp nhận một đối số dòng lệnh duy nhất, đó là khóa được sử dụng để thay thế. Bản thân khóa không nên phân biệt chữ hoa chữ thường, vì vậy việc bất kỳ ký tự nào trong khóa là chữ hoa hay chữ thường đều không ảnh hưởng đến hành vi của chương trình.
- Nếu chương trình của bạn được thực thi mà không có đối số dòng lệnh nào hoặc có nhiều hơn một đối số dòng lệnh, chương trình sẽ in một thông báo lỗi tùy chọn (bằng `printf`) và trả về từ `main` giá trị `1` (thường biểu thị lỗi) ngay lập tức.
- Nếu khóa không hợp lệ (như không chứa đúng 26 ký tự, chứa bất kỳ ký tự nào không phải chữ cái, hoặc không chứa mỗi chữ cái đúng một lần), chương trình của bạn sẽ in một thông báo lỗi tùy chọn (bằng `printf`) và trả về từ `main` giá trị `1` ngay lập tức.
- Chương trình của bạn phải xuất ra `plaintext:` (không có dòng mới) và sau đó nhắc người dùng nhập một chuỗi `string` văn bản gốc (sử dụng `get_string`).
- Chương trình của bạn phải xuất ra `ciphertext:` (không có dòng mới), theo sau là mã văn bản tương ứng của văn bản gốc, với mỗi ký tự chữ cái trong văn bản gốc được thay thế bằng ký tự tương ứng trong mã văn bản; các ký tự không phải chữ cái phải được giữ nguyên.
- Chương trình của bạn phải bảo toàn kiểu chữ: chữ in hoa phải giữ nguyên là chữ in hoa; chữ thường phải giữ nguyên là chữ thường.
- Sau khi xuất mã văn bản, bạn nên in một dòng mới. Chương trình của bạn sau đó sẽ kết thúc bằng cách trả về `0` từ `main`.

Bạn có thể thấy một hoặc nhiều hàm được khai báo trong `ctype.h` sẽ hữu ích, theo [manual.cs50.io](https://manual.cs50.io/).

## Walkthrough

## Cách kiểm tra

### Tính chính xác

```
check50 cs50/problems/2026/x/substitution
```

Cách sử dụng `debug50`

Bạn muốn chạy `debug50`? Bạn có thể làm như sau, sau khi biên dịch mã thành công với `make`,

```
debug50 ./substitution KEY
```

trong đó `KEY` là khóa bạn cung cấp dưới dạng đối số dòng lệnh cho chương trình của mình. Lưu ý rằng việc chạy

```
debug50 ./substitution
```

sẽ (lý tưởng nhất!) khiến chương trình của bạn kết thúc bằng cách nhắc người dùng cung cấp một khóa.

### Phong cách trình bày

```
style50 substitution.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài làm của mình, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/substitution
```
