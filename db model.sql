Organizer 
	id INTEGER PRIMARY KEY 
	name STRING

Tournament
	id INTEGER PRIMARY KEY
	name STRING
	org_id INTEGER FOREIGN KEY REFERENCES organizer(id)

Team
	id INTEGER PRIMARY KEY
	name STRING
	tournament_id INTEGER FOREIGN KEY REFERENCES Tournament(id)

Player
	id INTEGER PRIMARY KEY
	name	STRING
	number INTEGER
	role STRING
	is_captain BOOLEAN
	is_wicket_keeper BOOLEAN
	team_id INTEGER FOREIGN KEY REFERENCES team(id)
	
Matches
	id INTEGER PRIMARY KEY
	Tournament_id INTEGER FOREIGN KEY 
	team_a_id INTEGER FOREIGN KEY 
	team_b_id INTEGER FOREIGN KEY
	toss_winner_team_id INTEGER NULL FOREIGN KEY REFERENCES Team(id)
	winner_team_id INTEGER NULL FOREIGN KEY REFERENCES team(id)
	win_by_runs INTEGER  
	CONSTRAINT team_a_b_are_not_equal CHECK (team_a_id <> team_b_id)
	
Inning
	id
	match_id INTEGER FOREIGN KEY matches(id)
	Innings STRING {first_innings , second_innings}
	batting_team INTEGER FOREIGN KEY 
	bowling_team INTEGER FOREIGN key 
	
	
over
	id
	inning_id INTEGER FOREIGN KEY inning(id)
	over_number
	bowler_id
	
ball
	id 
	over_id INTEGER FOREIGN KEY over(id)
	ball_number
	striker_id
	non_striker_id
	bowler_id
	runs_batsman
	runs_extras
	extra_type
	is_wicket
	witcket_type(bowled,catch,runout,lbw)
	dismissed_player_id
	
	
	
	