'''functions to parse various attributes from the config file'''
import json
from os import path, remove

def vip_extractor(children):
    vip = list()
    for child_attri in children:
        vip_add = child_attri.re_match_typed(r'vip\s+address\s+(\S+)', default="NO_MATCH")
        if vip_add != "NO_MATCH":
            vip.append(vip_add)

    return vip

def port_extractor(children):
    port = list()
    for child_attri in children:
        port_add = child_attri.re_match_typed(r'port\s+(\S+)', default="NO_MATCH")
        if port_add != "NO_MATCH":
            port.append(port_add)

    return port

def protocol_extractor(children):
    protocol = list()
    for child_attri in children:
        protocol_add = child_attri.re_match_typed(r'protocol\s+(\S+)', default="NO_MATCH")
        if protocol_add != "NO_MATCH":
            protocol.append(protocol_add)

    return protocol

def ser_extractor(children):
    ser = list()
    for child_attri in children:
        ser_add = child_attri.re_match_typed(r'add\s+service\s+(\S+)', default="NO_MATCH")
        if ser_add != "NO_MATCH":
            ser.append(ser_add)
    return ser

def active_extractor(children):
    active = list()
    for child_attri in children:
        active_add = child_attri.re_match_typed(r'(active)', default="NO_MATCH")
        if active_add != "NO_MATCH":
            active.append(active_add)

    return active

def application_extractor(children):
    app = list()
    for child_attri in children:
        app_add = child_attri.re_match_typed(r'application\s+(\S+)', default="NO_MATCH")
        if app_add != "NO_MATCH":
            app.append(app_add)

    return app

def adbal_extractor(children):
    adbal = list()
    for child_attri in children:
        adbal_add = child_attri.re_match_typed(r'advanced-balance\s+(\S+)', default="NO_MATCH")
        if adbal_add != "NO_MATCH":
            adbal.append(adbal_add)

    return adbal

def ip_add_extractor(children):
    ip = list()
    for child_attri in children:
        ip_add = child_attri.re_match_typed(r'ip\s+address\s+(\S+)', default="NO_MATCH")
        if ip_add != "NO_MATCH":
            ip.append(ip_add)

    return ip

def string_extractor(children):
    strings = list()
    for child_attri in children:
        str_add = child_attri.re_match_typed(r'string\s+(\S+)', default="NO_MATCH")
        if str_add != "NO_MATCH":
            strings.append(str_add)

    return strings

def keepalive_extractor(children):
    kp = list()
    for child_attri in children:
        kp_type = child_attri.re_match_typed(r'keepalive\s+type\s+(\S+)', default="NO_MATCH")
        if kp_type != "NO_MATCH":
            kp.append(kp_type)

    return kp

def kpuri_extractor(children):
    kpuri = list()
    for child_attri in children:
        kpuri_type = child_attri.re_match_typed(r'keepalive\s+uri\s+(\S+)', default="NO_MATCH")
        if kpuri_type != "NO_MATCH":
            kpuri.append(kpuri_type)

    return kpuri

def content_json_builder(web_name, children):
    configs_json = {
        web_name: {
           # 'vip': vip_extractor(children)[0],
           # 'port': int(port_extractor(children)[0]), 
           # 'protocol': protocol_extractor(children)[0],
           # 'service': ser_extractor(children),
           # 'active_status': active_extractor(children)[0],
           # 'application': application_extractor(children),
           # 'advanced-balance': application_extractor(children)
    }
    }
    vip_temp = vip_extractor(children)
    port_temp = (port_extractor(children))
    protocol_temp =  protocol_extractor(children)
    service_temp = ser_extractor(children)
    active_status_temp = active_extractor(children)
    application_temp = application_extractor(children)
    advanced_balance_temp = application_extractor(children)
    
    if not vip_temp:
        configs_json[web_name].update(vip = None)
    else:
        configs_json[web_name].update(vip = vip_temp[0])
    
    if not port_temp:
        configs_json[web_name].update(port = None)
    else:
        configs_json[web_name].update(port = int(port_temp[0]))
    
    if not protocol_temp:
        configs_json[web_name].update(protocol = None)
    else:
        configs_json[web_name].update(protocol = protocol_temp[0])
    
    if not service_temp:
       configs_json[web_name].update(service = None)
    else:
        configs_json[web_name].update(service = service_temp)

    if not active_status_temp:
        configs_json[web_name].update(active_status = None)
    else:
        configs_json[web_name].update(active_status = active_status_temp[0])

    if not application_temp:
        configs_json[web_name].update(application = None)
    else:
        configs_json[web_name].update(application = application_temp[0])

    if not advanced_balance_temp:
        configs_json[web_name].update(advanced_balance = None)
    else:
        configs_json[web_name].update(advanced_balance = advanced_balance_temp[0])
    
    return configs_json

