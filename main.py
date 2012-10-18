import os
import shutil
import boto
from boto.s3.key import Key


class Main():
    def __init__(self):
        self.conn = boto.connect_s3()

    def run(self):
        bucket = self.conn.create_bucket("simpsons-backup")
        prefix = "20121014-000003"
        delimiter = "/"
        names = [
            "11210700833817781261712743431165789982",
            "11560959747817079145534931294571682254",
            "11612852994953413294466149974764415485",
        ]

        self.get_files(bucket, names, prefix=prefix, delimiter=delimiter)

    def exists(self, bucket, name):
        key = Key(bucket=bucket, name=name)
        return key.exists()

    def get_files(self, bucket, names, prefix=None, delimiter=None, directory='down', replace_directory=True):

        if replace_directory:
            if os.path.exists(directory):
                shutil.rmtree(directory)

        if not os.path.exists(directory):
            os.makedirs(directory)

        for name in names:
            file = open(directory + '/' + name, 'w')
            if prefix and delimiter:
                key = Key(bucket=bucket, name=prefix + delimiter + name)
            else:
                key = Key(bucket=bucket, name=name)
            key.get_file(file)
            file.close()


if __name__ == "__main__":
    Main().run()
