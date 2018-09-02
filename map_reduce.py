# it will first reduce the list of dictionaries

from collections import defaultdict


def dict_reducer(list_dict):
    """
    
    @param list_dict:
    @type list_dict:
    """
    dict1 = defaultdict(list)
    output_list = []
    test_list = []
    for data in list_dict:
        dict1[data['contract']].append(data)
    
    for key, dict_data in dict1.items():
        test_list = []
        reduced_dict = {}
        for data in dict_data:
            for k, v in data.items():
                if v == 'Null':
                    del data[k]
            
            try:
                test_list.append(data['keydate'])
            except:
                pass
                
            reduced_dict.update(data)
        
        # remove duplicate data from test_list
        
        clean_list = []
        for data in test_list:
            if data in clean_list:
                pass
            else:
                clean_list.append(data)
        
        for data in clean_list:
            reduced_dict.update({'keydate':data})
            output_list.append(dict(reduced_dict))
    
    return output_list


def line_mapper(main_list, reduced_list):
    """
    
    @param list1:
    @type list1:
    @param list2:
    @type list2:
    """
    clone_main = main_list[:]
    new_list = []
    for reduced_data in reduced_list:
        found = False
        print('loop starts, reduced data ', reduced_data)
        for main_data in main_list:
            if main_data['contract'] == reduced_data['contract']:
                try:
                    clone_main.remove(main_data)
                except ValueError:
                    pass
                main_data.update(reduced_data)
                a = main_data.copy()
                print('pre new data', new_list)
                new_list.append(a)
                print('main data', main_data)
                print('new data', new_list)
                print('\n')
                break
    
    print('clone_main_list', clone_main)
    for remaining_data in clone_main:
        new_list.append(remaining_data)
    return new_list


if __name__ == "__main__":
    list_of_dict = [
                    {'contract': 'AB1', 'Anum':'Null', 'Bnum': 'Null', 'keydate':'10/12/1988'  },
                    {'contract': 'AB1', 'Anum':2 , 'Bnum': 3, 'keydate':'Null'  },
                    {'contract': 'AB1', 'Anum':'Null', 'Bnum': 'Null', 'keydate':'30/12/2018'  },
                    {'contract': 'AB2', 'Anum': 4, 'Bnum': 10, 'keydate':'30/12/2018'  },
                    {'contract': 'AB2', 'Anum':'Null', 'Bnum': 'Null', 'keydate':'30/12/2018'  },
                    {'contract': 'AB3', 'Anum':56, 'Bnum': 53, 'keydate':'30/12/2018'  }
                   ]
    
    reduced_list = dict_reducer(list_of_dict)
    
    print(reduced_list)

    list1 = [{'contract': 'AB1'}, {'contract':'AB2'}, {'contract':'AB4'}]

    mapped_list = line_mapper(list1, reduced_list)
    
    print(mapped_list)
    
