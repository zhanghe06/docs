# RPA

RPA（机器人流程自动化）

rpa架构

config
    step 间隔时间
    task 间隔时间
    step 重试次数
    task 重试次数

pipeline
    - step
        - task
    - step
        - task

task
    - check（资源）
    - login（页面）
    - doing（执行）
    - store（存储）
