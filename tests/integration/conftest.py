"""Integration tests conftest."""

from collections import namedtuple
import os

from boto3facade.exceptions import AwsError
from humilis.environment import Environment
import pytest


@pytest.fixture(scope="session")
def settings():
    """Global test settings."""
    Settings = namedtuple('Settings', 'stage environment_path output_path')
    envfile = "tests/integration/humilis-asg"
    stage = os.environ.get("STAGE", "DEV")
    return Settings(
        stage=stage,
        environment_path="{}.yaml.j2".format(envfile),
        output_path="{}-{}.outputs.yaml".format(envfile, stage))


@pytest.yield_fixture(scope="session")
def environment(settings):
    """The test environment: this fixtures creates it and takes care of
    removing it after tests have run."""
    env = Environment(settings.environment_path, stage=settings.stage)

    if os.environ.get("UPDATE", "yes") == "yes":
        env.create(update=True, output_file=settings.output_path)
    else:
        env.create(output_file=settings.output_path)
    yield env
    if os.environ.get("DESTROY", "no").lower() == "yes":
        bucket = env.outputs["asg"]["BucketName"]
        empty_bucket(bucket)
        try:
            env.delete()
        except AwsError as err:
            # Some files may have arrived to the bucket after the bucket was 
            # emptied for the first time.
            empty_bucket(bucket)
            env.delete()


def empty_bucket(bucket):
    """Empties a S3 bucket."""
    subprocess.call(["aws", "s3", "rm", "s3://{}/".format(bucket),
                    "--recursive"], stdout=subprocess.PIPE)


