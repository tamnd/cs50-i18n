title: "Readability - CS50x 2026"
pset: 6
draft: "false"
---

## Bài toán cần giải quyết

Hãy viết một chương trình trong tệp `readability.py` nằm trong thư mục `sentimental-readability`, yêu cầu người dùng nhập vào một đoạn văn bản, sau đó xuất ra cấp độ lớp học (grade level) của văn bản đó theo công thức Coleman-Liau, tương tự như những gì bạn đã làm trong [Problem Set 2](../../2/), ngoại trừ việc chương trình lần này phải được viết bằng Python.

## Demo

## Yêu cầu kỹ thuật

- Hãy nhớ rằng chỉ số Coleman-Liau được tính bằng công thức `0.0588 * L - 0.296 * S - 15.8`, trong đó `L` là số chữ cái trung bình trên 100 từ trong văn bản, và `S` là số câu trung bình trên 100 từ trong văn bản.
- Sử dụng hàm `get_string` từ thư viện CS50 để lấy dữ liệu nhập từ người dùng, và hàm `print` để xuất kết quả.
- Chương trình của bạn nên đếm số lượng chữ cái, từ và câu trong văn bản. Bạn có thể giả định rằng một chữ cái là bất kỳ ký tự thường nào từ `a` đến `z` hoặc ký tự hoa từ `A` đến `Z`, bất kỳ chuỗi ký tự nào được phân tách bằng khoảng trắng sẽ được tính là một từ, và bất kỳ sự xuất hiện nào của dấu chấm, dấu chấm than hoặc dấu hỏi chấm đều biểu thị sự kết thúc của một câu.
- Chương trình của bạn nên in ra kết quả `"Grade X"`, trong đó `X` là cấp độ lớp học được tính bởi công thức Coleman-Liau, được làm tròn đến số nguyên gần nhất.
- Nếu chỉ số kết quả là 16 hoặc cao hơn (tương đương hoặc lớn hơn trình độ đọc của sinh viên năm cuối đại học), chương trình của bạn nên xuất ra `"Grade 16+"` thay vì đưa ra số chỉ số chính xác. Nếu chỉ số nhỏ hơn 1, chương trình của bạn nên xuất ra `"Before Grade 1"`.

## Cách kiểm thử

Mặc dù `check50` có sẵn cho bài toán này, bạn nên tự kiểm tra mã nguồn của mình trước với mỗi trường hợp sau đây.

- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `One fish. Two fish. Red fish. Blue fish.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Before Grade 1`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `Would you like them here or there? I would not like them here or there. I would not like them anywhere.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 2`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `Congratulations! Today is your day. You're off to Great Places! You're off and away!` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 3`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 5`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 7`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?"` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 8`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 8`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 9`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 10`.
- Chạy chương trình bằng lệnh `python readability.py` và đợi lời nhắc nhập dữ liệu. Nhập `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains.` và nhấn enter. Chương trình của bạn sẽ xuất ra `Grade 16+`.

### Tính đúng đắn

```
check50 cs50/problems/2026/x/sentimental/readability
```

### Phong cách lập trình

```
style50 readability.py
```

## Cách nộp bài

Trong terminal, hãy thực hiện lệnh dưới đây để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện lên.

```
submit50 cs50/problems/2026/x/sentimental/readability
```
