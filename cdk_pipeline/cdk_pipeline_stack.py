# from constructs import Construct
# from aws_cdk import (
#     Duration,
#     Stack,
#     aws_iam as iam,
#     aws_sqs as sqs,
#     aws_sns as sns,
#     aws_sns_subscriptions as subs,
# )


# class CdkPipelineStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)

#         queue = sqs.Queue(
#             self, "CdkPipelineQueue",
#             visibility_timeout=Duration.seconds(300),
#         )

#         topic = sns.Topic(
#             self, "CdkPipelineTopic"
#         )

#         topic.add_subscription(subs.SqsSubscription(queue))

import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     Stack,
                     aws_lambda as awslambda
                     )

import aws_cdk.aws_lambda_python_alpha as lambda_

class AwsCdkPythonDevcontainerMainStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # bucket = s3.Bucket(self, "TestNikhita667")

        handler = lambda_.PythonFunction(self, "TestLambdaPipeline",
                    entry="cdk_pipeline/lambda",
                    index="main.py",
                    handler="lambda_handler",
                    function_name="TestLambdaPipeline",
                    runtime=awslambda.Runtime.PYTHON_3_7,
                    timeout=cdk.Duration.seconds(300),
                    environment={"ENV": "dev"}
                    )


