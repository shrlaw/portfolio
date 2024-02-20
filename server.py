from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject},{message}')
def write_to_csv(data):
    with open('eggs4.csv', 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', 
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        writer.writerow([email, subject, message])
          
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    
    if request.method == 'POST':
        try:
            data = request.form.to_dict() 
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return ('Did not save to database')
    else:
        return "Something went wrong. Try again."

if __name__ == "__main__":
    app.run(debug=True)