def service_json_bulder(serv_name, children):
    ser_json = {
        serv_name: {
            #'ip_add': ip_add_extractor(children),
            #'string': string_extractor(children),
            #'port': port_extractor(children),
            #'keepalive_type': keepalive_extractor(children),
            #'keppalive_uri': kpuri_extractor(children),
            #'active_status': active_parse(children)
        }
    }

    ip_temp = ip_add_extractor(children)
    string_temp =  string_extractor(children)
    keepalive_temp = keepalive_extractor(children)
    kpuri_temp = kpuri_extractor(children)
    active_status_temp = active_extractor(children)

    if not ip_temp:
        ser_json[serv_name].update(ip_address = None)
    else:
        ser_json[serv_name].update(ip_address = ip_temp[0])

    if not string_temp:
        ser_json[serv_name].update(string = None)
    else:
        ser_json[serv_name].update(string = string_temp[0])

    if not keepalive_temp:
        ser_json[serv_name].update(keepalive_type = None)
    else:
        ser_json[serv_name].update(keepalive_type = keepalive_temp[0])
    
    if not kpuri_temp:
        ser_json[serv_name].update(keepalive_uri = None)
    else:
        ser_json[serv_name].update(keepalive_uri = kpuri_temp[0])
    
    if not active_status_temp:
        ser_json[serv_name].update(active_status = None)
    else:
        ser_json[serv_name].update(active_status = active_status_temp[0])

    return ser_json

def content_write_json_ifempty(parse, web_mig):
    with open('cfg.json', 'w+') as json_file:
        json_cfg = {}
        for attri in parse.find_objects("content {web_mig}".format(web_mig=web_mig)):
            web_name = attri.text
            web_name = web_name.strip(" ")
            web_name = web_name.replace("content ", "")
            data = content_json_builder(web_name, attri.children)
            json_cfg.update(data) 
        json.dump(json_cfg, json_file, indent=4)

def content_write_json(parse, web_mig):
    with open('cfg.json', 'r') as json_file:
        json_cfg = json.load(json_file)
        for attri in parse.find_objects("content {web_mig}".format(web_mig=web_mig)):
            web_name = attri.text
            web_name = web_name.strip(" ")
            web_name = web_name.replace("content ", "")
            data = content_json_builder(web_name, attri.children)
            json_cfg.update(data)
    with open('cfg.json', 'w') as json_file:
        json.dump(json_cfg, json_file, indent=4)

def server_json_builder(parse):
    with open('cfg.json') as json_file:
        content_json = json.load(json_file)
        for key in content_json:
            for server in content_json[key]['service']:
                for attri in parse.find_objects("^service {server}".format(server = server)):
                    server_json = service_json_bulder(server, attri.children)
                    content_json[key].update(server_json)
    with open('cfg.json', 'w') as json_file:
        json.dump(content_json, json_file, indent=4)

def content_suspender(parse, web_mig):
    with open('cfg.json') as json_file:
        cfgs = json.load(json_file)
        for attri in parse.find_objects("content {web_mig}".format(web_mig=web_mig)):
            web_name = attri.text
            web_name = web_name.strip(" ")
            web_name = web_name.replace("content ", "")
            for key in cfgs:
                if key == web_name:
                    with open('suspend_list.txt', 'a') as sus_file:
                        sus_file.write("content " + key + '\n')
                        sus_file.write("suspend" + '\n')
                        sus_file.write("exit" + '\n')
                        sus_file.write(" "+ '\n')

def ping_generator(cfg, web_mig):
    content = content_extractor(cfg, web_mig)
    with open('ping_list.txt', 'a') as sus_file:
        sus_file.write('ping ' + cfg[content]['vip'] + '\n')

