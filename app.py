from flask import Flask, request, render_template, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/api", methods=["POST"])
def api():
	result = subprocess.run(["python", "-c", request.data.decode("utf-8")], capture_output=True)
	return jsonify({
		"returncode": result.returncode,
        "stdout": result.stdout.decode("utf-8"),
        "stderr": result.stderr.decode("utf-8"),
	})

if __name__ == "__main__":
	app.run(debug=True)
