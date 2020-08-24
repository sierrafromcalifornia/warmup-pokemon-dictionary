from IPython.display import display, Markdown
import math
import json
import pickle
import os

answer_path = os.path.join('data','dictionary.json')

with open(answer_path, 'r') as fp:
    answer = json.load(fp)
    
class CheckDictionary():
    def __init__(self, dictionary):
        self.data = {}
        self.dictionary = dictionary
        
        for key in self.dictionary.keys():
            try:
                if math.isnan(self.dictionary[key]['stats']['type2']):
                    self.dictionary[key]['stats']['type2'] = 'None'
            except:
                continue

    def check_keys(self):
        keys = list(self.dictionary.keys())
        if all([x in ['Bayleef', 'Haunter', 'Poliwag', 'Pidgeotto', 'Kadabra'] for x in keys]):
            self.data['keys'] = 1
        else:
            self.data['keys'] = 0
        
    def check_values(self):
        nan = float('nan')
        self.answer = answer

        if list(self.dictionary.values()) == list(answer.values()):
            self.data['values'] = 1
        else:
            self.data['values'] = 0
            
    def results(self):
        check = '✅'
        X = '❌'
        correct = sum(self.data.values())
        
        if correct == len(self.data):
            header_emoji = check
        else:
            header_emoji = X
            
        
        header = '''# {} Your dictionary passed {} out of {} tests!\n\n'''.format(header_emoji, correct, len(self.data))
        
        
        

        if self.data['keys'] == 1:
            md = '''>{} *Dictionary Keys are correct!*'''.format(check)
            
        else:
            md = '''>{} *Dictionary Keys are incorrect*'''.format(X)
            
        md += "\n\n"    
        if self.data['values'] == 1:
            md += '''>{} *Dictionary data are correct!*'''.format(check)
        else:
            md += '''>{} *Dictionary data are incorrect.*'''.format(X)
            
        block = Markdown(header + md)
        
        display(block)
        
        
    def run(self):
        self.check_keys()
        self.check_values()
        self.results()
        
list_path = os.path.join('data', 'list.txt')       
with open(list_path, "rb") as fp:   # Unpickling
    list_test = pickle.load(fp)

class ListCheck():
    def __init__(self, list_):
        self.list = list_
        self.data = {}
        
    def check_length(self):
        if len(list_test) == len(self.list):
            self.data['length'] = 1
        else:
            self.data['length'] = 0
            
    def compare_lists(self):
        A = set(list_test)
        B = set(self.list)
        self.missing = A - B
        self.wrong = B - A
        
        if len(self.missing) == 0:
            if len(self.wrong) == 0:
                self.data['data'] = 1
            else:
                self.data['data'] = 0
        else:
                self.data['data'] = 0
                
        
        self.data['missing'] = self.missing
        self.data['wrong'] = self.wrong
        
    def results(self):
        check = '✅'
        X = '❌'
        if self.data['length'] == 1:
            md = '''>{} *List length is correct!*'''.format(check)
        else:
            md = '''>{} *List length is incorrect*'''.format(X)
            
        if len(self.data['missing']) > 0:
            number = len(self.data['missing'])
            md += '''\n\n>{} *List is missing {} data points* \n\n<details><summary>Click here to view what is missing.</summary>'''.format(X, number)
        
            for data in self.data['missing']:
                md += '''\n\n- {}'''.format(data)
                
            md += '</details>'
            
        if len(self.data['wrong']) > 0:
            number = len(self.data['wrong'])
            if number > 1:
                point = 'points'
            else:
                point = 'point'
            md += '''\n\n>{} *List contains {} incorrect data {}*\n\n\n\n<details><summary>Click here to view what data points are wrong</summary>'''.format(X, number, point)
            
            for data in self.data['wrong']:
                md +='''\n\n- {}'''.format(data)
                
            md += '</details>'
        else:
            md +='''\n\n>{} *List data are correct*'''.format(check)
            
        correct = self.data['length'] + self.data['data']
        md = '# Your list passed {} out of {} tests!\n\n'.format(correct, 2) + md
            
        md = Markdown(md)
        display(md)
            
    def run(self):
        self.check_length()
        self.compare_lists()
        self.results()
            