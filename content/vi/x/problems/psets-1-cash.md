title: "Tiền lẻ - CS50x 2026"
pset: 1
draft: "false"
---

![US coins](coins.jpg)

## Bài toán cần giải quyết

Giả sử bạn đang làm việc tại một cửa hàng và một khách hàng đưa cho bạn $1.00 (100 cent) để mua kẹo có giá $0.50 (50 cent). Bạn sẽ cần trả lại cho họ "tiền thừa", số tiền còn lại sau khi họ thanh toán chi phí của viên kẹo. Khi thối tiền thừa, khả năng cao là bạn muốn giảm thiểu số lượng đồng xu mà mình đưa ra cho mỗi khách hàng, kẻo bạn bị hết xu (hoặc làm phiền khách hàng!). Trong một tệp có tên là `cash.c` trong thư mục có tên `cash`, hãy triển khai một chương trình bằng C in ra số lượng đồng xu tối thiểu cần thiết để thối một số tiền thừa nhất định, tính theo đơn vị cent, như ví dụ dưới đây:

```python
Change owed: 25
1
```

Nhưng hãy yêu cầu người dùng nhập một số nguyên (`int`) lớn hơn 0, để chương trình có thể hoạt động với bất kỳ số tiền thừa nào:

```python
Change owed: 70
4
```

Yêu cầu người dùng nhập lại nhiều lần nếu cần thiết, nếu giá trị họ nhập vào không lớn hơn hoặc bằng 0 (hoặc nếu giá trị nhập vào hoàn toàn không phải là một số nguyên `int`!).

## Bản demo

## Thuật toán Tham lam

May mắn thay, khoa học máy tính đã cung cấp cho các thu ngân ở khắp mọi nơi những cách thức để giảm thiểu số lượng đồng xu cần thối: thuật toán tham lam (greedy algorithms).

Theo Viện Tiêu chuẩn và Công nghệ Quốc gia (NIST), thuật toán tham lam là thuật toán "luôn đưa ra lựa chọn tốt nhất ngay lập tức, hoặc lựa chọn tối ưu cục bộ, trong khi tìm kiếm câu trả lời. Thuật toán tham lam tìm thấy giải pháp tối ưu tổng thể, hoặc tối ưu toàn cục, cho một số bài toán tối ưu hóa, nhưng có thể tìm thấy các giải pháp kém tối ưu hơn trong một số trường hợp của các bài toán khác."

Tất cả những điều đó có nghĩa là gì? Giả sử một thu ngân nợ khách hàng một khoản tiền thừa và trong ngăn kéo của thu ngân đó có các đồng quarter (25¢), dime (10¢), nickel (5¢) và penny (1¢). Bài toán cần giải quyết là quyết định xem nên đưa những loại đồng xu nào và số lượng mỗi loại là bao nhiêu cho khách hàng. Hãy coi một thu ngân "tham lam" là người muốn giải quyết bài toán này nhanh nhất có thể với mỗi đồng xu họ lấy ra khỏi ngăn kéo. Ví dụ, nếu một khách hàng được thối 41¢, "miếng cắn" đầu tiên lớn nhất (tức là lựa chọn tốt nhất ngay lập tức, hoặc tối ưu cục bộ) có thể thực hiện là 25¢. (Lựa chọn đó là "tốt nhất" vì nó giúp chúng ta tiến gần đến mức 0¢ nhanh hơn bất kỳ đồng xu nào khác.) Lưu ý rằng một lựa chọn với kích thước này sẽ giảm bớt bài toán 41¢ ban đầu xuống còn bài toán 16¢, vì 41 - 25 = 16. Nghĩa là, phần còn lại là một bài toán tương tự nhưng nhỏ hơn. Không cần phải nói, một lựa chọn 25¢ khác sẽ là quá lớn (giả sử thu ngân không muốn bị lỗ tiền), và vì vậy thu ngân tham lam của chúng ta sẽ chuyển sang lựa chọn có kích thước 10¢, để lại cho anh ta hoặc cô ta một bài toán 6¢. Tại thời điểm đó, sự tham lam đòi hỏi một lựa chọn 5¢ sau đó là một lựa chọn 1¢, và bài toán được giải quyết. Khách hàng nhận được một đồng quarter, một đồng dime, một đồng nickel và một đồng penny: tổng cộng bốn đồng xu.

