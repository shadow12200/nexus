#python

import sqlite3
import os
from datetime import date as d
from pathlib import Path

def initialise(request):
    date = d.today()
    with sqlite3.connect("nexus.db") as conn:
        cursor = conn.cursor()
        cursor.execute('insert into atv_proj values (?, ?)', (request, date))
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {request} (datetime TEXT, input_prompt TEXT, output_json TEXT)")
    print('server side initialisation done :D')

    #os.makedirs("/memory", exist_ok=True)
    Path(f"/home/blackops/nexus/memory/{request}_log.txt").touch()
    Path(f"/home/blackops/nexus/memory/{request}_main_context.txt").touch()
    print('log and main context file initialisation done :D')

initialise("test_project")

    
