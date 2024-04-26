from flask import Flask, send_file, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
  
  return render_template('index.html', title='Main Page', dropdown_items=dropdown_items)

@app.route('/about')
def about():
    return render_template('about.html', title='About', dropdown_items=dropdown_items)  

@app.route('/authorise')
def authorisation():
    return render_template('authorisation-page.html', title='Enterance', dropdown_items=dropdown_items)

if __name__ == '__main__':
  dropdown_items = [
    {
      'name': 'Chairs',
      'items': [
        {'name': 'Soft Chairs'},
        {'name': 'Lether Chairs'},
        {'name': 'Plastic Chairs'}, 
        {'name': 'Wooden Chairs'},
        {'name': 'Metal Chairs'},
        {'name': 'Kitchen Dining Chairs'}
        ]
      },
    {
      'name': 'Category 2',
      'items': [
        {'name': 'Item 4'},
        {'name': 'Item 5'},
        {'name': 'Item 6'}
        ]
      },
    {
      'name': 'Tables',
      'items': [
        {'name': 'Kitchen Tables'},
        {'name': 'Dining Tables'},
        {'name': 'Glass Tables'}
      ]
    }
    ]
  app.run(debug=True)