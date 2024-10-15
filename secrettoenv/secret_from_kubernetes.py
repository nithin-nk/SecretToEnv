import base64

from kubernetes import client, config


def get_kubernetes_secret(namespace: str, secret_name: str, kube_config: str) -> dict:
    """
    Retrieve the secret from Kubernetes using the K8 APIs
    Returns the decoded values of key value payers of the given secret
    """
    try:
        config.load_kube_config(config_file=kube_config)
    except Exception as e:
        print(f"Kube config file not found in '{kube_config}' - {e}")
        return
    v1 = client.CoreV1Api()
    output = {}

    try:
        secret = v1.read_namespaced_secret(secret_name, namespace)
        for key, value in secret.data.items():
            output[key] = base64.b64decode(value).decode("utf-8")
        return output
    except client.ApiException as e:
        if e.status == 404:
            print(f"Secret '{secret_name}' not found in the namespace '{namespace}'")
        else:
            print(f"Error occurred: {e}")


if __name__ == "__main__":
    get_kubernetes_secret("default", "my-secret", "~/.kube/config")
