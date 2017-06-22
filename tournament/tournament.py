
import psycopg2

#Go through with the syntx please ?


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def querries(querry):
    db = connect()
    con = db.cursor()
    con.execute("querry")
    db.commit()
    db.close()

def deleteMatches():
        querries("TRUNCATE TABLE report_match cascade")
"""Remove all the match records from the database."""


def deletePlayers():
        querries("TRUNCATE TABLE player cascade")
"""Remove all the player records from the database."""


def countPlayers():
        db = connect()
        con = db.cursor()
        con.execute("SELECT count(id) from player") 
        result = con.fetchall()
        db.commit()
        db.close()
        return result[0][0]   
"""Returns the number of players currently registered."""


def registerPlayer(name):
       
        querries("INSERT INTO player(name) VALUES (%s);",(name,))
       

def playerStandings(): 

        db = connect()
        con = db.cursor()
        con.execute('''SELECT match_win.id,match_win.name,match_win.wins,
            total_match.matches from match_win,total_match where match_win.id = total_match.id
            order by wins desc''')
        final = []
        for x in con.fetchall():
            final.append(x)
        db.commit()
        db.close()
        return final

def reportMatch(winner, loser):
            querries("INSERT INTO report_match (winner_id, looser_id) VALUES (%s, %s);",(winner,loser))
 
def swissPairings(): 
            db = connect()
            con = db.cursor()
            con.execute("select * from match_win")
            result = con.fetchall()
            db.close()
            x = 0
            final =[] 
            total_row = len(result)
            while x < total_row:
                player_1_id = result[x][0]
                player_1_name = result[x][1]
                player_2_id = result[x+1][0]
                player_2_name = result[x+1][1]    
                list_ = (player_1_id, player_1_name, player_2_id, player_2_name)
                final.append(list_)
                x +=2

            return final

