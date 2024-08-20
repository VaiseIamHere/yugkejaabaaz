import heapq
import timetable as tt
import json

n = -1

days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday"
}

timeslots = {
    0: "8am - 8:30am",
    1: "8:30am - 9am",
    2: "9am - 9:30am",
    3: "9:30am - 10am",
    4: "10am - 10:30am",
    5: "10:30am - 11am",
    6: "11am - 11:30am",
    7: "11:30am - 12pm",
    8: "12pm - 12:30pm",
    9: "12:30pm - 1pm",
    10: "1pm - 1:30pm",
    11: "1:30pm - 2pm",
    12: "2pm - 2:30pm",
    13: "2:30pm - 3pm",
    14: "3pm - 3:30pm",
    15: "3:30pm - 4pm",
    16: "4pm - 4:30pm",
    17: "4:30pm - 5pm",
    18: "5pm - 5:30pm",
    19: "5:30pm - 6pm"
}


class Person:
    person_list = []

    def __init__(self, name, timetable, dept, ipd_day, senior, id):
        self.name = name
        self.timetable = timetable
        self.dept = dept
        self.ipd_day = ipd_day
        self.senior = senior
        self.id = id
        Person.person_list.append(self)


def load_data():
    global n
    with open('database.json', 'r') as file:
        data = json.load(file)
    n = len(data) - 1
    for i, j in enumerate(data):
        Person(data[i]['name'], data[i]['timetable'], data[i]['dept'], data[i]['ipd_day'], data[i]['senior'], str(j))


def append_to_db(name, dept, img, senior=False):
    global n
    with open('database.json', 'r') as file:
        data = json.load(file)
    n += 1
    timetable = tt.get_tt(img)

    ipd_day = 0
    for i, j in enumerate(timetable):
        if i is "1"*20:
            ipd_day = j
            break

    data[str(n)] = {
        "name": name,
        "timetable": timetable,
        "dept": dept,
        "ipd_day": ipd_day,
        "senior": senior,
        "id": n
    }

    with open('database.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_indexes(lst, value):
    indexes = []
    for i, v in enumerate(lst):
        if v == value:
            indexes.append(i)
    return indexes


def all_slots(tt_lists):
    slots = []
    no_of_people = len(tt_lists)
    for i in range(0, 6):
        for j in range(0, 20):
            free_people = 0
            for k in range(0, no_of_people):
                if tt_lists[k][i][j] is "0":
                    free_people += 1
            slots.append(free_people)
    return slots


def indices_to_slots(list_of_indices):
    for i in list_of_indices:
        for j in i:



# Accepts list of timetable attribute of person class
#       example:   [["00..000", "101011..", ...],
#                   ["00..000", "101011..", ...],
#                   ["00..000", "101011..", ...]]
def top_slots(tt_lists):
    slots = all_slots(tt_lists)
    top_5 = heapq.nlargest(5, slots)
    list_of_indices = []
    for i in top_5:
        list_of_indices.append(get_indexes(slots, i))
