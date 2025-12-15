# interesting-window

A Windows color auto popup written in Python (perhaps you can use it to confession?((
使用Python编写的一个windows彩色自动弹窗（也许你可以用来表白?((

## Language

- [English](#english)
- [中文](#中文)



---


### English


A Windows color auto popup written in Python (perhaps you can use it to confession?((
Recently, I saw online that after running Python code, there will be many pop ups with random color backgrounds. The content of the pop ups is to motivate myself or for other reasons. I also want to take a look at it, but I haven't found any related quick use code
So I wrote a code that allows me to customize window names, window text fonts, background colors, random text, and more

The following are customizable items
  Name | Description | Required
 ---- | ----- | ------  
 sfico | Uses base64 decoding | No
 sfname  | All names of the created windows | **Yes**
 sffonts | All text fonts for creating windows | **Yes**
sffontssize  | Size of all text created in the window | **Yes**
sftime  | Wait for how many seconds before starting to create the window | **Yes**
color_list  | List of background colors for creating windows | No (if not provided, a built-in list will be used for automatic randomization)
text_list | Create random text for the window | **Yes**



---


### 中文


使用Python编写的一个windows彩色自动弹窗（也许你可以用来表白?((
最近我在网上看到有关Python 运行代码以后会有很多弹窗 弹窗背景是随机颜色 弹窗的内容是激励自己或者其他话 我也想整一个看看 但是没有发现有关的快速使用代码
于是我写了一个可以自定义自定义窗口名称、自定义窗口文字字体、自定义背景颜色、自定义随机文字等等的代码


以下是可以自定义的东西
  名称 | 介绍  | 是否必填
 ---- | ----- | ------  
 sfico  | 使用的是base64解码 | 否
 sfname  | 创建窗口的所有名称 | **是**
 sffonts  | 创建窗口的所有文字字体 | **是**
sffontssize  | 创建窗口的所有文字大小 | **是**
sftime  | 等待多少秒后开始创建窗口 | **是**
color_list  | 创建窗口的背景颜色列表 | 否(没有的话有自带的列表自动随机)
text_list  | 创建窗口的随机文字 | **是**