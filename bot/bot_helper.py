import os
from jinja2 import Environment, FileSystemLoader
from bot_model import BotModel

b_obj = BotModel()
def run_payload(payload_name,vars):

    data = b_obj._get_detail(payload_name=payload_name)
    os.system("python3" +" "+payload_name+".py"+vars)

def verify_vars(payload_name):
    data = b_obj._get_detail(payload_name=payload_name)
    print(data['vars'])


def dockerize_function(payload_name):## build generated docker file
    file = b_obj._get_detail(payload_name=payload_name)

def generate_docker_file(payload_name):###generating docker file

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('Dockerfile')
    output_from_parsed_template = template.render(payload=payload_name,payload_file=payload_name+".py")
    print(output_from_parsed_template)
    with open(payload_name, "w") as fh:
        fh.write(output_from_parsed_template)
