from flask import Flask, request, g, redirect, render_template, url_for, flash, request
app = Flask(__name__)

# Homepage
@app.route('/')
def home():
	return render_template('index.html')

# Lists all the reports we've made
@app.route('/reports')
def reports():
	return render_template('reports/index.html')

# Generate New Report
@app.route('/reports/generate', methods=['POST'])
def generate_report():
	return redirect(url_for('reports'))

# Create a new report type
@app.route('/reports/build/add')
def add_report():
	return render_template('reports/add.html')

# Edit a report type
@app.route('/reports/build/edit/<id>')
def edit_report(id):
	return render_template('reports/add.html')

# Delete a report type
@app.route('/reports/build/delete/<id>')
def delete_report(id):
	return redirect(url_for('reports'))
	

if __name__ == "__main__":
    app.run()