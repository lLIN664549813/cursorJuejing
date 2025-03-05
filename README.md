<!--
 * @Description: Zhanglin Create File
 * @Version: 1.0
 * @Author: Zhanglin
 * @Date: 2025-03-05 10:10:25
 * @LastEditors: Zhanglin
 * @LastEditTime: 2025-03-05 14:18:06
-->
# 稀土掘金自动签到工作流

这是一个基于 GitHub Actions 的稀土掘金自动签到工具，可以帮助你实现每日自动签到，领取免费矿石。

## 功能特点

- 每日自动签到
- 显示签到获得的矿石数量
- 支持手动触发签到
- 通过 GitHub Actions 实现定时运行

## 使用方法

1. Fork 本仓库到你的 GitHub 账号下
   - 点击本仓库右上角的 `Fork` 按钮
   - 选择你的 GitHub 账号
   - 等待 Fork 完成

2. 获取掘金 Cookie（重要！）
   - 使用 Chrome 浏览器登录 [掘金网站](https://juejin.cn)
   - 确保你已经完全登录（可以看到你的头像和用户名）
   - 按 F12 打开浏览器开发者工具
   - 切换到 Network（网络）标签页
   - 在 Network 面板顶部，确保选中了 "Preserve log"（保留日志）选项
   - 清空当前的网络请求记录（点击 Network 面板中的 🚫 图标）
   - 点击掘金网站右上角的头像，再点击"我的主页"触发请求
   - 在 Network 面板中找到任意一个 `api.juejin.cn` 的请求（比如 `get_user_info` 或 `growth`）
   - 点击该请求，在右侧 Headers（标头）中找到 `Request Headers`（请求标头）
   - 找到 `cookie` 字段，完整复制其值（从开头到结尾，不要漏掉任何字符）
   - 注意：确保 Cookie 中包含以下关键信息：
     * `sessionid`
     * `uid`
     * `user_id`
     * `_tea_cookie_tokens`

3. 设置 GitHub Secrets
   - 在你 fork 的仓库中点击 `Settings`（设置）标签
   - 在左侧边栏中向下滚动，找到 `Security` 部分
   - 点击 `Secrets and variables`
   - 选择 `Actions`
   - 在 `Repository secrets` 部分，点击 `New repository secret` 按钮
   - 在 `Name` 字段中填写：`JUEJIN_COOKIE`
   - 在 `Secret` 字段中粘贴你刚才复制的完整 Cookie 内容
   - 点击 `Add secret` 保存
   - 注意事项：
     * Cookie 必须完整，不要漏掉任何部分
     * 不要包含多余的引号或空格
     * 不要手动修改 Cookie 的内容

4. 启用 GitHub Actions
   - 点击仓库顶部的 `Actions` 标签
   - 如果看到警告提示，点击 `I understand my workflows, go ahead and enable them`
   - 在左侧找到 `Juejin Check In` 工作流
   - 点击 `Enable workflow` 启用

## 自动运行时间

工作流会在每天北京时间早上 9:00（UTC+8）自动运行。你也可以随时手动触发运行：
1. 进入 Actions 标签页
2. 选择左侧的 "Juejin Check In" 工作流
3. 点击 "Run workflow" 下拉按钮
4. 选择分支（默认 main）并点击绿色的 "Run workflow" 按钮

## 查看运行结果

1. 在 Actions 标签页中点击最新的工作流运行记录
2. 展开 `Run check-in script` 步骤
3. 你可以看到签到结果和获得的矿石数量

## 常见问题

1. 签到失败问题
   - 最常见原因：Cookie 不完整或格式错误
     * 确保完全按照上述步骤获取 Cookie
     * 检查 Cookie 中是否包含所有必需的字段（sessionid、uid 等）
     * 不要手动编辑或修改 Cookie 内容
   - Cookie 过期问题
     * Cookie 有效期通常为 1-2 周
     * 如果提示未登录或签到失败，请重新获取 Cookie
     * 建议每周更新一次 Cookie
   - 请求失败问题
     * 确保你的掘金账号状态正常
     * 检查是否触发了掘金的风控机制
     * 尝试在浏览器中手动签到，确认账号正常

2. 工作流未自动运行
   - 检查是否已启用 Actions
   - 确认仓库的 Actions 权限（Settings -> Actions -> General）
   - 查看 Actions 页面中的运行日志
   - 检查工作流文件格式是否正确

## 注意事项

- Cookie 有效期比较短，建议每周更新一次
- 如果遇到 "未登录" 错误，说明 Cookie 已失效，需要重新获取
- 定期检查运行日志，确保签到正常进行
- 如果连续签到失败，建议：
  1. 重新获取完整的 Cookie
  2. 在浏览器中测试手动签到
  3. 检查 Actions 运行日志中的详细错误信息 