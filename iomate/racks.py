from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Racks

racks = Blueprint('racks', __name__)

@racks.route('/racks', methods=['GET', 'POST'])
@login_required
def racks_view():
    error = None
    if request.method == 'GET':
        return render_template('racks.html', racks=Racks.query.all())
    elif request.method == 'POST':
        if 'rack_add' in request.form:
            if not request.form['rack_name'] or not request.form['rack_location']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                rack = Racks(request.form['rack_name'], request.form['rack_location'])
                db.session.add(rack)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Rack Added</div>"
        elif 'rack_edit' in request.form:
            if not request.form['rack_name'] or not request.form['rack_location']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                rack_id = request.form.get('id')
                rack = Racks.query.filter_by(id=rack_id).one()
                rack.name=request.form['rack_name']
                rack.location=request.form['rack_location']
                db.session.add(rack)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Rack Edited</div>"
        elif 'rack_delete' in request.form:
            if not request.form['rack_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                rack_id = request.form.getlist('id')
                for u in rack_id:
                    rack  = Racks.query.filter_by(id=u).one()
                    db.session.delete(rack)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Rack Deleted</div>"
    return render_template('racks.html')
