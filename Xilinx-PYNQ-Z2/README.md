<!--
 * @Author: Frank Chu
 * @Date: 2022-12-07 15:03:30
 * @LastEditors: Frank Chu
 * @LastEditTime: 2022-12-07 21:43:56
 * @FilePath: /EE/Xilinx-PYNQ-Z2/README.md
 * @Description: 
 * 
 * Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
-->

# PYNQ-Z2

PYNQ-Z2 是一款 FPGA 开发板，具有双核 ARM Cortex-A9 处理器和 Xilinx ZYNQ-7000 FPGA 芯片。PYNQ-Z2 是一款高性能的 FPGA 开发板，可用于各种应用场景，包括视觉处理、信号处理、通信和网络等。

PYNQ-Z2 的设计基于 PYNQ 框架，支持使用 Python 语言进行 FPGA 设计和编程。PYNQ 框架可以简化 FPGA 设计流程，使用户可以轻松地利用 FPGA 的高性能，实现复杂的计算任务。PYNQ-Z2 还提供了丰富的资源和支持，包括各种硬件资源、软件库和教程，可以帮助用户使用 PYNQ-Z2 开发 FPGA 应用。PYNQ-Z2 还支持使用 Jupyter Notebook 进行 FPGA 开发，可以在交互式环境中进行设计和测试。

PYNQ-Z2 的主要优势在于提供了一个简单易用的开发环境，可以让用户更快地完成 FPGA 应用的开发。PYNQ-Z2 拥有高性能的 FPGA 芯片和双核处理器，可以满足各种复杂的计算需求。同时，PYNQ-Z2 还提供了丰富的资源和支持，可以帮助用户快速上手并完成 FPGA 应用的开发。

## 语音信号处理流程

```mermaid
graph LR

sampling["采集（PS 调用 BaseOverlay）"]
data["数据转换(PS)"]
fpga["FPGA 滤波(PL)"]
playback["储存回放(PS)"]

语音信号 --麦克风--> sampling --WAV文件--> data --n 维数组--> fpga --> playback --板子接耳机输出--> Output
```

## Software

* Vivado 2019.1
* Vivado HLS
* Jupyter NoteBook (PS: Processing System)
* Vivado / Vivado HLS (PL: Programmable Logic)

## PYNQ-Z2 的主要特性

* 双核 ARM Cortex-A9 处理器
* Xilinx ZYNQ-7000 FPGA 芯片

# 作业

1. 什么是语谱图
2. 事实滤波的原理，为后续设计做好准备。

# PYNQ 进行语音滤波的方式

由于代码的具体内容取决于语音滤波的具体实现方式，因此我无法给出 ZYNQ 语音滤波的代码。但是，基本的思路是需要编写软件代码来实现语音数据的采样、处理和输出，并将这些代码运行在 ZYNQ 芯片的处理器上。

如果要使用 PYNQ 框架来实现语音滤波功能，则需要编写 Python 程序来控制硬件加速器的运行。可以通过调用 PYNQ 库中的相关函数和方法，来实现语音滤波的功能。例如，可以调用 PYNQ 库中的 filter() 函数，来实现对语音数据的滤波处理。具体的代码示例如下：

```py
from pynq import Overlay
from pynq.lib.audio import Audio

# Load the audio overlay
overlay = Overlay("audio.bit")

# Initialize the audio codec
audio = Audio()

# Start the audio codec
audio.start()

# Read audio data from the microphone
data = audio.read()

# Apply the filter to the audio data
filtered_data = filter(data)

# Play the filtered audio data through the speaker
audio.write(filtered_data)
```

上面的代码演示了如何使用 PYNQ 库中的函数和方法，来实现语音滤波的功能。但是，实际应用中可能还需要对代码进行更多的调整和优化，以满足应用的具体需求。例如，可以通过更改滤波器的参数来改变滤波效果，或者通过多次调用 `filter()` 函数来实现多阶滤波。此外，也可以通过添加更多的 Python 代码来实现语音滤波的控制和管理，以及其他附加功能。

# 常见问题

## FPGA 编程语言

### HDL - Verilog and VHDL

hardware description languages (HDLs), such as Verilog and VHDL. 

These languages are specifically designed for describing the structure and behavior of digital circuits, and are commonly used to program FPGAs.

### C with High-level Synthesis

Another commonly used language for FPGA programming is C, which can be used in conjunction with a high-level synthesis (HLS) tool to automatically generate RTL (register-transfer level) code from a C or C++ program. This allows users to program an FPGA using a familiar, high-level language, while still taking advantage of the performance benefits of FPGA hardware acceleration.

### Xilinx Vivado Design Suite / Altera Quartus Prime

