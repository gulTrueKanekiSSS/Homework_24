import os
from typing import Optional, Union

from flask import Flask, request, abort, jsonify
from functions import commands

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query")
def perform_query():
    file_name: Optional[str] = request.args.get('file_name')
    command_1: Optional[str] = request.args.get('cmd1')
    command_2: Optional[str] = request.args.get('cmd2')
    value_1: Optional[str] = request.args.get('val1')
    value_2: Optional[str] = request.args.get('val2')

    if not value_1 and value_2 and file_name:
        abort(400, 'Недостаточно данных')

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400, "File not found")

    with open(file_name, 'r') as file:
        result: Union[list, str] = commands(command_1, value_1, file)
        if command_2 and value_2:
            result = commands(command_2, value_2, file)
    return jsonify(result)


if __name__ == "__main__":
    app.run()

