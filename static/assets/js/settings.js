// Tooltips on ready
$(document).ready(function() {
	// Add User
        $("#user_email").tooltip({
                container: 'body'
        });
        $("#user_name").tooltip({
                container: 'body'
        });
        $("#user_password").tooltip({
                container: 'body'
        });
        $("#user_active").tooltip({
                container: 'body'
        });
        $("#user_role").tooltip({
                container: 'body'
        });

	// Add vCenter
        $("#vc_hostname").tooltip({
                container: 'body'
        });
        $("#vc_ipaddress").tooltip({
                container: 'body'
        });
        $("#vc_subnet").tooltip({
                container: 'body'
        });
        $("#vc_gateway").tooltip({
                container: 'body'
        });
        $("#vc_username").tooltip({
                container: 'body'
        });
        $("#vc_password").tooltip({
                container: 'body'
        });

        // Add ESXi
        $("#esxi_hostname").tooltip({
                container: 'body'
        });
        $("#esxi_ipaddress").tooltip({
                container: 'body'
        });
        $("#esxi_subnet").tooltip({
                container: 'body'
        });
        $("#esxi_gateway").tooltip({
                container: 'body'
        });
        $("#esxi_username").tooltip({
                container: 'body'
        });
        $("#esxi_password").tooltip({
                container: 'body'
        });

        // Add DedicatedSAN
        $("#dedicatedsan_hostname").tooltip({
                container: 'body'
        });
        $("#dedicatedsan_ipaddress").tooltip({
                container: 'body'
        });
        $("#dedicatedsan_subnet").tooltip({
                container: 'body'
        });
        $("#dedicatedsan_gateway").tooltip({
                container: 'body'
        });
        $("#dedicatedsan_port").tooltip({
                container: 'body'
        });
        $("#dedicatedsan_provider").tooltip({
                container: 'body'
        });
        $("#dedicatedsan_username").tooltip({
                container: 'body'
        });
        $("#dedicatedsan_password").tooltip({
                container: 'body'
        });

        // Add Firewall
        $("#fw_hostname").tooltip({
                container: 'body'
        });
        $("#fw_ipaddress").tooltip({
                container: 'body'
        });
        $("#fw_subnet").tooltip({
                container: 'body'
        });
        $("#fw_gateway").tooltip({
                container: 'body'
        });
        $("#fw_mgmtnetwork").tooltip({
                container: 'body'
        });
        $("#fw_mgmtsubnet").tooltip({
                container: 'body'
        });

        // Add IPS
        $("#ips_hostname").tooltip({
                container: 'body'
        });
        $("#ips_ipaddress").tooltip({
                container: 'body'
        });
        $("#ips_subnet").tooltip({
                container: 'body'
        });
        $("#ips_gateway").tooltip({
                container: 'body'
        });
        $("#ips_username").tooltip({
                container: 'body'
        });
        $("#ips_password").tooltip({
                container: 'body'
        });

        // Add Rack
        $("#rack_name").tooltip({
                container: 'body'
        });
        $("#rack_location").tooltip({
                container: 'body'
        });

        // Add Subnet
        $("#subnet_name").tooltip({
                container: 'body'
        });
        $("#subnet_network").tooltip({
                container: 'body'
        });
        $("#subnet_mask").tooltip({
                container: 'body'
        });

	// Add Switch
        $("#switch_hostname").tooltip({
                container: 'body'
        });
        $("#switch_ip").tooltip({
                container: 'body'
        });
        $("#switch_subnet").tooltip({
                container: 'body'
        });
        $("#switch_gateway").tooltip({
                container: 'body'
        });
        $("#switch_mgmtvlan").tooltip({
                container: 'body'
        });

        // Add vDSswitch
        $("#vds_name").tooltip({
                container: 'body'
        });
        $("#vds_nic1").tooltip({
                container: 'body'
        });
        $("#vds_nic2").tooltip({
                container: 'body'
        });
        $("#vds_datacenter").tooltip({
                container: 'body'
        });
        $("#vds_portgroup").tooltip({
                container: 'body'
        });
        $("#vds_portgroupvlan").tooltip({
                container: 'body'
        });


        // Add vSswitch
        $("#vs_name").tooltip({
                container: 'body'
        });
        $("#vs_ipaddress").tooltip({
                container: 'body'
        });
        $("#vs_subnet").tooltip({
                container: 'body'
        });
        $("#vs_gateway").tooltip({
                container: 'body'
        });
        $("#vs_nic1").tooltip({
                container: 'body'
        });
        $("#vs_nic2").tooltip({
                container: 'body'
        });


	// Add VirtualMachine
        $("#vm_hostname").tooltip({
                container: 'body'
        });
        $("#vm_ipaddress").tooltip({
                container: 'body'
        });
        $("#vm_subnet").tooltip({
                container: 'body'
        });
        $("#vm_gateway").tooltip({
                container: 'body'
        });
        $("#vm_portgroup").tooltip({
                container: 'body'
        });
        $("#vm_username").tooltip({
                container: 'body'
        });
        $("#vm_password").tooltip({
                container: 'body'
        });

        // Add VLAN
        $("#vlan_name").tooltip({
                container: 'body'
        });
        $("#vlan_id").tooltip({
                container: 'body'
        });
	
	// Add Server
        $("#server_hostname").tooltip({
                container: 'body'
        });
        $("#server_ipaddress").tooltip({
                container: 'body'
        });
        $("#server_subnet").tooltip({
                container: 'body'
        });
        $("#server_gateway").tooltip({
                container: 'body'
        });
        $("#server_username").tooltip({
                container: 'body'
        });
        $("#server_password").tooltip({
                container: 'body'
        });

	//Add Router
        $("#router_hostname").tooltip({
                container: 'body'
        });
        $("#router_ipaddress").tooltip({
                container: 'body'
        });
        $("#router_subnet").tooltip({
                container: 'body'
        });
        $("#router_gateway").tooltip({
                container: 'body'
        });
        $("#router_mgmtport").tooltip({
                container: 'body'
        });

	//Add SharedSAN
        $("#sharedsan_lunname").tooltip({
                container: 'body'
        });
        $("#sharedsan_lunsize").tooltip({
                container: 'body'
        });

	//Add NAS
        $("#nas_hostname").tooltip({
                container: 'body'
        });
        $("#nas_ipaddress").tooltip({
                container: 'body'
        });
        $("#nas_subnet").tooltip({
                container: 'body'
        });
        $("#nas_gateway").tooltip({
                container: 'body'
        });
        $("#nas_port").tooltip({
                container: 'body'
        });
        $("#nas_provider").tooltip({
                container: 'body'
        });
        $("#nas_username").tooltip({
                container: 'body'
        });
        $("#nas_password").tooltip({
                container: 'body'
        });

	//Add vStorage
        $("#vstorage_name").tooltip({
                container: 'body'
        });

	//Add Snapshot
        $("#snapshot_name").tooltip({
                container: 'body'
        });
        $("#snapshot_path").tooltip({
                container: 'body'
        });

	//Add ISO
        $("#iso_name").tooltip({
                container: 'body'
        });
        $("#iso_upload").tooltip({
                container: 'body'
        });

        //Add Template
        $("#template_name").tooltip({
                container: 'body'
        });
        $("#template_path").tooltip({
                container: 'body'
        });

});



