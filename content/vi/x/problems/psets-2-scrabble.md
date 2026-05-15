title: "Scrabble - CS50x 2026"
pset: 2
draft: false
---

![Bàn cờ Scrabble](scrabble.png)

## Bài toán cần giải quyết

Trong trò chơi [Scrabble](https://en.wikipedia.org/wiki/Scrabble), người chơi tạo ra các từ để ghi điểm, và số điểm là tổng giá trị điểm của mỗi chữ cái trong từ đó.

| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q  | R | S | T | U | V | W | X | Y | Z  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|----|---|---|---|---|---|---|---|---|----|
| 1 | 3 | 3 | 2 | 1 | 4 | 2 | 4 | 1 | 8 | 5 | 1 | 3 | 1 | 1 | 3 | 10 | 1 | 1 | 1 | 1 | 4 | 4 | 8 | 4 | 10 |

Ví dụ, nếu chúng ta muốn tính điểm cho từ “CODE”, chúng ta sẽ lưu ý rằng chữ ‘C’ trị giá 3 điểm, chữ ‘O’ trị giá 1 điểm, chữ ‘D’ trị giá 2 điểm và chữ ‘E’ trị giá 1 điểm. Cộng các giá trị này lại, chúng ta có được “CODE” trị giá 7 điểm.

Trong một tệp có tên là `scrabble.c` trong một thư mục có tên là `scrabble`, hãy triển khai một chương trình bằng ngôn ngữ C để xác định người chiến thắng trong một trò chơi ngắn giống như Scrabble. Chương trình của bạn nên yêu cầu nhập dữ liệu hai lần: một lần để “Player 1” nhập từ của họ và một lần để “Player 2” nhập từ của họ. Sau đó, tùy thuộc vào người chơi nào ghi được nhiều điểm nhất, chương trình của bạn nên in ra “Player 1 wins!”, “Player 2 wins!”, hoặc “Tie!” (trong trường hợp hai người chơi ghi được số điểm bằng nhau).

## Bản demo

## Lời khuyên và Gợi ý

Viết một đoạn mã mà bạn biết chắc là sẽ biên dịch được

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{

}
```

Lưu ý rằng bây giờ bạn đã bao gồm một vài tệp tiêu đề (header files) để cung cấp cho bạn quyền truy cập vào các hàm có thể giúp bạn giải quyết bài toán này.

Viết mã giả trước khi viết thêm mã thật

Nếu không chắc chắn về cách giải quyết chính bài toán, hãy chia nhỏ nó thành các bài toán nhỏ hơn mà bạn có thể giải quyết trước. Ví dụ, bài toán này thực chất chỉ gồm một vài bài toán nhỏ:

1. Yêu cầu người dùng nhập hai từ
2. Tính điểm của mỗi từ
3. In ra người chiến thắng

Hãy viết một số mã giả dưới dạng chú thích để nhắc nhở bản thân thực hiện điều đó:

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt the user for two words

    // Compute the score of each word

    // Print the winner
}
```

Một số bài toán trong các bộ bài tập (problem sets), như bài này, có thể chứa các phần tiết lộ nội dung (spoilers) (giống như phần tiếp theo) hướng dẫn bạn thực hiện toàn bộ giải pháp. Mặc dù bạn được phép sử dụng mã này, chúng tôi thực sự khuyến khích bạn hãy tự mình thử sức trước! Các bài toán khác trong bộ bài tập sẽ không có kiểu hướng dẫn này, và thông thường bài toán có “toàn bộ spoiler” là một phiên bản khởi động cho bài toán lớn hơn mà bạn sẽ cần giải quyết sau đó.

Chuyển đổi mã giả thành mã thật

Đầu tiên, hãy xem xét cách bạn có thể yêu cầu người dùng nhập hai từ. Hãy nhớ lại rằng `get_string`, một hàm trong thư viện CS50, có thể yêu cầu người dùng nhập một chuỗi.

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word

    // Print the winner
}
```

Tiếp theo, hãy xem xét cách tính điểm của mỗi từ. Vì cùng một thuật toán tính điểm áp dụng cho cả hai từ, bạn có một cơ hội tốt cho việc *trừu tượng hóa* (abstraction). Ở đây chúng ta sẽ định nghĩa một hàm có tên là `compute_score` nhận vào một chuỗi, gọi là `word`, làm đầu vào, và sau đó trả về điểm của `word` dưới dạng một số nguyên `int`.

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner   
}

int compute_score(string word)
{
    // Compute and return score for word
}
```

