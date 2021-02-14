# Cisco-A10-LB-Converter
 Script to convert cisco load balancer config to A10 load balancer config

## Enabling Python Virtual Environment 
---
- This program needs the python virtual environment to be activated to add all the dependencies to run the program. 
 
- Navigate to the location of the script. 

- Run this command to activate the python virtual environment 

```console 
user@root:~$ source /parse_env/bin/activate
```

## Running the program
---

- To run the server searchable based Cisco to A10 converter run:

```console 
user@root:~$ python3 server_based_converter.py
```

- To run the content/website searchable based Cisco to A10 converter run:

```console 
user@root:~$ python3 cisco_a10_converter.py
```

- To create the json file of cisco configs run:

```console
user@root:~$ python3 cisco_json_converter.py
```

- To create a10 configs from the json file run:

```console
user@root:~$ python3 a10_cfg_builder.py
```

## Files created and their description
---
- *cfg.json*: json file of all attributes extracted from cisco config

- *a10_complete_config.txt* : complete a10 configs file

- *a10_groups.txt*: a10 groups configs

- *a10_services.txt*: a10 services configs

- *a10_vips.txt*: a10 virtual IPs configs

- *ping_list.txt*: list of public IPs to ping

- *suspend_list.txt*: cisco configs to suspend services

- *logs.txt*: log file with list of converted websites and keepsalive status

- *attribute_extractor.py*: backend methods for processing

- *server_based_converter.py*: server searchable configuration converter

- *cisco_a10_converter.py*: website/content searchable configuration builder

- *cisco_json_converter.py*: cisco to json converter based on website 

- *a10_cfg_builder.py*: json to A10 config builder based on website 




