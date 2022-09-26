# Linux Frame Buffer

## 如何直接操作 FrameBuffer

一般情况下，我们不会直接操作 FrameBuffer, 这是非常基础的操作，通常情况下我们会借助桌面开发环境或者图形开发环境的库和工具来开发图形应用。

但有一种情况是我们在开发嵌入式应用，有时候我们需要展示一些简单的图形界面。而运行一个完整的复杂的桌面环境很可能是非常困难的。

下面我们将简单的介绍一下如何去直接操作 FrameBuffer 的方法。

#### 开始写代码之前你需要知道的一些事情

1. 一般 FrameBuffer 是格式如 `/dev/fbxx` 的设备节点。
2. 你需要确保你拥有操作 `/dev/fbxx` 设备节点的权限
3. 先不要运行 X Window System 或者其他的一些桌面环境，因为他们会和你竞争资源，甚至导致你获取不到权限，
4. 清楚你平台的图像格式，比如色彩深度，现在很多高级一点的平台都是 32bit 的（四个字节分别是蓝绿红[没用到]），
   但也有一些可能是 16bit / 24bit 之内的。参考 wikipedia Color depth 词条。
   因此你需要清楚的知道 FBIOGET_FSCREENINFO 和 FBIOGET_VSCREENINFO 获取到的所有信息的具体含义。
   甚至有些时候，你需要深入驱动程序确认 FrameBuffer 的实现。
5. 直接修改 FB 的映射的内存可以直接修改图形显示效果

#### 一个简单的例子

1. 首先准备一些必要的头文件

```C
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
```

2. 打开您的 `/dev/fbxx` 节点，我的是 `/dev/fb01`

```C
int fbfd = 0;
if( (fbfd = open("/dev/fb0", O_RDWR)) < 0 ){
   // error handle
}
```

3. 获取 FB fixed 的一些属性

```C
struct fb_fix_screeninfo finfo;
if (ioctl(fbfd, FBIOGET_FSCREENINFO, &finfo) == -1) {
   // error handle
}
```

4. 获取修改一些可变的一些属性
```C
struct fb_var_screeninfo vinfo;
if (ioctl(fbfd, FBIOGET_VSCREENINFO, &vinfo) == -1) {
   // error handle
}
// 修改 vinfo
if (ioctl(fbfd, FBIOPUT_VSCREENINFO, &vinfo) == -1) {
   // error handle
}

```

5. 对 FB 做内存映射
```C
char *fbp = 0;
if( (fbp = (char *)mmap(0, screensize, PROT_READ | PROT_WRITE, MAP_SHARED, fbfd, 0)) < 0 ){
   // error handle
}
```

6. 修改图形缓存
```C
// 1. 你可以直接给 fbp 对应的区域进行复制，比如全白
for( int i = (vinfo.xoffset * vinfo.bits_per_pixel/8 + vinfo.yoffset*finfo.line_length);
      i < xxx; i++ )
   fbp[0] = 255;
// 2. 或者调用 opencv API 直接操作该内存
```

7. 最后不要忘了收拾现场
```C
munmap(fbp, screensize);
close(fbfd);
```

## Linux Kernel 中的简介

因为以前 Linux 并没有对 FB 做出严格的规范，因此在不同的 Linux 硬件上，FB 表现可能都有些不一样，此时，你可能需要根据具体问题具体分析。

你首先需要知道 FB 中每一个数据代表什么意思，如果你运行过 `ffmpeg --pxi-fmts`， 你就会知道，图像的格式有非常多的种类，因此你必须龙清楚当前 FB 中的颜色布局方式到底是怎么样的。

大概率情况下我们可以通过 fb_fix_screeninfo 中的 type 得知当前 FB 中的颜色布局方式，但其他的一些颜色可能需要一些额外的信息来说明，比如 fb_var_screeninfo 中的 bits_per_pixel， grayscale， red， green， blue 等字段。

因此我们先会介绍一下定义这些类型的最重要的两个结构体，然后介绍一下 FB 支持哪些显示类型。

与 fb 相关的定义在 `include/uapi/linux/fb.h` 目录内。

## 概念


### 下面是一些和 FourCC ( four-character code ) 相关的资料

1. FourCC 是一个四个字节的字符序列用来标识唯一的数据格式。它起源于经典 Mac OS 中使用的 OSType 或 ResType 元数据系统，并被 Amiga/Electronic Arts 交换文件格式及其衍生文件采用。
   这个想法后来被重新用于识别 QuickTime 和 DirectShow 中的压缩数据类型。

2. 完整的 FourCC list 可以从以下几个网站获取
   1. http://abcavi.kibi.ru/fourcc.php
   2. https://web.archive.org/web/20100922105522/http://www.microsoft.com/whdc/archive/fourcc.mspx
   3. https://web.archive.org/web/20100919132805/http://www.fourcc.org/yuv.php
   4. https://wiki.multimedia.cx/index.php?title=FourCC
   5. https://wiki.videolan.org/FourCC/
   6. http://www.faqs.org/rfcs/rfc2361.html
   7. https://mpeg.chiariglione.org/

