from flask import Flask, request, jsonify, abort

app = Flask(__name__)

DIRECTIONS = ['UP', 'DOWN']


def do_stuff(curtain_id, direction):
    pass


@app.route("/api", methods=["POST"])
def api():
    data = request.form
    if "curtain_id" not in data or "direction" not in data or data['direction'] not in DIRECTIONS:
        return abort(400)

    curtain_id = data['curtain_id']
    direction = data['direction']

    do_stuff(curtain_id, direction)

    return jsonify(success=True)


if __name__ == '__main__':
    app.run()
