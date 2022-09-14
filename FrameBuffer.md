https://learnopengl.com/Advanced-OpenGL/Framebuffers
# Frame Buffer

## FourCC ( four-character code )

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

## TwoCC (  )

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
3. 