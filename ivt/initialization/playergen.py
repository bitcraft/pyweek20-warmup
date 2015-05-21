#-*- encoding: utf-8 -*-
import random


class NameGenerator(object):
    NAME_LIST = ["Astrid",
        "Brynhild","Freydis","Gudrun","Gunnhild",
        "Gunnvor","Hilde","Ragnhild","Ranveig",
        "Sigrid","Sigrunn","Siv","Solveig",
        "Svanhild","Torhild","Torunn","Turid",
        "Vigdis","Yngvild","Arne","Eirik",
        "Geir","Gunnar","Harald","Håkon",
        "Inge","Ivar","Knut","Leif",
        "Magnus","Olav","Rolf","Sigurd",
        "Snorre","Steinar","Torstein","Trygve",
        "Ulf","Valdemar","Vidar","Yngve"]

    LAST_NAME_SUFFIXES = [
        "dóttir",
        "sson",
        "dotter",
        "dottersen",
        "son",
        "sonsen"
    ]

    @staticmethod
    def get_set_of_random_names(n):
        set_of_unique_names = set()
        while len(set_of_unique_names) != n:
            first_name = NameGenerator.generate_first_name()
            last_name = NameGenerator.generate_last_name()
            full_name = "%s %s" % (first_name, last_name)
            set_of_unique_names.add(full_name)
        return set_of_unique_names

    @staticmethod
    def generate_first_name():
        random_first_name_index = NameGenerator.get_random_number(len(NameGenerator.NAME_LIST)-1)
        return NameGenerator.get_name_of_name_list(random_first_name_index, NameGenerator.NAME_LIST)

    @staticmethod
    def generate_last_name():
        last_name_prefix = NameGenerator.generate_last_name_part(NameGenerator.NAME_LIST)
        last_name_suffix = NameGenerator.generate_last_name_part(NameGenerator.LAST_NAME_SUFFIXES)
        last_name = "%s%s" % (last_name_prefix, last_name_suffix)
        return NameGenerator.randomly_add_van_to_last_name(last_name)

    @staticmethod
    def generate_last_name_part(name_list):
        random_index = NameGenerator.get_random_number(len(name_list)-1)
        last_name_part = NameGenerator.get_name_of_name_list(random_index, name_list)
        return last_name_part

    @staticmethod
    def randomly_add_van_to_last_name(last_name):
        random_van_decider = NameGenerator.get_random_number(1)
        if random_van_decider == 1:
            last_name = "%s %s" % ("Van", last_name)
        return last_name

    @staticmethod
    def get_random_number(border):
        return random.randint(0, border)

    @staticmethod
    def get_name_of_name_list(index, name_list):
        return name_list[index]
