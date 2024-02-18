# 日志

```
crontab -e
# 定时切割
0 0 * * * find /medishare/run/log/*.log -size +0 -name '*.log' | xargs /tools/log_rotate.sh

# 手动切割
find /medishare/run/log/*.log -size +0 -name '*.log' | xargs /tools/log_rotate.sh
```
