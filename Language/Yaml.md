# Yaml

[阮一峰 YAML 语言教程](http://www.ruanyifeng.com/blog/2016/07/yaml.html)

[https://yaml.org/](https://yaml.org/)

[https://github.com/yaml](https://github.com/yaml)

[在线 Demo](https://nodeca.github.io/js-yaml/)

基本规则
```
大小写敏感
使用缩进表示层级关系
缩进时不允许使用Tab键，只允许使用空格。
缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
```

```
languages:
  - Ruby
  - Perl
  - Python
websites:
  YAML: yaml.org
  Ruby: ruby-lang.org
  Python: python.org
  Perl: use.perl.org
greeting:
  - title: Hello World
    language: English
  - title: Hello Everyone
    language: Chiness
emptyInfo: {}
```

```
{
  "languages": [
    "Ruby",
    "Perl",
    "Python"
  ],
  "websites": {
    "YAML": "yaml.org",
    "Ruby": "ruby-lang.org",
    "Python": "python.org",
    "Perl": "use.perl.org" 
  },
  "greeting": [
    {
      "title": "Hello World",
      "language": "English"
    },
    {
      "title": "Hello Everyone",
      "language": "Chiness"
    }
  ],
  "emptyInfo": {}
}
```
