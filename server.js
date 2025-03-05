/*
 * @Description: 掘金 Cookie 测试服务器
 * @Version: 1.0
 * @Author: Zhanglin
 * @Date: 2025-03-05 15:52:03
 * @LastEditors: Zhanglin
 * @LastEditTime: 2025-03-05 16:18:47
 */
import express from 'express';
import cors from 'cors';
import path from 'path';
import fetch from 'node-fetch';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const app = express();
const port = 8000;

// 配置 CORS
app.use(cors());

// 提供静态文件服务
app.use(express.static(__dirname));

// 首页重定向到测试页面
app.get('/', (req, res) => {
    res.redirect('/test_cookie.html');
});

// 代理掘金 API 请求
app.get('/api/test-cookie', async (req, res) => {
    try {
        // 从自定义请求头获取 Cookie
        const cookie = req.headers['x-custom-cookie'];
        
        if (!cookie) {
            return res.status(400).json({
                err_no: 1,
                err_msg: '请提供 Cookie'
            });
        }

        // 构建查询参数
        const params = new URLSearchParams({
            aid: '2608',
            uuid: '7108619669937612289',
            spider: '0'
        });

        console.log('使用的 Cookie:', cookie);  // 添加日志

        // 请求掘金 API
        const response = await fetch(`https://api.juejin.cn/growth_api/v1/get_cur_point?${params.toString()}`, {
            headers: {
                'Cookie': cookie,  // 直接使用原始 Cookie
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Origin': 'https://juejin.cn',
                'Referer': 'https://juejin.cn/',
                'Content-Type': 'application/json'
            }
        });

        const data = await response.json();
        console.log('API 响应:', data);  // 添加日志
        res.json(data);
    } catch (error) {
        console.error('API 请求错误:', error);
        res.status(500).json({
            err_no: 1,
            err_msg: '服务器错误：' + error.message
        });
    }
});

// 启动服务器
app.listen(port, () => {
    console.log(`
掘金 Cookie 测试服务器已启动！

请在浏览器中访问:
http://localhost:${port}/test_cookie.html

按 Ctrl+C 可停止服务器
`);
}); 