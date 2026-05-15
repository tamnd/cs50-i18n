title: "Bắt đầu với Scratch - CS50x 2026"
pset: 0
draft: false
---

Đã đến lúc chọn cuộc phiêu lưu của riêng bạn! Bài tập của bạn, nói một cách đơn giản, là triển khai trong Scratch, tại [scratch.mit.edu](https://scratch.mit.edu), bất kỳ dự án nào bạn chọn, có thể là một câu chuyện tương tác, trò chơi, hoạt ảnh hoặc bất kỳ điều gì khác, chỉ cần tuân theo các yêu cầu sau:

- Dự án của bạn phải sử dụng ít nhất hai sprite, trong đó ít nhất một sprite không được là con mèo.
- Dự án của bạn phải có tổng cộng ít nhất ba script (nghĩa là không nhất thiết phải có ba script cho mỗi sprite).
- Dự án của bạn phải sử dụng ít nhất một câu lệnh điều kiện (conditional), ít nhất một vòng lặp (loop) và ít nhất một biến (variable).
- Dự án của bạn phải sử dụng ít nhất một khối tùy chỉnh (custom block) mà bạn tự tạo (thông qua **Make a Block**), khối này phải nhận ít nhất một đầu vào (input).
- Dự án của bạn nên phức tạp hơn hầu hết các ví dụ đã được trình bày trong bài giảng (nhiều ví dụ trong số đó tuy mang tính hướng dẫn nhưng khá ngắn), nhưng nó có thể ít phức tạp hơn [Oscartime](https://scratch.mit.edu/projects/277537196) và [Ivy’s Hardest Game](https://scratch.mit.edu/projects/326129433).

Để đáp ứng các yêu cầu này, dự án của bạn có lẽ nên sử dụng tổng cộng khoảng vài chục mảnh ghép. Và lý tưởng nhất là mã nguồn của bạn không chỉ chính xác mà còn phải được thiết kế tốt. Nếu một trong các script của bạn bắt đầu trở nên hơi dài, hãy thử chia nhỏ nó thành nhiều script (mỗi script thực hiện một nhiệm vụ cụ thể). Và hãy cố gắng tận dụng sự "trừu tượng hóa" (abstraction) nếu có thể: nếu bạn có thể đặt một cái tên mô tả cho một chuỗi các khối lệnh (ví dụ: **meow**), thì những khối đó có lẽ nên được chuyển vào một khối tùy chỉnh!

Nếu bạn muốn tìm nguồn cảm hứng từ các sinh viên khóa trước, dưới đây là một số ví dụ:

- [It’s Raining Men](https://scratch.mit.edu/projects/37412/), từ bài giảng
- [Soccer](https://scratch.mit.edu/projects/37413/), một trò chơi
- [Cookie Love Story](https://scratch.mit.edu/projects/26329196/), một hoạt ảnh
- [Gingerbread tales](https://scratch.mit.edu/projects/277536784/), một câu chuyện tương tác
- [Intersection](https://scratch.mit.edu/projects/75390754/), một trò chơi
- [Hogwarts](https://scratch.mit.edu/projects/422258685), một trò chơi

Bạn có thể thấy các [hướng dẫn](https://scratch.mit.edu/projects/editor/?tutorial=all) hoặc [dự án khởi đầu](https://scratch.mit.edu/starter-projects) này hữu ích. Và bạn cũng có thể khám phá [scratch.mit.edu](https://scratch.mit.edu/explore/projects/all) để tìm cảm hứng. Nhưng hãy thử tự mình nghĩ ra một ý tưởng và sau đó bắt tay vào thực hiện nó. Tuy nhiên, đừng cố gắng thực hiện toàn bộ dự án của bạn cùng một lúc: hãy giải quyết từng phần một, giống như chúng ta đã làm trong bài giảng. Nói cách khác, hãy thực hiện những bước nhỏ (baby steps): viết một chút mã (tức là kéo và thả một vài mảnh ghép), kiểm tra, viết thêm một chút nữa, kiểm tra, v.v. Và hãy chọn **File &gt; Save now** vài phút một lần để không bị mất kết quả công việc!

Nếu trong quá trình thực hiện, bạn cảm thấy quá khó khăn để triển khai một tính năng nào đó, đừng quá lo lắng; hãy thay đổi thiết kế hoặc tìm cách khác để giải quyết vấn đề. Nếu bạn bắt đầu thực hiện một ý tưởng mà bạn thấy thú vị, rất có thể bạn sẽ không thấy quá khó khăn để đáp ứng các yêu cầu trên.

Nếu bạn quyết định nhập bất kỳ hình nền (backdrop), trang phục (costume) hoặc âm thanh nào vào dự án của mình, hãy nhớ trích dẫn nguồn gốc của chúng bằng một [chú thích](https://en.scratch-wiki.info/wiki/Comment_%28programming_feature%29)!

Được rồi, bắt đầu thôi. Hãy làm chúng tôi tự hào!

Đối với bài tập này, việc nộp một dự án Scratch mà bạn đã từng nộp cho một khóa học CS50 khác là **hợp lệ**, miễn là nó đáp ứng các yêu cầu trên.

Sau khi hoàn thành dự án, hãy chọn **File &gt; Save now** một lần cuối. Sau đó, chọn **File &gt; Save to your computer** và giữ file đó để nộp bài. Nếu máy tính hỏi bạn muốn **Mở** hay **Lưu** file, hãy chắc chắn chọn **Lưu**.

## Cách nộp bài

Hãy chắc chắn hoàn thành **các bước dưới đây, theo đúng thứ tự đó**!

### Bước 1 trên 2

Nộp [biểu mẫu này](https://forms.cs50.io/2c8a006a-ad63-4894-a380-f999b219436c).

Vào một thời điểm nào đó (có thể thay đổi từ vài tuần đến vài tháng, vì các biểu mẫu này được xử lý thủ công theo đợt) sau khi bạn nộp biểu mẫu này, bạn có thể nhận được lời mời tham gia GitHub Education, vì bạn đã cung cấp tên người dùng GitHub của mình như một phần của quá trình nộp bài này. Đây là điều bình thường! Tìm hiểu thêm tại [github.com/education/students](https://github.com/education/students).

### Bước 2 trên 2

Bước này giả định rằng bạn đã tải xuống dự án Scratch của mình dưới dạng một file có đuôi là `.sb3`. Và bước này cũng giả định rằng bạn đã đăng ký tài khoản GitHub theo biểu mẫu ở trên.

1. Truy cập [liên kết này](https://submit.cs50.io/invites/9770b67479384c4d8c37790779e466d9), đăng nhập bằng tài khoản GitHub của bạn và nhấp vào **Authorize cs50**.
2. Đánh dấu vào ô xác nhận rằng bạn muốn cấp cho nhân viên khóa học quyền truy cập vào các bài nộp của mình và nhấp vào **Join course**.
3. Truy cập [submit.cs50.io/upload/cs50/problems/2026/x/scratch](https://submit.cs50.io/upload/cs50/problems/2026/x/scratch).
4. Nhấp vào “Choose File” và chọn file `.sb3` của bạn. Nhấp vào **Submit**.

Nếu bạn gặp lỗi “No files in this directory are expected by cs50/problems/2026/x/scratch”, hãy đảm bảo tên file dự án Scratch của bạn thực sự kết thúc bằng `.sb3`!

Vậy là xong! Sau khi bài nộp của bạn được tải lên, bạn sẽ được chuyển hướng đến trang bài nộp của mình. Nhấp vào liên kết bài nộp và sau đó là liên kết **check50** để xem dự án của bạn đã đáp ứng được những yêu cầu nào. Bạn có thể nộp lại bao nhiêu lần tùy thích (trước thời hạn)! Lưu ý rằng nếu bạn tải lên một file có kích thước lớn hơn 10MB (khá lớn đối với một dự án Scratch), `check50` có thể gặp khó khăn khi xử lý. Tốt nhất hãy đảm bảo file của bạn nhỏ hơn giới hạn đó.

Để xem tiến trình hiện tại của bạn trong khóa học, hãy truy cập bảng điểm của khóa học tại [cs50.me/cs50x](https://cs50.me/cs50x)!
