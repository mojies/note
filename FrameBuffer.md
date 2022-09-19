https://learnopengl.com/Advanced-OpenGL/Framebuffers
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

```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <fcntl.h>
#include <linux/fb.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
```

2. 打开您的 `/dev/fbxx` 节点，我的是 `/dev/fb01`

```
int fbfd = 0;
if( (fbfd = open("/dev/fb0", O_RDWR)) < 0 ){
   // error handle
}
```

3. 获取 FB fixed 的一些属性

```
struct fb_fix_screeninfo finfo;
if (ioctl(fbfd, FBIOGET_FSCREENINFO, &finfo) == -1) {
   // error handle
}
```

4. 获取修改一些可变的一些属性
```
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
```
char *fbp = 0;
if( (fbp = (char *)mmap(0, screensize, PROT_READ | PROT_WRITE, MAP_SHARED, fbfd, 0)) < 0 ){
   // error handle
}
```

6. 修改图形缓存
```
// 1. 你可以直接给 fbp 对应的区域进行复制，比如全白
for( int i = (vinfo.xoffset * vinfo.bits_per_pixel/8 + vinfo.yoffset*finfo.line_length);
      i < xxx; i++ )
   fbp[0] = 255;
// 2. 或者调用 opencv API 直接操作该内存
```

7. 最后不要忘了收拾现场
```
munmap(fbp, screensize);
close(fbfd);
```

## struct fb_fix_screeninfo



## struct fb_var_screeninfo


## 下面是一些和 FourCC ( four-character code ) 相关的资料

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

## 下面是一些和 TwoCC (  ) 相关的资料

1. The TwoCC is the audio counterpart to the video FourCC. It is the audio format identifier used in the RIFF based multimedia formats by Microsoft (WAV and AVI). The TwoCC is 2 bytes long and stored in little endian format on disk. You can register your TwoCC with Microsoft but it seems that only some companies perform this process. [TCC](https://wiki.multimedia.cx/index.php/TwoCC)


## Frame Buffer API 有哪些



2. 
arkfb - fbdev driver for ARK Logic chips
What is aty128fb?
Framebuffer driver for Cirrus Logic chipsets
Understanding fbdev’s cmap
Deferred IO
What is efifb?
Driver for EP93xx LCD controller
Video Attribute Flags
Platform callbacks
Setting the video mode
Screenpage bug
The Framebuffer Console
The Frame Buffer Device
What is gxfb?
Intel 810/815 Framebuffer driver
Intel 830M/845G/852GM/855GM/865G/915G/945G Framebuffer driver
Frame Buffer device internals
What is lxfb?
What is matroxfb?
Metronomefb
modedb default video mode support
What is pvr2fb?
Driver for PXA25x LCD controller
s3fb - fbdev driver for S3 Trio/Virge chips
What is sa1100fb?
SH7760/SH7763 integrated LCDC Framebuffer driver
What is sisfb?
sm501fb
What is sm712fb?
sstfb
What is tgafb?
Tridentfb
What is udlfb?
uvesafb - A Generic Driver for VBE2+ compliant video cards
What is vesafb?
VIA Integration Graphic Chip Console Framebuffer Driver
vt8623fb - fbdev driver for graphics core in VIA VT8623 chipset



REF
---
1. [kernel framebuffer](https://docs.kernel.org/fb/index.html)
2. [learnopengl](https://learnopengl.com/Advanced-OpenGL/Framebuffers)
3. [一个简单的例子](https://kevinboone.me/linuxfbc.html?i=1)（亲测， raspberrypi 上无效）
4. [另一个简单的例子](https://gist.github.com/FredEckert/3425429) (亲测， raspberrypi 上有效)
