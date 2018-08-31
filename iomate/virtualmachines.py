from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required, db
from iomate.models import VirtualMachines

virtualmachines = Blueprint('virtualmachines', __name__)

@virtualmachines.route("/virtualmachines", methods=['GET', 'POST'])
@login_required
def virtualmachines_view():
    error = None
    if request.method == 'GET':
        return render_template('virtualmachines.html', vms=VirtualMachines.query.all())
    elif request.method == 'POST':
        if 'vm_add' in request.form:
            if not request.form['vm_hostname'] or not request.form['vm_ipaddress'] or not request.form['vm_subnet'] or not request.form['vm_gateway'] or not request.form['vm_portgroup'] or not request.form['vm_username'] or not request.form['vm_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vm = VirtualMachines(request.form['vm_hostname'], request.form['vm_ipaddress'], request.form['vm_subnet'], request.form['vm_gateway'], request.form['vm_portgroup'], request.form['vm_username'], request.form['vm_password'])
                db.session.add(vm)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>VM Added</div>"
        elif 'vm_edit' in request.form:
            if not request.form['vm_hostname'] or not request.form['vm_ipaddress'] or not request.form['vm_subnet'] or not request.form['vm_gateway'] or not request.form['vm_portgroup'] or not request.form['vm_username'] or not request.form['vm_password']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vm_id = request.form.get('id')
                vm = VirtualMachines.query.filter_by(id=vm_id).one()
                vm.hostname=request.form['vm_hostname']
                vm.ipaddress=request.form['vm_ipaddress']
                vm.subnet=request.form['vm_subnet']
                vm.gateway=request.form['vm_gateway']
                vm.portgroup=request.form['vm_portgroup']
                vm.username=request.form['vm_username']
                vm.password=request.form['vm_password']
                db.session.add(vm)
                db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>VM Edited</div>"
        elif 'vm_delete' in request.form:
            if not request.form['vm_delete']:
                return "<div class='alert alert-danger' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>ERROR</div>"
            else:
                vm_id = request.form.getlist('id')
                for u in vm_id:
                    vm  = VirtualMachines.query.filter_by(id=u).one()
                    db.session.delete(vm)
                    db.session.commit()
                return "<div class='alert alert-success' role='alert'><a href='#' class='close' data-dismiss='alert'>&times;</a>VM Deleted</div>"
    return render_template('virtualmachines.html')