### 下面是一些和 TwoCC (  ) 相关的资料

1. The TwoCC is the audio counterpart to the video FourCC. It is the audio format identifier used in the RIFF based multimedia formats by Microsoft (WAV and AVI). The TwoCC is 2 bytes long and stored in little endian format on disk. You can register your TwoCC with Microsoft but it seems that only some companies perform this process. [TCC](https://wiki.multimedia.cx/index.php/TwoCC)


https://www.kernel.org/doc/Documentation/fb/vesafb.txt
### ypan

enable display panning using the VESA protected mode 
interface.  The visible screen is just a window of the
video memory, console scrolling is done by changing the
start of the window.

pro:	* scrolling (fullscreen) is fast, because there is
      no need to copy around data.
   * You'll get scrollback (the Shift-PgUp thing),
      the video memory can be used as scrollback buffer
kontra: * scrolling only parts of the screen causes some
      ugly flicker effects (boot logo flickers for
      example).

### ywrap

Same as ypan, but assumes your gfx board can wrap-around 
the video memory (i.e. starts reading from top if it
reaches the end of video memory).  Faster than ypan.

## struct fb_fix_screeninfo

```C
struct fb_fix_screeninfo {
      char id[16];                    /* identification string eg "TT Builtin" */
      unsigned long smem_start;       /* FB 的其实地址（物理地址） */

      __u32 smem_len;                 /* FB 地址的大小 */

      __u32 type;                     /* 参考以上章节中 FB_TYPE_* 相关内容 */

      __u32 type_aux;                 /* 参考 FB_TYPE_PLANES 和 FB_TYPE_INTERLEAVED_PLANES 章节相关内容 */

      __u32 visual;                   /* 参考以上章节中 FB_VISUAL_* 相关内容 */

      __u16 xpanstep;                 /* 如果没有硬件平移，则为零 */
      __u16 ypanstep;                 /* 如果没有硬件平移，则为零 */
      __u16 ywrapstep;                /* 如果没有硬件 ywrap，则为零 */
      __u32 line_length;              /* 行的长度（以字节为单位）    */
      unsigned long mmio_start;       /* 内存映射 I/O 的开始（物理地址）*/
      __u32 mmio_len;                 /* 内存映射地址空间大小 */
      __u32 accel;                    /* 向驱动程序指示我们拥有的特定芯片/卡  */

      __u16 capabilities;             /* 参考 FB_CAP_* 相关说明 */
      __u16 reserved[2];              /* 保留字 */
};
```

## struct fb_var_screeninfo
```C
struct fb_var_screeninfo {
      __u32 xres;                     /* visible resolution           */
      __u32 yres;
      __u32 xres_virtual;             /* virtual resolution           */
      __u32 yres_virtual;
      __u32 xoffset;                  /* offset from virtual to visible */
      __u32 yoffset;                  /* resolution                   */

      __u32 bits_per_pixel;           /* guess what                   */
      __u32 grayscale;                /* 0 = color, 1 = grayscale,    */
                                      /* >1 = FOURCC                  */
      struct fb_bitfield red;         /* bitfield in fb mem if true color, */
      struct fb_bitfield green;       /* else only length is significant */
      struct fb_bitfield blue;
      struct fb_bitfield transp;      /* transparency                 */

      __u32 nonstd;                   /* != 0 Non standard pixel format */

      __u32 activate;                 /* see FB_ACTIVATE_*            */

      __u32 height;                   /* height of picture in mm    */
      __u32 width;                    /* width of picture in mm     */

      __u32 accel_flags;              /* (OBSOLETE) see fb_info.flags */

      /* Timing: All values in pixclocks, except pixclock (of course) */
      __u32 pixclock;                 /* pixel clock in ps (pico seconds) */
      __u32 left_margin;              /* time from sync to picture    */
      __u32 right_margin;             /* time from picture to sync    */
      __u32 upper_margin;             /* time from sync to picture    */
      __u32 lower_margin;
      __u32 hsync_len;                /* length of horizontal sync    */
      __u32 vsync_len;                /* length of vertical sync      */
      __u32 sync;                     /* see FB_SYNC_*                */
      __u32 vmode;                    /* see FB_VMODE_*               */
      __u32 rotate;                   /* angle we rotate counter clockwise */
      __u32 colorspace;               /* colorspace for FOURCC-based modes */
      __u32 reserved[4];              /* Reserved for future compatibility */
};
```

FB 设备提了两种途径来配置 FB 的格式：传统 API 和 FOURCC-based 的 API。

Legacy API 长期以来一直是唯一的帧缓冲区格式配置 API，因此被应用程序广泛使用。当使用 RGB 和灰度格式以及传统的非标准格式时，它是应用程序推荐的 API。

To select a format, applications set the fb_var_screeninfo bits_per_pixel field to the desired frame buffer depth. Values up to 8 will usually map to monochrome, grayscale or pseudocolor visuals, although this is not required.

## fb_fix_screeninfo type 有哪些类型？

首先我们先介绍一下 Linux 内核中定义的集中 FB 类型：

### FB_TYPE_PACKED_PIXELS

一般一个 Macropixels 存储在一个单独的 plane 中，如果 Macropixels 的位数不是 8 的整数倍，那么溢出的位有可能使用额外的 8 个位来表达，也有可能和其他像素一起打包，这取决于 visual 的类型。

行尾的填充有可能存在，也有可能不存在，这取决于 fb_fix_screeninfo 中的 line_length 字段。

### FB_TYPE_PLANES

Macropixels 的每一个 bit 分布在多个 plane 上，plane 的个数等于表示一个 macropixel 的像素深度，第 n 个 plane 存储这所有 macropixel 的第 n 位。

Plane 之间在内存中是连续的。

### FB_TYPE_INTERLEAVED_PLANES

Macropixels 的每一个 bit 分布在多个 plane 上，plane 的个数等于表示一个 macropixel 的像素深度，第 n 个 plane 存储这所有 macropixel 的第 n 位。

Plane 在内存中是交错（interleaved）分布的（内核文档也没有画图，不懂什么意思）。
interleave factor 定义了两个相邻的 blocks 开始地址的距离，该信息存储在 `fb_fix_screeninfo type_aux` 字段。


### FB_TYPE_FOURCC

Macropixels 以 FOURCC 格式存储在内存中，当 `fb_var_screeninfo grayscale` 字段的值大于 1 时则代之 FOURCC 类型。

## fb_fix_screeninfo visual 有哪些类型？
### FB_VISUAL_MONO01

像素是黑色或白色的，并存储在 `fb_var_screeninfo bpp` 字段指定的多个位（通常为一个）上。

如果像素是黑色的，那么所有的位都应该设置为 1；如果像素是白色的，那么所有的位都应该设置为 0。
当表示像素的位小于 8 位（一个字节）的时候，那么数个像素将会打包到一个字节（byte）中。

目前 `FB_VISUAL_MONO01` 仅和 `FB_TYPE_PACKED_PIXELS` 搭配使用。

### FB_VISUAL_MONO10

像素是黑色或白色的，并存储在 `fb_var_screeninfo bpp` 字段指定的多个位（通常为一个）上。

如果像素是黑色的，那么所有的位都应该设置为 0；如果像素是白色的，那么所有的位都应该设置为 1。
当表示像素的位小于 8 位（一个字节）的时候，那么数个像素将会打包到一个字节（byte）中。

目前 `FB_VISUAL_MONO01` 仅和 `FB_TYPE_PACKED_PIXELS` 搭配使用。

### FB_VISUAL_TRUECOLOR

一个像素分成红绿蓝三种颜色，没一个分量通过查寻一个只读的表，可以获取相关值。
表是和设备强相关的，而且其中数据的关系可能有线性关系，也可能有非线性关系。

每一个分量如何被存储由 `fb_var_screeninfo` 中 `red`, `green`, `blue`， `transp` 几个字段表示。

### FB_VISUAL_PSEUDOCOLOR and FB_VISUAL_STATIC_PSEUDOCOLOR

像素的红/绿/蓝的分量被编码成 color map 的索引。`FB_VISUAL_STATIC_PSEUDOCOLOR` 指代的 colormap 为只读的，
`FB_VISUAL_PSEUDOCOLOR` 指代的 colormap 为可读写的。

`fb_var_screeninfo bits_per_pixel` 字段标识了每一个像素的值由多少位（bit）表示。

### FB_VISUAL_DIRECTCOLOR

像素被拆分成红绿蓝几个部分，没一个部分的分量可通过可编程查找表获取相应的值。

每一个分量如何被存储由 `fb_var_screeninfo` 中 `red`, `green`, `blue`， `transp` 几个字段表示。

### FB_VISUAL_FOURCC

像素按照 `fb_var_screeninfo grayscale` 字段中的 FOURCC 格式进行编码和解释。

## fb_fix_screeninfo capabilities 有哪些类型？

目前只支持一种类型，即 `FB_CAP_FOURCC`， 

The driver supports the four character code (FOURCC) based format setting API. When supported, formats are configured using a FOURCC instead of manually specifying color components layout.



REF
---
1. [kernel framebuffer](https://docs.kernel.org/fb/index.html)
2. [learnopengl](https://learnopengl.com/Advanced-OpenGL/Framebuffers)
3. [一个简单的例子](https://kevinboone.me/linuxfbc.html?i=1)（亲测， raspberrypi 上无效）
4. [另一个简单的例子](https://gist.github.com/FredEckert/3425429) (亲测， raspberrypi 上有效)
