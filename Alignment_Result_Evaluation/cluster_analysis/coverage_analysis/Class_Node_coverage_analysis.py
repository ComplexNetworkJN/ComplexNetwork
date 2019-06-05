def line_dict(a_list: list):
    spe_pro_dict = {"cat": [], "cow": [], "dog": [], "guinea_pig": [], "horse": [], "human": [], "mouse": [], "pig": [],
                    "rabbit": [], "rat": [], "sheep": []}
    for each in a_list:
        if "ca" in each:
            spe_pro_dict["cat"].append(each)
        elif "co" in each:
            spe_pro_dict["cow"].append(each)
        elif "do" in each:
            spe_pro_dict["dog"].append(each)
        elif "gu" in each:
            spe_pro_dict["guinea_pig"].append(each)
        elif "ho" in each:
            spe_pro_dict["horse"].append(each)
        elif "hu" in each:
            spe_pro_dict["human"].append(each)
        elif "mo" in each:
            spe_pro_dict["mouse"].append(each)
        elif "pi" in each:
            spe_pro_dict["pig"].append(each)
        elif "ra" in each:
            spe_pro_dict["rabbit"].append(each)
        elif "rt" in each:
            spe_pro_dict["rat"].append(each)
        elif "sh" in each:
            spe_pro_dict["sheep"].append(each)
    return spe_pro_dict

if __name__ == '__main__':
    from collections import defaultdict

    total_node = 0
    cluster_count = defaultdict(int)
    node_count = defaultdict(int)
    number_of_clusters = 0
    alignment_file = input("enter alignment file:")
    #alignment_file='F:/SMETANA3/SMETANA_result/smetana_3iid_bitscore_alignmet_5m.txt'
    f = open(alignment_file)

    protein_set = set()
    number_of_node_covered=0
    for line in f:
        a_list = line.rstrip().split(" ")
        a_dict = line_dict(a_list)
        number_of_species_covered = 0
        node_number=0
        for _species, _proteins in a_dict.items():
            if len(_proteins) != 0:
                number_of_species_covered += 1
                for each in _proteins:
                    protein_set.add(each)
                node_number +=len(_proteins)
        node_count[number_of_species_covered] +=node_number

        total_node += node_number
        cluster_count[number_of_species_covered] += 1
        number_of_clusters += 1
    f.close()

    print(f"In total:\n\tthere are\t{number_of_clusters}\tclusters in the alignment result.")
    print(f"\tthere are\t{total_node}\tproteins are in the alignment result.")
    print(f"Cluster Coverage:")
    for no, _sum in sorted(cluster_count.items(),reverse=True):
        print(f"{no}\tEquivalent Class Coverage number :\t{_sum};\tProportion is :\t{'%f%%' % (_sum/(number_of_clusters) * 100)}.")
    print(f"Node Coverage:")
    for no, _sum in sorted(node_count.items(),reverse=True):
        print(f"{no}\tNodes Coverage number :\t{_sum};\tProportion is :\t{'%f%%' % (_sum/total_node * 100)}.")