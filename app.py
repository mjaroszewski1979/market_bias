from flask import Flask,render_template, url_for, request
from bias import adx, res_i, id_i, val_i, num_i, res_p, id_p, num_p, res_o, id_o, val_o, num_o
from strategies import top_index, nums
from send_mail import send_mail
import threading


app = Flask(__name__)
app.secret_key = 'secretkey1'
                 
@app.route('/')
def index():
    return render_template('index_min.html', adx=adx, res_i=res_i, id_i=id_i, val_i=val_i, num_i=num_i, res_p=res_p, id_p=id_p, num_p=num_p,
    res_o=res_o, id_o=id_o, val_o=val_o, num_o=num_o)

@app.route('/about')
def about():
    return render_template('about_min.html')

@app.route('/strategies')
def strategies():
    return render_template('strategies_min.html', top_index=top_index, nums=nums)

@app.route('/contact')
def contact():
    return render_template('contact_min.html')

@app.route('/success',methods=['GET', 'POST'] )
def success():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        t1 = threading.Thread(target=send_mail, args=[email])
        t1.start()
        return render_template('success_min.html', name=name, email=email)
    

@app.errorhandler(404)
def not_found(e):
    return render_template('404_min.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500_min.html'), 500


if __name__=='__main__':
    app.run(debug=True)
