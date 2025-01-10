import logging,json
from build_response import buildResponse
from services.ec2_manage import start_instance,stop_instance

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    print("event",event)
    if event["action"] == "start":
        result = {}
        if event["ec2Instannce"] is not None:
            instance = event["ec2Instannce"]
            ec2_resp = start_instance(instance)
            result ={**result,"ec2Result":ec2_resp}
        if event["rdsInstance"] is not None:
            rds_resp = event["rdsInstance"]
            result ={**result,"rdsResult":rds_resp}
        print("final_result",result)
        return buildResponse(200,{"status":"success","result":result,"message":"start event success"})
    elif event["action"] == "stop": 
        result = {}
        if event["ec2Instannce"] is not None:
            instance = event["ec2Instannce"]
            ec2_resp = stop_instance(instance)
            result ={**result,"ec2Result":ec2_resp}
        if event["rdsInstance"] is not None:
            rds_resp = event["rdsInstance"]
            result ={**result,"rdsResult":rds_resp}
        print("final_result",result)
        return buildResponse(200,{"status":"success","result":result,"message":"stop event success"})
    return buildResponse(200,{"status":"success","message":"Out of event!"})