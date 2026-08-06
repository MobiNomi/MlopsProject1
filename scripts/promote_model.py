import os
import mlflow
from mlflow.tracking import MlflowClient


def promote_model():
    """Promote the latest 'Staging' model version to 'Production'."""

    # Same production-use authentication pattern as your other scripts
    dagshub_token = os.getenv("CAPSTONE_TEST")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "MobiNomi"
    repo_name = "MlopsProject1"
    mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

    client = MlflowClient()
    model_name = "my_model"

    # Find the current Staging version
    staging_versions = client.get_latest_versions(model_name, stages=["Staging"])
    if not staging_versions:
        raise Exception(f"No model version found in 'Staging' for '{model_name}'")

    latest_version = staging_versions[0].version

    # Archive whatever is currently in Production (if anything),
    # so there's only ever one active Production version
    current_production = client.get_latest_versions(model_name, stages=["Production"])
    for version in current_production:
        client.transition_model_version_stage(
            name=model_name,
            version=version.version,
            stage="Archived"
        )
        print(f"Archived old Production version {version.version}")

    # Promote the Staging version to Production
    client.transition_model_version_stage(
        name=model_name,
        version=latest_version,
        stage="Production"
    )
    print(f"Promoted model version {latest_version} to Production")


if __name__ == "__main__":
    promote_model()