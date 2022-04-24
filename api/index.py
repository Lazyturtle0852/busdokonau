
# ライブラリをインポート
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
import os
#Flaskを準備
app = Flask(__name__)
#環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["Lgu/2HP9iar1Fk7exqjcUQYHBH8WdwijwoYQ8miM39bmeN9prGuIJl9/KGYRCS1PmEsPFOftefr5uoMSFvJS4NvZD4eTt3I9X9mp73hFFVXpr5PkrUr8m0oMn399Y5gXnNRoGOp5XyDJ407ezOXOFGQdB04t89/1O/w1cDnyilFU="]
#環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["37d7b1cfad1145e932830f360f541c23"]
#LineBotApiのインスタンスを生成
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
#WebhookHandlerのインスタンスを生成
webhook_handler = WebhookHandler(LINE_CHANNEL_SECRET)
@app.route("/callback", methods=['POST'])
def callback():
    # HTTPリクエストヘッダからX-Line-Signatureを取り出す
    signature = request.headers['X-Line-Signature']
    #テキストでpostされたデータを取得
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text )
    )
if __name__ == "__main__":
    app.run()
