#!/usr/bin/python3
"""
lists all cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    data_base = MySQLdb.connect(user=sys.argv[1],
                                passwd=sys.argv[2],
                                db=sys.argv[3])
    cur = data_base.cursor()
    cur.execute("SELECT * FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
    print(", ".join([ct[2] for ct in cur.fetchall() if ct[4] == sys.argv[4]]))
