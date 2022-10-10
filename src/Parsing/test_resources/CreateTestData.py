
class CreateTestData:
    get_input_token_list_entry = "create table customers\
        (\
	        customer_id  int PRIMARY KEY AUTO_INCREMENT comment=\"This is a random comment\",\
	        first_name	char(32) NOT NULL,\
	        last_name	char(32),\
	        status		int DEFAULT 1,\
	        comment		varchar(255),\
        );"
    get_input_token_list_expected = [[
        ['keyword', 'create'], ['keyword', 'table'],
        ['variable', 'customers'], ['separator', '('],
        ['variable', 'customer_id'], ['datatype', 'int'],
        ['variable', 'PRIMARY'], ['variable', 'KEY'],
        ['variable', 'AUTO_INCREMENT'], ['variable', 'comment'],
        ['operator', '='], ['variable', 'This is a random comment'],
        ['separator', ','], ['variable', 'first_name'],
        ['datatype', 'char'], ['separator', '('],
        ['variable', '32'], ['separator', ')'],
        ['operator', 'NOT'], ['variable', 'NULL'],
        ['separator', ','], ['variable', 'last_name'],
        ['datatype', 'char'], ['separator', '('],
        ['variable', '32'], ['separator', ')'],
        ['separator', ','], ['variable', 'status'],
        ['datatype', 'int'], ['variable', 'DEFAULT'],
        ['variable', '1'], ['separator', ','],
        ['variable', 'comment'], ['datatype', 'varchar'],
        ['separator', '('], ['variable', '255'],
        ['separator', ')'], ['separator', ','],
        ['separator', ')']
    ]]

    split_instruction_entry = "create table customers\
        (\
	        customer_id  int PRIMARY KEY AUTO_INCREMENT comment=\"This is a random comment\",\
	        first_name	char(32) NOT NULL,\
	        last_name	char(32),\
	        status		int DEFAULT 1,\
	        comment		varchar(255),\
        )"

    split_instruction_expected = ['create', 'table', 'customers', '(', 'customer_id', 'int', 'PRIMARY', 'KEY', 'AUTO_INCREMENT', 'comment', '=', 'This is a random comment', ',', 'first_name', 'char', '(', '32', ')', 'NOT', 'NULL', ',', 'last_name', 'char', '(', '32', ')', ',', 'status', 'int', 'DEFAULT', '1', ',', 'comment', 'varchar', '(', '255', ')', ',', ')']