Some FPGA vendors also provide their own programming languages and tools for programming their FPGA devices. For example, Xilinx provides the Vivado Design Suite, which includes a set of tools and languages for programming Xilinx FPGAs. Similarly, Altera (now part of Intel) provides the Quartus Prime software for programming Altera FPGAs.

## ARM FPGA 之间的联系

ARM 和 FPGA 是两种不同的技术，但它们可以结合在一起使用，为系统设计带来许多优势。
ARM 是一种微处理器架构，它通常用于嵌入式系统和移动设备中。ARM 处理器提供了一组固定的指令集，可以运行操作系统和应用程序。ARM 处理器的优势在于低功耗和高性能，适用于需要长电池寿命或低功耗预算的应用场合。

FPGA 是一种可编程逻辑门阵列，它可以通过编程来实现电路逻辑功能。FPGA 包含大量的可编程逻辑元件，可以用来实现各种不同的电路功能。FPGA 的优势在于高度可编程和高速度，可以实现自定义的硬件加速，提高系统性能。

ARM 和 FPGA 可以结合在一起使用，在同一个系统中共同完成功能。例如，可以在 FPGA 上设计电路逻辑，实现硬件加速器，然后通过 ARM 处理器来控制和使用这些加速器。这样可以充分利用 ARM 处理器的低功耗和高性能，以及 FPGA 的高度可编程和高速度，实现更快、更高效的系统性能。

在市面上有许多带有 ARM 处理器和 FPGA 逻辑元件的综合型芯片，可以同时提供这两种技术的优势。例如，Xilinx ZYNQ 芯片就是一种带有 ARM 处理器和 FPGA 逻辑元件的综合芯片，可以用于实现 ARM 和 FPGA 的结合应用。

总的来说，ARM 和 FPGA 在系统设计中可以结合使用，以实现更快、更高效的系统性能。此外，使用带有 ARM 和 FPGA 的综合芯片，可以更方便地实现这种结合应用。

## 如何进行 FPGA 加速

要进行 FPGA 加速，需要按照以下步骤进行：

1. 确定要加速的应用，并分析它的工作原理和性能瓶颈。
2. 使用一种 FPGA 开发工具，如 Vivado Design Suite，设计电路逻辑，实现硬件加速器。
3. 编写软件代码，在 FPGA 上运行硬件加速器。
4. 在 FPGA 开发板上烧写系统设计和软件代码，并对加速器进行测试。
5. 根据实际应用需求，调整系统设计和软件代码，以实现更好的加速效果。

以上是 FPGA 加速的基本流程。具体的实现方式可能会因应用的不同而有所差异，但基本的思路是一致的。在实际应用中，可以根据自己的需要进行适当的调整和优化，以提高系统性能。
另外，使用 FPGA 加速还可以通过一些其他方法来提高效率。例如，可以使用多个 FPGA 单元，分别实现不同的加速功能，然后将它们结合在一起，实现更大规模的加速。此外，还可以使用更高性能的 FPGA 开发板，或者使用更复杂的系统设计方法，来提高 FPGA 加速的效率。
总的来说，使用 FPGA 加速可以大大提高系统性能，但是需要按照步骤进行设计和实现，并通过不断调整和优化，来实现最佳的加速效果。

## FPGA 综合，HLS 区别

FPGA 综合是指将 FPGA 设计文件编译成可烧写到 FPGA 芯片上的硬件逻辑文件的过程。HLS（高级语言综合）是一种 FPGA 综合方法，它可以将高级语言（如 C++）编写的设计文件转换成 FPGA 芯片可识别的硬件逻辑文件。

两者的主要区别在于设计文件的语言类型。FPGA 综合可以支持各种 FPGA 设计语言，包括按照硬件描述语言（HDL）标准编写的语言，如 VHDL 和 Verilog。HLS 只支持高级语言，如 C++。

此外，两者在设计流程方面也存在一些差异。FPGA 综合需要按照确定的流程进行，通常需要经过预处理、综合、链接和位置配置等多个步骤。HLS 可以简化这一流程，通过高级语言的特性，使得设计者可以更快地完成 FPGA 设计。

总的来说，FPGA 综合和 HLS 是 FPGA 设计的两种重要方法，它们在语言类型和设计流程方面存在一些区别。但在实际应用中，两者都可以为 FPGA 设计提供支持，帮助用户实现自己的设计目标。在选择 FPGA 综合方法时，可以根据自己的需要和能力，选择适合自己的方法。
此外，在 FPGA 综合过程中，还可以使用一些工具和技术来提高综合效率和质量。例如，可以使用综合优化器来自动调整参数，提高综合速度和质量。还可以使用综合验证器来检查综合结果的正确性，以确保综合的设计能够正常工作。通过这些工具和技术的使用，可以大大提高 FPGA 综合的效率和质量。
