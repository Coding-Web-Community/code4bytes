# Hey Mathis
# Author: @Travis-Owens
# Date: 2020-09-23

from datetime import datetime

class challenge_14(object):
    def __init__(self):
        self.codes       = list()
        self.time_deltas = list()

        self.time_format = "%Y-%m-%d %H:%M:%S"

        self.read_file()
        self.challenge()

    def read_file(self):
        time_log_file  = open('time.log', 'r')
        time_log_lines = time_log_file.readlines()

        for line in time_log_lines:
            # Sperate the timestamps and code
            arguments = line.split('|')

            # append code to self.codes and remove the newline character
            self.codes.append(arguments[1].strip('\n'))

            # Append the time delta in seconds to self.time_deltas
            self.time_deltas.append(-1 * (datetime.strptime(arguments[0][0:19], self.time_format) - datetime.strptime(arguments[0][22:41], self.time_format)).total_seconds())

    def challenge(self):

        # Find indexs for challenge questions
        shortest = self.time_deltas.index(min(self.time_deltas))
        longest  = self.time_deltas.index(max(self.time_deltas))
        closest_to_average  = self.find_closest()

        print("shortest time delta: " + self.codes[shortest])
        print("longest time delta: " + self.codes[longest])
        print("code cloest to average: " + self.codes[closest_to_average])

    def find_closest(self):
        average = sum(self.time_deltas) / len(self.time_deltas)

        differences = list()

        for time_delta in self.time_deltas:
            differences.append(abs(average - time_delta))

        return(differences.index(min(differences)))


challenge_14().read_file()
