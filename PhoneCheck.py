import re
from flask import Flask
from flask import request

class PhoneCheck:
    def phoneCheck(string):
         pattern = r"[+7]\s[(][0-9]{3}[)]\s[0-9]{3}[-][0-9]{2}[-][0-9]{2}"
         return "true" if re.findall(pattern, string) else "false"
        
    



app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def postik():
        if request.method == "POST":
             Phone = request.get_json().get('phone')
             Valid = PhoneCheck.phoneCheck(Phone)
             jsonchik = {
                  "valid": Valid
             }
             return jsonchik
        return '''
             <form method="POST">
                 <div></div>
             </form>'''

if __name__ == "__main__":
    app.run(port=8000, debug=True)