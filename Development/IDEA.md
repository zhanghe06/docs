# IntelliJ IDEA

IntelliJ IDEA创建java项目

创建项目
```
File -> New -> Project... -> Next -> Next -> 输入 Project name & Project location
```
例如: java_project

创建包
```
项目根目录下蓝色的src目录, 右键 -> New -> Package -> Enter new package name -> OK
```
例如: students、teachers

创建类
```
在上面新建的包目录上, 右键 -> New -> Java Class -> Create New Class -> OK
```
例如: students.StudentInfo、teachers.TeacherInfo

代码自动生成
```
类文件，右键 -> Generate... -> 光标挪到变量定义下一行 -> Getter and Setter -> 选择变量（可以全选）-> OK
```

`src/zhanghe/HelloWorld.java`右键，Run 'HelloWorld.main()'，自动生成`out/production/java_project/zhanghe/HelloWorld.class`，并返回结果

## 排错

Q1: Intellij IDEA 中 Mybatis Mapper 自动注入 @Autowired 报错

A1: 用 @Resource 替换 @Autowired