Hóa ra cách tiếp cận tham lam này (tức là thuật toán này) không chỉ tối ưu cục bộ mà còn tối ưu toàn cục đối với hệ thống tiền tệ của Hoa Kỳ (và cả Liên minh Châu Âu). Nghĩa là, miễn là thu ngân có đủ mỗi loại đồng xu, cách tiếp cận từ lớn đến nhỏ này sẽ cho ra số lượng đồng xu ít nhất có thể. Ít bao nhiêu? Chà, bạn hãy cho chúng tôi biết nhé!

## Lời khuyên

Viết một đoạn mã mà bạn biết chắc sẽ biên dịch được

Mặc dù chương trình này sẽ chưa thực hiện bất kỳ chức năng nào, nhưng ít nhất nó phải biên dịch được với lệnh `make`!

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{

}
```

Lưu ý rằng bây giờ bạn đã bao gồm `cs50.h` và `stdio.h`, hai "tệp tiêu đề" (header files) sẽ cung cấp cho bạn quyền truy cập vào các hàm có thể giúp bạn giải quyết bài toán này.

Viết mã giả trước khi viết mã thật

Nếu không chắc chắn về cách giải quyết chính bài toán, hãy chia nó thành các bài toán nhỏ hơn mà bạn có thể giải quyết trước. Ví dụ, bài toán này thực chất chỉ gồm một vài bước sau:

1. Yêu cầu người dùng nhập số tiền thừa, tính bằng cent.
2. Tính toán xem bạn nên đưa cho khách hàng bao nhiêu đồng *quarter*. Trừ giá trị của những đồng quarter đó khỏi tổng số cent.
3. Tính toán xem bạn nên đưa cho khách hàng bao nhiêu đồng *dime*. Trừ giá trị của những đồng dime đó khỏi số cent còn lại.
4. Tính toán xem bạn nên đưa cho khách hàng bao nhiêu đồng *nickel*. Trừ giá trị của những đồng nickel đó khỏi số cent còn lại.
5. Tính toán xem bạn nên đưa cho khách hàng bao nhiêu đồng *penny*. Trừ giá trị của những đồng penny đó khỏi số cent còn lại.
6. Cộng tổng số lượng các đồng quarter, dime, nickel và penny đã sử dụng.
7. In tổng đó ra.

Đây là thuật toán tham lam mà bạn có thể sử dụng để giải quyết bài toán này, vì vậy hãy viết một số mã giả dưới dạng chú thích để nhắc nhở bản thân thực hiện điều đó:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for change owed, in cents

    // Calculate how many quarters you should give customer
    // Subtract the value of those quarters from cents

    // Calculate how many dimes you should give customer
    // Subtract the value of those dimes from remaining cents

    // Calculate how many nickels you should give customer
    // Subtract the value of those nickels from remaining cents

    // Calculate how many pennies you should give customer
    // Subtract the value of those pennies from remaining cents

    // Sum the number of quarters, dimes, nickels, and pennies used
    // Print that sum
}
```

Chuyển đổi mã giả thành mã thật

