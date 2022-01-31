# import csv


def read_image_pair(base, row):
    if len(row) == 3:
        # same
        return [load_image(base, row[0], row[1]), load_image(base, row[0], row[2])]
    else:
        # different
        return [load_image(base, row[0], row[1]), load_image(base, row[2], row[3])]


def load_image(base, name, number):
    filename = "{0}/{1}/{1}_{2:04d}.txt".format(base, name, int(number))
    # "base/name/name_0004.txt"
    with open(filename, 'r') as f:
        img = f.read()
        f.close()
    return img


def assign_label(row):
    if len(row) == 3:
        # same
        return 1
    else:
        # different
        return 0

# def customize_data(base, out_directory):
#     with open("pairsDevTrain.txt") as train:
#         train_rows = list(csv.reader(train, delimiter=))

