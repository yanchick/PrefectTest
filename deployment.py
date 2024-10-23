from prefect.deployments import Deployment
from prefect.filesystems import GitHub
from main import get_repo_info

# Настройка GitHub хранилища
github_storage = GitHub(
    repository="yanchick/PrefectTest",
    reference="main",
    path="main.py"
)

# Создание деплоймента
deployment = Deployment.build_from_flow(
    flow=get_repo_info,
    name="my-flow-deployment",    
    work_queue_name="default",
    storage=github_storage
)

if __name__ == "__main__":
    deployment.apply()
