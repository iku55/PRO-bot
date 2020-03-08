import requests, bs4
import json
# インストールした discord.py を読み込む
import discord

res = requests.get('https://playerrealms.com/server')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
print(soup.title)
#print(res.text)
elems = soup.select('.card-body')
for elem in elems:
    print(elem)

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'bottoken'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='24時間起動 | ヘルプ:$pro help | BOT作成:ik#3078'))
    print('ログインしました')
    webhook_url = 'loggingwebhookurl'
    main_content = {
  "username": "PlayerRealmsOnline",
  "embeds": [
    {
      "author": {
        "name": "ログ",
      },
      "title": "",
      "url": "",
      "description": "ログイン/再起動が完了しました。",
      "color": 15258703,
      "footer": {
        "text": "PlayerRealmsOnlineログ",
      }
    }
  ]
}
 
 
    requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
    
# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if '$pro' in message.content:
        await message.channel.send("PlayerRealmsOnlineは、9月のPlayerRealmsの閉鎖に伴い、9月22日に、開発終了及びサービス提供を終了しました。ご利用ありがとうございました。")
        user = message.author
        cmd = "[コマンドログ]ユーザー:" + str(message.author) + "(ユーザーID:" + str(message.author.id) + "),コマンド:" + str(message.content) + "(メッセージID:" + str(message.id) + "),チャンネル:" + str(message.channel) + ",(チャンネルID:" + str(message.channel.id) + ")" 
        moji = message.content
        Aarg = moji.split(' ')[0]
        Barg = moji.split(' ')[1]
        if user.id is "421215604767457280":
            embed=discord.Embed(color=0x80ffff)
            embed.add_field(name="あなたは処罰されています", value="PlayerRealms Server Checker:不適切な発言 / スパム行為 / BOTコマンドの悪用", inline=False)
            embed.add_field(name="異議申し立て", value="discordserverurl", inline=False)
            embed.set_footer(text="BOT作成:iku55")
            await message.channel.send(embed=embed)
            return
        
        if Barg == 'title':
            title = soup.title
            embed=discord.Embed(color=0x80ffff)
            embed.add_field(name='取得結果', value=str(title).replace("<title>", "").replace("</title>", ""), inline=False)
            embed.set_footer(text="BOT作成:iku55")
            await message.channel.send(embed=embed)
        elif Barg == 'invite':
            embed=discord.Embed(color=0x80ffff)
            embed.add_field(name='リンク', value="https://discordapp.com/api/oauth2/authorize?client_id=602308401212555287&permissions=11264&scope=bot", inline=False)
            embed.set_footer(text="BOT作成:iku55")
            await message.channel.send(embed=embed)
        elif Barg == 'check':
            Carg = moji.split(' ')[2]
            resA = requests.get('https://playerrealms.com/server/' + Carg)
            soupA = bs4.BeautifulSoup(resA.text, "html.parser")
            elemsA = soupA.select('.list-group-item')
            ln = 0
            for elemA in elemsA:
                ln += 1
                rd = str(elemA).replace("<li class=\"list-group-item\">", "").replace("主:", "サーバーオーナー:").replace("サーバー状態:", "状態:").replace("Motd:", "説明:").replace("投票:", "投票数:").replace("Last Start:", "最終起動:").replace("</li>", "").replace("<span class=\"label label-default premium\">Premium", "✔プレミアム").replace("<span class=\"label label-default ultra\">UltraPremium", "✔ウルトラプレミアム").replace("</span>", "")
                if ln == 1:
                    m = "ServerName: " + str(Carg) + "\n" + str(rd)
                    iti = str(m)
                else:
                    m = str(iti) + "\n" + str(rd)
                    iti = str(m)
            embed=discord.Embed(color=0x80ffff)
            if Carg == 'Hub':
                embed.add_field(name='取得結果', value=str(m) + '\nserverコマンド: /hub or /lobby', inline=False)
            else:
                embed.add_field(name='取得結果', value=str(m) + '\nserverコマンド: /server ' + str(Carg), inline=False)
            embed.set_footer(text="BOT作成:iku55")
            await message.channel.send(embed=embed)
        elif Barg == 'help':
            embed=discord.Embed(color=0x80ffff)
            embed.add_field(name='PRonlineヘルプ - プレフィックス:$', value="$pro help  - ヘルプを表示します。\n$pro invite  - 招待リンクを表示します。\n$pro check <サーバー名>  - サーバー情報を表示します。\n$pro update  - アップデート情報を表示します", inline=False)
            embed.set_footer(text="BOT作成:iku55")
            await message.channel.send(embed=embed)
        elif Barg == 'update':
            embed=discord.Embed(color=0x80ffff)
            embed.add_field(name='PRonlineアップデート情報', value="アップデート 2.0\n - いろいろ", inline=False)
            embed.set_footer(text="BOT作成:iku55")
            await message.channel.send(embed=embed)
        elif Barg == 'servers':
            servers = 0
            sn = ''
            for server in client.gulids:
                servers = servers + 1
                sn = sn + ' , '
            embed=discord.Embed(color=0x80ffff)
            embed.add_field(name='PRonlineを使用しているサーバー(' + str(servers) + ')', value=sn, inline=False)
            embed.set_footer(text="BOT作成:iku55")
            await message.channel.send(embed=embed)
        webhook_url = 'loggingwebhookurl'
        main_content = {
  "username": "PlayerRealmsOnline",
  "embeds": [
    {
      "author": {
        "name": "ログ",
      },
      "title": "",
      "url": "",
      "description": cmd,
      "color": 15258703,
      "footer": {
        "text": "PlayerRealmsOnlineコマンドログ",
      }
    }
  ]
}
 
 
        requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
        
                
# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
