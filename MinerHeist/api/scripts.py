from .models import Event, Team, Member, Assignment
import hashlib

def getMemberList(t: str):
    """
    Returns a list of member objects

        Parameters:
                team (Team): The Team whose Members you want listed
        
        Returns:
                m_dict (dict): A dict of Member objects belonging to Team
    """
    m_dict = {}
    m_list = []
    for m in Member.objects.filter(team__in=Team.objects.filter(name=t)):
        m_list.append(m)
    m_dict["members"] = m_list
    return m_dict

def getLeaderboard() -> dict:
    """
    Returns dict of team names and point totals

            Parameters:
                    none

            Returns:
                    leaderboard (dict): Key value pairs of team names and point totals
    """
    leaderboard = {}
    for s in Team.objects:
        leaderboard[s.name] = s.points
    return leaderboard

def hash(h_string: str) -> str:
    """
    Returns a sha256 hash of a provided string

            Parameters:
                    h_string (str): The string you need hashed

            Returns:
                    (str): String formatted sha256 hash of h_string
    """
    return hashlib.sha256(h_string.encode()).hexdigest()

def checkHash(sol_hash: str, tru_hash: str) -> bool:
    """
    Returns whether a submitted hash matches one on record

            Parameters:
                    tru_hash (str): The hash to check against
                    sol_hash (str): The hash being submitted for checking
            Returns:
                    (bool): Whether the solution is valid or not for the Puzzle
    """
    if tru_hash == hash(sol_hash):
        return True
    else:
        return False
