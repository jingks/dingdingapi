import dingding

access_token = ''
secret = ''

# {
#     "msgtype": "text", 
#     "text": {
#         "content": "我就是我, 是不一样的烟火@156xxxx8827"
#     }, 
#     "at": {
#         "atMobiles": [
#             "156xxxx8827", 
#             "189xxxx8325"
#         ], 
#         "isAtAll": false
#     }
# }
robot = dingding.customRobot(access_token, secret)
#jsn = robot.text("老郑 阿宝 你们好", "all")
#jsn = robot.link("这是测试的标题", "这是测试的一段内容，你好啊！阿宝，老郑，中午好！","https://www.baidu.com", "https://www.tp88.net/uploads/allimg/191215/100434HD-0.jpg")
str = """
#### 中旗天气
> 30度，西北风1级，空气良89，相对温度73%
> ![screenshot](https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png)
> ###### 10点20分发布 [天气](https://www.dingalk.com)

"""
#robot.markdown("中旗天气", str, to = "all")
str2 = """
![screenshot](http://image.naic.org.cn/uploadfile/2017/1210/1512869646802502.jpg) 
### 生存以上，生活以下
这是对城中村最佳的定义。城中村所承载的不只是这个特殊地区的生活故事，还有我们这个时代深深的印记。
"""
#jsn = robot.action_card_single("藏在繁华都市的伤疤，也是时代留下的印记", str2, "查看原文", "https://www.jianshu.com/p/747e7006f788")
dicts = {
    "拒绝": "https://www.baidu.com",
    "同意": "https://www.bilibili.com"
}
#jsn = robot.action_card_button("藏在繁华都市的伤疤，也是时代留下的印记", str2, dicts, 0)
articles = {
    "https://www.bilibili.com": ["今天好文推荐，必读好文", "http://image.naic.org.cn/uploadfile/2017/1210/1512869646802502.jpg"],
    "https://www.baidu.com": ["天气预报，提早知道", "https://img.alicdn.com/tfs/TB1NwmBEL9TBuNjy1zbXXXpepXa-2400-1218.png"]
}
jsn = robot.feed_card(articles, to = "all")
#jsn = robot._get_jsn("text", "wahaha", to = "all")
print(jsn)