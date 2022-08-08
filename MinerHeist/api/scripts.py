from .models import Puzzle, Team, Member, Solve
import hashlib

def getMemberList(team):
    """
    Returns a list of member objects

        Parameters:
                team (Team): The Team whose Members you want listed
        
        Returns:
                m_list (list): A list of Member objects containing team
    """
    m_list = []
    for m in Member.objects:
        if m.team == team:
            m_list.append([m.uname,m.email])
    return m_list

def getLeaderboard() -> dict:
    """
    Returns dict of team names and point totals

            Parameters:
                    none

            Returns:
                    leaderboard (dict): Key value pairs of team names and point totals
    """
    leaderboard = {}
    for s in Solve.objects:
        if s.team.name in leaderboard:
            leaderboard[s.team.name] += s.value
        else:
            leaderboard[s.team.name] = s.value
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

def checkSolve(puzz: Puzzle, sol: str) -> bool:
    """
    Returns whether a solution is correct for a given puzzle

            Parameters:
                    puzz (Puzzle): The Puzzle object being solved
            
            Returns:
                    (bool): Whether the solution is valid or not for the Puzzle
    """
    if puzz.solution == hash(sol):
        return True
    else:
        return False

