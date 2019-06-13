import urllib.request
import json
import urllib.parse

username = "admin"
password = "admin123"
top_level_url = "http://dev.ufotosoft.com:15672/api"
url_get_connections = "http://dev.ufotosoft.com:15672/api/connections"
url_base_client_conn = "http://dev.ufotosoft.com:15672/api/connections"
target_client_host = '192.168.62.80'

ps_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
ps_mgr.add_password(None, top_level_url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(ps_mgr)
opener = urllib.request.build_opener(handler)

# query all connections
response = opener.open(url_get_connections)
result = json.load(response)

print('all connections: \n', result)

# filter target connections
store_list = []
for item in result:
    if item['peer_host'] == target_client_host:
        store_list.append(item)

print("filtered connections: \n", store_list)



def build_target_url(conn):
    client_conn_name = "" + conn['name']
    print("target connection name: \n" + client_conn_name)
    encoded_client_conn_name = urllib.parse.quote(client_conn_name)
    url_client_conn = url_base_client_conn + "/" + encoded_client_conn_name
    print("target url: \n", url_client_conn)
    return url_client_conn

def view_conn(conn):
    # view the conn
    url_client_conn = build_target_url(conn)

    resp = opener.open(url_client_conn)
    rst = json.load(resp)
    print(rst)
    return

def delete_conn(conn):
    url_client_conn = build_target_url(conn)

    # delete the conn
    del_req = urllib.request.Request(url_client_conn, method="DELETE")
    result_del =opener.open(del_req)
    print(result_del)
    return


def del_first_target(store_list):
    item = store_list[0]
    print(item)
    view_conn(item)
    delete_conn(item)

def del_all_targets(store_list):
    for item in store_list:
        print(item)
        view_conn(item)
        delete_conn(item)

del_all_targets(store_list)