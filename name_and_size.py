import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
dotenv_path = os.path.join(basedir, '.env')
load_dotenv(dotenv_path)

try:
    connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client(os.getenv('AZURE_CONTAINER_NAME'))
    file = open(os.getenv('OUTPUT_FILE'), "a")
    blob_list = container_client.list_blobs() if not os.getenv('SUBDIRECTORY_PATH') else container_client.list_blobs(name_starts_with=os.getenv('SUBDIRECTORY_PATH'))
    for blob in blob_list:
        blob_name = blob.name.split('/')[-1]
        line = blob_name + ', ' + str(blob.size) + '\n'
        print(line)
        file.write(line)
    file.close()
except Exception as ex:
    print('Exception:')
    print(ex)

