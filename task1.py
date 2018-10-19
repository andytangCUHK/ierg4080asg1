# 1. Data Preparation
# 1.1 
#
# Prepare a full dataset by combining all the training and test data found in the downloaded raw data
# The full dataset is stored in the root as "combined"

import glob
import os
import pandas as pd
import re
from sklearn.model_selection import train_test_split

folder_path="aclImdb"
data_file_path = (folder_path + "/train/pos/", folder_path + "/test/pos/", folder_path + "/train/neg/", folder_path + "/test/neg/")

combined = open("combined", "w")
datacount = 0

for i in range(4):
    rate = "0"
    if i < 2:
        rate = "1"

    for datafile in glob.glob(os.path.join(data_file_path[i], '*.txt')):

        # Open train file
        data = open(datafile, "r")

        # String Preprocess
        content = data.read()
        content = content.replace("<br />", " ")
        content = content.replace("\t", " ")
        content = re.sub('[!@#$%^&*:<>,.\'\"()]', '', content)
        content = re.sub(' +', ' ', content)
        content = content + "\r\n"

        # Get the rating
        #temp = datafile.replace(".txt", "")
        #rate = temp.split("_")
        content = rate + "\t" + content

        # Copy to combined file
        combined.write(content)
        datacount += 1

        # Close train file
        data.close()

# Close the combined file
combined.close()

# 1.2 & 1.3
#
# Randomly split the full dataset into a training set with 70% of the data, and a test set with 30% of the data
# Check that the ratio of positive to negative reviews is roughly 1:1 in both the training and test set

import pandas as pd
from sklearn.model_selection import train_test_split

# Read the data into a dataframe
df = pd.read_csv("combined", sep="\t", header=None)
df.shape
df.columns = ["label", "text"]

# Extract the training data
X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y, random_state=100)