#def ping_generator(parse, web_mig):
   # with open('cfg.json') as json_file:
    #    cfgs = json.load(json_file)
     #   for attri in parse.find_objects("content {web_mig}".format(web_mig=web_mig)):
      #      web_name = attri.text
       #     web_name = web_name.strip(" ")
        #    web_name = web_name.replace("content ", "")
         #   for key in cfgs:
          #      if key == web_name:
           #         with open('ping_list.txt', 'a') as sus_file:
            #            sus_file.write('ping ' + cfgs[key]['vip'] + '\n')
    
# Methods for a10_builder
def content_extractor(cfg, web_mig):
    for key in cfg:
        if key == web_mig:    
            return key

def group_write_ssl(cfg, content, grp_file):
    content_name = content
    if '-ssl' in content_name:
        content_name = content.replace('-ssl', '')
    server_groups = 'SG_' + content_name + '-' + '443'
    grp_file.write("slb service-group " + server_groups + " " + str(cfg[content_name]['protocol']) + "\n")
    grp_file.write("method least-connection\n")
    for servers in cfg[content_name]['service']:
        srv_name = 'SRV_' + servers
        grp_file.write('member ' + srv_name + ' ' + '443' + '\n')
    grp_file.write('exit\n')
    grp_file.write('exit\n')
    grp_file.write(' ' + '\n')

def group_write(cfg, content, grp_file):
    content_name = content
    if '-ssl' in content_name:
        content_name = content.replace('-ssl', '')
    server_groups = 'SG_' + content_name + '-' + str(cfg[content]['port'])
    grp_file.write("slb service-group " + server_groups + " " + str(cfg[content]['protocol']) + "\n")
    grp_file.write("method least-connection\n")
    for servers in cfg[content]['service']:
        srv_name = 'SRV_' + servers
        grp_file.write('member ' + srv_name + ' ' + str(cfg[content]['port']) + '\n')
    grp_file.write('exit\n')
    grp_file.write('exit\n')
    grp_file.write(' ' + '\n')

def server_groups_builders(cfg, web_mig):
    content = content_extractor(cfg, web_mig)
    content_ssl = content + '-ssl'
    if path.isfile("a10_group.txt"):
        with open("a10_group.txt", 'a') as grp_file:
            group_write(cfg, content, grp_file)
        if content_ssl in cfg:
            with open("a10_group.txt", 'a') as grp_file:
                group_write(cfg, content_ssl, grp_file)
        else:
            with open("a10_group.txt", 'a') as grp_file:
                group_write_ssl(cfg, content_ssl, grp_file)
    else:
        with open("a10_group.txt", 'w') as grp_file:
            grp_file.write('#=====================================' + '\n')
            grp_file.write('#    SERVER GROUPS    ' + '\n')
            grp_file.write('#=====================================' + '\n')
            group_write(cfg, content, grp_file)
        if content_ssl in cfg:
            with open("a10_group.txt", 'a') as grp_file:
                group_write(cfg, content_ssl, grp_file)
        else:
            with open("a10_group.txt", 'a') as grp_file:
                group_write_ssl(cfg, content_ssl, grp_file)

def service_writer(cfg, content, srv_file):
    for server in cfg[content]['service']:
        srv_file.write('slb server ' + 'SRV_' + server + ' ' + cfg[content][server]['ip_address'] + '\n')
        if cfg[content][server]['keepalive_type'] == 'http':
            if cfg[content][server]['keepalive_uri'] == "\"/keepalive.aspx\"":
                srv_file.write('health-check HM-keepalive_aspx-TCP_80\n')
            else:
                srv_file.write('## error please check the keepsalive parameters\n')
        else:
            pass

        srv_file.write('slow-start\n')
        srv_file.write('port 80 '  + cfg[content]['protocol'] + '\n')
        srv_file.write('health-check-disable\n')
        srv_file.write('exit\n')
        srv_file.write('port 443 ' + cfg[content]['protocol'] + '\n')
        srv_file.write('health-check-disable\n')
        srv_file.write('exit\n')
        srv_file.write('exit\n')
        srv_file.write(' ' + '\n')

