import os
import json
from csep.utils.time import epoch_time_to_utc_datetime
from csep.utils.constants import SECONDS_PER_DAY

horizon_in_days=7
horizon_in_millis=horizon_in_days*SECONDS_PER_DAY*1000
with open('u3etas_simulation_list.txt', 'r') as f:
    for line in f:
        conf_fname = os.path.join(line.strip(), 'config.json')
        with open(conf_fname, 'r') as cf:
            config=json.load(cf)
            start_time=config['startTimeMillis']
            end_time=start_time+horizon_in_millis
            print(f"{line.strip()}: {epoch_time_to_utc_datetime(start_time)} - {epoch_time_to_utc_datetime(end_time)}")

