from utility import *
import pandas as pd


def main():
    taxon_file = "/geology-research/data/biv.csv"
    taxon = read_csv(taxon_file, False)

    read_biv = read_csv("/geology-research/data/biv.csv", True)
    biv_dict = map_(read_biv, 5, 13)
    for k in biv_dict:
        print(k + " -> \"" + biv_dict[k] + "\"")
    write_dict(biv_dict, "/geology-research/data/biv_dict.csv", col_header=["genus", "higher_taxon"])

    read_gast = read_csv("/geology-research/data/gast.csv", True)
    gast_dict = map_force_val(read_gast, 5, "Gastropod")
    for k in gast_dict:
        print(k + " -> \"" + gast_dict[k] + "\"")
    write_dict(gast_dict, "/geology-research/data/gast_dict.csv", col_header=["genus", "higher_taxon"])

    read_brach = read_csv("/geology-research/data/brach.csv", True)
    brach_dict = map_force_val(read_brach, 5, "Brachiopod")
    for k in brach_dict:
        print(k + "-> \"" + brach_dict[k] + "\"")
    write_dict(brach_dict, "/geology-research/data/brach_dict.csv", col_header=["genus", "higher_taxon"])

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

    coocc.to_csv("/geology-research/data/coocc.csv")




    df = pd.DataFrame(data=mat[1:], columns=mat[0])
    print(df)
    df.to_csv("df.csv")

    df_t = df.T
    print(df_t.corr())
    df_t.to_csv("df_t.csv")


    #total = []

    #df_float = df.astype(float)
    #co_occ_mat = df_float.T.dot(df_float)
    #print(co_occ_mat)

    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        #print(df)


if __name__ == "__main__":
    main()
