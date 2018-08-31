from iomate.iomate_app import Blueprint, render_template, request, flash, redirect, login_required

##IMPORT FROM IOMATE GLOBAL##
from iomate.iomate_global import get_deploy_device_last_build_log
from iomate.iomate_global import get_deploy_device_get_job_info


statistics = Blueprint('statistics', __name__)

@statistics.route("/statistics", methods=['GET', 'POST'])
@login_required
def statistics_view():
    deploy_sw_1 = get_deploy_device_last_build_log('deploy_sw_1')
    deploy_sw_1_job_info = get_deploy_device_get_job_info('deploy_sw_1')
    return render_template('statistics.html', deploy_sw_1=deploy_sw_1, deploy_sw_1_job_info=deploy_sw_1_job_info)
