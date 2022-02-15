
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# rpc_user and rpc_password are set in the litecoin.conf file
rpc_user = 'user'
rpc_password = 'password'

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:9332"%(rpc_user, rpc_password))

"""
this is the command format we are looking for.
rpc_connection.omni_sendissuancefixed("MTkjLJokhESbiTvxhtHPpkRG6XUyCjyM4o", 1, 1, 0, "d1", "d2", "name", "d3", "d4", "1")
"""