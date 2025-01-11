import boto3
from botocore.exceptions import BotoCoreError, ClientError

rds_client = boto3.client('rds')

def start_rds_instance(rds_identifier:str)->dict:
    try:
        response = rds_client.start_db_instance(DBInstanceIdentifier=rds_identifier)
        print("start",response)
        print(f"db instance {rds_identifier} start successfully.")
        return {"code":200,"status":"success","result":response}
    except ClientError as e:
        print(f"{rds_identifier} start error as ClientError.{e}")
        return {"code":400,"status":"success","result":f"{e}"}
    except BotoCoreError as e:
        print(f"{rds_identifier} start error as BotoCoreError.{e}")
        return {"code":400,"status":"error","result":f"{e}"}
    
def stop_rds_instance(rds_identifier:str)->dict:
    try:
        response = rds_client.stop_dbstop_db_instance(DBInstanceIdentifier=rds_identifier)
        print("start",response)
        print(f"db instance {rds_identifier} stop successfully.")
        return {"code":200,"status":"success","result":response}
    except ClientError as e:
        print(f"{rds_identifier} stop error as ClientError.{e}")
        return {"code":400,"status":"error","result":f"{e}"}
    except BotoCoreError as e:
        print(f"{rds_identifier} stop error as BotoCoreError.{e}")
        return {"code":400,"status":"error","result":f"{e}"}

       