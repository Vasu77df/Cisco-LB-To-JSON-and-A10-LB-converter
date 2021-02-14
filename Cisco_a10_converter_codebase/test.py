def file_merger():
    with open('a10_group.txt') as grp_file:
        with open('a10_complete_config.txt', 'w') as configs:
            for line in grp_file:
                configs.write(line)
    with open('a10_services.txt') as srv_file:
        with open('a10_complete_config.txt', 'a') as configs:
            for line in srv_file:
                configs.write(line)
    with open('a10_vips.txt') as vips_file:
        with open('a10_complete_config.txt', 'a') as configs:
            for line in vips_file:
                configs.write(line)


if __name__ == "__name__":
    file_merger()