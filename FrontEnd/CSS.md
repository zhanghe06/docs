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