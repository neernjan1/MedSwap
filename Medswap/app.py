from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)



@app.route('/')
def homepage():
    return render_template('front.html')

@app.route('/front.html')
def backhome():
    return render_template('front.html')
@app.route('/team.html')
def team():
    return render_template('team.html')

@app.route('/page1.html')
def page1():
    return render_template('page1.html')

@app.route('/page2.html')
def page2():
    return render_template('page2.html')

@app.route('/page3.html')
def page3():
    return render_template('page3.html')
@app.route('/location.html')
def location_page():
    
    return render_template("location.html")
@app.route('/location',methods= ['POST'])
def location():
    
        user_input = request.form.get('location_string')
        print(user_input)
        image_filename = "images/"+user_input+".png"
        return render_template('location.html', image_filename=image_filename)
        



        
    

@app.route('/submit',methods = ['POST'])
def search():
    
    search_keywords = request.form.get('input_string').split()
    


    # Load your CSV file into a DataFrame (replace 'your_data.csv' with your file's name)
    df = pd.read_csv('SheetCopy2.csv')

    # Initialize variables to track the best match and its score
    best_match = None
    best_score = -1  # Use a lower value if your scores are always positive

    # Iterate through rows and calculate a score for each match based on the number of matching keywords
    for index, row in df.iterrows():
        # Calculate a score for this row based on keywords
        score = sum(keyword.lower() in ' '.join(row.astype(str).str.lower()) for keyword in search_keywords)
        
        # If the current row has a higher score, update the best match
        if score > best_score:
            best_match = row
            best_score = score

    # Calculate the percentage of matching keywords
    percentage_matched = (best_score / len(search_keywords)) * 100

    # Display the best matching row and the percentage matched
    if best_match is not None:
        
        output_string = f"Best matching row: {best_match}  percentage matched: {percentage_matched:.2f}"
        return render_template("output.html" , output = output_string)
    else:
        output_string = "no result found correspondng to search"
        return render_template("output.html" , output = output_string)





if __name__ == '__main__':
    app.run(debug=True , port=8000)

