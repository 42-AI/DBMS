
class InsertTestData:
    get_input_token_list_entry = "   INSERT    INTO    customers (first_name, last_name, comment)\
            VALUES                    \
             ('Rébecca', 'Armand', 'Saint-Didier-des-Bois'),\
             ('Aimée', 'Hebert', 'Marigny-le-Châtel'),\
             ('Marielle', 'Ribeiro', 'Maillères'),\
             ('Hilaire', 'Savary', 'Conie-Molitard');"

    get_input_token_list_expected = [[
            ['keyword', 'INSERT'], ['keyword', 'INTO'],
            ['variable', 'customers'], ['separator', '('],
            ['variable', 'first_name'], ['separator', ','],
            ['variable', 'last_name'], ['separator', ','],
            ['variable', 'comment'], ['separator', ')'],
            ['keyword', 'VALUES'], ['separator', '('],
            ['variable', 'Rébecca'], ['separator', ','],
            ['variable', 'Armand'], ['separator', ','],
            ['variable', 'Saint-Didier-des-Bois'],
            ['separator', ')'], ['separator', ','],
            ['separator', '('], ['variable', 'Aimée'],
            ['separator', ','], ['variable', 'Hebert'],
            ['separator', ','], ['variable', 'Marigny-le-Châtel'],
            ['separator', ')'], ['separator', ','],
            ['separator', '('], ['variable', 'Marielle'],
            ['separator', ','], ['variable', 'Ribeiro'],
            ['separator', ','], ['variable', 'Maillères'],
            ['separator', ')'], ['separator', ','],
            ['separator', '('], ['variable', 'Hilaire'],
            ['separator', ','], ['variable', 'Savary'],
            ['separator', ','], ['variable', 'Conie-Molitard'],
            ['separator', ')']
        ]]

    split_instruction_entry = "   INSERT    INTO    customers (first_name, last_name, comment)\
            VALUES                    \
             ('Rébecca', 'Armand', 'Saint-Didier-des-Bois'),\
             ('Aimée', 'Hebert', 'Marigny-le-Châtel'),\
             ('Marielle', 'Ribeiro', 'Maillères'),\
             ('Hilaire', 'Savary', 'Conie-Molitard')"
    
    split_instruction_expected = ['INSERT', 'INTO', 'customers', '(', 'first_name', ',', 'last_name', ',', 'comment', ')', 'VALUES', '(', 'Rébecca', ',', 'Armand', ',', 'Saint-Didier-des-Bois', ')', ',', '(', 'Aimée', ',', 'Hebert', ',', 'Marigny-le-Châtel', ')', ',', '(', 'Marielle', ',', 'Ribeiro', ',', 'Maillères', ')', ',', '(', 'Hilaire', ',', 'Savary', ',', 'Conie-Molitard', ')']

