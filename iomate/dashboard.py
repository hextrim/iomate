from iomate.iomate_app import Blueprint, render_template

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/', methods=['GET'])
@dashboard.route('/dashboard', methods=['GET'])
#@login_required
def dashboard_view():
    return render_template('dashboard.html')


