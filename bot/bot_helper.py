from bot_model import BotModel

b_obj = BotModel()

def run_payload(path,payload_name,vars):
    data = get_vars(payload_name=payload_name)
    if len(vars) != data['vars']:
        return "Err"
    else:
        os.system("python3"+payload_name+".py"+vars)



def get_vars(payload_name):
    return b_obj._get_detail(payload_name=payload_name)
