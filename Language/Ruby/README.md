# Ruby

[Ruby官网](https://www.ruby-lang.org/zh_cn/)

[https://github.com/ruby/ruby](https://github.com/ruby/ruby)

```
ruby --version
```

```
irb
```

RVM
```
\curl -sSL https://get.rvm.io | bash -s stable --ruby
```

## 示例

```
#!/usr/bin/env ruby

class MegaGreeter
  attr_accessor :names

  # Create the object
  def initialize(names = "World")
    @names = names
  end

  # Say hi to everybody
  def say_hi
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("each")
      # @names is a list of some kind, iterate!
      @names.each do |name|
        puts "Hello #{name}!"
      end
    else
      puts "Hello #{@names}!"
    end
  end

  # Say bye to everybody
  def say_bye
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("join")
      # Join the list elements with commas
      puts "Goodbye #{@names.join(", ")}.  Come back soon!"
    else
      puts "Goodbye #{@names}.  Come back soon!"
    end
  end

end


if __FILE__ == $0
  mg = MegaGreeter.new
  mg.say_hi
  mg.say_bye

  # Change name to be "Zeke"
  mg.names = "Zeke"
  mg.say_hi
  mg.say_bye

  # Change the name to an array of names
  mg.names = ["Albert", "Brenda", "Charles",
    "Dave", "Engelbert"]
  mg.say_hi
  mg.say_bye

  # Change to nil
  mg.names = nil
  mg.say_hi
  mg.say_bye
end
```

## 语法

空白
```
a + b 被解释为 a+b （这是一个局部变量）
a  +b 被解释为 a(+b) （这是一个方法调用）
```

行尾
```
Ruby 把分号和换行符解释为语句的结尾。
但是，如果 Ruby 在行尾遇到运算符，比如 +、- 或反斜杠，它们表示一个语句的延续。
```

多行字符串
```
print <<EOF
    这是第一种方式创建here document 。
    多行字符串。
EOF
 
print <<"EOF";                # 与上面相同
    这是第二种方式创建here document 。
    多行字符串。
EOF
 
print <<`EOC`                 # 执行命令
    echo hi there
    echo lo there
EOC
 
print <<"foo", <<"bar"          # 您可以把它们进行堆叠
    I said foo.
foo
    I said bar.
bar
```

异常
```
begin   =>  try
rescue  =>  catch/except
ensure  =>  finaly
raise   =>  throw/raise
```

空值判断
```
.nil?     Ruby的方法
.empty?   Ruby的方法
.blank?   Rails的方法 相当于同时满足 .nil? 和 .empty?
.present? Rails的方法 就是!blank?
```

### 数据类型

- 数值(Number)
  - 整型(Integer)
  - 浮点型
- 字符串
- 数组
- 哈希
- 范围
  - 范围 (1..5) 意味着它包含值 1, 2, 3, 4, 5
  - 范围 (1...5) 意味着它包含值 1, 2, 3, 4

[Ruby Variable Scope](https://www.techotopia.com/index.php/Ruby_Variable_Scope)

### 变量(五种)

变量名称/前缀 | 说明
--- | ---
`$`	| 全局变量
`@`	| 实例变量
`[a-z]` or `_`	| 局部变量
`[A-Z]`	| 常量
`@@`	| 类变量

伪变量

变量 | 说明
--- | ---
`self` | 当前方法的接收器对象
`true` | 代表 true 的值
`false` | 代表 false 的值
`nil` | 代表 undefined 的值
`__FILE__` | 当前源文件的名称
`__LINE__` | 当前行在源文件中的编号

### 运算符

- 算术运算符
- 比较运算符
- 赋值运算符
- 并行赋值
- 位运算符
- 逻辑运算符
- 三元运算符和范围运算符
- Ruby defined? 运算符
- Ruby 点运算符 "." 和双冒号运算符 "::"
- Ruby 运算符的优先级

### 判断

- if...else 语句
- if 修饰符
- unless 语句
- unless 修饰符
- case 语句

### 循环

while 语句
while 修饰符
until 语句
until 修饰符
for 语句
break 语句
next 语句
redo 语句
retry 语句


### block
```
# 内部迭代器
[1, 2, 3].each {|x| puts x }

# 用f(x) = x * 2将原集合映射到一个新集合
[1, 2, 3].map {|x| x * 2 }

# 挑选出一个集合里的所有奇数
[1, 2, 3].select {|x| x%2 != 0 }

# 动态定义一个问候方法
define_method :greet do |name|
  puts "hello, #{name}"
end
...
```
