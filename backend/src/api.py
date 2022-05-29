import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
!! Running this function will add one
'''
db_drop_and_create_all()

# ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''

@app.route('/drinks', methods=['GET'])
def get_drinks():

    all_drinks = Drink.query.all()
    drink_details = [d.short() for d in all_drinks]

    return jsonify({
        'success': True,
        'drinks': [d.short() for d in all_drinks]
    }), 200


@app.route('/drinks-detail', methods=['GET'])
@requires_auth('get:drinks-detail')
def get_drinks_detail(jwt):

    all_drinks = Drink.query.all()
    drink_details = [d.long() for d in all_drinks]

    return jsonify({
        'success': True,
        'drinks': drink_details
    }), 200



# I consulted with mentor, and conversation of other classmates and mentors to fix my issue.

@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(jwt):

    data = request.get_json()
    new_title = data.get('title', None)
    new_recipe = data.get('recipe', None)

    try:
        new_drink = Drink(
            title = new_title,
            recipe = json.dumps(new_recipe)
        )
        new_drink.insert()

        return jsonify({
            'success': True,
            'drinks': Drink.long(new_drink)
        }), 200

    except Exception as e:
        print(e)
        abort(422)


@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(jwt, id):
    data = request.get_json()
    updated_drink = Drink.query.filter(Drink.id==id).one_or_none()

    if updated_drink is None:
        abort(404)

    try:
        # new_title = data.get('title', None)
        # new_recipe = data.get('recipe', None)

        # updated_drink.title=new_title
        # updated_drink.recipe=json.dumps(new_recipe)
        # updated_drink.update()
        #
        # return jsonify({
        #     'success': True,
        #     'drinks': updated_drink.long()
        # }), 200

        if not data.get("title", None) is None:
            updated_drink.title=data.get("title")

        if not data.get("recipe", None) is None:
            updated_drink.recipe = json.dumps(data.get("recipe"))

        updated_drink.update()

        return jsonify({
            'success': True,
            'drinks': updated_drink.long()
        }), 200

    except Exception as e:
        print(e)
        abort(400)



@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(jwt, id):
    delete_drink = Drink.query.filter(Drink.id==id).one_or_none()

    if not delete_drink:
        abort(404)

    try:
        delete_drink.delete()

        return jsonify({
            'success': True,
            'delete': id
        }), 200

    except Exception as e:
        print(e)
        abort(422)




# Error Handling
'''
Example error handling for unprocessable entity
'''

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(400)
def invalid_header(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "invalid_header"
    }), 400


@app.errorhandler(401)
def token_expired(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "token expired"
    }), 401

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404



'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above
'''


'''
@TODO implement error handler for AuthError
    error handler should conform to general task above
'''

@app.errorhandler(AuthError)
def auth_error(error):
    print(error)
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code



if __name__ == "__main__":
    app.debug = True
    app.run()
