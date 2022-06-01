# from constructs import Construct
# from aws_cdk import (
#     Stack
# )
# from pipeline_stage import WorkshopPipelineStage

# class WorkshopPipelineStack(Stack):

#     def __init__(self, scope: Construct, id: str, **kwargs) -> None:
#         super().__init__(scope, id, **kwargs)

#         # Pipeline code will go here


import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep, CodeBuildOptions
from cdk_pipeline.pipeline_app_stage import MyPipelineAppStage
import aws_cdk.aws_codebuild as codebuild
# from aws_cdk.pipelines import ManualApprovalStep

class CdkPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline", 
                        pipeline_name="CdkPipeline",
                        synth=ShellStep("Synth", 
                            input=CodePipelineSource.git_hub("NikhitaBusa/cdk_pipeline", "master"),
                            commands=["npm install -g aws-cdk",
                                "python -m pip install -r requirements.txt",
                                "cdk synth"]),
                        code_build_defaults=CodeBuildOptions(build_environment=codebuild.BuildEnvironment(privileged=True))
                        # environment=codebuild.BuildEnvironment(privileged=True)
                        )

        testing_stage = pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account="246213974221", region="us-west-2")))

        # testing_stage.add_post(ManualApprovalStep('approval'))
