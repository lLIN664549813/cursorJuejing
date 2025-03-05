# 稀土掘金自动签到工作流

这是一个基于 GitHub Actions 的稀土掘金自动签到工具，可以帮助你实现每日自动签到，领取免费矿石。

## 功能特点

- 每日自动签到
- 显示签到获得的矿石数量
- 支持手动触发签到
- 通过 GitHub Actions 实现定时运行

## 使用方法

1. Fork 本仓库到你的 GitHub 账号下

2. 获取掘金 Cookie
   - 登录 [掘金网站](https://juejin.cn)
   - 打开浏览器开发者工具（F12）
   - 在 Network 标签页中随便找一个请求
   - 在请求头中找到 Cookie 字段并复制完整内容

3. 设置 GitHub Secrets
   - 在你 fork 的仓库中进入 Settings -> Secrets and variables -> Actions
   - 点击 "New repository secret"
   - Name 填写：`JUEJIN_COOKIE`
   - Value 填写：你刚才复制的 Cookie 内容
   - 点击 "Add secret" 保存

4. 启用 GitHub Actions
   - 进入仓库的 Actions 标签页
   - 点击 "I understand my workflows, go ahead and enable them"

## 自动运行时间

工作流会在每天北京时间早上 9:00 自动运行。你也可以随时手动触发运行：
1. 进入 Actions 标签页
2. 选择 "Juejin Check In" 工作流
3. 点击 "Run workflow"

## 注意事项

- Cookie 有效期一般为 1 个月左右，过期后需要更新 GitHub Secrets 中的 Cookie
- 建议定期检查运行日志，确保签到正常进行
- 如果遇到签到失败，请检查 Cookie 是否过期 