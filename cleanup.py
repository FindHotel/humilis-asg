#!/usr/bin/env python

import os
import sys

from humilis.environment import Environment
import yaml


def empty_bucket(bucket):
    """Empty a specific bucket."""

    print("Emptying bucket {} ...".format(bucket))
    os.system("aws s3 rm s3://{} --recursive".format(bucket))
    print("Bucket {} has been emptied".format(bucket))


def produce_environment(envpath, stage, parameters=None):
    """Produce humilis environment object."""
    if parameters:
        with open(parameters, "r") as f:
            parameters = yaml.load(f.read())
            stage_params = parameters.get(stage, {})
            stage_params["_default"] = parameters.get("_default", {})
    else:
        stage_params = {}

    return Environment(envpath, stage=stage, parameters=stage_params)


def empty_all_buckets(env):
    """Empty all buckets associated with the environment."""
    for layer in env.outputs.values():
        buckets = [v for k, v in layer.items()
                   if k in ["Bucket", "BucketName"]]
        for bucket in buckets:
            empty_bucket(bucket)


if __name__ == "__main__":
    env = produce_environment(*sys.argv[1:])
    try:
        empty_all_buckets(env)
        env.delete()
    except:
        empty_all_buckets(env)
        env.delete()
