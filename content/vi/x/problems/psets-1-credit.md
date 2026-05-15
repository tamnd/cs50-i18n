title: "Credit - CS50x 2026"
pset: 1
draft: false
---

![Người cầm thẻ tín dụng](credit_cards.jpeg)

## Vấn đề cần giải quyết

Một chiếc thẻ tín dụng (hoặc thẻ ghi nợ), dĩ nhiên, là một tấm thẻ nhựa mà bạn có thể dùng để thanh toán hàng hóa và dịch vụ. Được in trên tấm thẻ đó là một dãy số cũng được lưu trữ trong một cơ sở dữ liệu ở đâu đó, để khi thẻ của bạn được sử dụng để mua thứ gì đó, chủ nợ sẽ biết phải gửi hóa đơn cho ai. Có rất nhiều người sở hữu thẻ tín dụng trên thế giới này, vì vậy những dãy số đó khá dài: American Express sử dụng dãy số 15 chữ số, MasterCard sử dụng dãy số 16 chữ số, và Visa sử dụng dãy số 13 và 16 chữ số. Và đó là các số thập phân (từ 0 đến 9), không phải hệ nhị phân, điều đó có nghĩa là, ví dụ, American Express có thể in tới 10^15 = 1.000.000.000.000.000 thẻ duy nhất! (Đó là, ừm, một triệu tỷ.)

Thực ra, đó là một chút nói quá, bởi vì các số thẻ tín dụng thực tế có cấu trúc nhất định. Tất cả các số American Express đều bắt đầu bằng 34 hoặc 37; hầu hết các số MasterCard bắt đầu bằng 51, 52, 53, 54 hoặc 55 (họ cũng có một số số bắt đầu tiềm năng khác mà chúng ta sẽ không quan tâm trong bài toán này); và tất cả các số Visa đều bắt đầu bằng 4. Nhưng các số thẻ tín dụng cũng có một "checksum" (số kiểm tra) được tích hợp bên trong, một mối quan hệ toán học giữa ít nhất một con số và các con số khác. Checksum đó cho phép máy tính (hoặc những người yêu toán học) phát hiện các lỗi đánh máy (ví dụ: hoán đổi vị trí), nếu không muốn nói là các số giả mạo, mà không cần phải truy vấn cơ sở dữ liệu, việc này có thể chậm. Tất nhiên, một nhà toán học không trung thực chắc chắn có thể tạo ra một số giả nhưng vẫn tuân thủ ràng buộc toán học, vì vậy việc tra cứu cơ sở dữ liệu vẫn là cần thiết cho các bước kiểm tra nghiêm ngặt hơn.

Trong một tệp có tên `credit.c` trong thư mục có tên `credit`, hãy triển khai một chương trình bằng C để kiểm tra tính hợp lệ của một số thẻ tín dụng cho trước.

## Thuật toán Luhn

Vậy công thức bí mật là gì? Hầu hết các loại thẻ đều sử dụng một thuật toán được phát minh bởi Hans Peter Luhn của IBM. Theo thuật toán Luhn, bạn có thể xác định xem một số thẻ tín dụng có hợp lệ (về mặt cú pháp) hay không như sau:

1. Nhân mọi chữ số thứ hai với 2, bắt đầu từ chữ số áp chót của dãy số, sau đó cộng các chữ số của các tích đó lại với nhau.
2. Cộng tổng đó với tổng của các chữ số không được nhân với 2.
3. Nếu chữ số cuối cùng của tổng thu được là 0 (hoặc nói một cách trang trọng hơn, nếu tổng modulo 10 bằng 0), thì con số đó hợp lệ!

Điều đó có vẻ hơi khó hiểu, vì vậy hãy thử một ví dụ với thẻ Visa của David: 4003600000000014.

