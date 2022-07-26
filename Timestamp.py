import os
from exif import Image
from datetime import datetime, timedelta

directories = ["Input"]

for directory in directories:

    in_directory = directory + "/"
    out_directory = "Output/"

    for file in os.listdir(in_directory):

        with open(in_directory + file, "rb") as infile:
            img = Image(infile)

        fake_datetime = datetime.strptime(img.datetime_original, "%Y:%m:%d %H:%M:%S")
        mid1_datetime = fake_datetime + timedelta(days=1629)
        mid2_datetime = mid1_datetime + timedelta(hours=17)

        real_datetime = mid2_datetime.strftime("%Y:%m:%d %H:%M:%S")

        print(real_datetime)

        img.datetime = real_datetime
        img.datetime_original = real_datetime
        img.datetime_digitized = real_datetime

        with open(out_directory + file, "wb") as outfile:
            outfile.write(img.get_file())