Đầu tiên, hãy xem xét cách bạn có thể yêu cầu người dùng nhập số cent mà họ được thối. Hãy nhớ rằng vòng lặp `do while` rất hữu ích khi bạn muốn thực hiện một việc gì đó ít nhất một lần, và có thể lặp đi lặp lại nhiều lần, như ví dụ dưới đây:

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);
}
```

Bạn nên dừng lại ở đây và chạy lệnh `make` cho chương trình của mình. Kiểm tra để chắc chắn rằng chương trình biên dịch được, và nó sẽ yêu cầu bạn nhập lại nếu bạn nhập số cent nhỏ hơn 0 (hoặc nếu bạn nhập một giá trị không phải số như "cat").

Tiếp theo, hãy xem xét cách tính toán xem bạn nên đưa cho khách hàng bao nhiêu đồng quarter. Vì chúng ta đang sử dụng thuật toán tham lam, câu hỏi này trở thành "số lượng đồng quarter *lớn nhất* mà bạn có thể đưa cho họ là bao nhiêu?". Bạn *có thể* viết giải pháp cho bài toán này ngay trong hàm `main` của mình. Tuy nhiên, việc viết một hàm mới có thể giúp tư duy của bạn mạch lạc hơn: ví dụ như một hàm tên là `calculate_quarters`. Bằng cách đó, bạn có thể tập trung tốt hơn vào logic để tính toán số đồng quarter. Sau này, bạn có thể tích hợp hàm này vào giải pháp tổng thể của mình.

```
int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
}
```

Lưu ý rằng hàm này thực sự được đặt tên là `calculate_quarters`. Thông qua `int cents` trong dấu ngoặc đơn, nó nhận một số nguyên `int` tên là `cents` làm đầu vào. Và, với từ khóa `int` ở phía trước tên hàm, nó cũng sẽ "trả về" (return) một số nguyên `int`. Nghĩa là, đầu ra của hàm này là một số nguyên: số lượng đồng quarter có thể tách ra từ số cent đó.

Bây giờ hãy xem xét cách triển khai `calculate_quarters` bằng cách tăng dần số lượng đồng quarter cho đến khi chúng ta không còn đủ cent để đổi sang quarter nữa:

```
int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

Tất nhiên, có ít nhất một cách đơn giản hơn để giải quyết bài toán `calculate_quarters` này. Nhưng chúng tôi sẽ để bạn tự mình tìm hiểu điều đó!

Khi `calculate_quarters` hoạt động như ý muốn, bạn có thể tích hợp hàm này vào chương trình của mình. Hãy cẩn thận "khai báo" (declare) "nguyên mẫu" (signature) của hàm (tức là `int calculate_quarters(int cents)`) phía trên hàm `main`, để bạn thực sự có thể sử dụng `calculate_quarters` ở đó trong khi vẫn định nghĩa chi tiết hàm ở bên dưới hàm `main`.

```c
#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;
    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Calculate how many quarters you should give customer
    int quarters = calculate_quarters(cents);

    // Subtract the value of those quarters from cents
    cents = cents - (quarters * 25);
}

int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
```

Một vài vấn đề đã được giải quyết, và vẫn còn một vài bước nữa! Bạn có nhận thấy một khuôn mẫu (pattern) mà bạn có thể tái sử dụng ở đây không?

## Cách kiểm tra

Đối với chương trình này, hãy thử kiểm tra mã của bạn một cách thủ công. Đây là một thói quen tốt:

- Nếu bạn nhập `-1`, chương trình của bạn có yêu cầu nhập lại không?
- Nếu bạn nhập `0`, chương trình của bạn có in ra `0` không?
- Nếu bạn nhập `1`, chương trình của bạn có in ra `1` không (tức là một đồng penny)?
- Nếu bạn nhập `4`, chương trình của bạn có in ra `4` không (tức là bốn đồng penny)?
- Nếu bạn nhập `5`, chương trình của bạn có in ra `1` không (tức là một đồng nickel)?
- Nếu bạn nhập `24`, chương trình của bạn có in ra `6` không (tức là hai đồng dime và bốn đồng penny)?
- Nếu bạn nhập `25`, chương trình của bạn có in ra `1` không (tức là một đồng quarter)?
- Nếu bạn nhập `26`, chương trình của bạn có in ra `2` không (tức là một đồng quarter và một đồng penny)?
- Nếu bạn nhập `99`, chương trình của bạn có in ra `9` không (tức là ba đồng quarter, hai đồng dime và bốn đồng penny)?

### Tính chính xác

```
check50 cs50/problems/2026/x/cash
```

### Phong cách

```
style50 cash.c
```

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài làm của mình, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/cash
```
