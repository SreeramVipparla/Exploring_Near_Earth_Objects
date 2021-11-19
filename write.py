"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, 'w', newline='')as csvFile:
        csv_writer = csv.writer(csvFile)
        csv_writer.writerow(fieldnames)
        for result in results:
            if result.neo.name is None:
                fName = ''
            else:
                fName = result.neo.name
            line = (result.time_str, str(result.distance), str(result.velocity), result.neo.designation, fName, str(result.neo.diameter), str(result.neo.hazardous))
            csv_writer.writerow(line)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output isa
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to wherethedatashouldbesaved.
    """
    list1 = []
    keys = ['datetime_utc', 'distance_au', 'velocity_km_s', 'neo']

    for approach in results:
        dict1 = {'datetime_utc': approach.time_str,
                 'distance_au': approach.distance,
                 'velocity_km_s': approach.velocity,
                 'neo': {'designation': approach.neo.designation,
                         'name': approach.neo.name,
                         'diameter_km': approach.neo.diameter,
                         'potentially_hazardous': approach.neo.hazardous
                         }
                 }
        list1.append(dict1)

    with open(filename, 'w') as outfile:
        if results:
            json.dump(list1, outfile, indent=2)
        else:
            json.dump([], outfile)