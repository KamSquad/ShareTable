import os

from lib import config

conf = config.JsonConfig('config.json')
server_args = conf.value['server_args']
root_path = conf.value['table_folder_path']
cmd_str = f'./bin/http-server {server_args} {root_path}'


if __name__ == '__main__':
    os.system(cmd_str)
