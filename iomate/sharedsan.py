from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Sharedsan

sharedsan = Blueprint('sharedsan', __name__)

@sharedsan.route("/sharedsan", methods=['GET', 'POST'])
@login_required
def sharedsan_view():
    error = None
    if request.method == 'GET':
        return render_template('sharedsan.html', sharedsans=Sharedsan.query.all())
    elif request.method == 'POST':
        if 'sharedsan_add' in request.form:
            if not request.form['sharedsan_lunname'] or not request.form['sharedsan_lunsize']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                sharedsan = Sharedsan(request.form['sharedsan_lunname'], request.form['sharedsan_lunsize'])
                db.session.add(sharedsan)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>SharedSAN Added</div>"
        elif 'sharedsan_edit' in request.form:
            if not request.form['sharedsan_lunname'] or not request.form['sharedsan_lunsize']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                sharedsan_id = request.form.get('id')
                sharedsan = Sharedsan.query.filter_by(id=sharedsan_id).one()
                sharedsan.lunname=request.form['sharedsan_lunname']
                sharedsan.lunsize=request.form['sharedsan_lunsize']
                db.session.add(sharedsan)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>SharedSAN Edited</div>"
        elif 'sharedsan_delete' in request.form:
            if not request.form['sharedsan_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                sharedsan_id = request.form.getlist('id')
                for u in sharedsan_id:
                    sharedsan  = Sharedsan.query.filter_by(id=u).one()
                    db.session.delete(sharedsan)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>SharedSAN Deleted</div>"
    return render_template('sharedsan.html')

