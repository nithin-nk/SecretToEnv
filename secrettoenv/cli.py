import click

from .secret_from_file import get_secrets_from_json_file, get_secrets_from_yaml_file
from .secret_from_kubernetes import get_kubernetes_secret


@click.command()
@click.option(
    "--namespace",
    default="default",
    help="Kubernetes namespace where your secret resides, default namespace is 'default'",
)
@click.option("--secret-name", help="Kubernetes secret name")
@click.option("--file", help="File which contain the Kubernetes secret, supports JSON or YAML files")
@click.option("--output-file", default="env", help="Output file for .env format, default name is env")
@click.option(
    "--kube-config",
    default="~/.kube/config",
    help="Location of the kube config file, by default it will take ~/.kube/config",
)
def convert(namespace, secret_name, file, output_file, kube_config):
    """
    Convert Kubernetes secret file to .env file with secrets as key value pairs
    Output: env file on a specified location, can override the env file name.
    """
    output = dict()
    if file:
        if file.lower().endswith(".json"):
            output = get_secrets_from_json_file(file)
        elif file.lower().endswith(".yml") or file.lower().endswith(".yaml"):
            output = get_secrets_from_yaml_file(file)
        else:
            print("Invalid file type, supports .yaml, .yml or .json")
    elif namespace and secret_name:
        output = get_kubernetes_secret(namespace=namespace, secret_name=secret_name, kube_config=kube_config)
    else:
        print(
            "You should provide secret name and namespace or the file name which contains the secret to generate the env file"
        )
    if output:
        with open(output_file, "w", encoding="utf-8") as fp:
            for key, value in output.items():
                fp.write(f"{key}={value}\n")
        print(f"Output env file generated at {output_file}")
