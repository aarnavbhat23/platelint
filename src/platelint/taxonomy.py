"""Defect names, objections and measured noise per rule.

Names and objections mirror 03_defects.py; tests/test_taxonomy.py fails if they drift.
``false_alarm_upper_bound_pct`` is the share of 255 un-injected LLM-written requests
the rule flagged (results/checks_rules.csv). Those requests are un-edited, not verified
correct, so it is an upper bound on false alarms.
"""

TAXONOMY = {'well_volume_exceeded': {'name': 'Volume exceeds well capacity',
                          'objection': 'The liquid does not fit. A 96-well flat-bottom '
                                       'plate holds about 360 uL per well, a 384-well '
                                       'about 112 uL; the request asks the lab to put '
                                       'more than that in one well.',
                          'false_alarm_upper_bound_pct': 6.3},
 'conflicting_conditions': {'name': 'Conflicting incubation conditions',
                            'objection': 'The same step carries two conditions that '
                                         'cannot both hold: 37 C and 4 C, or 1 hour '
                                         'and overnight.',
                            'false_alarm_upper_bound_pct': 28.6},
 'missing_control': {'name': 'Required control missing',
                     'objection': 'The readout cannot be interpreted: no no-template '
                                  'control for qPCR, no vehicle or untreated arm for '
                                  'viability, no blank for ELISA.',
                     'false_alarm_upper_bound_pct': 54.5},
 'unit_mismatch': {'name': 'Unit mismatch or wrong magnitude',
                   'objection': 'The quantity is off by orders of magnitude or in the '
                                'wrong dimension: mL where uL was meant, mg/mL for a '
                                'working antibody dilution, nm where nM was meant.',
                   'false_alarm_upper_bound_pct': 8.2},
 'instrument_readout_mismatch': {'name': 'Named instrument cannot produce the readout',
                                 'objection': 'The request names an instrument and '
                                              'asks it for a signal it does not '
                                              'measure: luminescence from an '
                                              'absorbance-only reader, 450 nm '
                                              'absorbance from a thermocycler.',
                                 'false_alarm_upper_bound_pct': 5.1},
 'temperature_out_of_range': {'name': 'Temperature outside the workable range',
                              'objection': 'The step cannot be run: live cells at 95 '
                                           'C, an antibody incubation at -80 C, an '
                                           'enzyme step above its denaturation point.',
                              'false_alarm_upper_bound_pct': 38.4},
 'missing_required_duration': {'name': 'Essential duration missing',
                               'objection': 'The step cannot be run as written: an '
                                            'incubation with no length, thermocycling '
                                            'with no cycle count, a development step '
                                            'with no stop time.',
                               'false_alarm_upper_bound_pct': 39.2},
 'contradictory_ordering': {'name': 'Steps ordered impossibly',
                            'objection': 'The schedule contradicts itself: a plate '
                                         'read immediately that also follows an '
                                         'overnight incubation, a substrate read '
                                         'before the substrate is added.',
                            'false_alarm_upper_bound_pct': 0.0}}
