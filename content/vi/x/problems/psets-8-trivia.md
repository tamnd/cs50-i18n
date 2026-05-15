title: "Trivia - CS50x 2026"
pset: 8
draft: false
---

Hãy viết một trang web cho phép người dùng trả lời các câu hỏi đố vui (trivia).

![screenshot of trivia questions](questions.png)

## Bắt đầu

Mở [cs50.dev](https://cs50.dev).

Bắt đầu bằng cách nhấp chuột vào bên trong cửa sổ terminal, sau đó thực thi lệnh `cd` đơn lẻ. Bạn sẽ thấy dấu nhắc (prompt) của nó tương tự như dưới đây.

```
$
```

Nhấp vào bên trong cửa sổ terminal đó và thực thi lệnh:

```python
wget https://cdn.cs50.net/2025/fall/psets/8/trivia.zip
```

theo sau là phím Enter để tải về một tệp ZIP có tên là `trivia.zip` vào codespace của bạn. Hãy cẩn thận đừng bỏ sót dấu cách giữa `wget` và URL theo sau, hoặc bất kỳ ký tự nào khác!

Bây giờ hãy thực thi:

```
unzip trivia.zip
```

để tạo một thư mục có tên là `trivia`. Bạn không còn cần tệp ZIP nữa, vì vậy bạn có thể thực thi:

```
rm trivia.zip
```

và trả lời “y” rồi nhấn Enter tại dấu nhắc để xóa tệp ZIP bạn đã tải xuống.

Bây giờ hãy gõ:

```bash
cd trivia
```

theo sau là phím Enter để di chuyển vào (tức là mở) thư mục đó. Dấu nhắc của bạn bây giờ sẽ tương tự như dưới đây.

```
trivia/ $
```

Nếu mọi việc thành công, bạn nên thực thi lệnh:

```bash
ls
```

và bạn sẽ thấy một tệp `index.html` và một tệp `styles.css`.

Nếu bạn gặp bất kỳ rắc rối nào, hãy thực hiện lại các bước tương tự và xem liệu bạn có thể xác định mình đã sai ở đâu không!

## Chi tiết triển khai

Thiết kế một trang web sử dụng HTML, CSS, và JavaScript để cho phép người dùng trả lời các câu hỏi đố vui.

- Trong `index.html`, hãy thêm vào dưới phần “Part 1” một câu hỏi đố vui trắc nghiệm (multiple-choice) do bạn tự chọn bằng HTML.
  
  - Bạn nên sử dụng thẻ tiêu đề `h3` cho nội dung câu hỏi.
  - Bạn nên có một thẻ `button` cho mỗi lựa chọn trả lời có thể. Phải có ít nhất ba lựa chọn trả lời, trong đó chính xác một lựa chọn là đúng.
- Sử dụng JavaScript, hãy thêm logic để các nút thay đổi màu sắc khi người dùng nhấp vào chúng.
  
  - Nếu người dùng nhấp vào nút có câu trả lời sai, nút đó sẽ chuyển sang màu đỏ và văn bản sẽ xuất hiện bên dưới câu hỏi với nội dung “Incorrect”.
  - Nếu người dùng nhấp vào nút có câu trả lời đúng, nút đó sẽ chuyển sang màu xanh lá cây và văn bản sẽ xuất hiện bên dưới câu hỏi với nội dung “Correct!”.
- Trong `index.html`, hãy thêm vào dưới phần “Part 2” một câu hỏi trả lời tự do (free response) dựa trên văn bản do bạn tự chọn bằng HTML.
  
  - Bạn nên sử dụng thẻ tiêu đề `h3` cho nội dung câu hỏi.
  - Bạn nên sử dụng một trường `input` để cho phép người dùng nhập câu trả lời.
  - Bạn nên sử dụng một thẻ `button` để cho phép người dùng xác nhận câu trả lời của họ.
- Sử dụng JavaScript, hãy thêm logic để trường văn bản thay đổi màu sắc khi người dùng xác nhận câu trả lời.
  
  - Nếu người dùng nhập câu trả lời sai và nhấn nút xác nhận, trường văn bản sẽ chuyển sang màu đỏ và văn bản sẽ xuất hiện bên dưới câu hỏi với nội dung “Incorrect”.
  - Nếu người dùng nhập câu trả lời đúng và nhấn nút xác nhận, trường nhập liệu sẽ chuyển sang màu xanh lá cây và văn bản sẽ xuất hiện bên dưới câu hỏi với nội dung “Correct!”.

Tùy chọn, bạn cũng có thể:

- Chỉnh sửa `styles.css` để thay đổi CSS của trang web!
- Thêm các câu hỏi đố vui bổ sung vào bài trắc nghiệm nếu bạn muốn!

### Video hướng dẫn

Video này được ghi lại khi khóa học vẫn còn sử dụng CS50 IDE để viết mã. Mặc dù giao diện có thể trông khác so với codespace của bạn, nhưng hành vi của hai môi trường về cơ bản là tương tự nhau!

### Gợi ý

- Sử dụng [`document.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector) để truy vấn một phần tử HTML đơn lẻ.
- Sử dụng [`document.querySelectorAll`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll) để truy vấn nhiều phần tử HTML khớp với một truy vấn. Hàm này trả về một mảng gồm tất cả các phần tử khớp.

Bạn không chắc chắn cách giải quyết?

### Kiểm tra

Không có `check50` cho bài này, vì các bản triển khai sẽ khác nhau tùy thuộc vào câu hỏi của bạn! Nhưng hãy nhớ kiểm tra cả phản hồi đúng và sai cho mỗi câu hỏi để đảm bảo rằng trang web của bạn phản hồi thích hợp.

Chạy `http-server` trong terminal khi đang ở trong thư mục `trivia` để khởi động máy chủ web phục vụ trang web của bạn.

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh dưới đây để nộp bài làm, đồng thời trả lời các dấu nhắc hiện ra.

```
submit50 cs50/problems/2026/x/trivia
```

Bạn muốn xem lời giải mẫu? Bạn có thể tìm thấy hai cách giải quyết vấn đề tại đây!

Tạo event listeners với JavaScript

```c
<!DOCTYPE html>

<html lang="en">
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link href="styles.css" rel="stylesheet">
        <title>Trivia!</title>
        <script>

            // Wait for DOM content to load
            document.addEventListener('DOMContentLoaded', function() {

                // Get all elements with class "correct"
                let corrects = document.querySelectorAll('.correct');

                // Add event listeners to each correct button
                for (let i = 0; i < corrects.length; i++) {
                    corrects[i].addEventListener('click', function() {

                        // Set background color to green
                        corrects[i].style.backgroundColor = 'Green';

                        // Go to parent element of correct button and find the first element with class "feedback" which has that parent
                        corrects[i].parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                    });
                }

                // When any incorrect answer is clicked, change color to red.
                let incorrects = document.querySelectorAll(".incorrect");
                for (let i = 0; i < incorrects.length; i++) {
                    incorrects[i].addEventListener('click', function() {

                        // Set background color to green
                        incorrects[i].style.backgroundColor = 'Red';

                        // Go to parent element of correct button and find the first element with class "feedback" which has that parent
                        incorrects[i].parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                    });
                }

                // Check free response submission
                document.querySelector('#check').addEventListener('click', function() {
                    let input = document.querySelector('input');
                    if (input.value === 'Switzerland') {
                        input.style.backgroundColor = 'green';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                    }
                    else {
                        input.style.backgroundColor = 'red';
                        input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                    }
                });
            });
        </script>
    </head>
    <body>
        <div class="header">
            <h1>Trivia!</h1>
        </div>

        <div class="container">
            <div class="section">
                <h2>Part 1: Multiple Choice </h2>
                <hr>
                <h3>What is the approximate ratio of people to sheep in New Zealand?</h3>
                <button class="incorrect">6 people per 1 sheep</button>
                <button class="incorrect">3 people per 1 sheep</button>
                <button class="incorrect">1 person per 1 sheep</button>
                <button class="incorrect">1 person per 3 sheep</button>
                <button class="correct">1 person per 6 sheep</button>
                <p class="feedback"></p>
            </div>

            <div class="section">
                <h2>Part 2: Free Response</h2>
                <hr>
                <h3>In which country is it illegal to own only one guinea pig, as a lone guinea pig might get lonely?</h3>
                <input type="text"></input>
                <button id="check">Check Answer</button>
                <p class="feedback"></p>
            </div>
        </div>
    </body>
</html>
```

Tạo event listeners với HTML

```js
<!DOCTYPE html>

<html lang="en">
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500&display=swap" rel="stylesheet">
        <link href="styles.css" rel="stylesheet">
        <title>Trivia!</title>
        <script>
            function checkMultiChoice(event) {

                // Get the element which triggered the event
                let button = event.target;

                // Check if the element's inner HTML matches expected answer
                if (button.innerHTML == '1 person per 6 sheep') {
                    button.style.backgroundColor = 'Green';
                    button.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                }
                else {
                    button.style.backgroundColor = 'Red';
                    button.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                }
            }

            function checkFreeResponse(event) {

                // Get the element which triggered the event
                let button = event.target;

                // Get the input element corresponding to the button
                let input = button.parentElement.querySelector('input');

                // Check for correct answer
                if (input.value === 'Switzerland') {
                    input.style.backgroundColor = 'Green';
                    input.parentElement.querySelector('.feedback').innerHTML = 'Correct!';
                }
                else {
                    input.style.backgroundColor = 'Red';
                    input.parentElement.querySelector('.feedback').innerHTML = 'Incorrect';
                }
            }
        </script>
    </head>
    <body>
        <div class="header">
            <h1>Trivia!</h1>
        </div>

        <div class="container">
            <div class="section">
                <h2>Part 1: Multiple Choice </h2>
                <hr>
                <h3>What is the approximate ratio of people to sheep in New Zealand?</h3>
                <button onclick="checkMultiChoice(event)">6 people per 1 sheep</button>
                <button onclick="checkMultiChoice(event)">3 people per 1 sheep</button>
                <button onclick="checkMultiChoice(event)">1 person per 1 sheep</button>
                <button onclick="checkMultiChoice(event)">1 person per 3 sheep</button>
                <button onclick="checkMultiChoice(event)">1 person per 6 sheep</button>
                <p class="feedback"></p>
            </div>

            <div class="section">
                <h2>Part 2: Free Response</h2>
                <hr>
                <h3>In which country is it illegal to own only one guinea pig, as a lone guinea pig might get lonely?</h3>
                <input type="text"></input>
                <button onclick="checkFreeResponse(event)">Check Answer</button>
                <p class="feedback"></p>
            </div>
        </div>
    </body>
</html>
```
