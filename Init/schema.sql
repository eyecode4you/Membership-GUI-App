/*Initial creation scheme for simple database Creation*/
DROP TABLE IF EXISTS members;
CREATE TABLE members(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50),
	phone VARCHAR,
	email VARCHAR,
	address VARCHAR,
	nationality VARCHAR,
	category CHAR,
	company VARCHAR,
	position VARCHAR,
	accountname VARCHAR,
	IBAN VARCHAR,
	BIC VARCHAR,
	created DATE DEFAULT CURRENT_DATE,
	expiry VARCHAR
);