def services_builder(cfg, web_mig):
    content = content_extractor(cfg, web_mig)
    if path.isfile("a10_services.txt"):
        with open("a10_services.txt", 'a') as srv_file:
            service_writer(cfg, content, srv_file)
    else:
        with open("a10_services.txt", 'w') as srv_file:
            srv_file.write('#======================================' + '\n')
            srv_file.write('#  SERVER INSTANCES' + '\n')
            srv_file.write('#======================================' + '\n')
            service_writer(cfg, content, srv_file)

def vips_writer(cfg, content, vips_file):
    proto_nossl = 'http'
    proto_ssl = 'tcp'
    vips_file.write("slb virtual-server " + "VIP_" + content + " " + cfg[content]['vip'] + '\n')
    vips_file.write("port " + str(cfg[content]['port']) + " " + proto_nossl + '\n')
    vips_file.write("source-nat pool NAT-GROUP-1\n")
    vips_file.write("service-group " + "SG_" + content + "-80\n")
    vips_file.write("template " + proto_nossl + " " + "X-Forwarded-FOR\n")
    vips_file.write("exit\n")
    vips_file.write("port " + "443" + " " + proto_ssl + '\n')
    vips_file.write("source-nat pool NAT-GROUP-1\n")
    vips_file.write("service-group " + "SG_" + content + "-443\n")
    vips_file.write("template tcp client-ip-header_tcp\n")
    vips_file.write("exit\n")
    vips_file.write("exit\n")
    vips_file.write(' ' + '\n')

def vip_builder(cfg, web_mig):
    content = content_extractor(cfg, web_mig)
    content_ssl = content + '-ssl'
    content = content_extractor(cfg, web_mig)
    if path.isfile("a10_vips.txt"):
        with open("a10_vips.txt", 'a') as vips_file:
            vips_writer(cfg, content, vips_file)
    else:
        with open("a10_vips.txt", 'w') as vips_file:
            vips_file.write('#========================================' + '\n')
            vips_file.write('#  VIP Configuration' + '\n')
            vips_file.write('#========================================' + '\n')
            vips_writer(cfg, content, vips_file)

def file_merger():
    with open('a10_services.txt') as srv_file:
        with open('a10_complete_config.txt', 'w') as configs:
            for line in srv_file:
                configs.write(line)
    with open('a10_group.txt') as grp_file:
        with open('a10_complete_config.txt', 'a') as configs:
            for line in grp_file:
                configs.write(line)
    with open('a10_vips.txt') as vips_file:
        with open('a10_complete_config.txt', 'a') as configs:
            for line in vips_file:
                configs.write(line)

def server_finder(parse, srv):
    all_content = parse.find_objects(r"^  content")
    srv_list = list()
    for obj in all_content:
        if obj.re_search_children(f"{srv} $"):
            web_name = obj.text
            web_name = web_name.strip(" ")
            web_name = web_name.replace("content ", "")
            srv_list.append(web_name)

    return srv_list

def ssl_list_filter(srv_list):
    for item in srv_list:
        if '-ssl' in item:
            srv_list.remove(item)

    return srv_list

def LOG_kp_cond_checker(cfg, web_mig):
    content = content_extractor(cfg, web_mig)
    with open("logs.txt", 'a') as lg:
        lg.write(f"CONVERTED: {web_mig}\n")
        for server in cfg[content]['service']:
            if cfg[content][server]['keepalive_type'] == 'http':
                if cfg[content][server]['keepalive_uri'] == "\"/keepalive.aspx\"":
                    lg.write(f'\tLOG: For {server}: Keepalive.aspx exists and valid\n')
                else:
                    lg.write(f'\tLOG: For {server}: Error please check the keepsalive parameters\n')
            else:
                lg.write(f'\tLOG: For {server}: Keepalive parameter does not exits\n')
        lg.write(' ' + '\n')

def delete_contents():
    if path.isfile('ping_list.txt'):
        remove('ping_list.txt')
    else: 
        pass
    if path.isfile('suspend_list.txt'):
        remove('suspend_list.txt')
    else:
        pass
    if path.isfile('a10_group.txt'):
        remove('a10_group.txt')
    else: 
        pass
    if path.isfile('a10_services.txt'):
        remove('a10_services.txt')
    else: 
        pass
    if path.isfile('a10_vips.txt'):
        remove('a10_vips.txt')
    else: 
        pass
    if path.isfile('logs.txt'):
        remove('logs.txt')
    else: 
        pass