import urllib
import pandas
import os.path
import zipfile
import tempfile


DATA_URL = 'http://www5.cde.ca.gov/caasppresearchfiles/2015/ca2015_all_csv_v1.zip'
FILE_NAME = 'ca2015_all_csv_v1.txt'


def download_data(target_dir):
    """
    Get the file from the internet

    :param target_path: Local path for storing the file.
    :return:
    """
    download_file = os.path.join(target_dir, 'download.zip')
    urllib.urlretrieve(DATA_URL, download_file)
    zip_handler = zipfile.ZipFile(download_file)
    zip_handler.extractall(path=target_dir)


def run():
    """
    Run the entire process
    :return:
    """

    target_dir = tempfile.mkdtemp()
    download_data(target_dir=target_dir)
    csv_file = os.path.join(target_dir, FILE_NAME)
    df = pandas.DataFrame.from_csv(path=csv_file)

    print(df)


if __name__=='__main__':
    run()