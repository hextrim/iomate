from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Snapshots

snapshots = Blueprint('snapshots', __name__)

@snapshots.route("/snapshots", methods=['GET', 'POST'])
@login_required
def snapshots_view():
    error = None
    if request.method == 'GET':
        return render_template('snapshots.html', snapshots=Snapshots.query.all())
    elif request.method == 'POST':
        if 'snapshot_add' in request.form:
            if not request.form['snapshot_name'] or not request.form['snapshot_path']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                snapshot = Snapshots(request.form['snapshot_name'], request.form['snapshot_path'])
                db.session.add(snapshot)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Snapshot Added</div>"
        elif 'snapshot_edit' in request.form:
            if not request.form['snapshot_name'] or not request.form['snapshot_path']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                snapshot_id = request.form.get('id')
                snapshot = Snapshots.query.filter_by(id=snapshot_id).one()
                snapshot.name=request.form['snapshot_name']
                snapshot.path=request.form['snapshot_path']
                db.session.add(snapshot)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Snapshot Edited</div>"
        elif 'snapshot_delete' in request.form:
            if not request.form['snapshot_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                snapshot_id = request.form.getlist('id')
                for u in snapshot_id:
                    snapshot = Snapshots.query.filter_by(id=u).one()
                    db.session.delete(snapshot)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Snapshot Deleted</div>"
    return render_template('snapshots.html')

