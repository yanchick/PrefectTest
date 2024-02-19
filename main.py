from prefect import flow


@flow
def get_repo_info():
    print("Hello world")

if __name__ == "__main__":
    get_repo_info()