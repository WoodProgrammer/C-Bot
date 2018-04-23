from bot_model import BotModel
import os
b_obj = BotModel()

def run_payload(message):

    msg = message.split(',')
    file = msg[0]
    msg.remove(msg[0])

    vars = ''.join(msg)

    #vars = b_obj._get_detail(payload_name=msg[0]) for validation

    try:
        return os.system("python3"+" "+file+".py {}".format(vars))
    except Exception as exp:
        print(exp)
