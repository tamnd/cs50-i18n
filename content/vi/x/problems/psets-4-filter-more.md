---
title: "Bộ lọc - CS50x 2026"
pset: 4
draft: false
---

![Harvard Yard với phát hiện cạnh](yard-edges.bmp)

## Bài toán cần giải quyết

Có lẽ cách đơn giản nhất để biểu diễn một hình ảnh là dùng một lưới các pixel (tức là các điểm), mỗi điểm có thể có một màu sắc khác nhau. Đối với hình ảnh đen trắng, chúng ta cần 1 bit cho mỗi pixel, trong đó 0 có thể đại diện cho màu đen và 1 có thể đại diện cho màu trắng, như hình dưới đây.

![một bitmap đơn giản](bitmap.png)

Theo nghĩa này, một hình ảnh chỉ là một bitmap (tức là một bản đồ các bit). Đối với các hình ảnh nhiều màu sắc hơn, bạn chỉ đơn giản là cần nhiều bit hơn cho mỗi pixel. Một định dạng tệp (như [BMP](https://en.wikipedia.org/wiki/BMP_file_format), [JPEG](https://en.wikipedia.org/wiki/JPEG), hoặc [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics)) hỗ trợ "màu 24-bit" sẽ sử dụng 24 bit cho mỗi pixel. (BMP thực tế hỗ trợ các loại màu 1, 4, 8, 16, 24 và 32-bit.)

Một tệp BMP 24-bit sử dụng 8 bit để biểu thị lượng màu đỏ (red) trong màu của một pixel, 8 bit để biểu thị lượng màu xanh lá (green) và 8 bit để biểu thị lượng màu xanh dương (blue). Nếu bạn từng nghe về màu RGB, thì đó chính là nó: red, green, blue.

Nếu các giá trị R, G và B của một pixel trong tệp BMP, chẳng hạn, là `0xff`, `0x00` và `0x00` ở hệ thập lục phân, thì pixel đó hoàn toàn là màu đỏ, vì `0xff` (còn được gọi là `255` ở hệ thập phân) có nghĩa là "rất nhiều đỏ", trong khi `0x00` và `0x00` tương ứng có nghĩa là "không có xanh lá" và "không có xanh dương". Trong bài toán này, bạn sẽ thao tác với các giá trị R, G và B của từng pixel riêng lẻ, từ đó tạo ra các bộ lọc hình ảnh của riêng mình.

Trong tệp có tên `helpers.c` nằm trong thư mục `filter-more`, hãy viết một chương trình để áp dụng các bộ lọc cho các tệp BMP.

## Demo

## Mã nguồn phân phối

Trong bài toán này, bạn sẽ mở rộng chức năng của mã nguồn do đội ngũ CS50 cung cấp.

Tải mã nguồn phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal của bạn và thực thi lệnh `cd`. Bạn sẽ thấy lời nhắc của cửa sổ terminal giống như dưới đây:

```
$
```

Tiếp theo, hãy thực thi

```python
wget https://cdn.cs50.net/2026/x/psets/4/filter-more.zip
```

để tải một tệp ZIP có tên `filter-more.zip` vào codespace của bạn.

Sau đó thực thi

```
unzip filter-more.zip
```

để tạo một thư mục có tên `filter-more`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi

```
rm filter-more.zip
```

và trả lời "y" rồi nhấn Enter tại lời nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy nhập

```bash
cd filter-more
```

rồi nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Lời nhắc của bạn bây giờ sẽ giống như dưới đây.

```
filter-more/ $
```

Thực thi lệnh `ls`, bạn sẽ thấy một vài tệp: `bmp.h`, `filter.c`, `helpers.h`, `helpers.c` và `Makefile`. Bạn cũng sẽ thấy một thư mục có tên `images` chứa bốn tệp BMP. Nếu bạn gặp bất kỳ khó khăn nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Bối cảnh

### Chi tiết kỹ thuật hơn về Bit(map)

Hãy nhớ rằng một tệp chỉ là một chuỗi các bit, được sắp xếp theo một cách nào đó. Một tệp BMP 24-bit, do đó, về cơ bản chỉ là một chuỗi các bit, mà (hầu như) cứ mỗi 24 bit lại đại diện cho màu của một pixel nào đó. Nhưng một tệp BMP cũng chứa một số "metadata" (siêu dữ liệu), thông tin như chiều cao và chiều rộng của hình ảnh. Metadata đó được lưu trữ ở đầu tệp dưới dạng hai cấu trúc dữ liệu thường được gọi là "headers" (phần đầu), đừng nhầm lẫn với các tệp tiêu đề (header files) của C. (Nhân tiện, các header này đã phát triển theo thời gian. Bài toán này sử dụng phiên bản mới nhất của định dạng BMP của Microsoft, 4.0, ra mắt cùng với Windows 95.)

Header đầu tiên trong số này, được gọi là `BITMAPFILEHEADER`, dài 14 byte. (Nhớ rằng 1 byte bằng 8 bit.) Header thứ hai, được gọi là `BITMAPINFOHEADER`, dài 40 byte. Ngay sau các header này là bitmap thực tế: một mảng các byte, trong đó mỗi bộ ba byte đại diện cho màu của một pixel. Tuy nhiên, BMP lưu trữ các bộ ba này theo thứ tự ngược lại (tức là BGR), với 8 bit cho màu xanh dương (blue), tiếp theo là 8 bit cho màu xanh lá (green), và cuối cùng là 8 bit cho màu đỏ (red). (Một số tệp BMP cũng lưu trữ toàn bộ bitmap theo thứ tự ngược, với hàng trên cùng của ảnh nằm ở cuối tệp BMP. Nhưng chúng tôi đã lưu trữ các tệp BMP của bài tập này như mô tả ở đây, với hàng trên cùng của mỗi bitmap ở đầu và hàng dưới cùng ở cuối.) Nói cách khác, nếu chúng ta chuyển đổi hình mặt cười 1-bit ở trên thành mặt cười 24-bit, thay màu đỏ cho màu đen, một tệp BMP 24-bit sẽ lưu trữ bitmap này như sau, trong đó `0000ff` biểu thị màu đỏ và `ffffff` biểu thị màu trắng; chúng tôi đã làm nổi bật màu đỏ cho tất cả các trường hợp của `0000ff`.

![mặt cười màu đỏ](red_smile.png)

Vì chúng tôi đã trình bày các bit này từ trái sang phải, từ trên xuống dưới, trong 8 cột, bạn thực sự có thể nhìn thấy mặt cười màu đỏ nếu lùi lại một chút.

Để rõ ràng hơn, hãy nhớ rằng một chữ số thập lục phân đại diện cho 4 bit. Theo đó, `ffffff` trong hệ thập lục phân thực sự biểu thị `111111111111111111111111` trong hệ nhị phân.

Lưu ý rằng bạn có thể biểu diễn một bitmap dưới dạng mảng 2 chiều của các pixel: trong đó hình ảnh là một mảng của các hàng, mỗi hàng là một mảng của các pixel. Thật vậy, đó là cách chúng tôi chọn để biểu diễn các hình ảnh bitmap trong bài toán này.

### Bộ lọc hình ảnh

Việc lọc một hình ảnh thực sự có nghĩa là gì? Bạn có thể coi việc lọc một hình ảnh là lấy các pixel của một hình ảnh gốc và sửa đổi từng pixel theo cách để một hiệu ứng cụ thể hiển thị rõ trong hình ảnh kết quả.

#### Thang độ xám (Grayscale)

Một bộ lọc phổ biến là bộ lọc "grayscale", nơi chúng ta lấy một hình ảnh và muốn chuyển nó sang màu đen trắng. Điều đó hoạt động như thế nào?

Hãy nhớ rằng nếu các giá trị red, green và blue đều được đặt thành `0x00` (thập lục phân của `0`), thì pixel đó là màu đen. Và nếu tất cả các giá trị được đặt thành `0xff` (thập lục phân của `255`), thì pixel đó là màu trắng. Miễn là các giá trị red, green và blue đều bằng nhau, kết quả sẽ là các sắc thái xám khác nhau dọc theo phổ đen-trắng, với các giá trị cao hơn nghĩa là các sắc thái sáng hơn (gần với màu trắng hơn) và các giá trị thấp hơn nghĩa là các sắc thái tối hơn (gần với màu đen hơn).

Vì vậy, để chuyển đổi một pixel sang thang độ xám, chúng ta chỉ cần đảm bảo các giá trị red, green và blue đều là cùng một giá trị. Nhưng làm thế nào để chúng ta biết nên đặt chúng thành giá trị nào? Có lẽ hợp lý khi mong đợi rằng nếu các giá trị red, green và blue ban đầu đều khá cao, thì giá trị mới cũng phải khá cao. Và nếu các giá trị ban đầu đều thấp, thì giá trị mới cũng phải thấp.

Thực tế, để đảm bảo mỗi pixel của hình ảnh mới vẫn có cùng độ sáng hoặc độ tối tổng thể như hình ảnh cũ, chúng ta có thể lấy trung bình cộng của các giá trị red, green và blue để xác định sắc thái xám cho pixel mới.

Nếu bạn áp dụng điều đó cho từng pixel trong ảnh, kết quả sẽ là một hình ảnh được chuyển đổi sang thang độ xám.

#### Phản chiếu (Reflection)

Một số bộ lọc cũng có thể di chuyển các pixel xung quanh. Chẳng hạn, phản chiếu một hình ảnh là một bộ lọc mà hình ảnh kết quả là những gì bạn sẽ nhận được khi đặt hình ảnh gốc trước gương. Vì vậy, bất kỳ pixel nào ở phía bên trái của hình ảnh sẽ nằm ở bên phải và ngược lại.

Lưu ý rằng tất cả các pixel ban đầu của hình ảnh gốc vẫn sẽ hiện diện trong hình ảnh phản chiếu, chỉ là các pixel đó có thể đã được sắp xếp lại để ở một vị trí khác trong hình ảnh.

#### Làm mờ (Blur)

Có nhiều cách để tạo ra hiệu ứng làm mờ hoặc làm mềm hình ảnh. Đối với bài toán này, chúng ta sẽ sử dụng "box blur", hoạt động bằng cách lấy từng pixel và đối với mỗi giá trị màu, gán cho nó một giá trị mới bằng cách tính trung bình các giá trị màu của các pixel lân cận.

Hãy xem lưới các pixel sau đây, nơi chúng tôi đã đánh số cho từng pixel.

![một lưới các pixel](grid.png)

Giá trị mới của mỗi pixel sẽ là trung bình cộng giá trị của tất cả các pixel nằm trong phạm vi 1 hàng và 1 cột của pixel ban đầu (tạo thành một hộp 3x3). Ví dụ, mỗi giá trị màu cho pixel 6 sẽ nhận được bằng cách tính trung bình các giá trị màu ban đầu của các pixel 1, 2, 3, 5, 6, 7, 9, 10 và 11 (lưu ý rằng chính pixel 6 cũng được bao gồm trong giá trị trung bình). Tương tự, các giá trị màu cho pixel 11 sẽ nhận được bằng cách tính trung bình các giá trị màu của các pixel 6, 7, 8, 10, 11, 12, 14, 15 và 16.

Đối với một pixel dọc theo cạnh hoặc ở góc, như pixel 15, chúng ta vẫn sẽ tìm kiếm tất cả các pixel trong phạm vi 1 hàng và cột: trong trường hợp này là các pixel 10, 11, 12, 14, 15 và 16.

#### Phát hiện cạnh (Edges)

Trong các thuật toán trí tuệ nhân tạo để xử lý hình ảnh, việc phát hiện các cạnh trong một hình ảnh thường rất hữu ích: đó là các đường trong hình ảnh tạo ra ranh giới giữa vật thể này với vật thể khác. Một cách để đạt được hiệu ứng này là áp dụng [toán tử Sobel](https://en.wikipedia.org/wiki/Sobel_operator) cho hình ảnh.

Giống như làm mờ ảnh, phát hiện cạnh cũng hoạt động bằng cách lấy từng pixel và sửa đổi nó dựa trên lưới pixel 3x3 bao quanh pixel đó. Nhưng thay vì chỉ lấy giá trị trung bình của chín pixel, toán tử Sobel tính toán giá trị mới của mỗi pixel bằng cách lấy tổng có trọng số của các giá trị cho các pixel xung quanh. Và vì các cạnh giữa các vật thể có thể diễn ra theo cả hướng dọc và hướng ngang, bạn thực sự sẽ tính toán hai tổng có trọng số: một để phát hiện các cạnh theo hướng x và một để phát hiện các cạnh theo hướng y. Cụ thể, bạn sẽ sử dụng hai "kernels" sau:

![các Sobel kernels](sobel.png)

Làm thế nào để giải thích các kernel này? Tóm lại, đối với mỗi giá trị trong ba giá trị màu cho mỗi pixel, chúng ta sẽ tính toán hai giá trị `Gx` và `Gy`. Chẳng hạn, để tính `Gx` cho giá trị kênh đỏ của một pixel, chúng ta sẽ lấy các giá trị đỏ ban đầu của chín pixel tạo thành một hộp 3x3 xung quanh pixel đó, nhân mỗi giá trị với giá trị tương ứng trong kernel `Gx`, và lấy tổng của các giá trị kết quả.

Tại sao lại là những giá trị cụ thể này cho kernel? Chẳng hạn theo hướng `Gx`, chúng ta đang nhân các pixel ở bên phải của pixel mục tiêu với một số dương và nhân các pixel ở bên trái của pixel mục tiêu với một số âm. Khi chúng ta tính tổng, nếu các pixel ở bên phải có màu tương tự với các pixel ở bên trái, kết quả sẽ gần bằng 0 (các con số triệt tiêu nhau). Nhưng nếu các pixel ở bên phải rất khác với các pixel ở bên trái, thì giá trị kết quả sẽ rất dương hoặc rất âm, cho thấy một sự thay đổi màu sắc mà khả năng cao là kết quả của ranh giới giữa các vật thể. Và lập luận tương tự cũng đúng khi tính toán các cạnh theo hướng `y`.

Sử dụng các kernel này, chúng ta có thể tạo ra một giá trị `Gx` và `Gy` cho mỗi kênh đỏ, xanh lá và xanh dương cho một pixel. Nhưng mỗi kênh chỉ có thể nhận một giá trị, không phải hai: vì vậy chúng ta cần một cách nào đó để kết hợp `Gx` và `Gy` thành một giá trị duy nhất. Thuật toán bộ lọc Sobel kết hợp `Gx` và `Gy` thành một giá trị cuối cùng bằng cách tính căn bậc hai của `Gx^2 + Gy^2`. Và vì giá trị kênh chỉ có thể nhận giá trị nguyên từ 0 đến 255, hãy đảm bảo giá trị kết quả được làm tròn đến số nguyên gần nhất và giới hạn ở mức tối đa là 255!

Còn về việc xử lý các pixel ở cạnh hoặc ở góc của hình ảnh thì sao? Có nhiều cách để xử lý các pixel ở cạnh, nhưng cho mục đích của bài toán này, chúng tôi yêu cầu bạn coi hình ảnh như thể có một đường viền màu đen tuyền rộng 1 pixel bao quanh cạnh của hình ảnh: do đó, việc cố gắng truy cập một pixel vượt quá cạnh của hình ảnh nên được coi là một pixel đen tuyền (các giá trị 0 cho mỗi màu đỏ, xanh lá và xanh dương). Điều này sẽ loại bỏ hiệu quả các pixel đó khỏi tính toán `Gx` và `Gy` của chúng ta.

## Đặc tả kỹ thuật

Hãy triển khai các hàm trong `helpers.c` sao cho người dùng có thể áp dụng các bộ lọc grayscale (thang độ xám), reflection (phản chiếu), blur (làm mờ) hoặc edge detection (phát hiện cạnh) cho hình ảnh của họ.

- Hàm `grayscale` nên nhận một hình ảnh và chuyển nó thành phiên bản đen trắng của chính hình ảnh đó.
- Hàm `reflect` nên nhận một hình ảnh và phản chiếu nó theo chiều ngang.
- Hàm `blur` nên nhận một hình ảnh và chuyển nó thành phiên bản được làm mờ (box-blurred) của chính hình ảnh đó.
- Hàm `edges` nên nhận một hình ảnh và làm nổi bật các cạnh giữa các vật thể, theo toán tử Sobel.

Bạn không nên sửa đổi bất kỳ khai báo hàm (function signatures) nào, cũng như không nên sửa đổi bất kỳ tệp nào khác ngoài `helpers.c`.

## Hiểu về mã nguồn

Bây giờ hãy cùng xem qua một số tệp được cung cấp cho bạn dưới dạng mã nguồn phân phối để hiểu những gì bên trong chúng.

### `bmp.h`

Hãy mở `bmp.h` (bằng cách nhấp đúp vào nó trong trình duyệt tệp) và quan sát.

Bạn sẽ thấy các định nghĩa về các header mà chúng tôi đã đề cập (`BITMAPINFOHEADER` và `BITMAPFILEHEADER`). Ngoài ra, tệp đó còn định nghĩa các kiểu dữ liệu `BYTE`, `DWORD`, `LONG` và `WORD`, vốn thường thấy trong thế giới lập trình Windows. Lưu ý cách chúng chỉ là các bí danh cho các kiểu dữ liệu cơ bản (primitives) mà bạn (hy vọng) đã quen thuộc. Có vẻ như `BITMAPFILEHEADER` và `BITMAPINFOHEADER` sử dụng các kiểu dữ liệu này.

Có lẽ quan trọng nhất đối với bạn, tệp này cũng định nghĩa một `struct` có tên `RGBTRIPLE`, đơn giản là "bao bọc" ba byte: một xanh dương, một xanh lá và một đỏ (hãy nhớ đây là thứ tự mà chúng ta mong đợi tìm thấy các bộ ba RGB thực sự trên đĩa).

Tại sao các `struct` này lại hữu ích? Hãy nhớ rằng một tệp chỉ là một chuỗi các byte (hoặc cuối cùng là các bit) trên đĩa. Nhưng các byte đó thường được sắp xếp theo cách mà một vài byte đầu tiên đại diện cho thứ này, một vài byte tiếp theo đại diện cho thứ khác, v.v. "Định dạng tệp" tồn tại vì thế giới đã tiêu chuẩn hóa byte nào có ý nghĩa gì. Bây giờ, chúng ta có thể chỉ cần đọc một tệp từ đĩa vào RAM dưới dạng một mảng byte lớn. Và chúng ta có thể nhớ rằng byte tại `array[i]` đại diện cho một thứ, trong khi byte tại `array[j]` đại diện cho một thứ khác. Nhưng tại sao không đặt tên cho một số byte đó để chúng ta có thể truy xuất chúng từ bộ nhớ dễ dàng hơn? Đó chính xác là những gì các struct trong `bmp.h` cho phép chúng ta làm. Thay vì nghĩ về một tệp như một chuỗi dài các byte, thay vào đó chúng ta có thể coi nó như một chuỗi các `struct`.

### `filter.c`

Bây giờ, hãy mở `filter.c`. Tệp này đã được viết sẵn cho bạn, nhưng có một vài điểm quan trọng đáng chú ý ở đây.

Đầu tiên, hãy chú ý đến định nghĩa của `filters` ở dòng 10. Chuỗi đó cho chương trình biết các đối số dòng lệnh được phép của chương trình là gì: `b`, `e`, `g` và `r`. Mỗi đối số chỉ định một bộ lọc khác nhau mà chúng ta có thể áp dụng cho hình ảnh của mình: làm mờ (blur), phát hiện cạnh (edge detection), thang độ xám (grayscale) và phản chiếu (reflection).

Một vài dòng tiếp theo mở một tệp hình ảnh, đảm bảo đó thực sự là một tệp BMP và đọc tất cả thông tin pixel vào một mảng 2D có tên là `image`.

Cuộn xuống câu lệnh `switch` bắt đầu ở dòng 101. Lưu ý rằng, tùy thuộc vào `filter` (bộ lọc) mà chúng ta đã chọn, một hàm khác nhau sẽ được gọi: nếu người dùng chọn bộ lọc `b`, chương trình sẽ gọi hàm `blur`; nếu là `e`, hàm `edges` sẽ được gọi; nếu là `g`, hàm `grayscale` sẽ được gọi; và nếu là `r`, hàm `reflect` sẽ được gọi. Cũng lưu ý rằng mỗi hàm này đều nhận các đối số là chiều cao của ảnh, chiều rộng của ảnh và mảng pixel 2D.

Đây là những hàm mà bạn sẽ (sớm thôi!) triển khai. Như bạn có thể hình dung, mục tiêu là để mỗi hàm này chỉnh sửa mảng pixel 2D sao cho bộ lọc mong muốn được áp dụng cho hình ảnh.

Các dòng còn lại của chương trình lấy `image` kết quả và ghi chúng ra một tệp hình ảnh mới.

### `helpers.h`

Tiếp theo, hãy xem `helpers.h`. Tệp này khá ngắn và chỉ cung cấp các nguyên mẫu hàm (function prototypes) cho các hàm bạn đã thấy trước đó.

Ở đây, hãy lưu ý rằng mỗi hàm nhận một mảng 2D có tên `image` làm đối số, trong đó `image` là một mảng gồm `height` (chiều cao) hàng và mỗi hàng bản thân nó lại là một mảng gồm `width` (chiều rộng) các `RGBTRIPLE`. Vì vậy, nếu `image` đại diện cho toàn bộ bức tranh, thì `image[0]` đại diện cho hàng đầu tiên và `image[0][0]` đại diện cho pixel ở góc trên bên trái của bức ảnh.

### `helpers.c`

Bây giờ, hãy mở `helpers.c`. Đây là nơi chứa phần triển khai của các hàm đã khai báo trong `helpers.h`. Nhưng lưu ý rằng, hiện tại, các phần triển khai đang bị thiếu! Phần này là tùy thuộc vào bạn.

### `Makefile`

Cuối cùng, hãy xem `Makefile`. Tệp này chỉ định những gì sẽ xảy ra khi chúng ta chạy một lệnh terminal như `make filter`. Trong khi các chương trình bạn có thể đã viết trước đây chỉ gói gọn trong một tệp, `filter` có vẻ sử dụng nhiều tệp: `filter.c` và `helpers.c`. Vì vậy, chúng ta sẽ cần cho `make` biết cách biên dịch tệp này.

Hãy thử tự biên dịch `filter` bằng cách vào terminal và chạy

```bash
$ make filter
```

Sau đó, bạn có thể chạy chương trình bằng cách chạy:

```bash
$ ./filter -g images/yard.bmp out.bmp
```

lệnh này sẽ lấy hình ảnh tại `images/yard.bmp` và tạo ra một hình ảnh mới có tên `out.bmp` sau khi chạy các pixel qua hàm `grayscale`. Tuy nhiên, `grayscale` vẫn chưa thực hiện bất cứ điều gì, vì vậy hình ảnh đầu ra sẽ trông giống như hình ảnh sân cỏ ban đầu.

## Gợi ý

- Các giá trị của các thành phần `rgbtRed`, `rgbtGreen` và `rgbtBlue` của một pixel đều là số nguyên, vì vậy hãy đảm bảo làm tròn bất kỳ số dấu phẩy động nào thành số nguyên gần nhất khi gán chúng cho một giá trị pixel!

## Video hướng dẫn

**Lưu ý rằng có 5 video trong danh sách phát này. [Mở trên YouTube](https://www.youtube.com/playlist?list=PLhQjrBD2T382OwvMbZuaMGtD9wZkhnhYj)**

## Cách kiểm thử

Hãy đảm bảo kiểm thử tất cả các bộ lọc của bạn trên các tệp bitmap mẫu được cung cấp!

### Tính chính xác

```
check50 cs50/problems/2026/x/filter/more
```

### Phong cách trình bày (Style)

```
style50 helpers.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện lên.

```
submit50 cs50/problems/2026/x/filter/more
```
