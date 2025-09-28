print("Running AL services...")

print("Importing: flask - Flask, render_template, send_file, jsonify, request, redirect")
from flask import Flask, render_template, send_file, jsonify, request, redirect
print("Importing hashlib")
import hashlib
print("Importing os")
import os

print("Creating admin password verification system...")
ADMIN_PASSWORD_HASH = os.environ.get('ADMIN_PASSWORD_HASH')
def verify_password(password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash == ADMIN_PASSWORD_HASH

print("Creating app...")
app = Flask(__name__)

print("Creating website...")

@app.errorhandler(404)
def not_found(error):
    """
    Глобальный обработчик 404 ошибок
    """
    app.logger.warning(f"404 Not Found: {request.path}")
    
    return jsonify({"error": "Resource not found"}), 404

@app.route("/icon", methods=["GET"])
def icon():
    return send_file("icon.png")

@app.route("/lesson/icon", methods=["GET"])
def lesson_icon():
    return send_file("lesson.png")

@app.route("/source/l2x94mfjsa8.js", methods=["GET"])
def source_admin_css():
    return send_file("static/admin.css")

@app.route("/source/l2x94mfjsa8.css", methods=["GET"])
def source_lesson1_js():
    return send_file("static/lesson1.js")

@app.route("/source/12dmedmwiqiw3rn.php", methods=["GET"])
def source_index_js():
    return send_file("static/index.js")

@app.route("/source/l241nddd28d.php", methods=["GET"])
def source_admin_js():
    return send_file("static/admin.js")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/lesson/<lessonNumber>", methods=["GET"])
def lesson(lessonNumber):
    if os.path.exists(os.path.join(os.getcwd(), f"templates/lesson{lessonNumber}.html")) == True:
        return render_template(f"lesson{lessonNumber}.html")
    else:
        return redirect("/lesson/1")

@app.route("/admin", methods=["GET"])
def admin():
    print("Someone opened admin page")
    return render_template("admin.html")

#@app.route("/admin/correct/<password>", methods=["GET"])
#def admin_correct(password):
#    return jsonify(password == "5800_adminz_pass_current*")

@app.route("/admin/check", methods=["POST"])
def admin_check():
    password = request.form.get("pass")
    if verify_password(password):
        return render_template("admin.dashboard.html")
    else:
        return redirect("/admin")

if __name__ == "__main__":
    print("Running app on http://127.0.0.1:5000")
    app.run(debug=True) 
else:
    print(f"__name__: {__name__} is not __main__")