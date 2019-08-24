import sys

OUTPUT_TYPE = 'Output'
ANSWER_TYPE = 'Answer'
GOTO_TYPE = 'Goto'
CONCLUSION_TYPE = 'Conclusion'

HOPPER_MESSAGE_PREFIX = 'Hopper: '
USER_MESSAGE_PREFIX = 'User: '
CONCLUSION_MESSAGE_PREFIX = 'Conclusion: '

class Output:
    def __init__(self, text, label=None):
        self.text = text
        self.label = label
        self.type = OUTPUT_TYPE
    def __str__(self):
        return 'Output({}, label={})'.format(self.text, self.label)
          

class Answer:
    def __init__(self, text):
        self.text = text
        self.type = ANSWER_TYPE
    def __str__(self):
        return 'Answer({})'.format(self.text)

      
class Goto:
    def __init__(self, label):
        self.label = label
        self.type = GOTO_TYPE
    def __str__(self):
        return 'Goto({})'.format(self.label)

      
class Conclusion:
    def __init__(self, text):
        self.text = text
        self.type = CONCLUSION_TYPE
    def __str__(self):
        return 'Conclusion({})'.format(self.text)
      
      
class IndentationAndInputObject:
    def __init__(self, indentation, input_object):
        self.indentation = indentation
        self.input_object = input_object

def print_conversation(flat_tree, user_answers):
    # Write your solution below
    # Some example code is provided to show you how to access our data structures, feel free to modify/delete
    cur_indent, res = 0, []
    response = 0 
    chosen = True
    label_dictionary = {}
    for i, v in enumerate(flat_tree):
        if v.input_object.type == OUTPUT_TYPE:
            label_dictionary[v.input_object.label] = i
    i = 0 
    answers = []
    while i < len(flat_tree):
        row = flat_tree[i]
        i += 1 
        if row.input_object.type == OUTPUT_TYPE and row.indentation == cur_indent and chosen:
            res.append(row)
        elif row.input_object.type == ANSWER_TYPE:
            answers.append(row.input_object.text)
            if user_answers[response] == row.input_object.text:
                res.append(row)
                response += 1 
                cur_indent += 2 
                chosen = True
            else:
                if i == len(flat_tree)-1:
                    res.append("User: "+user_answers[response])
                    response += 1 
                    res.append("Hopper: Invalid input") 
                    for j in range(response, len(user_answers)):
                        res.append("User: " + user_answers[j])
                    res.append("Conclusion: Goodbye!")
                    break 
                chosen = False
        elif row.input_object.type == GOTO_TYPE and chosen:
            i = label_dictionary[row.input_object.label]
        
        elif row.input_object.type == CONCLUSION_TYPE and chosen:
            res.append(row)
            break 

    for row in res:
        if type(row) == str:
            print(row)
        elif row.input_object.type == OUTPUT_TYPE:
            print(HOPPER_MESSAGE_PREFIX + row.input_object.text)
        elif row.input_object.type == ANSWER_TYPE:
            print(USER_MESSAGE_PREFIX + row.input_object.text)
        elif row.input_object.type == CONCLUSION_TYPE:
            print(CONCLUSION_MESSAGE_PREFIX + row.input_object.text)

    # for row in flat_tree:
    #     if row.input_object.type == OUTPUT_TYPE:
    #         print(HOPPER_MESSAGE_PREFIX + row.input_object.text)
    #     elif row.input_object.type == ANSWER_TYPE:
    #         print(USER_MESSAGE_PREFIX + row.input_object.text)
    #     elif row.input_object.type == CONCLUSION_TYPE:
    #         print(CONCLUSION_MESSAGE_PREFIX + row.input_object.text)

def parse_line(line):
    def parse_spaces_and_line(line):
        for i, c in enumerate(line):
            if c != ' ':
                return len(line[:i]), line[i:]
        raise RuntimeError("Found all whitespace line")
        
    def parse_label_and_output(line_content):
        for i, c in enumerate(line_content):
            if not c.isdigit():
                if c == ':' and i > 0:
                    return int(line_content[:i]), line_content[i+1:]
                else:
                    return None, line_content
        return None, line_content
      
    indentation, line_content = parse_spaces_and_line(line)
    if line_content.startswith('-'):
        return IndentationAndInputObject(indentation, Answer(line_content[1:]))
    elif line_content.startswith('='):
        return IndentationAndInputObject(indentation, Conclusion(line_content[1:]))
    elif line_content.startswith('>'):
        return IndentationAndInputObject(indentation, Goto(int(line_content[1:])))
    else:
        label, output = parse_label_and_output(line_content)
        return IndentationAndInputObject(indentation, Output(output, label))

  
def read_input():
    tree = []
    answers = []
    reading_examples = False
    for line in sys.stdin.readlines():
        line = line.rstrip()
        if line == '---':
            reading_examples = True
        elif not reading_examples:
            tree.append(parse_line(line))
        else:
            answers.append(line)
    return tree, answers
  
  
flat_tree, user_answers = read_input()
print_conversation(flat_tree, user_answers)