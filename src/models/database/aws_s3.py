import os
import time
import boto3
import logging
import pandas as pd
from typing import Union, Optional
from botocore.exceptions import ClientError


class S3Bucket:
    """
    | Methods for reading and writing files to S3
    """

    def __init__(self,
                 bucket_name: str):
        self.bucket_name = bucket_name
        self.client = boto3.client('s3',
                                   aws_access_key_id="AKIA5RO4IS2EOVLSGRTP",
                                   aws_secret_access_key="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",
                                   region_name='us-east-1')

    def save_to_s3(self,
                   file_name: str,
                   src_data: Union[pd.DataFrame, str, bytes, bytearray],
                   overwrite: bool = True):

        df_type = os.path.splitext(file_name)[1]

        # Serialize dataframe
        if isinstance(src_data, pd.DataFrame):
            if df_type == '.csv':
                src_data = src_data.to_csv(index=False)
            elif df_type == '.json':
                src_data = src_data.to_json(orient='records')

        # Write the file, trying 3 times with exponential backoff
        write_success = False
        n_iter = 0

        while write_success is False and n_iter < 3:
            try:
                self.client.put_object(Bucket=self.bucket_name, Key=file_name, Body=src_data)
                write_success = True
            except ClientError as e:
                time.sleep(4 ** n_iter)
                n_iter += 1
                logging.warning(e)
                logging.warning("S3Bucket failed to write data; trying again.")

        if write_success:
            return True
        else:
            return False
