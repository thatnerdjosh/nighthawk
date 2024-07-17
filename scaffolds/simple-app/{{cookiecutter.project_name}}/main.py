{%- if cookiecutter.generate_api -%}
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run(host='0.0.0.0', port=8000)
{% else -%}
def main() -> int:
    return 0

if __name__ == "__main__":
    main()
{% endif -%}
