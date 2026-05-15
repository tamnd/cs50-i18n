---
title: "Filter - CS50x 2026"
pset: 4
draft: false
---

![Harvard Yard in grayscale](yard-grayscale.bmp)

## Bài toán cần giải quyết

Có lẽ cách đơn giản nhất để biểu diễn một hình ảnh là sử dụng một lưới các điểm ảnh (pixel), trong đó mỗi điểm ảnh có thể có một màu sắc khác nhau. Đối với hình ảnh đen trắng, chúng ta cần 1 bit cho mỗi pixel, vì 0 có thể đại diện cho màu đen và 1 có thể đại diện cho màu trắng, như hình bên dưới.

![a simple bitmap](bitmap.png)

Theo nghĩa này, một hình ảnh thực chất chỉ là một bản đồ bit (bitmap). Đối với những hình ảnh nhiều màu sắc hơn, bạn chỉ cần nhiều bit hơn cho mỗi pixel. Một định dạng tệp (như [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG), hoặc [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) hỗ trợ "màu 24-bit" sẽ sử dụng 24 bit cho mỗi pixel. (BMP thực tế hỗ trợ màu 1, 4, 8, 16, 24 và 32-bit.)

Một tệp BMP 24-bit sử dụng 8 bit để biểu thị lượng màu đỏ (red) trong màu của một pixel, 8 bit để biểu thị lượng màu xanh lá cây (green) và 8 bit để biểu thị lượng màu xanh dương (blue). Nếu bạn đã từng nghe nói về màu RGB, thì chính là nó: red, green, blue.

Nếu các giá trị R, G và B của một pixel nào đó trong tệp BMP lần lượt là `0xff`, `0x00` và `0x00` trong hệ thập lục phân (hexadecimal), thì pixel đó hoàn toàn là màu đỏ, vì `0xff` (tương đương với `255` trong hệ thập phân) có nghĩa là "rất nhiều màu đỏ", trong khi `0x00` và `0x00` lần lượt có nghĩa là "không có màu xanh lá" và "không có màu xanh dương". Trong bài toán này, bạn sẽ thao tác các giá trị R, G và B của từng pixel riêng lẻ, để cuối cùng tạo ra các bộ lọc hình ảnh của riêng mình.

Trong tệp có tên `helpers.c` nằm trong thư mục `filter-less`, hãy viết một chương trình để áp dụng các bộ lọc cho các tệp BMP.

## Minh họa

## Mã nguồn phân phối

Trong bài toán này, bạn sẽ mở rộng chức năng của mã nguồn do đội ngũ CS50 cung cấp.

Tải xuống mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực hiện lệnh `cd` một mình. Bạn sẽ thấy dấu nhắc terminal của mình trông giống như sau:

```
$
```

Tiếp theo thực hiện lệnh

```python
wget https://cdn.cs50.net/2026/x/psets/4/filter-less.zip
```

để tải xuống một tệp ZIP có tên `filter-less.zip` vào Codespace của bạn.

Sau đó thực hiện lệnh

```
unzip filter-less.zip
```

để tạo một thư mục có tên `filter-less`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực hiện lệnh

```
rm filter-less.zip
```

và trả lời "y" sau đó nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ gõ

```bash
cd filter-less
```

tiếp theo là Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ trông giống như dưới đây.

```
filter-less/ $
```

Thực hiện lệnh `ls` một mình, và bạn sẽ thấy một vài tệp: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` và `Makefile`. Bạn cũng sẽ thấy một thư mục, `images/`, chứa bốn tệp BMP. Nếu bạn gặp bất kỳ rắc rối nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Bối cảnh

### Kỹ thuật hơn một chút về Bitmap

Hãy nhớ rằng một tệp thực chất chỉ là một chuỗi các bit, được sắp xếp theo một cách nào đó. Do đó, một tệp BMP 24-bit về cơ bản chỉ là một chuỗi các bit, mà (hầu như) cứ mỗi 24 bit lại đại diện cho màu của một pixel nào đó. Nhưng một tệp BMP cũng chứa một số "siêu dữ liệu" (metadata), thông tin như chiều cao và chiều rộng của hình ảnh. Siêu dữ liệu đó được lưu trữ ở đầu tệp dưới dạng hai cấu trúc dữ liệu thường được gọi là "headers" (phần đầu), không nên nhầm lẫn với các tệp tiêu đề (header files) của C. (Nhân tiện, các header này đã phát triển theo thời gian. Bài toán này sử dụng phiên bản mới nhất của định dạng BMP của Microsoft, 4.0, ra mắt cùng với Windows 95.)

Header đầu tiên, được gọi là `BITMAPFILEHEADER`, dài 14 byte. (Hãy nhớ rằng 1 byte bằng 8 bit.) Header thứ hai, được gọi là `BITMAPINFOHEADER`, dài 40 byte. Ngay sau các header này là bitmap thực tế: một mảng các byte, trong đó mỗi bộ ba (triple) đại diện cho màu của một pixel. Tuy nhiên, BMP lưu trữ các bộ ba này theo thứ tự ngược lại (tức là BGR), với 8 bit cho màu xanh dương, tiếp theo là 8 bit cho màu xanh lá cây, sau đó là 8 bit cho màu đỏ. (Một số tệp BMP cũng lưu trữ toàn bộ bitmap theo thứ tự ngược lại, với hàng trên cùng của hình ảnh ở cuối tệp BMP. Nhưng chúng tôi đã lưu trữ các tệp BMP của bài tập này như mô tả ở đây, với hàng trên cùng của mỗi bitmap ở đầu tiên và hàng dưới cùng ở cuối cùng.) Nói cách khác, nếu chúng ta chuyển đổi biểu tượng mặt cười 1-bit ở trên thành mặt cười 24-bit, thay thế màu đen bằng màu đỏ, thì một tệp BMP 24-bit sẽ lưu trữ bitmap này như sau, trong đó `0000ff` biểu thị màu đỏ và `ffffff` biểu thị màu trắng; chúng tôi đã đánh dấu màu đỏ cho tất cả các trường hợp của `0000ff`.

![red smile](red_smile.png)

Vì chúng tôi đã trình bày các bit này từ trái sang phải, từ trên xuống dưới, theo 8 cột, bạn thực sự có thể nhìn thấy mặt cười màu đỏ nếu bạn lùi lại một bước.

Để rõ ràng hơn, hãy nhớ rằng một chữ số thập lục phân đại diện cho 4 bit. Theo đó, `ffffff` trong hệ thập lục phân thực sự biểu thị `111111111111111111111111` trong hệ nhị phân.

Lưu ý rằng bạn có thể biểu diễn một bitmap dưới dạng một mảng 2 chiều các pixel: trong đó hình ảnh là một mảng các hàng, và mỗi hàng là một mảng các pixel. Thật vậy, đó là cách chúng tôi đã chọn để biểu diễn hình ảnh bitmap trong bài toán này.

### Lọc hình ảnh

Lọc một hình ảnh thực chất có nghĩa là gì? Bạn có thể hiểu việc lọc một hình ảnh là lấy các pixel của một hình ảnh gốc và sửa đổi từng pixel theo cách mà một hiệu ứng cụ thể sẽ xuất hiện trong hình ảnh kết quả.

## Yêu cầu kỹ thuật

Cài đặt các hàm trong `helpers.c` sao cho người dùng có thể áp dụng các bộ lọc grayscale (thang độ xám), sepia (màu nâu đỏ), reflection (phản chiếu) hoặc blur (làm mờ) cho hình ảnh của họ.

- Hàm `grayscale` nên nhận một hình ảnh và chuyển nó thành phiên bản đen trắng của chính hình ảnh đó.
- Hàm `sepia` nên nhận một hình ảnh và chuyển nó thành phiên bản màu nâu đỏ (sepia) của chính hình ảnh đó.
- Hàm `reflect` nên nhận một hình ảnh và phản chiếu nó theo chiều ngang.
- Cuối cùng, hàm `blur` nên nhận một hình ảnh và chuyển nó thành phiên bản được làm mờ (box-blur) của chính hình ảnh đó.

Bạn không nên sửa đổi bất kỳ chữ ký hàm (function signatures) nào, cũng như không được sửa đổi bất kỳ tệp nào khác ngoài `helpers.c`.

## Gợi ý

Hiểu mã nguồn phân phối

Bây giờ chúng ta hãy xem xét một số tệp được cung cấp cho bạn dưới dạng mã nguồn phân phối để hiểu những gì bên trong chúng.

### `bmp.h`

Mở `bmp.h` (bằng cách nhấp đúp vào nó trong trình duyệt tệp) và xem thử.

Bạn sẽ thấy các định nghĩa của các header mà chúng tôi đã đề cập (`BITMAPINFOHEADER` và `BITMAPFILEHEADER`). Ngoài ra, tệp đó định nghĩa `BYTE`, `DWORD`, `LONG` và `WORD`, các kiểu dữ liệu thường thấy trong thế giới lập trình Windows. Lưu ý cách chúng chỉ là các tên thay thế (aliases) cho các kiểu dữ liệu cơ bản (primitives) mà bạn (hy vọng) đã quen thuộc. Có vẻ như `BITMAPFILEHEADER` và `BITMAPINFOHEADER` sử dụng các kiểu dữ liệu này.

Có lẽ quan trọng nhất đối với bạn, tệp này cũng định nghĩa một `struct` gọi là `RGBTRIPLE`, hiểu một cách đơn giản là nó "bao bọc" (encapsulates) ba byte: một xanh dương, một xanh lá cây và một đỏ (thứ tự mà chúng ta mong đợi tìm thấy các bộ ba RGB thực tế trên đĩa).

Tại sao các `struct` này lại hữu ích? Hãy nhớ rằng một tệp chỉ là một chuỗi các byte (hoặc, cuối cùng là các bit) trên đĩa. Nhưng các byte đó thường được sắp xếp theo cách mà một vài byte đầu tiên đại diện cho một cái gì đó, một vài byte tiếp theo đại diện cho một cái gì đó khác, v.v. Các "định dạng tệp" tồn tại vì thế giới đã tiêu chuẩn hóa ý nghĩa của từng byte. Bây giờ, chúng ta có thể chỉ cần đọc một tệp từ đĩa vào RAM dưới dạng một mảng lớn các byte. Và chúng ta có thể chỉ cần nhớ rằng byte tại `array[i]` đại diện cho một thứ, trong khi byte tại `array[j]` đại diện cho một thứ khác. Nhưng tại sao không đặt tên cho một số byte đó để chúng ta có thể truy xuất chúng từ bộ nhớ dễ dàng hơn? Đó chính xác là những gì các struct trong `bmp.h` cho phép chúng ta làm. Thay vì coi một tệp là một chuỗi dài các byte, chúng ta có thể coi nó là một chuỗi các `struct`.

### `filter.c`

Bây giờ, hãy mở `filter.c`. Tệp này đã được viết sẵn cho bạn, nhưng có một vài điểm quan trọng đáng lưu ý ở đây.

Đầu tiên, hãy lưu ý định nghĩa của `filters` ở dòng 10. Chuỗi đó cho chương trình biết các đối số dòng lệnh hợp lệ cho chương trình là gì: `b`, `g`, `r` và `s`. Mỗi đối số chỉ định một bộ lọc khác nhau mà chúng ta có thể áp dụng cho hình ảnh của mình: làm mờ (blur), thang độ xám (grayscale), phản chiếu (reflection) và màu nâu đỏ (sepia).

Mấy dòng tiếp theo mở một tệp hình ảnh, đảm bảo nó thực sự là một tệp BMP và đọc tất cả thông tin pixel vào một mảng 2D gọi là `image`.

Cuộn xuống câu lệnh `switch` bắt đầu ở dòng 101. Lưu ý rằng, tùy thuộc vào bộ lọc (`filter`) mà chúng ta đã chọn, một hàm khác nhau sẽ được gọi: nếu người dùng chọn bộ lọc `b`, chương trình sẽ gọi hàm `blur`; nếu là `g`, thì `grayscale` được gọi; nếu là `r`, thì `reflect` được gọi; và nếu là `s`, thì `sepia` được gọi. Lưu ý thêm rằng mỗi hàm này đều nhận đối số là chiều cao của hình ảnh, chiều rộng của hình ảnh và mảng pixel 2D.

Đây là các hàm mà bạn sẽ (sớm thôi!) cài đặt. Như bạn có thể hình dung, mục tiêu là mỗi hàm này sẽ chỉnh sửa mảng pixel 2D theo cách mà bộ lọc mong muốn được áp dụng cho hình ảnh.

Các dòng còn lại của chương trình lấy hình ảnh (`image`) kết quả và ghi chúng ra một tệp hình ảnh mới.

### `helpers.h`

Tiếp theo, hãy xem `helpers.h`. Tệp này khá ngắn và chỉ cung cấp các nguyên mẫu hàm (function prototypes) cho các hàm bạn đã thấy trước đó.

Ở đây, hãy lưu ý rằng mỗi hàm nhận một mảng 2D gọi là `image` làm đối số, trong đó `image` là một mảng gồm `height` hàng và mỗi hàng bản thân nó là một mảng gồm `width` cấu trúc `RGBTRIPLE`. Vì vậy, nếu `image` đại diện cho toàn bộ bức tranh, thì `image[0]` đại diện cho hàng đầu tiên và `image[0][0]` đại diện cho pixel ở góc trên bên trái của hình ảnh.

### `helpers.c`

Bây giờ, hãy mở `helpers.c`. Đây là nơi chứa phần cài đặt của các hàm đã được khai báo trong `helpers.h`. Nhưng lưu ý rằng, hiện tại, phần cài đặt đang bị thiếu! Phần này là tùy thuộc vào bạn.

### `Makefile`

Cuối cùng, hãy xem `Makefile`. Tệp này chỉ định những gì sẽ xảy ra khi chúng ta chạy một lệnh terminal như `make filter`. Trong khi các chương trình bạn có thể đã viết trước đây chỉ nằm gọn trong một tệp, `filter` có vẻ như sử dụng nhiều tệp: `filter.c` và `helpers.c`. Vì vậy, chúng ta sẽ cần cho `make` biết cách biên dịch tệp này.

Hãy thử tự mình biên dịch `filter` bằng cách đi tới terminal và chạy

```bash
$ make filter
```

Sau đó, bạn có thể chạy chương trình bằng cách chạy:

```bash
$ ./filter -g images/yard.bmp out.bmp
```

lệnh này lấy hình ảnh tại `images/yard.bmp` và tạo ra một hình ảnh mới gọi là `out.bmp` sau khi chạy các pixel qua hàm `grayscale`. Tuy nhiên, `grayscale` vẫn chưa thực hiện bất cứ điều gì, vì vậy hình ảnh đầu ra sẽ trông giống như hình ảnh sân trường (yard) ban đầu.

Cài đặt `grayscale`

Một bộ lọc phổ biến là bộ lọc "grayscale" (thang độ xám), nơi chúng ta lấy một hình ảnh và muốn chuyển nó sang đen trắng. Cơ chế hoạt động của nó như thế nào?

- Hãy nhớ rằng nếu các giá trị red, green và blue đều được đặt thành `0x00` (thập lục phân của `0`), thì pixel đó là màu đen. Và nếu tất cả các giá trị được đặt thành `0xff` (thập lục phân của `255`), thì pixel đó là màu trắng. Miễn là các giá trị red, green và blue đều bằng nhau, kết quả sẽ là các sắc thái xám khác nhau dọc theo phổ đen-trắng, với các giá trị cao hơn có nghĩa là các sắc thái nhạt hơn (gần màu trắng hơn) và các giá trị thấp hơn có nghĩa là các sắc thái đậm hơn (gần màu đen hơn).
- Vì vậy, để chuyển đổi một pixel sang thang độ xám, bạn chỉ cần đảm bảo các giá trị red, green và blue đều có cùng một giá trị. Nhưng làm thế nào để bạn biết nên đặt chúng thành giá trị nào? Có lẽ hợp lý khi mong đợi rằng nếu các giá trị red, green và blue ban đầu đều khá cao, thì giá trị mới cũng nên khá cao. Và nếu các giá trị ban đầu đều thấp, thì giá trị mới cũng nên thấp.
- Trên thực tế, để đảm bảo mỗi pixel của hình ảnh mới vẫn có cùng độ sáng hoặc độ tối chung như hình ảnh cũ, bạn có thể lấy **giá trị trung bình** của các giá trị red, green và blue để xác định sắc thái xám cho pixel mới.

Nếu bạn áp dụng thuật toán trên cho từng pixel trong hình ảnh, kết quả sẽ là một hình ảnh được chuyển đổi sang thang độ xám. Hãy viết một số mã giả (pseudocode) để giúp bạn giải quyết bài toán này.

```c
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Lặp qua tất cả các pixel

        // Lấy trung bình cộng của red, green và blue

        // Cập nhật giá trị pixel
}
```

Đầu tiên, làm thế nào bạn có thể lặp qua tất cả các pixel? Hãy nhớ rằng các pixel của hình ảnh được lưu trữ trong mảng hai chiều, `image`. Để lặp qua một mảng hai chiều, bạn sẽ cần hai vòng lặp, một vòng lặp lồng bên trong vòng lặp kia.

```c
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Lặp qua tất cả các pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Lấy trung bình cộng của red, green và blue

            // Cập nhật giá trị pixel
        }
    }
}
```

Bây giờ, bạn có thể sử dụng `image[i][j]` để truy cập bất kỳ pixel riêng lẻ nào của hình ảnh. Nhưng làm thế nào để lấy trung bình cộng của các thành phần red, green và blue? Hãy nhớ mỗi phần tử của `image` là một `RGBTRIPLE`, là `struct` được định nghĩa trong `bmp.h` để đại diện cho một pixel. Cú pháp thông thường để truy cập các thành viên của một `struct` được áp dụng, trong đó `image[i][j].rgbtRed` sẽ cho bạn quyền truy cập vào giá trị màu đỏ của `RGBTRIPLE`, `image[i][j].rgbtGreen` sẽ cho bạn quyền truy cập vào giá trị màu xanh lá cây của nó, v.v.

Khi bạn tính toán giá trị trung bình, hãy lưu ý rằng giá trị của các thành phần `rgbtRed`, `rgbtGreen` và `rgbtBlue` của một pixel đều là các số nguyên. Vì vậy, hãy đảm bảo [làm tròn](https://manual.cs50.io/3/round) bất kỳ số thực dấu phẩy động nào thành số nguyên gần nhất khi gán chúng cho giá trị pixel! Và tại sao bạn lại muốn chia tổng của các số nguyên này cho 3.0 chứ không phải 3?

Sau khi bạn đã tính trung bình các giá trị red, green và blue của pixel thành màu xám kết quả, hãy tiếp tục và cập nhật các giá trị red, green và blue của pixel đó. Đến bây giờ, bạn đã quen thuộc với cú pháp gán rồi!

Cài đặt `sepia`

Hầu hết các chương trình chỉnh sửa hình ảnh đều hỗ trợ bộ lọc "sepia", bộ lọc này mang lại cho hình ảnh cảm giác cổ xưa bằng cách làm cho toàn bộ hình ảnh trông hơi nâu đỏ.

- Một hình ảnh có thể được chuyển đổi sang màu sepia bằng cách lấy từng pixel và tính toán các giá trị red, green và blue mới dựa trên các giá trị ban đầu của cả ba.
- Có một số thuật toán để chuyển đổi hình ảnh sang màu sepia, nhưng đối với bài toán này, chúng tôi yêu cầu bạn sử dụng thuật toán sau. Đối với mỗi pixel, các giá trị màu sepia nên được tính toán dựa trên các giá trị màu ban đầu theo công thức bên dưới.
  
  ```
  sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue
  sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue
  sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue
  ```
- Tất nhiên, kết quả của mỗi công thức này có thể không phải là một số nguyên, nhưng mỗi giá trị có thể được làm tròn đến số nguyên gần nhất. Cũng có khả năng kết quả của công thức là một số lớn hơn 255, giá trị tối đa cho giá trị màu 8-bit. Trong trường hợp đó, các giá trị red, green và blue nên được giới hạn ở mức 255. Do đó, chúng ta có thể đảm bảo rằng các giá trị red, green và blue kết quả sẽ là các số nguyên nằm trong khoảng từ 0 đến 255.

Viết một số mã giả để giúp bạn giải quyết bài toán này và nhớ sử dụng các vòng lặp `for` lồng nhau để duyệt qua mọi pixel.

```c
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Lặp qua tất cả các pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
            // Tính toán giá trị sepia

            // Cập nhật pixel với giá trị sepia
        }
    }
}
```

Để tính toán các giá trị `sepia`, hãy xem lại các dấu đầu dòng ở trên. Bạn có công thức để tính toán các giá trị sepia, nhưng vẫn còn một vài điểm cần lưu ý. Cụ thể, bạn sẽ cần...

- Làm tròn kết quả của mỗi phép tính đến số nguyên gần nhất
- Đảm bảo giá trị kết quả không lớn hơn 255

Làm thế nào một hàm trả về giá trị nhỏ hơn trong hai số nguyên có thể hữu ích khi cài đặt `sepia`, đặc biệt là khi bạn cần đảm bảo giá trị của một màu không cao hơn 255? Bạn có thể, nhưng không bắt buộc, tự viết một hàm bổ trợ (helper function) của riêng mình để làm điều đó!

Cài đặt `reflect`

Một số bộ lọc cũng có thể di chuyển các pixel xung quanh. Ví dụ, phản chiếu (reflecting) một hình ảnh là một bộ lọc mà hình ảnh kết quả là những gì bạn sẽ nhận được bằng cách đặt hình ảnh ban đầu trước gương.

- Bất kỳ pixel nào ở phía bên trái của hình ảnh sẽ kết thúc ở phía bên phải và ngược lại.
- Lưu ý rằng tất cả các pixel ban đầu của hình ảnh gốc vẫn sẽ hiện diện trong hình ảnh phản chiếu, chỉ là các pixel đó có thể đã được sắp xếp lại để ở một vị trí khác trong hình ảnh.

Do đó, trong hàm `reflect`, bạn sẽ cần hoán đổi giá trị của các pixel ở các phía đối diện của một hàng. Viết một số mã giả để giúp bạn bắt đầu:

```c
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Lặp qua tất cả các pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Hoán đổi pixel
        }
    }
}
```

Nhớ lại từ bài giảng cách chúng ta thực hiện hoán đổi hai giá trị bằng một biến tạm thời. Không cần sử dụng một hàm riêng để hoán đổi trừ khi bạn muốn!

Và bây giờ là lúc thích hợp để nghĩ về các vòng lặp `for` lồng nhau của bạn. Vòng lặp `for` bên ngoài lặp qua mọi hàng, trong khi vòng lặp `for` bên trong lặp qua mọi pixel trong hàng đó. Tuy nhiên, để phản chiếu thành công một hàng, bạn có cần lặp qua mọi pixel trong hàng đó không?

Cài đặt `blur`

Có một số cách để tạo hiệu ứng làm mờ hoặc làm mềm hình ảnh. Đối với bài toán này, chúng ta sẽ sử dụng "box blur", hoạt động bằng cách lấy từng pixel và đối với mỗi giá trị màu, cung cấp cho nó một giá trị mới bằng cách tính trung bình các giá trị màu của các pixel lân cận.

- Hãy xem xét lưới pixel sau đây, trong đó chúng tôi đã đánh số cho từng pixel.
  
  ![a grid of pixels](grid.png)
- Giá trị mới của mỗi pixel sẽ là trung bình cộng giá trị của tất cả các pixel nằm trong phạm vi 1 hàng và 1 cột so với pixel ban đầu (tạo thành một ô vuông 3x3). Ví dụ: mỗi giá trị màu cho pixel 6 sẽ được tính bằng cách lấy trung bình các giá trị màu ban đầu của các pixel 1, 2, 3, 5, 6, 7, 9, 10 và 11 (lưu ý rằng pixel 6 cũng được bao gồm trong giá trị trung bình). Tương tự, giá trị màu cho pixel 11 sẽ được tính bằng cách lấy trung bình các giá trị màu của các pixel 6, 7, 8, 10, 11, 12, 14, 15 và 16.
- Đối với một pixel dọc theo cạnh hoặc góc, như pixel 15, chúng ta vẫn sẽ tìm kiếm tất cả các pixel trong phạm vi 1 hàng và 1 cột: trong trường hợp này là các pixel 10, 11, 12, 14, 15 và 16.

Khi cài đặt hàm `blur`, bạn có thể thấy rằng việc làm mờ một pixel cuối cùng sẽ ảnh hưởng đến việc làm mờ một pixel khác. Tốt nhất là tạo một bản sao của `image` bằng cách khai báo một mảng hai chiều mới với mã như `RGBTRIPLE copy[height][width];`. Sau đó, sao chép `image` vào `copy`, từng pixel một, bằng các vòng lặp `for` lồng nhau, như sau:

```c
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Tạo một bản sao của image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
}
```

Bây giờ, bạn có thể đọc màu của các pixel từ `copy` nhưng ghi (tức là thay đổi) màu của các pixel trong `image`!

## Hướng dẫn chi tiết

**Lưu ý rằng có 5 video trong danh sách phát này. [Mở trên YouTube](https://www.youtube.com/playlist?list=PLhQjrBD2T3837jmUt0ep7Tpmnxdv9NVut).**

## Cách kiểm tra

Hãy nhớ kiểm tra tất cả các bộ lọc của bạn trên các tệp bitmap mẫu được cung cấp!

### Tính chính xác

```
check50 cs50/problems/2026/x/filter/less
```

### Phong cách

```
style50 helpers.c
```

## Cách nộp bài

Trong terminal của bạn, thực hiện lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/filter/less
```
