from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Vstorage

vstorage = Blueprint('vstorage', __name__)

@vstorage.route("/vstorage", methods=['GET', 'POST'])
@login_required
def vstorage_view():
    error = None
    if request.method == 'GET':
        return render_template('vstorage.html', vstorages=Vstorage.query.all())
    elif request.method == 'POST':
        if 'vstorage_add' in request.form:
            if not request.form['vstorage_name']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vstorage = Vstorage(request.form['vstorage_name'])
                db.session.add(vstorage)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vStorage Added</div>"
        elif 'vstorage_edit' in request.form:
            if not request.form['vstorage_name']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vstorage_id = request.form.get('id')
                vstorage = Vstorage.query.filter_by(id=vstorage_id).one()
                vstorage.name=request.form['vstorage_name']
                db.session.add(vstorage)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vStorage Edited</div>"
        elif 'vstorage_delete' in request.form:
            if not request.form['vstorage_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vstorage_id = request.form.getlist('id')
                for u in vstorage_id:
                    vstorage  = Vstorage.query.filter_by(id=u).one()
                    db.session.delete(vstorage)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>vStorage Deleted</div>"
    return render_template('vstorage.html')


