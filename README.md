# 玲儿

自用 QQ 机器人。

## 功能

- Bilibili 用户监控，参见：[nonebot-plugin-bam]
- 跑团骰子，参见 [nonebot-plugin-7s-roll]

## 使用

```bash
pip install qqbot-linger
cd /a/path/you/want/store/config/and/database
vim .env # edit this file, see `.env.sample file` for a example

# Start a IM Bot Client compatible with OneBot v11 protocol
# Like go-cqhttp, cqhttp-mirai etc

linger # start the bot
```

注意：你需要一个支持连接 OneBot V11 协议的 IM 客户端的具体实现，并将其配置为连接到此机器人的 WS 端口，才能实际使用其功能。

## 截图

以后再弄。

## LICENSE

Unlicense.

[nonebot-plugin-bam]: https://github.com/7sDream/nonebot-plugin-bam
[nonebot-plugin-7s-roll]: https://github.com/7sDream/nonebot-plugin-7s-roll
