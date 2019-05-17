import pickle

f1 = open("cat_dict_reverse", "rb")
cat = pickle.load(f1)
f1.close()
f2 = open("cow_dict_reverse", "rb")
cow = pickle.load(f2)
f2.close()
f3 = open("dog_dict_reverse", "rb")
dog = pickle.load(f3)
f3.close()
f4 = open("guinea_pig_dict_reverse", "rb")
guinea_pig = pickle.load(f4)
f4.close()
f5 = open("horse_dict_reverse", "rb")
horse = pickle.load(f5)
f5.close()
f6 = open("human_dict_reverse", "rb")
human = pickle.load(f6)
f6.close()
f7 = open("mouse_dict_reverse", "rb")
mouse = pickle.load(f7)
f7.close()
f8 = open("pig_dict_reverse", "rb")
pig = pickle.load(f8)
f8.close()
f9 = open("rabbit_dict_reverse", "rb")
rabbit = pickle.load(f9)
f9.close()
f10 = open("rat_dict_reverse", "rb")
rat = pickle.load(f10)
f10.close()
f11 = open("sheep_dict_reverse", "rb")
sheep = pickle.load(f11)
f11.close()


def line_dict(a_list: list):
    spe_pro_dict = {"cat": [], "cow": [], "dog": [], "guinea_pig": [], "horse": [], "human": [], "mouse": [], "pig": [],
                    "rabbit": [], "rat": [], "sheep": []}
    for each in a_list:
        if "ca" in each:
            spe_pro_dict["cat"].append(cat[each])
        elif "co" in each:
            spe_pro_dict["cow"].append(cow[each])
        elif "do" in each:
            spe_pro_dict["dog"].append(dog[each])
        elif "gu" in each:
            spe_pro_dict["guinea_pig"].append(guinea_pig[each])
        elif "ho" in each:
            spe_pro_dict["horse"].append(horse[each])
        elif "hu" in each:
            spe_pro_dict["human"].append(human[each])
        elif "mo" in each:
            spe_pro_dict["mouse"].append(mouse[each])
        elif "pi" in each:
            spe_pro_dict["pig"].append(pig[each])
        elif "ra" in each:
            spe_pro_dict["rabbit"].append(rabbit[each])
        elif "rt" in each:
            spe_pro_dict["rat"].append(rat[each])
        elif "sh" in each:
            spe_pro_dict["sheep"].append(sheep[each])
    return spe_pro_dict


_total = set(cat.values()) | set(cow.values()) | set(dog.values()) | set(guinea_pig.values()) | set(
    horse.values()) | set(human.values()) | set(mouse.values()) | set(pig.values()) | set(rabbit.values()) | set(
    rat.values()) | set(sheep.values())

# l=['cat', 'cow', 'dog', 'guinea_pig', 'horse', 'human', 'mouse', 'pig', 'rabbit', 'rat', 'sheep']
# for each in l:
#    s+=f'set({each}.values()) | '

if __name__ == '__main__':
    from collections import defaultdict

    cluster_count = defaultdict(int)
    node_count = defaultdict(int)
    number_of_clusters = 0
    alignment_file = input("enter alignment file:")
    #alignment_file='C:/Users/DELL/Desktop/SMETANA_result_iid11.txt'
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

        cluster_count[number_of_species_covered] += 1
        number_of_clusters += 1



    f.close()

    print(f"In total:\n\tthere are\t{number_of_clusters}\tclusters in the alignment result.")
    print(f"\t{len(protein_set)}\tout of\t{len(_total)}\tproteins are in the alignment result.")
    print(f"Cluster Coverage:")
    for no, _sum in sorted(cluster_count.items(),reverse=True):
        print(f"{no}\tEquivalent Class Coverage number :\t{_sum};\tProportion is :\t{'%f%%' % (_sum/(number_of_clusters) * 100)}.")
    print(f"Node Coverage:")
    for no, _sum in sorted(node_count.items(),reverse=True):
        print(f"{no}\tNodes Coverage number :\t{_sum};\tProportion is :\t{'%f%%' % (_sum/len(protein_set) * 100)}.")


