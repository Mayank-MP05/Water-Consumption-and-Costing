
from constant import DEBUG_MODE

def debug(*args):
    if(DEBUG_MODE):
        print(*args)