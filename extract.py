"""Extract data on near-Earth objects and close approaches from CSV and JSON
files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of
`NearEarthObject`s. The `load_approaches` function extracts close
approach data from a JSON file, formatted as described in the project
instructions, into a collection of `CloseApproach` objects. The main
module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.
You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing
    data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    csv_result = []
    with open(neo_csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            near_earth = NearEarthObject(row[3], row[4], row[15], row[7])
            csv_result.append(near_earth)
    return csv_result


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file
    containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as infile:
        json_result = json.load(infile)
    result = []
    close_approach_key_index_map = {}

    for index in range(len(json_result['fields'])):
        key = json_result['fields'][index]
        close_approach_key_index_map[key] = index

    for curr_approach_data in json_result['data']:
        # _designation, time, distance = 0.0 , velocity = 0.0
        #  date and time (in UTC) of closest approach, the nominal
        # approach distance in astronomical units,
        # and the relative approach velocity in kilometers per second.
        '''
            des - primary designation of the asteroid or comet
            (e.g., 443, 2000 SG344)
            cd - time of close-approach (formatted calendar date/time, in UTC)
            dist - nominal approach distance (au)
            v_rel - velocity relative to the approach body at close
            approach (km/s)
            v_inf - velocity relative to a massless body (km/s)
        '''
        close_approach = CloseApproach(
            curr_approach_data[close_approach_key_index_map['des']],
            curr_approach_data[close_approach_key_index_map['cd']],
            curr_approach_data[close_approach_key_index_map['dist']],
            curr_approach_data[close_approach_key_index_map['v_rel']]
        )
        result.append(close_approach)

    return result
