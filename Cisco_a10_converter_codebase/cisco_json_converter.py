from ciscoconfparse import CiscoConfParse
from attribute_extractor import content_write_json, content_write_json_ifempty, \
    server_json_builder, content_suspender, ping_generator
from os import path

def content_parser(parse, web_mig):
    if path.isfile('cfg.json'):
        content_write_json(parse, web_mig)
    else:
        content_write_json_ifempty(parse, web_mig)

def service_parser(parse):
    if path.isfile('cfg.json'):
        server_json_builder(parse)
    else:
        print("failed")
       
if __name__ == "__main__":
    parse =  CiscoConfParse("cisco_config.conf")
    web_mig = input("For which website would you like to convert configs to json: ")
    content_parser(parse, web_mig)
    service_parser(parse)
    content_suspender(parse, web_mig)
    ping_generator(parse, web_mig)