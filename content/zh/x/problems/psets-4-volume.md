---
title: "音量 (Volume) - CS50x 2026"
pset: 4
draft: false
---

![WAV 文件波形图](wav_file.png)

## 待解决的问题

[WAV 文件](https://docs.fileformat.com/audio/wav/) 是一种常见的音频表示格式。WAV 文件将音频存储为一系列“采样”（samples）：即代表特定时间点音频信号值的数字。WAV 文件以 44 字节的“文件头”（header）开头，其中包含有关文件本身的信息，包括文件大小、每秒采样数以及每个采样的大小。在文件头之后，WAV 文件包含一系列采样，每个采样是一个 2 字节（16 位）的整数，代表特定时间点的音频信号。

按给定因子缩放每个采样值具有改变音频音量的效果。例如，将每个采样值乘以 2.0 将使原始音频的音量翻倍。同时，将每个采样乘以 0.5 将使音量减半。

在名为 `volume` 的文件夹中一个名为 `volume.c` 的文件中，编写一个程序来修改音频文件的音量。

## 演示

## 发行代码

对于这个问题，你将扩展 CS50 工作人员提供给你的代码的功能。

下载发行代码

登录 [cs50.dev](https://cs50.dev/)，点击终端窗口，然后执行 `cd` 命令。你应该会发现终端窗口的提示符如下所示：

```
$
```

接下来执行

```python
wget https://cdn.cs50.net/2026/x/psets/4/volume.zip
```

以便将名为 `volume.zip` 的 ZIP 文件下载到你的 codespace 中。

然后执行

```
unzip volume.zip
```

来创建一个名为 `volume` 的文件夹。你不再需要该 ZIP 文件，因此可以执行

```
rm volume.zip
```

并在提示符处输入 “y” 后按回车键，以删除你下载的 ZIP 文件。

现在输入

```bash
cd volume
```

然后按回车键进入（即打开）该目录。你的提示符现在应该如下所示。

```
volume/ $
```

如果一切顺利，你应该执行

```bash
ls
```

并看到一个名为 `volume.c` 的文件。执行 `code volume.c` 应该会打开该文件，你将在其中输入此问题集的代码。如果没有，请重新检查你的步骤，看看是否能确定哪里出了问题！

## 实现细节

完成 `volume.c` 的实现，使其按给定的因子改变音频文件的音量。

- 该程序应接受三个命令行参数。第一个是 `input`，代表原始音频文件的名称。第二个是 `output`，代表应生成的正新音频文件的名称。第三个是 `factor`，是原始音频文件音量缩放的倍数。
  
  - 例如，如果 `factor` 是 `2.0`，那么你的程序应该将 `input` 中音频文件的音量翻倍，并将新生成的音频文件保存在 `output` 中。
- 你的程序应首先从输入文件中读取文件头，并将文件头写入输出文件。
- 你的程序随后应从 WAV 文件中读取剩余的数据，每次读取一个 16 位（2 字节）的采样。你的程序应将每个采样乘以 `factor`，并将新采样写入输出文件。
  
  - 你可以假设 WAV 文件将使用 16 位有符号值作为采样。实际上，WAV 文件可以具有不同位数的采样，但在此问题中我们假设采样为 16 位。
- 如果你的程序使用了 `malloc`，则不得泄露任何内存。

## 提示

理解 `volume.c` 中的代码

首先注意 `volume.c` 已经设置为接受三个命令行参数：`input`、`output` 和 `factor`。

- `main` 函数接受一个 `int` 类型的 `argc` 和一个 `char *` 数组（字符串！） `argv`。
- 如果命令行参数的数量（包括程序本身）`argc` 不等于 4，程序将打印其正确用法并以状态代码 1 退出。

```c
int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // ...
}
```

接下来，`volume.c` 使用 [`fopen`](https://manual.cs50.io/3/fopen) 打开作为命令行参数提供的两个文件。

- 最佳实践是检查调用 `fopen` 的结果是否为 `NULL`。如果是，则表示未找到该文件或无法打开该文件。

```c
// Open files and determine scaling factor
FILE *input = fopen(argv[1], "r");
if (input == NULL)
{
    printf("Could not open file.\n");
    return 1;
}

FILE *output = fopen(argv[2], "w");
if (output == NULL)
{
    printf("Could not open file.\n");
    return 1;
}
```

稍后，这些文件将通过 `fclose` 关闭。每当你调用 `fopen` 时，稍后都应该调用 `fclose`！

```
// Close files
fclose(input);
fclose(output);
```

不过，在关闭文件之前，请注意我们有几个 TODO。

```python
// TODO: Copy header from input file to output file

// TODO: Read samples from input file and write updated data to output file
```

你很可能需要知道缩放音量的因子，这就是为什么 `volume.c` 已经为你将第三个命令行参数转换为 `float` 的原因！

```
float factor = atof(argv[3]);
```

从输入文件复制 WAV 文件头到输出文件

你的第一个 TODO 是从 `input` 复制 WAV 文件头并将其写入 `output`。不过，首先你需要了解一些特殊的数据类型。

到目前为止，我们已经在 C 中看到了许多不同的类型，包括 `int`、`bool`、`char`、`double`、`float` 和 `long`。然而，在名为 `stdint.h` 的头文件中声明了许多 *其他* 类型，这些类型允许我们非常精确地定义整数的大小（以位为单位）和符号（有符号或无符号）。在处理 WAV 文件时，有两种类型对我们特别有用：

- `uint8_t` 是一种存储 8 位（因此是 `8`！）无符号（即非负）整数（因此是 `uint`！）的类型。我们可以将 WAV 文件头的每个字节视为 `uint8_t` 值。
- `int16_t` 是一种存储 16 位有符号（即正数或负数）整数的类型。我们可以将 WAV 文件中的每个音频采样视为 `int16_t` 值。

你可能想要创建一个字节数组来存储从输入文件中读取的 WAV 文件头数据。使用 `uint8_t` 类型来表示一个字节，你可以使用如下语法为你的文件头创建一个包含 `n` 个字节的数组：

```
uint8_t header[n];
```

将 `n` 替换为字节数。然后，你可以将 `header` 作为参数传递给 [`fread`](https://manual.cs50.io/3/fread) 或 [`fwrite`](https://manual.cs50.io/3/fwrite)，以便读取到文件头或从文件头写入。

回想一下，WAV 文件的文件头始终恰好是 44 字节长。请注意，`volume.c` 已经为你定义了一个名为 `HEADER_SIZE` 的变量，它等于文件头中的字节数。

下面是一个相当大的提示，但这就是你完成此 TODO 的方法！

```sql
// Copy header from input file to output file
uint8_t header[HEADER_SIZE];
fread(header, HEADER_SIZE, 1, input);
fwrite(header, HEADER_SIZE, 1, output);
```

将更新后的数据写入输出文件

你的下一个 TODO 是从 `input` 读取采样，更新这些采样，并将更新后的采样写入 `output`。读取文件时，通常会创建一个“缓冲区”（buffer）来临时存储数据。在那里，你可以修改数据，一旦准备就绪，就可以将缓冲区的数据写入新文件。

回想一下，我们可以使用 `int16_t` 类型来表示 WAV 文件的采样。那么，要存储一个音频采样，你可以使用如下语法创建一个缓冲区变量：

```sql
// Create a buffer for a single sample
int16_t buffer;
```

有了采样缓冲区后，你现在可以一次读取一个采样的数据。尝试使用 `fread` 来完成此任务！你可以使用 `&buffer`（`buffer` 的地址）作为 `fread` 或 `fwrite` 的参数，以便读取到缓冲区或从缓冲区写入。（回想一下，`&` 运算符用于获取变量的地址。）

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample into buffer
fread(&buffer, sizeof(int16_t), 1, input);
```

现在，要增加（或减少）采样的音量，你只需将其乘以某个因子即可。

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample into buffer
fread(&buffer, sizeof(int16_t), 1, input);

// Update volume of sample
buffer *= factor;
```

最后，你可以将该更新后的采样写入 `output`：

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample from input into buffer
fread(&buffer, sizeof(int16_t), 1, input);

// Update volume of sample
buffer *= factor;

// Write updated sample to new file
fwrite(&buffer, sizeof(int16_t), 1, output);
```

只是有一个问题：你需要 *继续* 将采样读取到缓冲区、更新其音量并将更新后的采样写入输出文件，直到没有剩余采样可读。

- 幸运的是，根据其文档，`fread` 将返回成功读取的数据项数量。你可能会发现，在检查是否已到达文件末尾时，这很有用！
- 请记住，没有理由不能在 `while` 循环的条件语句中调用 `fread`。例如，你可以像下面这样调用 `fread`：
  
  ```
  while (fread(...))
  {
  
  }
  ```

这是一个很大的提示，但请参阅下文以了解解决此问题的有效方法：

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample from input into buffer while there are samples left to read
while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
{
    // Update volume of sample
    buffer *= factor;

    // Write updated sample to new file
    fwrite(&buffer, sizeof(int16_t), 1, output);
}
```

因为你使用的 C 版本将非零值视为 `true`，将零值视为 `false`，所以你可以将上述语法简化如下：

```sql
// Create a buffer for a single sample
int16_t buffer;

// Read single sample from input into buffer while there are samples left to read
while (fread(&buffer, sizeof(int16_t), 1, input))
{
    // Update volume of sample
    buffer *= factor;

    // Write updated sample to new file
    fwrite(&buffer, sizeof(int16_t), 1, output);
}
```

## 视频演示

不确定如何解决？

## 如何测试

你的程序的行为应如下例所示。

```bash
$ ./volume input.wav output.wav 2.0
```

当你听 `output.wav` 时（例如通过在文件浏览器中按住 Control 键并点击 `output.wav`，选择 **Download**，然后在电脑上的音频播放器中打开该文件），它的音量应该是 `input.wav` 的两倍！

```bash
$ ./volume input.wav output.wav 0.5
```

当你听 `output.wav` 时，它的音量应该是 `input.wav` 的一半！

### 正确性

```
check50 cs50/problems/2026/x/volume
```

### 风格

```
style50 volume.c
```

## 如何提交

在你的终端中执行以下命令以提交你的作品，并根据提示回答问题。

```
submit50 cs50/problems/2026/x/volume
```
