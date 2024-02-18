# 加密解密 (Encrypt Decrypt)

格式工具 [https://lapo.it/asn1js/](https://lapo.it/asn1js/)


获取百度的证书
```
echo -n | openssl s_client -connect 180.101.49.12:443 | openssl x509 > baidu.crt
```


python的加密算法一般在PyCrypto库中，这个库包含了常见的:

- 对称加密算法（DES、AES、IDEA、等）
- 公钥加密算法（RSA、DSA、等）
- 散列算法（MD5、SHA1、RIPEMD、等）


pycrypto，pycrytodome和crypto是一个东西，crypto在python上面的名字是pycrypto它是一个第三方库，但是已经停止更新三年了，所以不建议安装这个库；

2
windows下python3.6安装也不会成功！

这个时候pycryptodome就来了，它是pycrypto的延伸版本，用法和pycrypto 是一模一样的；

3
所以，我现在告诉一种真的解决方法：直接安装：

pip install pycryptodome




X.509格式证书


DSS Digital Signature Standard (DSS) 

- RSA
- 数字签名算法(DSA)




DSA（Digital Signature Algorithm，数字签名算法，用作数字签名标准的一部分），它是另一种公开密钥算法，它不能用作加密，只用作数字签名。
DSA使用公开密钥，为接受者验证数据的完整性和数据发送者的身份。它也可用于由第三方去确定签名和所签数据的真实性。
DSA算法的安全性基于解离散对数的困难性，这类签字标准具有较大的兼容性和适用性，成为网络安全体系的基本构件之一。

