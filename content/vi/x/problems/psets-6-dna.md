---
title: "DNA - CS50x 2026"
pset: 6
draft: false
---

## Bài toán cần giải quyết

DNA, vật mang thông tin di truyền trong các sinh vật sống, đã được sử dụng trong tư pháp hình sự trong nhiều thập kỷ. Nhưng chính xác thì việc lập hồ sơ DNA hoạt động như thế nào? Với một chuỗi DNA cho trước, làm thế nào các điều tra viên pháp y có thể xác định nó thuộc về ai?

Trong một tệp có tên là `dna.py` nằm trong thư mục mang tên `dna`, hãy triển khai một chương trình xác định xem một chuỗi DNA thuộc về ai.

## Bản demo

## Mã phân phối

Trong bài tập này, bạn sẽ mở rộng chức năng của mã nguồn được cung cấp bởi đội ngũ giảng huấn của CS50.

Tải về mã phân phối

Đăng nhập vào [cs50.dev](https://cs50.dev/), nhấp vào cửa sổ terminal và thực thi lệnh `cd` một mình. Bạn sẽ thấy dấu nhắc lệnh trong cửa sổ terminal của mình trông giống như bên dưới:

```
$
```

Tiếp theo thực thi

```python
wget https://cdn.cs50.net/2026/x/psets/6/dna.zip
```

để tải một tệp ZIP có tên là `dna.zip` vào codespace của bạn.

Sau đó thực thi

```
unzip dna.zip
```

để tạo một thư mục có tên là `dna`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi

```
rm dna.zip
```

và trả lời với “y” rồi nhấn Enter tại dấu nhắc lệnh để xóa tệp ZIP bạn đã tải xuống.

Bây giờ gõ

```bash
cd dna
```

rồi nhấn Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc lệnh của bạn bây giờ sẽ giống như bên dưới.

```
dna/ $
```

Thực thi lệnh `ls` một mình, bạn sẽ thấy một vài tệp và thư mục:

```
databases/ dna.py sequences/
```

Nếu bạn gặp bất kỳ khó khăn nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Bối cảnh

DNA thực chất chỉ là một chuỗi các phân tử được gọi là nucleotide, được sắp xếp thành một hình dạng cụ thể (xoắn kép). Mỗi tế bào của con người có hàng tỷ nucleotide được sắp xếp theo trình tự. Mỗi nucleotide của DNA chứa một trong bốn loại base khác nhau: adenine (A), cytosine (C), guanine (G), hoặc thymine (T). Một số phần của trình tự này (tức là bộ gen - genome) là giống nhau, hoặc ít nhất là rất giống nhau ở hầu hết tất cả mọi người, nhưng các phần khác của trình tự lại có sự đa dạng di truyền cao hơn và do đó thay đổi nhiều hơn trong cộng đồng dân cư.

Một nơi mà DNA thường có sự đa dạng di truyền cao là các đoạn Lặp lại Ngắn Nối tiếp (Short Tandem Repeats - STRs). STR là một chuỗi ngắn các base DNA có xu hướng lặp lại liên tiếp nhiều lần tại các vị trí cụ thể bên trong DNA của một người. Số lần lặp lại của bất kỳ STR cụ thể nào thay đổi rất nhiều giữa các cá nhân. Trong các mẫu DNA bên dưới, ví dụ, Alice có STR `AGAT` lặp lại bốn lần trong DNA của mình, trong khi Bob có cùng STR đó lặp lại năm lần.

![Các mẫu STR](strs.png)

Việc sử dụng nhiều STR, thay vì chỉ một, có thể cải thiện độ chính xác của việc lập hồ sơ DNA. Nếu xác suất để hai người có cùng số lần lặp lại cho một STR duy nhất là 5%, và nhà phân tích xem xét 10 STR khác nhau, thì xác suất để hai mẫu DNA khớp nhau hoàn toàn do ngẫu nhiên là khoảng 1 trên 1 triệu tỷ (giả sử tất cả các STR là độc lập với nhau). Vì vậy, nếu hai mẫu DNA khớp nhau về số lần lặp lại cho mỗi STR, nhà phân tích có thể khá tự tin rằng chúng đến từ cùng một người. CODIS, [cơ sở dữ liệu DNA](https://www.fbi.gov/services/laboratory/biometric-analysis/codis/codis-and-ndis-fact-sheet) của FBI, sử dụng 20 STR khác nhau như một phần của quy trình lập hồ sơ DNA.

Một cơ sở dữ liệu DNA như vậy trông sẽ thế nào? Ở dạng đơn giản nhất, bạn có thể hình dung việc định dạng cơ sở dữ liệu DNA dưới dạng tệp CSV, trong đó mỗi hàng tương ứng với một cá nhân và mỗi cột tương ứng với một STR cụ thể.

```
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```

Dữ liệu trong tệp trên cho thấy Alice có chuỗi `AGAT` lặp lại 28 lần liên tiếp ở đâu đó trong DNA của mình, chuỗi `AATG` lặp lại 42 lần và `TATC` lặp lại 14 lần. Trong khi đó, Bob có cùng ba STR đó lặp lại lần lượt là 17 lần, 22 lần và 19 lần. Và Charlie có ba STR đó lặp lại lần lượt là 36, 18 và 25 lần.

Vậy với một chuỗi DNA cho trước, làm thế nào bạn có thể xác định nó thuộc về ai? Hãy tưởng tượng rằng bạn đã tìm kiếm trong chuỗi DNA chuỗi lặp lại liên tiếp dài nhất của `AGAT` và thấy rằng chuỗi dài nhất đó là 17 lần lặp lại. Nếu sau đó bạn thấy rằng chuỗi dài nhất của `AATG` là 22 lần lặp lại, và chuỗi dài nhất của `TATC` là 19 lần lặp lại, điều đó sẽ cung cấp bằng chứng khá rõ ràng rằng DNA đó là của Bob. Tất nhiên, cũng có khả năng là sau khi bạn đếm số lần lặp cho mỗi STR, nó không khớp với bất kỳ ai trong cơ sở dữ liệu DNA của bạn, trong trường hợp đó bạn sẽ không tìm thấy kết quả khớp nào.

Trong thực tế, vì các nhà phân tích biết STR sẽ được tìm thấy trên nhiễm sắc thể nào và tại vị trí nào trong DNA, họ có thể khu trú việc tìm kiếm của mình chỉ trong một phần hẹp của DNA. Nhưng chúng ta sẽ bỏ qua chi tiết đó trong bài tập này.

Nhiệm vụ của bạn là viết một chương trình nhận vào một chuỗi DNA và một tệp CSV chứa số lượng STR cho một danh sách các cá nhân, sau đó xuất ra tên người mà DNA đó (có khả năng nhất) thuộc về.

## Yêu cầu kỹ thuật

- Chương trình phải yêu cầu đối số dòng lệnh đầu tiên là tên của tệp CSV chứa số lượng STR cho một danh sách các cá nhân, và yêu cầu đối số dòng lệnh thứ hai là tên của tệp văn bản chứa chuỗi DNA cần xác định.
  
  - Nếu chương trình của bạn được thực thi với số lượng đối số dòng lệnh không chính xác, chương trình sẽ in ra một thông báo lỗi tùy chọn (bằng lệnh `print`). Nếu số lượng đối số chính xác, bạn có thể giả định rằng đối số đầu tiên thực sự là tên tệp của một tệp CSV hợp lệ và đối số thứ hai là tên tệp của một tệp văn bản hợp lệ.
- Chương trình của bạn nên mở tệp CSV và đọc nội dung của nó vào bộ nhớ.
  
  - Bạn có thể giả định rằng hàng đầu tiên của tệp CSV sẽ là tên các cột. Cột đầu tiên sẽ là từ `name` và các cột còn lại sẽ là chính các chuỗi STR.
- Chương trình của bạn nên mở chuỗi DNA và đọc nội dung của nó vào bộ nhớ.
- Đối với mỗi STR (từ dòng đầu tiên của tệp CSV), chương trình của bạn nên tính toán chuỗi lặp lại liên tiếp dài nhất của STR đó trong chuỗi DNA cần xác định. Lưu ý rằng chúng tôi đã định nghĩa sẵn một hàm bổ trợ cho bạn, `longest_match`, hàm này sẽ thực hiện đúng việc đó!
- Nếu số lượng STR khớp chính xác với bất kỳ cá nhân nào trong tệp CSV, chương trình của bạn nên in ra tên của cá nhân khớp đó.
  
  - Bạn có thể giả định rằng số lượng STR sẽ không khớp với nhiều hơn một cá nhân.
  - Nếu số lượng STR không khớp chính xác với bất kỳ cá nhân nào trong tệp CSV, chương trình của bạn nên in ra `No match`.

## Gợi ý

- Bạn có thể thấy module [`csv`](https://docs.python.org/3/library/csv.html) của Python hữu ích để đọc các tệp CSV vào bộ nhớ. Đặc biệt hữu ích có thể là [`csv.DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader).
  
  - Ví dụ: nếu một tệp như `foo.csv` có một hàng tiêu đề, trong đó mỗi chuỗi là tên của một trường nào đó, đây là cách bạn có thể in các `fieldnames` đó dưới dạng một `list`:
    
    ```python
    import csv
    
    with open("foo.csv") as file:
        reader = csv.DictReader(file)
        print(reader.fieldnames)
    ```
  - Và đây là cách bạn đọc tất cả các hàng (khác) từ tệp CSV vào một `list`, trong đó mỗi phần tử là một `dict` đại diện cho hàng đó:
    
    ```python
    import csv
    
    rows = []
    with open("foo.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    ```
- Các hàm [`open`](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) và [`read`](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) cũng có thể hữu ích để đọc các tệp văn bản vào bộ nhớ.
- Hãy xem xét những cấu trúc dữ liệu nào có thể hữu ích để theo dõi thông tin trong chương trình của bạn. Một [`list`](https://docs.python.org/3/tutorial/introduction.html#lists) hoặc một [`dict`](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) có thể sẽ giúp ích.
- Hãy nhớ rằng chúng tôi đã định nghĩa một hàm (`longest_match`) mà khi nhận cả chuỗi DNA và một STR làm đầu vào, nó sẽ trả về số lần lặp lại tối đa của STR đó. Sau đó, bạn có thể sử dụng hàm đó trong các phần khác của chương trình!

## Hướng dẫn chi tiết

## Cách kiểm thử

Mặc dù `check50` có sẵn cho bài tập này, bạn được khuyến khích trước tiên hãy tự kiểm thử mã nguồn của mình cho mỗi trường hợp sau đây.

- Chạy chương trình của bạn với lệnh `python dna.py databases/small.csv sequences/1.txt`. Chương trình của bạn sẽ xuất ra `Bob`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/small.csv sequences/2.txt`. Chương trình của bạn sẽ xuất ra `No match`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/small.csv sequences/3.txt`. Chương trình của bạn sẽ xuất ra `No match`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/small.csv sequences/4.txt`. Chương trình của bạn sẽ xuất ra `Alice`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/5.txt`. Chương trình của bạn sẽ xuất ra `Lavender`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/6.txt`. Chương trình của bạn sẽ xuất ra `Luna`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/7.txt`. Chương trình của bạn sẽ xuất ra `Ron`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/8.txt`. Chương trình của bạn sẽ xuất ra `Ginny`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/9.txt`. Chương trình của bạn sẽ xuất ra `Draco`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/10.txt`. Chương trình của bạn sẽ xuất ra `Albus`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/11.txt`. Chương trình của bạn sẽ xuất ra `Hermione`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/12.txt`. Chương trình của bạn sẽ xuất ra `Lily`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/13.txt`. Chương trình của bạn sẽ xuất ra `No match`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/14.txt`. Chương trình của bạn sẽ xuất ra `Severus`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/15.txt`. Chương trình của bạn sẽ xuất ra `Sirius`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/16.txt`. Chương trình của bạn sẽ xuất ra `No match`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/17.txt`. Chương trình của bạn sẽ xuất ra `Harry`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/18.txt`. Chương trình của bạn sẽ xuất ra `No match`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/19.txt`. Chương trình của bạn sẽ xuất ra `Fred`.
- Chạy chương trình của bạn với lệnh `python dna.py databases/large.csv sequences/20.txt`. Chương trình của bạn sẽ xuất ra `No match`.

### Độ chính xác

```
check50 cs50/problems/2026/x/dna
```

### Phong cách lập trình

```
style50 dna.py
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh bên dưới để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/dna
```
