from os import getenv
from typing import Tuple, Union, List
from functools import wraps


from flask import render_template, Blueprint, jsonify


from service.database import  Database
from service.models.page_items import WebPage


bp = Blueprint("main", __name__)


DATABASE = Database()


def retry_call(func):
    """Makes a couple of retries before giving up"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        error = None
        for _ in range(5):
            try:
                return func(*args, **kwargs)
            except Exception as err:
                error = err
        else:
            raise error
    return wrapper


@retry_call
def get_values_list() -> List[WebPage]:
    return DATABASE.get_pages()


@bp.route("/")
def main():
    return render_template("index.html", pages=[val.to_dict() for val in get_values_list()])


@retry_call
def increase_counter(value: WebPage) -> WebPage:
    value.counter += 1
    DATABASE.update_value(value)
    return value


@bp.route('/increment_counter/<site>', methods=['POST'])
def increment_counter(site):
    # Flattens all the values of the service in one Dictionary
    values = {val.page.lower(): val for val in get_values_list()}

    if not values.get(site):
        return jsonify({'error': 'Invalid site'}), 400

    value = increase_counter(values.get(site))
    new_count = int(value.counter)

    return jsonify({'count': new_count})
