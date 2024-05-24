from flask import Flask, send_file, render_template, redirect, url_for, current_app
import os
import json

app = Flask(__name__)

def load_json_data(base_dir):
    data = {}
    for category_dir in os.listdir(base_dir):
        category, sub_category = category_dir.split('_')
        category_data = data.setdefault(category, {}).setdefault(sub_category, {'items': []})
        
        category_path = os.path.join(base_dir, category_dir)
        for file_name in os.listdir(category_path):
            if file_name.endswith('.json'):
                file_path = os.path.join(category_path, file_name)
                with open(file_path, 'r') as f:
                    product_data = json.load(f)
                    category_data['items'].append(product_data)
    
    return data
  
def list_template_names():
    templates_dir = os.path.join(current_app.root_path, 'templates')
    template_names = []
    
    for root, dirs, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.html'):
                file_name = os.path.splitext(file)[0] 
                template_names.append(file_name)
    
    return template_names

@app.route('/')
def home():
    return render_template('index.html', title='Main Page',
                           dropdown_items=dropdown_items,
                           Items=Items,
                           products_data=products_data)

@app.route('/<string:doc_name>')
def about(doc_name: str):
    if (doc_name not in templates):
      # Handle exception
      pass
    return render_template('{}.html'.format(doc_name), title=doc_name,
                           dropdown_items=dropdown_items,
                           products_data=products_data,
                           Items=Items)  

def find_id(product_list, id: int) -> int:
    for index, item in enumerate(product_list):
        if item['id'] == id:
            return index
    return None

@app.route('/Item/<string:category>/<string:sub_category>/<int:id>')
def getItem(category: str, sub_category: str, id: int):
    item_name = dropdown_items[category]['items'][id - 1]['name']
    title = f'{item_name}'
    product_list = products_data[category][sub_category]['items']
    index = find_id(product_list, id)
    
    if index is not None:
        product_data = product_list[index]
    else:
        product_data = None  # Handle the case where the product is not found
    
    # Render a template for displaying a specific product
    return render_template('product.html', title=title, 
                           dropdown_items=dropdown_items,
                           product_data=product_data)

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
    'Tables': {
        'items': [
            {'name': 'Kitchen Tables'},
            {'name': 'Dining Tables'},
            {'name': 'Glass Tables'}
        ]
    }
}
  Items = { 
           ('Home', 'index'): True,
           ('About', 'about'): True,
           ('Contacts', 'contacts'): False,
           ('Stores', 'stores'): False
           }
  with app.app_context():
    templates = list_template_names()
  base_dir = 'data'
  products_data = load_json_data(base_dir)
  app.run(debug=True)