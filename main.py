from individ import Individ
from random import seed
from random import randint
import time

def get_pairs(individs):
    pair_1, pair_2 = list(), list()
    for i in range(2):
        if i == 1:
            tmp_1 = randint(0, 3)
            tmp_2 = randint(0, 3)
            while tmp_1 == pair_1[0] or tmp_2 == pair_2[0]:
                if tmp_1 == pair_1[0]:
                    tmp_1 = randint(0, 3)
                
                if tmp_2 == pair_2[0]:
                    tmp_2 = randint(0, 3)

            pair_1.append(tmp_1)
            pair_2.append(tmp_2)

        else: 
            pair_1.append(randint(0, 3))
            pair_2.append(randint(0, 3))

    for i in range(2):
        pair_1[i] = individs[pair_1[i]]
        pair_2[i] = individs[pair_2[i]]

    return pair_1, pair_2


def new_child(pairs):
    child_list = list()
    for pair in pairs:
        tmp = randint(1, 5)
        child_list.append(Individ(pair[0].gen & (64 - 2 ** tmp) | pair[1].gen & (2 ** tmp - 1)))
        child_list.append(Individ(pair[1].gen & (64 - 2 ** tmp) | pair[0].gen & (2 ** tmp - 1)))

    return child_list


def mutation(childs):
    tmp_1 = randint(0, 7)
    tmp_2 = randint(0, 5)
    
    if (childs[tmp_1].gen >> tmp_2) & 1 == 1:
        childs[tmp_1] = Individ(childs[tmp_1].gen & (63 - 2 ** tmp_2))
    else:
        childs[tmp_1] = Individ(childs[tmp_1].gen | (2 ** tmp_2))

    return childs


def cross(individs):
    pair_1, pair_2 = get_pairs(individs)
    return mutation(new_child([pair_1, pair_2]) + individs)


def reduction(all_individs, alg_type):
    if alg_type == "min":
        return sorted(all_individs, key = lambda individ: individ.value)[0:4]
    else:
        return sorted(all_individs, key = lambda individ: individ.value)[4:8]


'''def calc_gen_alg(individs, count, alg_type):
    count -= 1
    all_individs = cross(individs)
    new_individs = reduction(all_individs, alg_type)

    for i in new_individs:
        print("{0:b}".format(i.gen) + "  " + str(i.gen) + "  " + str(i.phenotype) 
        + "  " + str(i.value))
    print()

    if count == 0:
        if alg_type == "min":
            print(new_individs[0].phenotype)
        else:
            print(new_individs[3].phenotype)
        return 

    calc_gen_alg(new_individs, count, alg_type)'''

def calc_gen_alg(individs, count, alg_type):
    all_individs = cross(individs)
    new_individs = reduction(all_individs, alg_type)
    for i in new_individs:
        print("{0:b}".format(i.gen) + "  " + str(i.gen) + "  " + str(i.phenotype) 
        + "  " + str(i.value))
    print()

    for _ in range(count - 1):
        all_individs = cross(new_individs)
        new_individs = reduction(all_individs, alg_type)

        for i in new_individs:
            print("{0:b}".format(i.gen) + "  " + str(i.gen) + "  " + str(i.phenotype) 
            + "  " + str(i.value))
        print()

    if alg_type == "min":
        print(new_individs[0].phenotype)
    else:
        print(new_individs[3].phenotype)
    return



def gen_alg(count, alg_type):
    seed(time.time())
    individ_list = list()

    for _ in range(4):
        individ_list.append(Individ(randint(0, 63)))

    calc_gen_alg(individ_list, count, alg_type)


gen_alg(50, "min")

#for i in individ_list:
    #print(i.gen)



