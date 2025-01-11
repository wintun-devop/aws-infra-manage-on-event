import logging,json
from build_response import buildResponse
from services.ec2_manage import start_instance,stop_instance
from services.rds_manage import start_rds_instance,stop_rds_instance

# Python Logging Service
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    print("event",event)
    if event["action"] == "start":
        result = {}
        if event["ec2Instannce"] is not None:
            ec2_resp = start_instance(event["ec2Instannce"])
            result ={**result,"ec2Result":ec2_resp}
        if event["rdsInstance"] is not None:
            rds_resp = start_rds_instance(event["rdsInstance"])
            result ={**result,"rdsResult":rds_resp}
        print("final_result",result)
        return buildResponse(200,{"status":"success","result":result,"message":"start event success"})
    elif event["action"] == "stop": 
        result = {}
        if event["ec2Instannce"] is not None:
            ec2_resp = stop_instance(event["ec2Instannce"])
            result ={**result,"ec2Result":ec2_resp}
        if event["rdsInstance"] is not None:
            rds_resp = stop_rds_instance(event["rdsInstance"])
            result ={**result,"rdsResult":rds_resp}
        print("final_result",result)
        return buildResponse(200,{"status":"success","result":result,"message":"stop event success"})
    return buildResponse(200,{"status":"success","message":"Out of event!"})