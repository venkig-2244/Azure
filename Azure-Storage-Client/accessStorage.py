import os, uuid
from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import random

try:
    print("Azure Blob Storage Python quickstart sample")
  

    # Quickstart code goes here
    connect_string = "DefaultEndpointsProtocol=https;AccountName=venkystorage204;AccountKey=EgukhIZZ+WUgimDbtCNMt3vaxfeqlQd8pvd7AmdN+nECRezmh6/2TrhbF4i/1BPQTdjfcK+bre+t+AStfGY1qw==;EndpointSuffix=core.windows.net"

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(connect_string)

    # Create a unique name for the container
    container_name = "picsofvenky" #str(uuid.uuid4())

    # Create the container
    #container_client = blob_service_client.create_container(container_name)
    #dir(blob_service_client)

    # Create a blob client using the local file name as the name for the blob
    blob_file_name = "ICSE-Class-9-English-Sample-Paper-1.pdf"
    local_file_name = "C:\\Users\\itsve\\Downloads\\ICSE-Class-9-English-Sample-Paper-1.pdf"
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_file_name)

    # print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

    # Upload the created file
    # with open(file=local_file_name, mode="rb") as data:
    #     blob_client.upload_blob(data)
    container = blob_service_client.get_container_client(container_name)
    blob_client_dst = blob_service_client.get_blob_client(container="backuppics", blob="backup-"+str(random.randrange(1,1000))+".pdf")

    blob_list = container.list_blobs()
    for blob in blob_list:
        print(blob.name)

    blob_client_dst.start_copy_from_url(blob_client.url)
    print(blob_client_dst.get_blob_properties())

except Exception as ex:
    print('Exception:')
    print(ex)
