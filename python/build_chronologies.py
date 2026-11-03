"""Construct chronologies for a given fault
"""

from QuakeRates.dataman.parse_params import parse_param_file, get_event_sets
from glob import glob

#paramfiles = ['../params/Willunga_earthquake_soils_6_events.txt']
paramfiles = ['../params/Willunga_earthquake_soils_8_events.txt']
# Number of sample chronologies to generate
current_year = 2022 # Offst for OxCal models defined in AD/BC
n_samples = 10000

names, event_sets, event_certainties, num_events, \
    tect_regions, fault_styles = get_event_sets(paramfiles, ['all'], ['all'], 1,
                                                current_year=current_year)
print(names)
for i, event_set in enumerate(event_sets):
    event_set.gen_chronologies(n_samples, observation_end=current_year, min_separation=1)
    chron_filename = '../data/chronologies/' + event_set.name + \
        '_%i_chronologies.csv' % n_samples
    event_set.write_chronology(chron_filename)
    
