"""
this module will correct the syntax error of coding standards
1. remove only trailing spaces
2. Convert CamelCase to snake_case outside main
3. Convert snake_case to SNAKE_CASE inside main
4. It will change the attribure and methods name not the string
"""
import inflection

if __name__ == "__main__":
    with open('testfile.py', 'r') as read_fp:
        with open('test_correct.py', 'w') as write_fp:
            convert_case = True
            for rows in read_fp:
                if rows.strip(' ') == '\n':
                    write_fp.write(rows.strip(' '))
                else:
                    rows = rows.rstrip(' ')
                    if "class " in rows:
                        wite_fp.write(rows)
                    elif "__main__" in rows:
                        convert_case = False
                        write_fp.write(rows)
                    else:
                        if convert_case:
                            write_fp.write(inflection.underscore(rows))
                        else:
                            write_fp.write(inflection.underscore(rows).upper())
