from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import Templates

templates = Blueprint('templates', __name__)

@templates.route("/templates", methods=['GET', 'POST'])
@login_required
def templates_view():
    error = None
    if request.method == 'GET':
        return render_template('templates.html', templates=Templates.query.all())
    elif request.method == 'POST':
        if 'template_add' in request.form:
            if not request.form['template_name'] or not request.form['template_path']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                template = Templates(request.form['template_name'], request.form['template_path'])
                db.session.add(template)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Template Added</div>"
        elif 'template_edit' in request.form:
            if not request.form['template_name'] or not request.form['template_path']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                template_id = request.form.get('id')
                template = Templates.query.filter_by(id=template_id).one()
                template.name=request.form['template_name']
                template.path=request.form['template_path']
                db.session.add(template)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Template Edited</div>"
        elif 'template_delete' in request.form:
            if not request.form['template_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                template_id = request.form.getlist('id')
                for u in template_id:
                    template = Templates.query.filter_by(id=u).one()
                    db.session.delete(template)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>Template Deleted</div>"
    return render_template('templates.html')
