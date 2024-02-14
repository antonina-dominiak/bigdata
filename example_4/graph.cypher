// CREATE GRAPH

CREATE (TheMatrix:Movie {title:'The Matrix', released:1999,
 tagline:'Welcome to the Real World'})
CREATE (JohnWick:Movie {title:'John Wick', released:2014,
 tagline:'Silliest Keanu movie ever'})
CREATE (Keanu:Person {name:'Keanu Reeves', born:1964})
CREATE (AndyW:Person {name:'Andy Wachowski', born:1967})
CREATE
 (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix),
 (Keanu)-[:ACTED_IN {roles:['John Wick']}]->(JohnWick),
 (AndyW)-[:DIRECTED]->(TheMatrix)
 
// DELETE GRAPH

MATCH (n) DETACH DELETE n

// DISPLAY GRAPH

MATCH (n)-[r]->(m) RETURN n,r,m