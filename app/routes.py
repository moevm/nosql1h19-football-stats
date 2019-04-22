from app import app
from flask import render_template, session, request, redirect, url_for, abort, current_app, flash, jsonify, json
from app.main import db
from bson.json_util import dumps


def merge_two_dicts(x, y):
    z = x.copy()   # start with x keys and values
    z.update(y)    # modifies z with y keys and values & returns None
    return z

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/teams')
def show_teams():
	teams = db.findAllTeams()
	return render_template('teams.html',teams = teams);
@app.route('/findmatch')
def find_match():
	return render_template('findmatch.html')
	
@app.route('/findmatch/find/', methods=['POST'])
def show_match():
	post_data = request.json
	result = dumps(db.findMatchs(post_data))
	print("this is date: ",post_data)
	
	print("this is result: ",result)
	return result
	
@app.route('/export/')
def export_json():
	result=dumps(db.getAll())
	return result
@app.route('/statteam/<teamname>/')
def show_stat_team(teamname):
	
	statis = list(db.getTeamDetails(teamname)) 
	statis = statis[0]
	
	matres = list(db.getTeamResult(teamname))
	matres = matres[0]
	
	result = merge_two_dicts(statis,matres)
	
	return render_template('statteam.html',teamname = teamname, stat = result)
	
@app.route('/compare/f=<name_1>&s=<name_2>')
def compare(name_1,name_2):
	name_1 = name_1
	name_2 = name_2
	
	

	statis1 = list(db.getTeamDetails(name_1)) 
	statis1 = statis1[0]
	
	matres1 = list(db.getTeamResult(name_1))
	matres1 = matres1[0]
	
	result1 = merge_two_dicts(statis1,matres1)
	
	
	
	
	
	statis2 = list(db.getTeamDetails(name_1)) 
	statis2 = statis2[0]
	
	matres2 = list(db.getTeamResult(name_1))
	matres2 = matres2[0]
	
	result2 = merge_two_dicts(statis2,matres2)
	
	
	
	
	
	
	

	return render_template('compare.html',team1 = result1,name_1 = name_1,name_2 = name_2, team2 = result2)
@app.route('/test/')
def test():
	second_t = list(db.getTeamDetails("Arsenal")) 
	second_t = second_t[0]
	result = list(db.getTeamResult("Arsenal"))
	result = result[0]
	
	test = merge_two_dicts(second_t,result)
	print(test)
	return "1"