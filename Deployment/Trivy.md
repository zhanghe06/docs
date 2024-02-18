# Trivy

Trivy 是一款功能全面的安全扫描器。 Trivy 拥有查找安全问题的扫描器，并定位可以找到这些问题的位置。

[https://github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)

```
docker run aquasec/trivy
```

忽略待修漏洞（漏洞报出到官方修复有时间差）
```
# trivy image --ignore-unfixed nginx:1.16
```

跳过指定漏洞（）
```
Ignore the specified vulnerabilities

Use .trivyignore.

$ cat .trivyignore
# Accept the risk
CVE-2018-14618

# No impact in our settings
CVE-2019-1543

$ trivy python:3.4-alpine3.9
```
