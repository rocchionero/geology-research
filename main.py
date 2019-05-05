from utility import *
import pandas as pd
import matplotlib.pylab as plt
from scipy.spatial import distance


def main():
    taxon_file = "data/biv.csv"
    taxon = read_csv(taxon_file, False)

    read_biv = read_csv("data/biv.csv", True)
    biv_dict = map_(read_biv, 5, 13)
    for k in biv_dict:
        print(k + " -> \"" + biv_dict[k] + "\"")
    write_dict(biv_dict, "data/biv_dict.csv", col_header=["genus", "higher_taxon"])

    read_gast = read_csv("data/gast.csv", True)
    gast_dict = map_force_val(read_gast, 5, "Gastropod")
    for k in gast_dict:
        print(k + " -> \"" + gast_dict[k] + "\"")
    write_dict(gast_dict, "data/gast_dict.csv", col_header=["genus", "higher_taxon"])

    read_brach = read_csv("data/brach.csv", True)
    brach_dict = map_force_val(read_brach, 5, "Brachiopod")
    for k in brach_dict:
        print(k + "-> \"" + brach_dict[k] + "\"")
    write_dict(brach_dict, "data/brach_dict.csv", col_header=["genus", "higher_taxon"])

    biv_list = list(biv_dict.keys())
    gast_list = list(gast_dict.keys())
    brach_list = list(brach_dict.keys())
    genus_space = list(set(biv_list + gast_list + brach_list))

    mat = [["genus", "biv", "gast", "brach"]]
    for genus in genus_space:
        corr = [genus, 0, 0, 0]
        if genus in biv_list:
            corr[1] = 1
        if genus in gast_list:
            corr[2] = 1
        if genus in brach_list:
            corr[3] = 1
        mat.append(corr)

    mat = [list(x) for x in zip(*mat)]
    heading = mat[0]
    mat = mat[1:]
    mat_over = [list(x) for x in zip(*mat)][1:]
    mat_under = [list(x) for x in zip(*mat_over)]
    over = pd.DataFrame(data=mat_over)
    # under = pd.DataFrame(data=mat_under)
    coocc = over.T.dot(over)
    print(coocc)

    coocc.to_csv("data/coocc.csv")

    df = pd.DataFrame(data=mat[1:], columns=mat[0])
    print(df)
    df.to_csv("data/df.csv")

    df_t = df.T
    print(df_t.corr())
    df_t.to_csv("data/df_t.csv")

    df_brach = pd.read_csv("data/brach.csv")
    brach_collect = df_brach.collection_no
    brach_collect_freq = CountFrequency(brach_collect)
    sorted_brach = sorted(brach_collect_freq.items(), key=lambda kv: -kv[1])
    print(sorted_brach)

    y, x = zip(*sorted_brach)
    plt.plot(y, x)
    plt.show()

    df_biv = pd.read_csv("data/biv.csv")
    biv_collect = df_biv.collection_no
    biv_collect_freq = CountFrequency(biv_collect)
    sorted_biv = sorted(biv_collect_freq.items(), key=lambda kv: - kv[1])
    print(sorted_biv)

    df_gast = pd.read_csv("data/gast.csv")
    gast_collect = df_gast.collection_no
    gast_collect_freq = CountFrequency(gast_collect)
    sorted_gast = sorted(gast_collect_freq.items(), key=lambda kv: -kv[1])
    print(sorted_gast)

    taxon_list = ["brachipod", "gastropod", "bivalve"]

    randsite_dict = RandTaxa(sorted_brach, taxon_list)
    print(randsite_dict)

    # print("(gastro, bivalve, brachipod):= " + str(_gastropod) + ", " + str(_bivalve) + ", " + str(_brachipod))

    lat1 = 52.2296756
    lon1 = 21.0122287
    lat2 = 52.406374
    lon2 = 16.9251681

    count = 0
    average_list = []
    dist_list = []
    while count < 100:
        dist = geodistance(lat1, lon1, lat2, lon2)
        _gastropod, _bivalve, _brachipod = 0, 0, 0
        for k, v in randsite_dict.items():
            if "brachipod" in v:
                _brachipod += 1
            elif "bivalve" in v:
                _bivalve += 1
            elif "gastropod" in v:
                _gastropod += 1

        count += 1
        average = (_gastropod + _bivalve + _brachipod) / 3

        dist_list.append(dist)
        average_list.append(average)
    print(dist_list)
    print(average_list)
    
    j_coeff1 = distance.jaccard(biv_collect_freq, brach_collect_freq)
    j_coeff2 = distance.jaccard(brach_collect_freq, gast_collect_freq)
    j_coeff3 = distance.jaccard(biv_collect_freq, gast_collect_freq)
    j_coeff_total = j_coeff1 + j_coeff2 + j_coeff3
    j_dist = 1/j_coeff_total
    print("Jaccard Coefficient: ", j_dist)





if __name__ == "__main__":
    main()
