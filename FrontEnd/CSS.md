# 层叠样式 (CSS)

## 选择器

“~”（波浪号）、“，”（逗号）、 “ + ”（加号）和 “ > ”（大于号）


- p ~ ul

选择器`<p>`元素的所有`<ul>`元素

- .a, .b

逗号指相同的css样式，选择包含a类或b类的元素，并应用相同的样式

- .a.b

无空格，获取同时包含a类和b类的元素

- .a .b

空格指后代元素，a类下所有含有b类的后代元素 (包括儿子节点、孙子节点)

- .a > .b

大于号指子代元素，a类下所有含有b类的子元素 (只包括儿子节点)

- .a + .b

这个`+`是选择相邻兄弟，叫做`相邻兄弟选择器`，与a类相邻的所有b类兄弟元素 (li + li 表示选择第2个到最后一个的所有li标签)

```
.tag + .tag {
  margin-left: 10px;
}
```

## 盒模型

box-sizing:
- content-box (border和padding不计算入width之内, default)
- padding-box (padding计算入width内)
- border-box (border和padding计算入width之内)

通常实现自适应效果的方案: flex + 百分比width + box-sizing:border-box

采用的是flex布局的方式，为了自适应，宽度width采用的是百分比%的形式，border，padding，margin采用的是px尺寸，所有外层的盒子运用了box-sizing:border-box;

## CSS 定位

CSS 有两个最重要的基本属性，前端开发必须掌握：display 和 position。

display属性 指定网页的布局。弹性布局flex和网格布局grid

position属性 指定网页定位。

- static (默认值)
- relative
- fixed
- absolute
- sticky


```css
@supports (position: sticky) {
  .list-header {
    position: sticky;
    top: 0;
  }
}
```

**word-break**

[word-break](https://www.w3school.com.cn/cssref/pr_word-break.asp) 属性规定自动换行的处理方法。

值 | 描述
--- | ---
normal    | 使用浏览器默认的换行规则。
break-all | 允许在单词内换行。
keep-all  | 只能在半角空格或连字符处换行。

**white-space**

[white-space](https://www.w3school.com.cn/cssref/pr_text_white-space.asp) 属性设置如何处理元素内的空白。

值 | 描述
--- | ---
normal   | 默认。空白会被浏览器忽略。
pre      | 空白会被浏览器保留。其行为方式类似 HTML 中的 <pre> 标签。
nowrap   | 文本不会换行，文本会在在同一行上继续，直到遇到 <br> 标签为止。
pre-wrap | 保留空白符序列，但是正常地进行换行。
pre-line | 合并空白符序列，但是保留换行符。
inherit  | 规定应该从父元素继承 white-space 属性的值。

**word-wrap**

[word-wrap](https://www.w3school.com.cn/cssref/pr_word-wrap.asp) 属性允许长单词或 URL 地址换行到下一行。

值 | 描述
--- | ---
normal     | 只在允许的断字点换行（浏览器保持默认处理）。
break-word | 在长单词或 URL 地址内部进行换行。

**text-overflow**

[text-overflow](https://www.w3school.com.cn/cssref/pr_text-overflow.asp) 属性规定当文本溢出包含元素时发生的事情。

值 | 描述
--- | ---
clip     | 修剪文本。
ellipsis | 显示省略符号来代表被修剪的文本。
string   | 使用给定的字符串来代表被修剪的文本。

**overflow**

[overflow](https://www.w3school.com.cn/cssref/pr_pos_overflow.asp) 属性规定当内容溢出元素框时发生的事情。

值 | 描述
--- | ---
visible	| 默认值。内容不会被修剪，会呈现在元素框之外。
hidden	| 内容会被修剪，并且其余内容是不可见的。
scroll	| 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
auto	| 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
inherit	| 规定应该从父元素继承 overflow 属性的值。

**Flex box**

[flex box](https://www.w3school.com.cn/css/css3_flexbox.asp) 弹性框布局模块，可以更轻松地设计灵活的响应式布局结构，而无需使用浮动或定位。

```
布局的传统解决方案，基于盒状模型，依赖 display 属性 + position属性 + float属性。
它对于那些特殊布局非常不方便，比如，垂直居中就不容易实现。
2009年，W3C 提出了一种新的方案----Flex 布局，可以简便、完整、响应式地实现各种页面布局。
目前，它已经得到了所有浏览器的支持，这意味着，现在就能很安全地使用这项功能。
```

父元素（容器）
```
.flex-container {
  display: flex;
}
```

以下是 flex 容器属性：

- flex-direction 属性定义容器要在哪个方向上堆叠 flex 项目。
    - column 值设置垂直堆叠 flex 项目（从上到下）
    - column-reverse 值垂直堆叠 flex 项目（但从下到上）
    - row 值水平堆叠 flex 项目（从左到右）
    - row-reverse 值水平堆叠 flex 项目（但从右到左）
- flex-wrap 属性规定是否应该对 flex 项目换行。
    - wrap 值规定 flex 项目将在必要时进行换行
    - nowrap 值规定将不对 flex 项目换行（默认）
    - wrap-reverse 值规定如有必要，弹性项目将以相反的顺序换行
- flex-flow 属性是用于同时设置 flex-direction 和 flex-wrap 属性的简写属性。
- justify-content 属性用于对齐 flex 项目。
    - center 值将 flex 项目在容器的中心对齐
    - flex-start 值将 flex 项目在容器的开头对齐（默认）
    - flex-end 值将 flex 项目在容器的末端对齐
    - space-around 值显示行之前、之间和之后带有空格的 flex 项目
    - space-between 值显示行之间有空格的 flex 项目
    - space-evenly 项目之间间距与项目与容器间距相等，相当于除去项目宽度，平均分配了剩余宽度作为项目左右margin
- align-items 属性用于垂直对齐 flex 项目。
    - center 值将 flex 项目在容器中间对齐
    - flex-start 值将 flex 项目在容器顶部对齐
    - flex-end 值将弹性项目在容器底部对齐
    - stretch 值拉伸 flex 项目以填充容器（默认）
    - baseline 值使 flex 项目基线对齐
- align-content 属性用于对齐弹性线，用于控制多行项目的对齐方式。
    - space-between 值显示的弹性线之间有相等的间距
    - space-around 值显示弹性线在其之前、之间和之后带有空格
    - stretch 值拉伸弹性线以占据剩余空间（默认）
    - center 值在容器中间显示弹性线
    - flex-start 值在容器开头显示弹性线
    - flex-end 值在容器的末尾显示弹性线


以下是 flex 项目属性：

- order 属性规定 flex 项目的顺序。值必须是数字，默认值是 0。
- flex-grow 属性规定某个 flex 项目相对于其余 flex 项目将增长多少。该值必须是数字，默认值是 0。
- flex-shrink 属性规定某个 flex 项目相对于其余 flex 项目将收缩多少。该值必须是数字，默认值是 0。
- flex-basis 属性规定 flex 项目的初始长度。
- flex 属性是 flex-grow、flex-shrink 和 flex-basis 属性的简写属性。
- align-self 属性规定弹性容器内所选项目的对齐方式。将覆盖容器的 align-items 属性所设置的默认对齐方式。

flex 默认值：`0 1 auto;`

`flex: 1;` 等价于 `flex: 1 1 0%;`

flex 常用场景

1. 数据列表

2. 宫格

## LESS

```
npm install -g less
```

WebStorm 配置 Less File Watcher
