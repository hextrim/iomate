from werkzeug.utils import secure_filename
from iomate.iomate_app import app, Blueprint, render_template, request, flash, redirect, login_required, db, os
from iomate.models import Isos

isos = Blueprint('isos', __name__)

### ISO UPLOAD ###
ALLOWED_EXTENSIONS_ISO = set(['iso', 'ISO'])

def allowed_file_iso(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_ISO

@isos.route("/isos", methods=['GET', 'POST'])
@login_required
def isos_view():
    error = None
    if request.method == 'GET':
        return render_template('isos.html', isos=Isos.query.all())
    elif request.method == 'POST':
        if 'iso_add' in request.form:
            if not request.form['iso_name']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                iso = Isos(request.form['iso_name'])
                db.session.add(iso)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ISO Added</div>"
        elif 'iso_edit' in request.form:
            if not request.form['iso_name']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                iso_id = request.form.get('id')
                iso = Isos.query.filter_by(id=iso_id).one()
                iso.name=request.form['iso_name']
                db.session.add(iso)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ISO Edited</div>"
        elif 'iso_delete' in request.form:
            if not request.form['iso_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                iso_id = request.form.getlist('id')
                for u in iso_id:
                    iso  = Isos.query.filter_by(id=u).one()
                    db.session.delete(iso)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ISO Deleted</div>"
        elif 'iso_upload' in request.form:
            if 'file' not in request.files:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>No File in Request</div>"
            file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
            if file.filename == '':
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Filename Empty</div>"
            if file and allowed_file_iso(file.filename):
                filename = secure_filename(file.filename)
                iso_file = file.save(os.path.join(app.config['UPLOAD_CONFIG_ISO'], filename))
                iso_id = request.form.get('dataid')
                iso_id_strip = iso_id[3:]
                iso = Isos.query.filter_by(id=iso_id_strip).first()
#               # iso.filename = request.files['iso_upload']
                iso.filename = filename
                iso.filepath = os.path.join(app.config['UPLOAD_DIR_ISO'], filename)
                db.session.add(iso)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ISO Uploaded</div>"
    return render_template('isos.html')


