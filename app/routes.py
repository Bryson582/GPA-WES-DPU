from flask import render_template,Response
from app import app
from app.form import MailForm
import app.run.main as arm
import app.run.Plot as arp
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


@app.route('/',methods = ['GET','POST'])
def index():
    form = MailForm()
    if form.validate_on_submit():
        name = form.name.data
        pwd = form.pwd.data
        final = arm.rundemo(name,pwd)
        return render_template('flash.html',final=round(final,2))
    return render_template('index.html',form=form)


@app.route('/plot.png')
def plot_png():
    print(">>>>>>>>>>>>>>")
    fig = arp.avgPlot()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')





