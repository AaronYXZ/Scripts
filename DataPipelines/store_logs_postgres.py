import time
import sys
import psycopg2
from datetime import datetime


def create_table():
    conn_string = " dbname='projects' user='project_u' password='projects'"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE  logs (
      raw_log TEXT NOT NULL UNIQUE,
      remote_addr TEXT,
      time_local TEXT,
      request_type TEXT,
      request_path TEXT,
      status INTEGER,
      body_bytes_sent INTEGER,
      http_referer TEXT,
      http_user_agent TEXT,
      created TIMEStamp DEFAULT CURRENT_TIMESTAMP
      )
    """)
    conn.close()

def parse_line(line):
    split_line = line.split(" ")
    if len(split_line) < 12:
        return []
    remote_addr = split_line[0]
    time_local = split_line[3] + " " + split_line[4]
    request_type = split_line[5]
    request_path = split_line[6]
    status = split_line[8]
    body_bytes_sent = split_line[9]
    http_referer = split_line[10]
    http_user_agent = " ".join(split_line[11:])
    created = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    return [
        remote_addr,
        time_local,
        request_type,
        request_path,
        status,
        body_bytes_sent,
        http_referer,
        http_user_agent,
        created
    ]

def insert_record(line, parsed):
    conn_string = "dbname='projects' user='project_u' password='projects'"
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    args = [line] + parsed
    cur.execute('INSERT INTO logs (raw_log,remote_addr,time_local,request_type,request_path,status,body_bytes_sent, http_referer,http_user_agent,created) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s,%s)', args)
    conn.commit()
    conn.close()

LOG_FILE_A = "log_a.txt"
LOG_FILE_B = "log_b.txt"

if __name__ == "__main__":
    ## create_table()
    try:
        f_a = open(LOG_FILE_A, 'r')
        f_b = open(LOG_FILE_B, 'r')
        while True:
            where_a = f_a.tell()
            line_a = f_a.readline()
            where_b = f_b.tell()
            line_b = f_b.readline()

            if not line_a and not line_b:
                time.sleep(1)
                f_a.seek(where_a)
                f_b.seek(where_b)
                continue
            else:
                if line_a:
                    line = line_a
                else:
                    line = line_b

                line = line.strip()
                parsed = parse_line(line)
                if len(parsed) > 0:
                    insert_record(line, parsed)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        f_a.close()
        f_b.close()
        sys.exit()