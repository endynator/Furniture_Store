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

@app.route('/Item/<string:category>/<int:id>')
def getItem(category: str, id: int):
    item_name = dropdown_items[category]['items'][id - 1]['name']
    title = f'{item_name}'
    return render_template('index.html', title=title, dropdown_items=dropdown_items)

if __name__ == '__main__':
  dropdown_items = {
    'Chairs': {
        'items': [
            {'name': 'Soft Chairs'},
            {'name': 'Lether Chairs'},
            {'name': 'Plastic Chairs'}, 
            {'name': 'Wooden Chairs'},
            {'name': 'Metal Chairs'},
            {'name': 'Kitchen Dining Chairs'}
        ]
    },
    'Category 2': {
        'items': [
            {'name': 'Item 4'},
            {'name': 'Item 5'},
            {'name': 'Item 6'}
        ]
    },
    'Tables': {
        'items': [
            {'name': 'Kitchen Tables'},
            {'name': 'Dining Tables'},
            {'name': 'Glass Tables'}
        ]
    }
}
  for category, data in dropdown_items.items():
    for i, item in enumerate(data['items'], start=1):
        item['id'] = i
  app.run(debug=True)