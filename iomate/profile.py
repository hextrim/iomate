from werkzeug.utils import secure_filename
from iomate.iomate_app import app, Blueprint, render_template, request, flash, redirect, login_required, db, os, verify_password, current_user
from iomate.models import User

profile = Blueprint('profile', __name__)

### PROFILE PIC UPLOAD ###
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@profile.route("/profile", methods=['GET', 'POST'])
@login_required
def profile_view():
    error = None
    if request.method == 'GET':
        page = request.args.get('page')
        return render_template('profile.html', page=page)
    elif request.method == 'POST':
        # check if the post request has the file part
        if 'profile_change_pic' in request.form:
            if 'file' not in request.files:
                flash('Please make sure you are submitting a file part request!','warning')
                return redirect(request.url)
            file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
            if file.filename == '':
                flash('Please select a file for upload!','warning')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                profile_pic = file.save(os.path.join(app.config['UPLOAD_CONFIG'], filename))
                user_pic = User.query.filter_by(email=current_user.email).first()
                user_pic.profile_pic = os.path.join(app.config['PROFILE_PICS_DIR'], filename)
                db.session.add(user_pic)
                db.session.commit()
                return redirect(request.url)
        elif 'profile_change_username' in request.form:
            if not request.form['profile_change_username']:
                flash('Please fill all the fields before sending a request!','danger')
            else:
                user = User.query.filter_by(email=current_user.email).first()
                user.username = request.form['profile_username']
                db.session.add(user)
                db.session.commit()
                flash('Your username details have been changed.','success')
        elif 'profile_change_email' in request.form:
            if not request.form['profile_change_email'] or request.form['profile_email'] == '':
                flash('Email address field cannot be empty for this request!','danger')
            else:
                user = User.query.filter_by(email=current_user.email).first()
                user.email = request.form['profile_email']
                db.session.add(user)
                db.session.commit()
                flash('Your email details have been changed.','success')
        elif 'profile_change_password' in request.form:
            if not request.form['profile_old_password'] or not request.form['profile_new_password'] or not request.form['profile_new_password_repeat']:
                flash('Please fill all the fields before sending a request!','danger')
            else:
                if request.form['profile_new_password'] != request.form['profile_new_password_repeat']:
                    flash('Please ensure you type the new password correctly!','danger')
                else:
                    user = User.query.filter_by(email=current_user.email).first()
                    profile_old_password = request.form['profile_old_password']
                    profile_old_password_hash = user.password
                    profile_password_verify = verify_password(profile_old_password, profile_old_password_hash)
                    if profile_password_verify != True:
                        flash('Please provide your old password for this request!','danger')
                    else:
                        user.password = request.form['profile_new_password']
                        db.session.add(user)
                        db.session.commit()
                        flash('Your password has been changed.','success')
    page = request.args.get('page')
    return render_template('profile.html', page=page)
