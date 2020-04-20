import json
from core import settings

def server_deal_disconnect(self, *args):
    cmd_dic = args[0]
    print("need to close the connection")
