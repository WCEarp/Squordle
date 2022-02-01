import settings
import psycopg2
import atexit
from typing_extensions import Self
#from tabulate import tabulate

def parse(message):
    tmp = message.split("\n")[0].split(" ")
    return tmp[1], tmp[2]

def get_scoreboard():
    raise NotImplemented

def get_points(score):
    points = 0
    if (score.split("/")[0] == "x"):
        points = 0
    elif (score.split("/")[0] == "1"):
        points = 6
    elif (score.split("/")[0] == "2"):
        points.split("/")[0] = 5
    elif (score.split("/")[0] == "3"):
        points = 4
    elif (score.split("/")[0] == "4"):
        points = 3
    elif (score.split("/")[0] == "5"):
        points = 2
    elif (score.split("/")[0] == "6"):
        points = 1

    return points

########################################################################################################

if __name__ == "__main__":
    #print(debug.data["scoreboard"]["players"][0]["Squitward"])
    name = 'Squitward'
    msg = "Wordle 223 4/6\n\n⬛⬛⬛⬛⬛\n⬛⬛🟨⬛⬛\n⬛🟨🟨⬛⬛\n🟨🟩🟨⬛🟩\n🟩🟩🟩🟩🟩"
    cid = 1234567890
    day, score = parse(msg)
    points = get_points(score)
    try:
        # Connect to DB
        connection = psycopg2.connect(user=settings.DATABASE_USER,
                                      password=settings.DATABASE_PSWD,
                                      host=settings.DATABASE_HOST,
                                      port=settings.DATABASE_PORT,
                                      database=settings.DATABASE_NAME)
        # Create a cursor to perform database operations
        cursor = connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute('INSERT INTO scoreboard (channel_id,player,score,points,wordle_number) \
                        VALUES (%s, %s, %s, %s, %s);', (cid, 'Squitward', '5/6', 2, 225))
        # Fetch result
        connection.commit()
    except Exception as error:
        print( "Error connecting to DB: ", error)
    finally:
        if (connection):
            cursor.close()
            connection.close()