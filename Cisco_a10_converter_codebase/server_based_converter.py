from ciscoconfparse import CiscoConfParse
import json
from attribute_extractor import server_finder, ssl_list_filter, delete_contents
from cisco_a10_converter import main



if __name__ == "__main__":
    parse =  CiscoConfParse("cisco_config.conf")
    srv = input("Which server would you like migrate configs for?: ")
    srv_list = server_finder(parse, srv)
    srv_list = ssl_list_filter(srv_list)
    delete_contents()
    for item in srv_list:
        main(parse, item)