from google.cloud import storage
from datetime import datetime
import shutil

BUCKET_NAME = 'jasonkuan_minecraft_world_backup'
WORLD_MAP_PATH = '/home/jasonkuan2020/minecraft/world'


def main():
    shutil.make_archive('world_backup', 'zip', WORLD_MAP_PATH)

    backup_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    output_filename = f'{backup_date}_jkmc.zip'

    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(output_filename)

    blob.upload_from_filename('world_backup.zip')

    print(f"File {output_filename} uploaded to {BUCKET_NAME}.")


if __name__ == '__main__':
    main()
