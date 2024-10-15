# `secrettoenv`

**`secrettoenv`** is a Python command-line tool that converts Kubernetes secrets into `.env` files for easier local development. It supports secret retrieval from both Kubernetes clusters and local files in JSON or YAML format.


## Features

- Converts Kubernetes secrets to `.env` files with key-value pairs.
- Supports secret files in JSON or YAML format.
- Can fetch secrets directly from a Kubernetes namespace using your local `kubectl` configuration.
- Customizable output file name and location for the generated `.env` file.


## Installation

You can install the package directly from [PyPI](https://pypi.org/project/secrettoenv/) using `pip`:

```bash
pip install secrettoenv
```

### Requirements

- **Python version:** 3.9 or higher
- **Dependencies:** The necessary dependencies (e.g., `click`, `kubernetes`) are automatically installed with `pip`.


## Usage

Once installed, you can use the `secrettoenv` command to convert a Kubernetes secret or a local file to an `.env` file.

### Basic Command:

```bash
secrettoenv --namespace <namespace> --secret-name <secret_name> --output-file <output_file>
secrettoenv --file <file_path> --output-file <output_file>
```

### Options:

- `--namespace`: Specifies the Kubernetes namespace where the secret resides. Default is `default`.
- `--secret-name`: The name of the Kubernetes secret.
- `--file`: The file containing Kubernetes secrets (supports JSON and YAML formats).
- `--output-file`: The output `.env` file name. Default is `env`.
- `--kube-config`: The path to your Kubernetes configuration file. Default is `~/.kube/config`.

### Example:

```bash
secrettoenv --namespace my-namespace --secret-name my-secret --output-file my-secrets.env
secrettoenv --file my_secret.json --output-file my-secrets.env
```

This command will generate a file `my-secrets.env` with secrets in key-value format from the specified Kubernetes secret.


## Development Setup

If you want to contribute or modify the code, you can set up the project locally using [Poetry](https://python-poetry.org/).

### Steps:

1. Clone the repository.
2. Install dependencies with Poetry:

   ```bash
   poetry install
   ```

3. Run the project using:

   ```bash
   poetry run secrettoenv --namespace <namespace> --secret-name <secret_name> --output-file <output_file>
   ```


## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.


## Future Enhancements

- Add support for additional secret formats.
- Provide more advanced error handling and validation.

