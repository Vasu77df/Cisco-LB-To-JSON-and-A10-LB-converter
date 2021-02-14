from attribute_extractor import server_groups_builders, services_builder, vip_builder, file_merger
import json


if __name__ == "__main__": 
    with open('cfg.json') as cf_file:
        web_mig = input("For which website would you like to build a10 configs: ")
        cfg = json.load(cf_file)
        server_groups_builders(cfg, web_mig)
        services_builder(cfg, web_mig)
        vip_builder(cfg, web_mig)
        file_merger()