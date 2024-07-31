import io
import requests
import boto3
from urllib.parse import urlparse
import zipfile

# DONT NEED THIS
def download(url):
    parsed_url = urlparse(url)
    
    if parsed_url.scheme == 's3':
        s3 = boto3.client('s3')
        bucket_name = parsed_url.netloc
        object_key = parsed_url.path.lstrip('/')
        
        # Download the S3 object
        s3_object = s3.get_object(Bucket=bucket_name, Key=object_key)
        zip_content = s3_object['Body'].read()
    else:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        zip_content = response.content
    
    return io.BytesIO(zip_content)

def extract_txt(zip_content: io.BytesIO, txt_filename: str = 'requirements.txt'):
    def get_depth(filepath):
        return filepath.count('/') + (1 if filepath.endswith('/') else 0)

    with zipfile.ZipFile(zip_content) as the_zip:
        for file in the_zip.namelist():
            print(file)
            if file.endswith(txt_filename) and get_depth(file) <= 1:
                with the_zip.open(file) as txt_file:
                    txt_content = txt_file.read().decode('utf-8')
                return txt_content
        
        raise FileNotFoundError(f"The file '{txt_filename}' was not found within 1-2 levels of directory depth in the zip archive")

def requirements_txt_to_list(requirements_str: str):
    return [line for line in requirements_str.splitlines() if line.strip()]
