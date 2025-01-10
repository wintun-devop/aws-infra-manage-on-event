import logging,json
from build_response import buildResponse

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    print("ev",event)
    return buildResponse(200,{"status":"success","message":"Out of event!"})