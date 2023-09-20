import json
from flask import Flask, redirect, url_for, render_template, request, session
import re
import logging.handlers

homepage = "home"
logger = logging.getLogger("my_loger")


def setLogging():
    LOG_FORMAT = "%(asctime)s - [%(levelname)s] - %(message)s"
    # logging.basicConfig(filename="test.log", level=logging.DEBUG, format=LOG_FORMAT)
    # logger = logging.getLogger("my_loger")
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    log_format = logging.Formatter(LOG_FORMAT)

    console_handler.setFormatter(log_format)

    file_handler = logging.FileHandler("my_test.log", encoding="utf-8")

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.debug("this is debug log")
    logger.info("this is info log")


def create_app():
    app = Flask(__name__, template_folder='./templates', static_folder='./static')
    # app.config.from_object(settings)
    # app.register_blueprint(login)
    setLogging()
    return app



app = create_app()
app.secret_key = '123456'


@app.route('/')
def home():  # put application's code here
    return render_template(homepage, title='kdkd')


#/lain/gpt
@app.route('/lain/gpt')
def lain():
    # 接受parament,解析json,调用接口
    request.form.g



def validate_string(pattern, input_string):
    # pattern = r'^BP(32|50|100|150|200|250|300|350|400|450|500|550)[bm]\d{1,3}-[304|316|tai|ni|mo|ha]-[0.5|0.6|0.7|0.8|1.0|1.2]-\d{0.1|0.16|0.2|0.25}Mpa-[epdm|nbr|fkm]-(304|316)衬套-[tan|304|316]接管-(1|2)$'

    if re.match(pattern, input_string):
        print("字符串验证通过")
        return True
    else:
        print("字符串验证失败")
        return False


if __name__ == '__main__':
    app.run()
