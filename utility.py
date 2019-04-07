import csv
import random


def write_dict(d, write_loc, col_header=[]):
    with open(write_loc, "w", newline="") as guy:
        writer = csv.writer(guy)
        if col_header != [] and len(col_header) == 2:
            writer.writerow([col_header[0], col_header[1]])
        for k in d:
            writer.writerow([k, d[k]])


def write_lists(lists, write_loc):
    with open(write_loc, "w", newline="") as guy:
        writer = csv.writer(guy)
        writer.writerows(lists)


def read_csv(filename, contains_header=False):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        if contains_header:
            next(reader)

        list_out = []
        for row in reader:
            list_out.append(row)

        return list_out




def map_(df, key, val):
    d = {}
    for row in df:
        k, v = row[key], row[val]
        if v != "":
            d[k] = v
    return d


def print_df(df):
    for row in df:
        print(row)


def head(df):
    for x in range(0, 100):
        print(df[x])


def construct_list(d,df,key,val):
    for key in d:
        df.append(key)


def map_force_val(df, key, forced_val):
    d = {}
    for row in df:
        k = row[key]
        d[k] = forced_val
    return d

def new_list(dict,list):
    for k in dict.keys():
        list.append(k)

    return list

def CountFrequency(dict):

    freq = {}
    for item in dict:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print("% d : % d"%(key, value))

    return freq


def RandTaxa(dict, list):
    randtaxa= {}
    for item in dict:
        if item != 1:
            for k in list:
                rand_index = list[random.randint(0,2)]
            randtaxa[item] = rand_index

        else:
            randtaxa[item] = item

    return randtaxa







