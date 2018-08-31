from iomate.iomate_app import Blueprint, render_template, login_required

automation = Blueprint('automation', __name__)

@automation.route('/automation', methods=['GET'])
@login_required
def automation_view():
    return render_template('automation.html')


