from flask import Flask, render_template_string
import os
from jinja2 import FileSystemLoader, ChoiceLoader

# テンプレートフォルダをルートディレクトリに設定
template_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_dir, static_folder=template_dir, static_url_path='')

# Jinja2のローダーをカスタマイズして_includesフォルダも検索パスに追加
jinja_env = app.jinja_env
jinja_env.loader = ChoiceLoader([
    FileSystemLoader(template_dir),
    FileSystemLoader(os.path.join(template_dir, '_includes'))
])

@app.route("/")
def home():
    with open(os.path.join(template_dir, "index.html"), encoding="utf-8") as f:
        template = f.read()
    template = template.replace(
        "{% include achievements.html %}", "{% include 'achievements.html' %}"
    )
    if template.startswith("---"):
        template = template.split("---", 2)[-1]
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True)
