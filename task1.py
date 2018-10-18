import glob
import os
import random

def problem_1(folder_path):
   
    data_file_path = (folder_path + "/train/pos/", folder_path + "/test/pos/", folder_path + "/train/neg/", folder_path + "/test/neg/")
    
    pos_temp = open("pos_temp.txt", "w")
    neg_temp = open("neg_temp.txt", "w")
    pos_temp.close()
    neg_temp.close()

    datacount = 0

    for i in range(4):

        if i < 2:
            tempfile = open("pos_temp.txt", "a+")
        else:
            tempfile = open("neg_temp.txt", "a+")

        for datafile in glob.glob(os.path.join(data_file_path[i], '*.txt')):

            # Open train file
            data = open(datafile, "r")

            # Replace <br> tag with space
            content = data.read()
            content = content.replace("<br />", " ")
            content = content + "\r\n"

            # Get the rating
            temp = datafile.replace(".txt", "")
            rate = temp.split("_")
            content = rate[1] + "\t" + content

            # Copy to temp file
            tempfile.write(content)
            datacount += 1

            # Close train file
            data.close()

        # Close the temp file
        tempfile.close()
        
    print(datacount)

    # Preparing data
    train = open("train_data.txt", "w")
    test = open("test_data.txt", "w")

    # Combine pos data
    train_count = 0
    test_count = 0
    train_qouta = datacount/2*0.7
    test_qouta = datacount/2 - (datacount/2*0.7)

    with open("pos_temp.txt") as pos:
        for line in pos:
            if (random.randint(1,101) < 70 and train_count < train_qouta) or (test_count >= test_qouta):
                train.write(line)
                train_count += 1
            else:
                if test_count < test_qouta:
                    test.write(line)
                    test_count += 1

    # Combine neg data
    train_count = 0
    test_count = 0

    with open("neg_temp.txt") as neg:
        for line in neg:
            if (random.randint(1,101) < 70 and train_count < train_qouta) or (test_count >= test_qouta):
                train.write(line)
                train_count += 1
            else:
                if test_count < test_qouta:
                    test.write(line)
                    test_count += 1
    
# Main Program
folder_path = "aclImdb"
problem_1(folder_path)
print("hello world")
        