#!/usr/bin/env python3
import io
from aws_cdk import core

from mwaa_cdk.mwaa_cdk_backend import MwaaCdkStackBackend
from mwaa_cdk.mwaa_cdk_env import MwaaCdkStackEnv

env_EU=core.Environment(region="eu-central-1", account="754398815384")
mwaa_props = {'dagss3location': 'airflow-cdk-demo-09349084459','mwaa_env' : 'mwaa-cdk-demo3434'}

app = core.App()

mwaa_backend = MwaaCdkStackBackend(
    scope=app,
    id="MWAA-Backend",
    env=env_EU,
    mwaa_props=mwaa_props
)

mwaa_env = MwaaCdkStackEnv(
    scope=app,
    id="MWAA-Environment",
    vpc=mwaa_backend.vpc,
    env=env_EU,
    mwaa_props=mwaa_props
)

app.synth()
