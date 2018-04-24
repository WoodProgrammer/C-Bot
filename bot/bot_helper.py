from bot_model import BotModel
import os
b_obj = BotModel()
os.environ['BOT_SCRIPT_PATH'] = "~/scripts"

def run_payload(message):

    msg = message.split(',')
    file = msg[0]
    msg.remove(msg[0])


    vars = spliting_vars(message=message)
    #vars = b_obj._get_detail(payload_name=msg[0]) for validation

    try:
        print("python3"+" "+file+".py {}".format(vars))
        return os.system("python3"+" "+file+".py {}".format(vars))
    except Exception as exp:
        print(exp)

def spliting_vars(message):
    msg = message.split(',')
    file = msg[0]
    msg.remove(msg[0])
    var_arr = []
    vars = ','.join(msg)

    for var in vars.split(','):

        tmp = var.split('=')
        var_arr.append(tmp[1])


    return  ' '.join(var_arr)
