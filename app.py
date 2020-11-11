from flask import Flask, render_template, request
app = Flask(__name__)

#Home
@app.route("/home")
def home():
	return render_template('home.html', the_title="Home")

#Personal page
@app.route("/aboutme")
def aboutme():
	return render_template('aboutme.html', the_title="About Me")
	
#Tech Page
@app.route("/comp_tech")
def comp_tech():
	return render_template('comp_tech.html', the_title="Computer Tech")

#Tech Page
@app.route("/comp_tech/tech1")
def tech1():
	return render_template('tech1.html', the_title="Tech 1")

#Tech Page
@app.route("/comp_tech/tech2")
def tech2():
	return render_template('tech2.html', the_title="Tech 2")	
	
#Tech Page
@app.route("/comp_tech/tech3")
def tech3():
	return render_template('tech3.html', the_title="Tech 3")

#Interests page
@app.route("/photos")
def photos():
	return render_template('photos.html', the_title="Photos")

#Portfolio
@app.route("/portfolio")
def portfolio():
	return render_template('portfolio.html', the_title="Portfolio")

#CV
@app.route("/cv")
def cv():
	return render_template('cv.html', the_title="CV")

#Contact
@app.route("/contact", methods=["GET", "POST"])
def contact():
        return render_template('contact.html', the_title="Contact")
		
if __name__ == "__main__":
    app.run()