// Tooltips after AJAX
$(document).ajaxComplete(function(){
	// Permissions
	$(".edit").tooltip({
		container: 'body'
	});
	$(".up").tooltip({
		container: 'body'
	});
	$(".down").tooltip({
		container: 'body'
	});
	$(".delete").tooltip({
		container: 'body'
	});
	$("#perm_name").tooltip({
		container: 'body'
	});
	$("#perm_level").tooltip({
		container: 'body'
	});
	$("#admin_info").tooltip({
		container: 'body'
	});
	$("#level_warning").tooltip({
		container: 'body'
	});
		
	// Main settings
	$("#disable_title").tooltip({
		container: 'body'
	});
	$("#default_permission_title").tooltip({
		container: 'body'
	});
	$("#allow_title").tooltip({
		container: 'body'
	});
	$("#login_with_title").tooltip({
		container: 'body'
	});
	$("#admin_email_title").tooltip({
		container: 'body'
	});
	$("#email_name_title").tooltip({
		container: 'body'
	});
	
	// Login settings
	$("#login_log").tooltip({
		container: 'body'
	});
	$("#max_failed_attempts").tooltip({
		container: 'body'
	});
	$("#redirect_last_page").tooltip({
		container: 'body'
	});
	$("#blocked_time").tooltip({
		container: 'body'
	});
	$("#case_sensitive").tooltip({
		container: 'body'
	});
	$("#username_length").tooltip({
		container: 'body'
	});
	$("#password_length").tooltip({
		container: 'body'
	});
	
});



$('#delete_modal').on('hidden.bs.modal', function () {
	$('#delete_response').html("");
});
