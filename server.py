from flask import Flask, request, jsonify,render_template
app = Flask(__name__)


# Основной маршрут для веб-приложения
@app.route('/kvest_app', methods=['GET'])
def webapp():
    return render_template('kvest.html')
if __name__ == '__main__':
  # Запускаем Flask-приложение  
    app.run(debug=True, use_reloader=False)  # use_reloader=False, чтобы избежать повторного запуска  