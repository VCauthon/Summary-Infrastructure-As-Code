from functools import wraps
from typing import List

from flask import render_template, Blueprint, request, redirect, url_for

from service.database import Database
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


@bp.route("/backoffice/", methods=["GET"])
def main():
    pages = get_values_list()
    return render_template("index.html", pages=pages)


@bp.route("/backoffice/page", methods=["POST"])
def create_page():
    """Create a new page entry."""
    page = request.form.get("page", "").strip()
    url = request.form.get("url", "").strip()
    counter_raw = request.form.get("counter", "0").strip() or "0"

    try:
        counter = int(counter_raw)
    except ValueError:
        counter = 0

    if not page or not url:
        return redirect(url_for("main.main"))

    record = WebPage(page=page, url=url, counter=counter)
    DATABASE.save_page(record)

    pages = get_values_list()
    return render_template("index.html", pages=pages)


@bp.route("/backoffice/page/<string:page_name>", methods=["POST"])
def update_or_delete_page(page_name: str):
    """Update or delete an existing page."""
    action = request.form.get("action")

    if action == "delete":
        DATABASE.delete_page(page_name)
        return redirect(url_for("main.main"))

    # Default action: save/update
    url = request.form.get("url", "").strip()
    counter_raw = request.form.get("counter", "0").strip() or "0"

    try:
        counter = int(counter_raw)
    except ValueError:
        counter = 0

    if not url:
        return redirect(url_for("main.main"))

    record = WebPage(page=page_name, url=url, counter=counter)
    DATABASE.save_page(record)

    pages = get_values_list()
    return render_template("index.html", pages=pages)
