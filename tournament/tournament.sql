

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE player(
	id serial primary key,
	name varchar(40)
	);

CREATE TABLE report_match(
	id serial primary key,
	winner_id int references player(id),
	looser_id int references player(id),
	);

CREATE VIEW match_win as
select player.id, player.name, count(report_match.winner_id) as wins 
from player left join report_match on player.id = report_match.winner_id
GROUP BY player.id 
ORDER BY wins DESC;

CREATE VIEW total_match as 
select player.id, player.name, count(report_match.id) as matches
from player left join report_match on player.id = report_match.winner_id or player.id = report_match.looser_id
GROUP BY player.id;
