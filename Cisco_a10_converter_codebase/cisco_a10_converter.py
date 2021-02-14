from ciscoconfparse import CiscoConfParse
from attribute_extractor import content_write_json, content_write_json_ifempty, server_json_builder, content_suspender, ping_generator, server_groups_builders, services_builder, vip_builder, file_merger, LOG_kp_cond_checker, delete_contents
from os import path
import json

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

def main(parse, web_mig):
    print(f"{web_mig} website to be converted!")
    content_parser(parse, web_mig)
    service_parser(parse)
    content_suspender(parse, web_mig)
    with open('cfg.json') as cf_file:
        cfg = json.load(cf_file)
        ping_generator(cfg, web_mig)
        server_groups_builders(cfg, web_mig)
        services_builder(cfg, web_mig)
        vip_builder(cfg, web_mig)
        file_merger()
        LOG_kp_cond_checker(cfg, web_mig)
    print(f"Successfully Converted {web_mig}")

       
if __name__ == "__main__":
    parse =  CiscoConfParse("cisco_config.conf")
    web_mig = input("For which website would you like to convert configs: ")
    # comment out to not delete before each append
    delete_contents()
    main(parse, web_mig)