1. Để phục vụ thảo luận, trước tiên hãy gạch chân mọi chữ số thứ hai, bắt đầu từ chữ số áp chót của dãy số:
   
   4003600000000014
   
   Được rồi, hãy nhân mỗi chữ số được gạch chân với 2:
   
   1•2 + 0•2 + 0•2 + 0•2 + 0•2 + 6•2 + 0•2 + 4•2
   
   Kết quả là:
   
   2 + 0 + 0 + 0 + 0 + 12 + 0 + 8
   
   Bây giờ hãy cộng các chữ số của các tích đó (tức là không phải bản thân các tích) lại với nhau:
   
   2 + 0 + 0 + 0 + 0 + 1 + 2 + 0 + 8 = 13
2. Bây giờ hãy cộng tổng đó (13) với tổng của các chữ số không được nhân với 2 (bắt đầu từ cuối):
   
   13 + 4 + 0 + 0 + 0 + 0 + 0 + 3 + 0 = 20
3. Đúng vậy, chữ số cuối cùng trong tổng đó (20) là 0, vì vậy thẻ của David là hợp lệ!

Vì vậy, việc xác thực số thẻ tín dụng không khó, nhưng làm bằng tay thì hơi tẻ nhạt. Hãy viết một chương trình.

## Chi tiết triển khai

Trong tệp `credit.c` ở thư mục `credit`, hãy viết một chương trình yêu cầu người dùng nhập số thẻ tín dụng và sau đó báo cáo (qua `printf`) xem đó có phải là số thẻ American Express, MasterCard hoặc Visa hợp lệ hay không, theo định nghĩa định dạng của từng loại ở đây. Để chúng tôi có thể tự động hóa một số kiểm tra cho mã của bạn, chúng tôi yêu cầu dòng đầu ra cuối cùng của chương trình phải là `AMEX\n` hoặc `MASTERCARD\n` hoặc `VISA\n` hoặc `INVALID\n`, không thừa không thiếu. Để đơn giản, bạn có thể giả định rằng đầu vào của người dùng sẽ hoàn toàn là số (nghĩa là không có dấu gạch ngang, như có thể được in trên thẻ thực tế) và nó sẽ không có các số 0 ở đầu. Nhưng đừng giả định rằng đầu vào của người dùng sẽ vừa với kiểu `int`! Tốt nhất nên sử dụng `get_long` từ thư viện của CS50 để lấy đầu vào của người dùng. (Tại sao?)

Hãy xem ví dụ dưới đây về cách chương trình của bạn nên hoạt động khi được cung cấp một số thẻ tín dụng hợp lệ (không có dấu gạch ngang).

```bash
$ ./credit
Number: 4003600000000014
VISA
```

Bản thân `get_long` sẽ từ chối các dấu gạch ngang (và nhiều thứ khác):

```bash
$ ./credit
Number: 4003-6000-0000-0014
Number: foo
Number: 4003600000000014
VISA
```

Nhưng việc bắt các đầu vào không phải là số thẻ tín dụng (ví dụ: số điện thoại) là tùy thuộc vào bạn, ngay cả khi nó là số:

```bash
$ ./credit
Number: 6176292929
INVALID
```

Kiểm tra chương trình của bạn với nhiều đầu vào khác nhau, cả hợp lệ và không hợp lệ. (Chúng tôi chắc chắn sẽ làm vậy!) Dưới đây là một [vài số thẻ](https://developer.paypal.com/api/nvp-soap/payflow/integration-guide/test-transactions/#standard-test-cards) mà PayPal đề xuất để kiểm tra.

Nếu chương trình của bạn hoạt động không chính xác trên một số đầu vào (hoặc hoàn toàn không biên dịch được), đã đến lúc gỡ lỗi!

### Hướng dẫn (Walkthrough)

### Cách kiểm tra mã của bạn

Bạn cũng có thể thực thi lệnh dưới đây để đánh giá tính chính xác của mã bằng cách sử dụng `check50`. Nhưng hãy nhớ tự mình biên dịch và kiểm tra nó trước!

```
check50 cs50/problems/2026/x/credit
```

Thực thi lệnh dưới đây để đánh giá phong cách lập trình của bạn bằng cách sử dụng `style50`.

```
style50 credit.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài làm của bạn.

```
submit50 cs50/problems/2026/x/credit
```
