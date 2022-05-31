import aws_cdk as cdk
from constructs import Construct
from cdk_pipeline.cdk_pipeline_stack import AwsCdkPythonDevcontainerMainStack

class MyPipelineAppStage(cdk.Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambdaStack = AwsCdkPythonDevcontainerMainStack(self, "LambdaStack")
