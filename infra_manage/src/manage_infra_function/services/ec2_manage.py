import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

session = boto3.Session()

ec2 = session.resource('ec2')


def start_instance(instance_id:str)->dict:
    try:
        instance = ec2.Instance(instance_id) 
        response = instance.start()
        print("start",response)
        print(f"instance {instance_id} start successfully.")
        return {"code":200,"status":"success","result":response}
    except NoCredentialsError as e:
        print("NoCredentialsError",e)
        return {"code":401,"status":"error","result":None}
    except PartialCredentialsError as e:
         print("PartialCredentialsError",e)
         return {"code":401,"status":"error","result":None}
    except ClientError as e:
         print("ClientError",e)
         return {"code":401,"status":"error","result":None}
    
def stop_instance(instance_id:str)->dict:
    try:
        instance = ec2.Instance(instance_id) 
        response = instance.stop()
        print("stop",response)
        print(f"instance {instance_id} stop successfully.")
        return {"code":200,"status":"success","result":response}
    except NoCredentialsError as e:
        print("NoCredentialsError",e)
        return {"code":401,"status":"error","result":None}
    except PartialCredentialsError as e:
         print("PartialCredentialsError",e)
         return {"code":401,"status":"error","result":None}
    except ClientError as e:
         print("ClientError",e)
         return {"code":401,"status":"error","result":None}
    
