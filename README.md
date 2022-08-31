# MinerHeist-Backend
<pre>
Current API calls and what they need to work:

GET /lb/
  needs: nothing
  returns: JSON formatted leaderboard in team:points pairs
  
POST /lb/  
  needs:  
    sol: solution being submitted  
    team: team keyword for authentication  
    event: string used as puzzle name to lookup in the event table  
  returns:  
    JSON response solved:True or solved:False. Can refactor to HTTPresponse of strings if desired.  
  side effects: if solved:True, changes boolean is_solved for corresponding assignment in Assignment table.  
  
GET /mem/  
  needs: team:<string name of team> in body. #TODO if body is blank list all members  
  returns: JSON formatted list of usernames in that team and whether they are the owner.  
  
POST /mem/  
  needs:  
    uname: username  
    is_owner: boolean, do they own their team  
    hash: keyword for individual authentication  
    email: email address for contact info  
    team: string formatted name of desired team. #TODO change this. needs to authenticate to make sure they have permission  
  returns: HTTPresponse confirming user creation #TODO handle failure cases  
  side effects: creates new user in Member table  
  
GET /team/  
  needs: nothing  
  returns: list of all team names  
  
POST /team/  
  needs:  
    name: desired name for new team  
    hash: desired keyword for new team  
  returns: HTTPresponse confirming team creation #TODO handle failure cases  
  side effects: creates new team in Team table  
</pre>
