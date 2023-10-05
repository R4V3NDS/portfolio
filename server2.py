from flask import Flask, render_template, url_for, request, redirect
import csv

# Create variable of the Flask class
# Remember, Capitals denote a Class
app = Flask(__name__)
#print(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# generalised function to work for any page
@app.route("/<string:page_name>")
def my_page(page_name):
	return render_template(page_name)

# function to write to a csv file 
def write_to_csv(data):
	# open in append mode
	with open("database.csv", mode ="a", newline='') as database2:
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_writer = csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subject, message])

# https://flask.palletsprojects.com/en/2.3.x/quickstart/#accessing-request-data
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == "POST":
		try:
			# request.form["email"]
			# request.form["subject"]
			# request.form["message"]
			#  convert all the data to a dict
			data = request.form.to_dict()
			#print(data)
			write_to_csv(data)
			#return "Form submitted"
			return redirect("/thankyou.html")
		except:
			return "did not save to database"
	else:
		"Something went wrong try again"


# # function to write the data to a txt file 
# def write_to_file(data):
# 	# open in append mode
# 	with open("database.txt", mode ="a") as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f'\n {email},{subject},{message}')