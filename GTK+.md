


Getting Started
---

GTK4 的架构
---
![](https://www.gtk.org/assets/img/docs/docs-gtk-architecture.svg)
1. GLib
   GLib is a low-level core library that forms the basis of GTK. It provides data structure handling for C, portability wrappers and interfaces for such run-time functionality as an event loop, threads, dynamic loading and an object system.
   GLib 是构成 GTK 基础的低级核心库。它为 C 语言提供数据结构处理、可移植性包装器和用于诸如事件循环、线程、动态加载和对象系统等运行时功能的接口。
2. Pango
   Pango is a library for layout and rendering of text with an emphasis on internationalization. It forms the core of text and font handling for GTK.
   Pango 是一个用于布局和呈现文本的库，重点是国际化。它构成了 GTK 文本和字体处理的核心。
3. Cairo
   Cairo is a library for 2D graphics with support for multiple output devices (including the X Window System, Win32) while producing a consistent output on all media while taking advantage of display hardware acceleration when available.
   Cairo 是一个 2D 图形库，支持多种输出设备（包括 X Window 系统、Win32），同时在所有媒体上产生一致的输出，同时利用可用的显示硬件加速。
4. GdkPixbuf
   GdkPixbuf is a library for loading graphical assets like icons in various formats, like PNG, JPEG, and GIF.
   GdkPixbuf 是一个用于加载图形资源的库，例如各种格式的图标，例如 PNG、JPEG 和 GIF。
5. ATK
   ATK is a library for a set of interfaces providing accessibility. By supporting the ATK interfaces, an application or toolkit can be used with tools such as screen readers, magnifiers, and alternative input devices.
   ATK 是一组提供可访问性的接口的库。通过支持 ATK 接口，应用程序或工具包可以与屏幕阅读器、放大镜和替代输入设备等工具一起使用。


参考文档
---
1. [GTK docs](https://www.gtk.org/docs/https://www.gtk.org/docs/apis/)
2. [API](https://www.gtk.org/docs/apis/)
3. [Gnome 与 GTK 相关的文档](https://developer.gnome.org/documentation/)
4. [rust 相关 API](https://www.gtk.org/docs/language-bindings/rust/)
5. [gtk rs](https://gtk-rs.org/)