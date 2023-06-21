# azure-scripts
This repository is a collection of scripts using the Azure SDK for Python.

## Getting Started
Begin by installing the necessary Python packages found in `Pipfile` using `pipenv install`.

## Setup your .env
`AZURE_STORAGE_CONNECTION_STRING` is the connection string for the Azure storage account. This value can be found in the Azure portal under `Home > Storage accounts > YOUR_STORAGE_ACCOUNT_NAME > Access keys`. 

`AZURE_CONTAINER_NAME` is the name of the Azure container you are using.

`SUBDIRECTORY_PATH` is the subdirectory that you want to start at in the Azure container (optional).

`OUTPUT_FILE` is the name of the file that the script will be outputting to.

## name_and_size.py
This script will list and create an output file containing the name and size (in bytes) of all blobs in a given container.

To list all blobs in the `digital-preservation` container, set `AZURE_CONTAINER_NAME=digital-preservation`.

If the blobs you want to list are located in a subdirectory of the container, set `SUBDIRECTORY_PATH`.

For example, to list all blobs found in the `REC0040_1940sTaxPhotos/1_Manhattan` subdirectory of the `digital-preservation` container, set `SUBDIRECTORY_PATH=REC0040_1940sTaxPhotos/1_Manhattan/`.

Run this script with `pipenv run python name_and_size.py`

