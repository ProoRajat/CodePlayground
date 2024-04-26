text.upper()
if text == '':
    return 0
text_elements = list(text)
without_repetition = set(text)
      
no_of_repetition = [x.count(text_elements) for x in without_repetition]
        
    if no_of_repetition.count(1) == len(text_element):
        return 0
    elif no_of_repetition.count(1) == len(text_element) - 1:
        return 1
    else:
        return (x != 1 for x in no_of_repetition)