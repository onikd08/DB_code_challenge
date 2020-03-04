import string
from flask import Flask, request, jsonify

app = Flask(__name__)

app.config['JSON_SORT_KEYS'] = False
@app.route('/analyze', methods=['POST'])
    

def post():
    
    new_task = {'text': request.json['text']}   
    text = (str(new_task.get('text')))
    
    with_space = len(text)
    
    space_counter = 0
    for ch in text:
        if ch == " ":
            space_counter += 1
            
    without_space = with_space - space_counter
    
    counted_words = []
    words = text.split()
    for word in words:
        if word not in counted_words:
            counted_words.append(word)

    total_words = len(counted_words)
    
    ch_list = list(text.lower())
    english_letters = list(string.ascii_lowercase)

    new_ch_list = sorted([ch for ch in ch_list if ch in english_letters])
    ch_dict = {}
    for i in new_ch_list:
        counter = new_ch_list.count(i)
        ch_dict[i] = counter
    
    return jsonify(
        {
        "textLength" :{"withSpaces" :with_space,"withoutSpaces" :without_space},
        "wordCount" :total_words,
        "characterCount" : ch_dict
        }), 201
    
if __name__ == "__main__":
    app.run(debug=True)
    


# curl -i -H "Content-Type: application/json" -X POST -d '{"text":"hello 2 times  "}' http://localhost:5000//analyze
