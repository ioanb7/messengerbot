"""from pymessenger.bot import Bot
bot = Bot("EAAQ0cw89UL4BANjJR09Hhmu4Iu4clVa5Qw4KIb81D3e0Ia8LxV03I3ZAICAPef6ob2ZATHBLglQ3Ax0T1mdFCfxUwQh0BL1M0YRTLbG22mrQwNDXuAk317MJ6p73rhFqlXY34zVYLFuzpz33ZASjAgYXoDnZBTleQ0JxMkRtCgZDZD")
elements = []
element = Element(title="test", subtitle="subtitle", item_url="http://arsenal.com")
elements.append(element)

bot.send_generic_message("ioanb7", elements)
"""
"""
This bot listens to port 5002 for incoming connections from Facebook. It takes
in any messages that the bot receives and echos it back.
"""
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)

ACCESS_TOKEN = ""
VERIFY_TOKEN = ""
bot = Bot(ACCESS_TOKEN)


@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'GET':
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        else:
            return 'Invalid verification token'

    if request.method == 'POST':
        output = request.get_json()
        print(output)
        for event in output['entry']:
            messaging = event['messaging']
            for x in messaging:
                if x.get('message'):
                    recipient_id = x['sender']['id']
                    if x['message'].get('text'):
                        message = x['message']['text']
                        bot.send_text_message(recipient_id, message)
                        bot.send_text_message(recipient_id, "Tom sucks")
                    if x['message'].get('attachment'):
                        bot.send_attachment_url(recipient_id, x['message']['attachment']['type'],
                                                x['message']['attachment']['payload']['url'])
                else:
                    pass
        return "Success"


if __name__ == "__main__":
    app.run(port=5000, debug=True)