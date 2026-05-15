---
title: "Readability - CS50x 2026"
pset: 2
draft: false
---

![Charlotte's Web Cover](charlottes_web.jpg)

## Bài toán cần giải quyết

Theo [Scholastic](https://www.scholastic.com/teachers/teaching-tools/collections/guided-reading-book-lists-for-every-level.html), tác phẩm *Charlotte’s Web* của E.B. White có mức độ đọc được dành cho học sinh từ lớp 2 đến lớp 4, và cuốn *The Giver* của Lois Lowry dành cho học sinh từ lớp 8 đến lớp 12. Tuy nhiên, việc một cuốn sách ở một mức độ đọc nhất định thực sự có ý nghĩa gì?

Thông thường, một chuyên gia có thể đọc một cuốn sách và quyết định khối lớp (tức là năm học) mà họ cho là phù hợp nhất. Nhưng một thuật toán cũng có khả năng làm được điều đó!

Trong một tệp có tên là `readability.c` nằm trong thư mục `readability`, bạn sẽ triển khai một chương trình tính toán cấp độ lớp học xấp xỉ cần thiết để hiểu một đoạn văn bản. Chương trình của bạn nên in ra kết quả “Grade X” với “X” là cấp độ lớp học được tính toán, làm tròn đến số nguyên gần nhất. Nếu cấp độ lớp học từ 16 trở lên (tương đương hoặc cao hơn trình độ đọc của sinh viên năm cuối đại học), chương trình của bạn nên in ra “Grade 16+” thay vì đưa ra con số chính xác. Nếu cấp độ lớp học nhỏ hơn 1, chương trình nên in ra “Before Grade 1”.

## Bản demo

## Cơ sở lý thuyết

Vậy những đặc điểm nào đặc trưng cho các cấp độ đọc cao hơn? Những từ dài hơn có lẽ tương quan với cấp độ đọc cao hơn. Tương tự, những câu dài hơn cũng có thể tương quan với cấp độ đọc cao hơn.

Nhiều “bài kiểm tra độ đọc được” đã được phát triển qua nhiều năm nhằm xác định các công thức tính toán mức độ đọc của một văn bản. Một trong số đó là *chỉ số Coleman-Liau*. Chỉ số Coleman-Liau của một văn bản được thiết kế để đưa ra cấp độ lớp học (tại Hoa Kỳ) cần thiết để hiểu văn bản đó. Công thức là:

```
index = 0.0588 * L - 0.296 * S - 15.8
```

Trong đó `L` là số chữ cái trung bình trên mỗi 100 từ trong văn bản, và `S` là số câu trung bình trên mỗi 100 từ trong văn bản.

## Lời khuyên

Viết mã nguồn mà bạn biết chắc sẽ biên dịch được

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

}
```

Lưu ý rằng bạn hiện đã bao gồm một vài tệp tiêu đề (header files) cho phép bạn truy cập vào các hàm có thể giúp bạn giải quyết bài toán này.

Viết mã giả trước khi viết mã nguồn thực tế

Nếu bạn không chắc chắn về cách giải quyết bài toán, hãy chia nhỏ nó thành các vấn đề nhỏ hơn mà bạn có thể giải quyết trước. Ví dụ, bài toán này thực chất chỉ gồm một vài bước chính:

1. Yêu cầu người dùng nhập một đoạn văn bản
2. Đếm số chữ cái, số từ và số câu trong đoạn văn bản
3. Tính toán chỉ số Coleman-Liau
4. In ra cấp độ lớp học

Hãy viết một số mã giả dưới dạng chú thích để nhắc nhở bản thân thực hiện các bước đó:

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Yêu cầu người dùng nhập một đoạn văn bản

    // Đếm số chữ cái, số từ và số câu trong đoạn văn bản

    // Tính toán chỉ số Coleman-Liau

    // In ra cấp độ lớp học
}
```

Chuyển mã giả thành mã nguồn

Trước tiên, hãy cân nhắc cách bạn yêu cầu người dùng nhập văn bản. Hãy nhớ lại rằng `get_string`, một hàm trong thư viện CS50, có thể yêu cầu người dùng nhập một chuỗi.

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Yêu cầu người dùng nhập một đoạn văn bản
    string text = get_string("Text: ");

    // Đếm số chữ cái, số từ và số câu trong đoạn văn bản

    // Tính toán chỉ số Coleman-Liau

    // In ra cấp độ lớp học
}
```

Sau khi đã thu thập dữ liệu nhập từ người dùng, bạn có thể bắt đầu phân tích dữ liệu đó. Trước hết, hãy thử đếm số chữ cái trong văn bản. Chữ cái được tính là các ký tự bảng chữ cái viết hoa hoặc viết thường, không bao gồm dấu câu, chữ số hoặc các biểu tượng khác.

Một cách để tiếp cận vấn đề này là tạo một hàm tên là `count_letters` nhận đầu vào là một chuỗi `text`, và sau đó trả về số lượng chữ cái trong đoạn văn bản đó dưới dạng một số nguyên (`int`).

```
int count_letters(string text)
{
    // Trả về số lượng chữ cái trong text
}
```

Bạn sẽ cần tự viết mã của mình để đếm số chữ cái trong văn bản. Tuy nhiên, có thể ai đó có kinh nghiệm hơn đã viết sẵn một hàm để xác định xem một ký tự có phải là chữ cái hay không. Đây là cơ hội tốt để sử dụng [CS50 manual](https://manual.cs50.io/), một bộ giải thích các hàm phổ biến trong thư viện chuẩn C.

Bạn có thể tích hợp `count_letters` vào mã nguồn bạn đã viết như sau:

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);

int main(void)
{
    // Yêu cầu người dùng nhập một đoạn văn bản
    string text = get_string("Text: ");

    // Đếm số chữ cái, số từ và số câu trong đoạn văn bản
    int letters = count_letters(text);

    // Tính toán chỉ số Coleman-Liau

    // In ra cấp độ lớp học
}

int count_letters(string text)
{
    // Trả về số lượng chữ cái trong text
}
```

