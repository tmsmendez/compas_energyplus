from __future__ import print_function

__author__ = ["Tomas Mendez Echenagucia"]
__copyright__ = "Copyright 2020, Design Machine Group - University of Washington"
__license__ = "MIT License"
__email__ = "tmendeze@uw.edu"
__version__ = "0.1.0"

import os
import compas_energyplus
import subprocess

from compas_energyplus.writer import write_idf

#TODO: Volmesh?
#TODO: Assembly?

class Building(object):
    def __init__(self, filepath, weather):
        self.filepath = filepath
        self.weather = weather

        self.name = 'Building'
        self.ep_version = '9.5'
        self.num_timesteps = 6
        self.terrain = 'City'
        self.solar_distribution = 'FullExteriorWithReflections'

        self.zones = {}

    def write_idf(self):
        write_idf(self)

    def add_zone(self, zone):
        self.zones[len(self.zones)] = zone


    def analyze(self):
        idf = self.filepath
        eplus = 'energyplus'
        out = os.path.join(compas_energyplus.TEMP, 'eplus_output')
        subprocess.call([eplus, '-w', self.weather,'--output-directory', out, idf])

if __name__ == '__main__':
    from compas_energyplus.datastructures import Zone

    data = compas_energyplus.DATA
    for i in range(50): print('')
    filepath = os.path.join(compas_energyplus.TEMP, 'idf_testing.idf')
    wea = os.path.join(data, 'weather_files', 'USA_WA_Seattle-Tacoma.Intl.AP.727930_TMY3.epw')
    b = Building(filepath, wea)

    z1 = Zone.from_json(os.path.join(compas_energyplus.DATA, 'zones', 'zone1.json'))
    b.add_zone(z1)

    print(b.zones[0])

    b.write_idf()
    # b.analyze()




    # per zone ----------------------------
    # building_surface
    # fenestration_surface
    # zone_control_thermostat, schedule, thermostat_time, 
    # zone_hvac_equipment connections, node lists, ideal loads air system
    # outdoor air
    # zone supply air data
    # -------------------------------------


    # simulation control, heat balance, run period, shadow calc, sizing params

    # materials, window_materials

    # constructions

    # schedule type limits, day interval

    # zone list
    # lights
    # people
    # electric equipment
    # zone infiltration

    # outputs
    # daylighting controls