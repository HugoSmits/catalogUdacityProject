from flask import Flask, flash
from flask import render_template, url_for
from flask import request, redirect
from flask import Session, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/JSON')
def restaurantJSON():
    restaurant = session.query(Restaurant).all()
    return jsonify(Restaurant=[i.serialize for i in restaurant])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return jsonify(MenuItems=[i.serialize for i in items])


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menuItem = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).\
        filter_by(id=menu_id).one()
    return jsonify(MenuItem=[menuItem.serialize])


@app.route('/')
@app.route('/restaurants/')
def showRestaurant():
    restaurant = session.query(Restaurant).all()
    # return 'This page will show all of my Restaurants!'
    return render_template('restaurant.html', restaurants=restaurant)


@app.route('/restaurant/new',
           methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        # save the album
        newItem = Restaurant(
            name=request.form['name'])
        session.add(newItem)
        session.commit()
        flash('Restaurant created successfully!')
        return redirect(url_for('showRestaurant'))
    # return 'This page will create a new Restaurant!'
    else:
        return render_template('restaurantNew.html')


@app.route('/restaurants/<int:restaurant_id>/edit')
def editRestaurant(restaurant_id):
    editedItem = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        session.add(editedItem)
        session.commit()
        flash('Restaurant edited successfully!')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    # return 'This page will edit Restaurant %s' % restaurant_id
    else:
        return render_template(
            'restaurantEdit.html',
            restaurant_id=restaurant_id,
            item=editedItem)


@app.route('/restaurants/<int:restaurant_id>/delete')
def deleteRestaurant(restaurant_id):
    itemToDelete = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Restaurant deleted successfully!')
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
        # return 'This page will delete menu %s for Restaurant %s' % menu_id ,
        # restaurant_id
    else:
        return render_template(
            'restaurantDelete.html',
            restaurant_id=restaurant_id,
            item=itemToDelete)


@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    menu = session.query(MenuItem).filter_by(restaurant_id=restaurant.id).all()
    # return 'This page will show all menus from Restaurant %s' % restaurant_id
    return render_template('menu.html', restaurant=restaurant, menus=menu)


@app.route('/restaurant/<int:restaurant_id>/menu/new',
           methods=['GET', 'POST'])
def newMenu(restaurant_id):
    if request.method == 'POST':
        # save the album
        newItem = MenuItem(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            course=request.form['course'],
            restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash('Menu created successfully!')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('menuNew.html', restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit',
           methods=['GET', 'POST'])
def editMenu(restaurant_id, menu_id):
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        flash('Menu edited successfully!')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template(
            'menuEdit.html',
            restaurant_id=restaurant_id,
            menu_id=menu_id,
            item=editedItem)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete',
           methods=['GET', 'POST'])
def deleteMenu(restaurant_id, menu_id):
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Menu deleted successfully!')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
        # return 'This page will delete menu %s for Restaurant %s' % menu_id ,
        # restaurant_id
    else:
        return render_template(
            'menuDelete.html',
            restaurant_id=restaurant_id,
            menu_id=menu_id,
            item=itemToDelete)


if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
