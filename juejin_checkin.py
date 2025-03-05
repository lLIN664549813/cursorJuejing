'''
Description: 掘金自动签到脚本
Version: 1.0
Author: Zhanglin
Date: 2025-03-05 10:09:33
LastEditors: Zhanglin
LastEditTime: 2025-03-05 15:52:07
'''
import requests
import json
import os
from datetime import datetime

class JuejinCheckIn:
    def __init__(self):
        self.cookie = os.environ.get("JUEJIN_COOKIE", "")
        if not self.cookie:
            raise ValueError("请设置JUEJIN_COOKIE环境变量")
        
        # 基础请求头
        self.headers = {
            "Cookie": self.cookie,  # 直接使用原始 Cookie
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Origin": "https://juejin.cn",
            "Referer": "https://juejin.cn/",
            "Content-Type": "application/json"
        }

    def _make_request(self, method, url, **kwargs):
        """统一的请求处理"""
        try:
            # 使用 requests 而不是 session，避免 Cookie 被自动处理
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                **kwargs
            )
            return response.json()
        except Exception as e:
            print(f"请求异常: {str(e)}")
            return {"err_no": 1, "err_msg": str(e)}

    def check_in(self):
        """执行签到操作"""
        url = "https://api.juejin.cn/growth_api/v1/check_in"
        params = {
            "aid": "2608",
            "uuid": "7108619669937612289",
            "spider": "0"
        }
        
        try:
            result = self._make_request("POST", url, params=params)
            
            if result.get("err_no") == 0:
                data = result.get("data", {})
                return f"签到成功！当前矿石数: {data.get('sum_point')}"
            else:
                return f"签到失败：{result.get('err_msg', '未知错误')}"
        except Exception as e:
            return f"签到异常：{str(e)}"

    def get_current_point(self):
        """获取当前矿石数"""
        url = "https://api.juejin.cn/growth_api/v1/get_cur_point"
        params = {
            "aid": "2608",
            "uuid": "7108619669937612289",
            "spider": "0"
        }
        
        try:
            result = self._make_request("GET", url, params=params)
            
            if result.get("err_no") == 0:
                return result.get("data", 0)
            return 0
        except:
            return 0

def main():
    try:
        checkin = JuejinCheckIn()
        
        # 获取签到前的矿石数
        point_before = checkin.get_current_point()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 签到前矿石数：{point_before}")
        
        # 执行签到
        result = checkin.check_in()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {result}")
        
        # 获取签到后的矿石数
        point_after = checkin.get_current_point()
        print(f"本次签到获得矿石：{point_after - point_before}")
        
    except Exception as e:
        print(f"程序运行异常：{str(e)}")

if __name__ == "__main__":
    main() 