Bây giờ hãy chuyển sang việc triển khai `compute_score`. Để tính điểm của một từ, bạn cần biết giá trị điểm của từng chữ cái trong từ đó. Bạn có thể liên kết các chữ cái và giá trị điểm của chúng bằng một *mảng* (array). Hãy tưởng tượng một mảng gồm 26 số nguyên `int`, gọi là `POINTS`, trong đó số đầu tiên là giá trị điểm của chữ ‘A’, số thứ hai là giá trị điểm của chữ ‘B’, và cứ tiếp tục như vậy. Bằng cách khai báo và khởi tạo một mảng như vậy bên ngoài bất kỳ hàm riêng lẻ nào, bạn có thể đảm bảo mảng này có thể được truy cập bởi bất kỳ hàm nào, bao gồm cả `compute_score`.

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner   
}

int compute_score(string word)
{
    // Compute and return score for word
}
```

Để triển khai `compute_score`, trước tiên hãy thử tìm giá trị điểm của một chữ cái duy nhất trong `word`.

- Hãy nhớ lại rằng để tìm ký tự ở chỉ số thứ n của một chuỗi, `s`, bạn có thể viết `s[n]`. Vì vậy, ví dụ `word[0]` sẽ cho bạn ký tự đầu tiên của `word`.
- Bây giờ, hãy nhớ lại rằng máy tính biểu diễn các ký tự bằng mã ASCII, một tiêu chuẩn biểu diễn mỗi ký tự dưới dạng một con số.
- Cũng hãy nhớ rằng chỉ số thứ 0 của `POINTS`, `POINTS[0]`, cho bạn giá trị điểm của chữ ‘A’. Hãy suy nghĩ về cách bạn có thể chuyển đổi biểu diễn số của chữ ‘A’ thành chỉ số của giá trị điểm của nó. Bây giờ, còn chữ ‘a’ thì sao? Bạn sẽ cần áp dụng các phép biến đổi khác nhau cho chữ hoa và chữ thường, vì vậy bạn có thể thấy các hàm [`isupper`](https://manual.cs50.io/3/isupper) và [`islower`](https://manual.cs50.io/3/islower) sẽ giúp ích cho bạn.
- Lưu ý rằng các ký tự *không phải* là chữ cái nên được tính 0 điểm. Ví dụ, `!` trị giá 0 điểm.

Nếu bạn có thể tính toán chính xác giá trị của *một* ký tự trong `word`, rất có thể bạn có thể sử dụng một vòng lặp để cộng tổng số điểm cho các ký tự còn lại. Khi bạn đã tự mình thử những điều trên, hãy xem xét gợi ý (khá lộ liễu!) dưới đây.

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
}

int compute_score(string word)
{
    // Keep track of score
    int score = 0;

    // Compute score for each character
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
    }

    return score;
}
```

Cuối cùng, hãy hoàn thành bước cuối cùng trong mã giả của bạn: in ra người chiến thắng. Hãy nhớ lại rằng một câu lệnh `if` có thể được sử dụng để kiểm tra xem một điều kiện có đúng hay không, và việc sử dụng thêm `else if` hoặc `else` có thể kiểm tra các điều kiện khác (loại trừ lẫn nhau).

```
if (/* Player 1 wins */)
{
    // ...
}
else if (/* Player 2 wins */)
{
    // ...
}
else
{
    // ...
}
```

Và một khi bạn đã thử những điều trên, hãy thoải mái liếc qua gợi ý (hay đúng hơn là giải pháp hoàn chỉnh!) dưới đây.

```c
#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Prompt the user for two words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Compute the score of each word
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Print the winner
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // Keep track of score
    int score = 0;

    // Compute score for each character
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 'A'];
        }
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 'a'];
        }
    }

    return score;
}
```

## Cách kiểm tra

Chương trình của bạn nên hoạt động theo các ví dụ bên dưới.

```bash
$ ./scrabble
Player 1: Question?
Player 2: Question!
Tie!
```

```bash
$ ./scrabble
Player 1: red
Player 2: wheelbarrow
Player 2 wins!
```

```bash
$ ./scrabble
Player 1: COMPUTER
Player 2: science
Player 1 wins!
```

```bash
$ ./scrabble
Player 1: Scrabble
Player 2: wiNNeR
Player 1 wins!
```

### Độ chính xác

```
check50 cs50/problems/2026/x/scrabble
```

### Phong cách

```
style50 scrabble.c
```

## Cách nộp bài

Trong terminal của bạn, hãy thực thi lệnh bên dưới để nộp bài làm của bạn, đồng thời trả lời các câu hỏi hiện ra.

```
submit50 cs50/problems/2026/x/scrabble
```