Tiếp theo, hãy viết một hàm để đếm số từ.

```
int count_words(string text)
{
    // Trả về số lượng từ trong text
}
```

Đối với bài toán này, chúng ta sẽ coi bất kỳ chuỗi ký tự nào được phân tách bằng dấu cách là một từ (vì vậy một từ có dấu gạch nối như “sister-in-law” nên được coi là một từ, không phải ba). Bạn có thể giả định rằng một câu:

- sẽ chứa ít nhất một từ;
- sẽ không bắt đầu hoặc kết thúc bằng dấu cách; và
- sẽ không có nhiều dấu cách liên tiếp.

Với những giả định đó, bạn có thể tìm thấy mối liên hệ giữa số lượng từ và số lượng dấu cách. Tất nhiên, bạn được khuyến khích thử một giải pháp có thể xử lý nhiều dấu cách giữa các từ hoặc thậm chí không có từ nào!

Bây giờ bạn có thể tích hợp `count_words` vào chương trình của mình như sau:

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);

int main(void)
{
    // Yêu cầu người dùng nhập một đoạn văn bản
    string text = get_string("Text: ");

    // Đếm số chữ cái, số từ và số câu trong đoạn văn bản
    int letters = count_letters(text);
    int words = count_words(text);

    // Tính toán chỉ số Coleman-Liau

    // In ra cấp độ lớp học
}

int count_letters(string text)
{
    // Trả về số lượng chữ cái trong text
}

int count_words(string text)
{
    // Trả về số lượng từ trong text
}
```

Cuối cùng, hãy viết một hàm để đếm số câu. Bạn có thể coi bất kỳ chuỗi ký tự nào kết thúc bằng dấu `.`, `!` hoặc `?` là một câu.

```
int count_sentences(string text)
{
    // Trả về số lượng câu trong text
}
```

Bạn có thể tích hợp `count_sentences` vào chương trình như sau:

```c
#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Yêu cầu người dùng nhập một đoạn văn bản
    string text = get_string("Text: ");

    // Đếm số chữ cái, số từ và số câu trong đoạn văn bản
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Tính toán chỉ số Coleman-Liau

    // In ra cấp độ lớp học
}

int count_letters(string text)
{
    // Trả về số lượng chữ cái trong text
}

int count_words(string text)
{
    // Trả về số lượng từ trong text
}

int count_sentences(string text)
{
    // Trả về số lượng câu trong text
}
```

Cuối cùng, hãy tính chỉ số Coleman-Liau và in ra cấp độ lớp học kết quả.

- Hãy nhớ rằng chỉ số Coleman-Liau được tính bằng công thức `index = 0.0588 * L - 0.296 * S - 15.8`
- `L` là số chữ cái trung bình trên 100 từ trong văn bản: tức là số chữ cái chia cho số từ, rồi tất cả nhân với 100.
- `S` là số câu trung bình trên 100 từ trong văn bản: tức là số câu chia cho số từ, rồi tất cả nhân với 100.
- Bạn sẽ muốn làm tròn kết quả đến số nguyên gần nhất, vì vậy hãy nhớ rằng hàm `round` được khai báo trong `math.h`, theo [manual.cs50.io](https://manual.cs50.io/).
- Hãy nhớ rằng, khi chia các giá trị kiểu `int` trong C, kết quả cũng sẽ là một số nguyên `int`, và mọi phần dư (tức là các chữ số sau dấu thập phân) sẽ bị loại bỏ. Nói cách khác, kết quả sẽ bị “cắt cụt”. Bạn có thể muốn ép kiểu một hoặc nhiều giá trị sang `float` trước khi thực hiện phép chia khi tính toán `L` và `S`!

Nếu chỉ số kết quả là 16 hoặc cao hơn (tương đương hoặc cao hơn trình độ đọc của sinh viên năm cuối đại học), chương trình của bạn nên in ra “Grade 16+” thay vì in ra một con số cụ thể. Nếu chỉ số nhỏ hơn 1, chương trình nên in ra “Before Grade 1”.

## Hướng dẫn chi tiết

## Cách kiểm thử

Hãy thử chạy chương trình của bạn với các đoạn văn bản sau để đảm bảo bạn thấy cấp độ lớp học tương ứng. Đảm bảo chỉ sao chép phần văn bản, không có khoảng trắng thừa.

- `One fish. Two fish. Red fish. Blue fish.` (Before Grade 1)
- `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` (Grade 2)
- `Congratulations! Today is your day. You're off to Great Places! You're off and away!` (Grade 3)
- `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` (Grade 5)
- `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` (Grade 7)
- `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` (Grade 8)
- `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` (Grade 8)
- `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` (Grade 9)
- `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` (Grade 10)
- `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` (Grade 16+)

### Độ chính xác

```
check50 cs50/problems/2026/x/readability
```

### Phong cách

```
style50 readability.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực hiện lệnh dưới đây để nộp bài, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/readability
```
