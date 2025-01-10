from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    aws_lambda as _lambda
)
from constructs import Construct
import os

class InfraManageStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "InfraManageQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        """ lambda function for apis define """
        cwd = os.getcwd()
        infra_manage_function = _lambda.Function(
            self, 'InfraManageFunction',
            runtime=_lambda.Runtime.PYTHON_3_13,
            handler='lambda_function.handler',
            code=_lambda.Code.from_asset(os.path.join(cwd, "src/manage_infra_function")),
            # Customize the Lambda function name
            function_name='InfraManageFunction'
        )
