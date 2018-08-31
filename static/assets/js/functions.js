// Automation
// deploy_sw1
//$("#automation").submit(function() {
  // Send data to posthandler view.py
//  $.ajax({
//   data: $(this).serialize() + "&automation=Deploy",
//   type: "post",
//   url: "/automation",
//   success: function(response) {
//    $('#automation_response').html(response);
//   }
//   });
//  return false;
//});


// users
// user add
$("#user_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&user_add=Add",
  type: "post",
  url: "/users",
  success: function(response) {
   $('#user_add_response').html(response);
   // When the modal hides, refresh the page
   $('#user_add').on('hide.bs.modal', function (e) {
    window.location.href = "/users";
   });
  }
 });

 return false;
});

// user edit
$("#user_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#usertable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&user_edit=Update",
  type: "post",
  url: "/users",
  success: function(response) {
   $('#user_edit_response').html(response);
   $('#user_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/users";
    });
   }
  });

 return false;
});

// user role add
$("#user_role_add_form").submit(function() {
 // Get data from DataTable
 var table = $('#usertable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&user_role_add=Add",
  type: "post",
  url: "/users",
  success: function(response) {
   $('#user_role_add_response').html(response);
   $('#user_role_add').on('hide.bs.modal', function (e) {
    window.location.href = "/users";
    });
   }
  });

 return false;
});


// user role remove
$("#user_role_remove_form").submit(function() {
 // Get data from DataTable
 var table = $('#usertable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&user_role_remove=Remove",
  type: "post",
  url: "/users",
  success: function(response) {
   $('#user_role_remove_response').html(response);
   $('#user_role_remove').on('hide.bs.modal', function (e) {
    window.location.href = "/users";
    });
   }
  });

 return false;
});

// user delete
$("#user_delete_form").submit(function() {
 var table = $('#usertable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&user_delete=Yes",
  type: "post",
  url: "/users",
  success: function(response) {
   $('#user_delete_response').html(response);
   $('#user_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/users";
    });
   }
  });

 return false;
});



// Servers
// server add
$("#server_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&server_add=Add",
  type: "post",
  url: "/servers",
  success: function(response) {
   $('#server_add_response').html(response);
   // When the modal hides, refresh the page
   $('#server_add').on('hide.bs.modal', function (e) {
    window.location.href = "/servers";
   });
  }
 });

 return false;
});

// server edit
$("#server_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#serverstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&server_edit=Update",
  type: "post",
  url: "/servers",
  success: function(response) {
   $('#server_edit_response').html(response);
   $('#server_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/servers";
    });
   }
  });

 return false;
});

// server delete
$("#server_delete_form").submit(function() {
 var table = $('#serverstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&server_delete=Yes",
  type: "post",
  url: "/servers",
  success: function(response) {
   $('#server_delete_response').html(response);
   $('#server_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/servers";
    });
   }
  });

 return false;
});


// Racks
// rack add
$("#rack_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&rack_add=Add",
  type: "post",
  url: "/racks",
  success: function(response) {
   $('#rack_add_response').html(response);
   // When the modal hides, refresh the page
   $('#rack_add').on('hide.bs.modal', function (e) {
    window.location.href = "/racks";
   });
  }
 });

 return false;
});

// rack edit
$("#rack_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#utable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&rack_edit=Update",
  type: "post",
  url: "/racks",
  success: function(response) {
   $('#rack_edit_response').html(response);
   $('#rack_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/racks";
    });
   }
  });

 return false;
});

// rack delete
$("#rack_delete_form").submit(function() {
 var table = $('#utable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&rack_delete=Yes",
  type: "post",
  url: "/racks",
  success: function(response) {
   $('#rack_delete_response').html(response);
   $('#rack_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/racks";
    });
   }
  });

 return false;
});


// Routers
// router add
$("#router_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&router_add=Add",
  type: "post",
  url: "/routers",
  success: function(response) {
   $('#router_add_response').html(response);
   // When the modal hides, refresh the page
   $('#router_add').on('hide.bs.modal', function (e) {
    window.location.href = "/routers";
   });
  }
 });

 return false;
});

// router edit
$("#router_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#routerstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&router_edit=Update",
  type: "post",
  url: "/routers",
  success: function(response) {
   $('#router_edit_response').html(response);
   $('#router_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/routers";
    });
   }
  });

 return false;
});

// router delete
$("#router_delete_form").submit(function() {
 var table = $('#routerstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&router_delete=Yes",
  type: "post",
  url: "/routers",
  success: function(response) {
   $('#router_delete_response').html(response);
   $('#router_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/routers";
    });
   }
  });

 return false;
});


// Firewalls
// fw add
$("#fw_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&fw_add=Add",
  type: "post",
  url: "/firewalls",
  success: function(response) {
   $('#fw_add_response').html(response);
   // When the modal hides, refresh the page
   $('#fw_add').on('hide.bs.modal', function (e) {
    window.location.href = "/firewalls";
   });
  }
 });

 return false;
});

// fw edit
$("#fw_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#fwtable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&fw_edit=Update",
  type: "post",
  url: "/firewalls",
  success: function(response) {
   $('#fw_edit_response').html(response);
   $('#fw_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/firewalls";
    });
   }
  });

 return false;
});

// fw delete
$("#fw_delete_form").submit(function() {
 var table = $('#fwtable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&fw_delete=Yes",
  type: "post",
  url: "/firewalls",
  success: function(response) {
   $('#fw_delete_response').html(response);
   $('#fw_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/firewalls";
    });
   }
  });

 return false;
});


// IPS
// ips add
$("#ips_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&ips_add=Add",
  type: "post",
  url: "/ips",
  success: function(response) {
   $('#ips_add_response').html(response);
   // When the modal hides, refresh the page
   $('#ips_add').on('hide.bs.modal', function (e) {
    window.location.href = "/ips";
   });
  }
 });

 return false;
});

// ips edit
$("#ips_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#ipstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&ips_edit=Update",
  type: "post",
  url: "/ips",
  success: function(response) {
   $('#ips_edit_response').html(response);
   $('#ips_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/ips";
    });
   }
  });

 return false;
});

// ips delete
$("#ips_delete_form").submit(function() {
 var table = $('#ipstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&ips_delete=Yes",
  type: "post",
  url: "/ips",
  success: function(response) {
   $('#ips_delete_response').html(response);
   $('#ips_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/ips";
    });
   }
  });

 return false;
});


// Switches
// sw add
$("#sw_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&sw_add=Add",
  type: "post",
  url: "/switches",
  success: function(response) {
   $('#sw_add_response').html(response);
   // When the modal hides, refresh the page
   $('#sw_add').on('hide.bs.modal', function (e) {
    window.location.href = "/switches";
   });
  }
 });

 return false;
});

// sw edit
$("#sw_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#swtable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&sw_edit=Update",
  type: "post",
  url: "/switches",
  success: function(response) {
   $('#sw_edit_response').html(response);
   $('#sw_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/switches";
    });
   }
  });

 return false;
});

// sw delete
$("#sw_delete_form").submit(function() {
 var table = $('#swtable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&sw_delete=Yes",
  type: "post",
  url: "/switches",
  success: function(response) {
   $('#sw_delete_response').html(response);
   $('#sw_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/switches";
    });
   }
  });

 return false;
});


// Subnets
// subnet add
$("#subnet_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&subnet_add=Add",
  type: "post",
  url: "/subnets",
  success: function(response) {
   $('#subnet_add_response').html(response);
   // When the modal hides, refresh the page
   $('#subnet_add').on('hide.bs.modal', function (e) {
    window.location.href = "/subnets";
   });
  }
 });

 return false;
});

// subnet edit
$("#subnet_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#subnetstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&subnet_edit=Update",
  type: "post",
  url: "/subnets",
  success: function(response) {
   $('#subnet_edit_response').html(response);
   $('#subnet_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/subnets";
    });
   }
  });

 return false;
});

// subnet delete
$("#subnet_delete_form").submit(function() {
 var table = $('#subnetstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&subnet_delete=Yes",
  type: "post",
  url: "/subnets",
  success: function(response) {
   $('#subnet_delete_response').html(response);
   $('#subnet_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/subnets";
    });
   }
  });

 return false;
});


// Vlans
// vlan add
$("#vlan_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&vlan_add=Add",
  type: "post",
  url: "/vlans",
  success: function(response) {
   $('#vlan_add_response').html(response);
   // When the modal hides, refresh the page
   $('#vlan_add').on('hide.bs.modal', function (e) {
    window.location.href = "/vlans";
   });
  }
 });

 return false;
});

// vlan edit
$("#vlan_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#vlanstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vlan_edit=Update",
  type: "post",
  url: "/vlans",
  success: function(response) {
   $('#vlan_edit_response').html(response);
   $('#vlan_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/vlans";
    });
   }
  });

 return false;
});

// vlan delete
$("#vlan_delete_form").submit(function() {
 var table = $('#vlanstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vlan_delete=Yes",
  type: "post",
  url: "/vlans",
  success: function(response) {
   $('#vlan_delete_response').html(response);
   $('#vlan_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/vlans";
    });
   }
  });

 return false;
});


// sharedsan
// sharedsan add
$("#sharedsan_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&sharedsan_add=Add",
  type: "post",
  url: "/sharedsan",
  success: function(response) {
   $('#sharedsan_add_response').html(response);
   // When the modal hides, refresh the page
   $('#sharedsan_add').on('hide.bs.modal', function (e) {
    window.location.href = "/sharedsan";
   });
  }
 });

 return false;
});

// sharedsan edit
$("#sharedsan_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#sharedsantable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&sharedsan_edit=Update",
  type: "post",
  url: "/sharedsan",
  success: function(response) {
   $('#sharedsan_edit_response').html(response);
   $('#sharedsan_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/sharedsan";
    });
   }
  });

 return false;
});

// sharedsan delete
$("#sharedsan_delete_form").submit(function() {
 var table = $('#sharedsantable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&sharedsan_delete=Yes",
  type: "post",
  url: "/sharedsan",
  success: function(response) {
   $('#sharedsan_delete_response').html(response);
   $('#sharedsan_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/sharedsan";
    });
   }
  });

 return false;
});


// dedicatedsan
// dedicatedsan add
$("#dedicatedsan_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&dedicatedsan_add=Add",
  type: "post",
  url: "/dedicatedsan",
  success: function(response) {
   $('#dedicatedsan_add_response').html(response);
   // When the modal hides, refresh the page
   $('#dedicatedsan_add').on('hide.bs.modal', function (e) {
    window.location.href = "/dedicatedsan";
   });
  }
 });

 return false;
});

// dedicatedsan edit
$("#dedicatedsan_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#dedicatedsantable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&dedicatedsan_edit=Update",
  type: "post",
  url: "/dedicatedsan",
  success: function(response) {
   $('#dedicatedsan_edit_response').html(response);
   $('#dedicatedsan_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/dedicatedsan";
    });
   }
  });

 return false;
});

// dedicatedsan delete
$("#dedicatedsan_delete_form").submit(function() {
 var table = $('#dedicatedsantable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&dedicatedsan_delete=Yes",
  type: "post",
  url: "/dedicatedsan",
  success: function(response) {
   $('#dedicatedsan_delete_response').html(response);
   $('#dedicatedsan_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/dedicatedsan";
    });
   }
  });

 return false;
});


// nas
// nas add
$("#nas_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&nas_add=Add",
  type: "post",
  url: "/nas",
  success: function(response) {
   $('#nas_add_response').html(response);
   // When the modal hides, refresh the page
   $('#nas_add').on('hide.bs.modal', function (e) {
    window.location.href = "/nas";
   });
  }
 });

 return false;
});

// nas edit
$("#nas_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#nastable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&nas_edit=Update",
  type: "post",
  url: "/nas",
  success: function(response) {
   $('#nas_edit_response').html(response);
   $('#nas_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/nas";
    });
   }
  });

 return false;
});

// nas delete
$("#nas_delete_form").submit(function() {
 var table = $('#nastable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&nas_delete=Yes",
  type: "post",
  url: "/nas",
  success: function(response) {
   $('#nas_delete_response').html(response);
   $('#nas_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/nas";
    });
   }
  });

 return false;
});


// vCenter
// vc add
$("#vc_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&vc_add=Add",
  type: "post",
  url: "/vcenter",
  success: function(response) {
   $('#vc_add_response').html(response);
   // When the modal hides, refresh the page
   $('#vc_add').on('hide.bs.modal', function (e) {
    window.location.href = "/vcenter";
   });
  }
 });

 return false;
});

// vc edit
$("#vc_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#vctable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vc_edit=Update",
  type: "post",
  url: "/vcenter",
  success: function(response) {
   $('#vc_edit_response').html(response);
   $('#vc_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/vcenter";
    });
   }
  });

 return false;
});

// vc delete
$("#vc_delete_form").submit(function() {
 var table = $('#vctable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vc_delete=Yes",
  type: "post",
  url: "/vcenter",
  success: function(response) {
   $('#vc_delete_response').html(response);
   $('#vc_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/vcenter";
    });
   }
  });

 return false;
});

// esxis
// esxi add
$("#esxi_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&esxi_add=Add",
  type: "post",
  url: "/esxi",
  success: function(response) {
   $('#esxi_add_response').html(response);
   // When the modal hides, refresh the page
   $('#esxi_add').on('hide.bs.modal', function (e) {
    window.location.href = "/esxi";
   });
  }
 });

 return false;
});

// esxi edit
$("#esxi_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#esxistable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&esxi_edit=Update",
  type: "post",
  url: "/esxi",
  success: function(response) {
   $('#esxi_edit_response').html(response);
   $('#esxi_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/esxi";
    });
   }
  });

 return false;
});

// esxi delete
$("#esxi_delete_form").submit(function() {
 var table = $('#esxistable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&esxi_delete=Yes",
  type: "post",
  url: "/esxi",
  success: function(response) {
   $('#esxi_delete_response').html(response);
   $('#esxi_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/esxi";
    });
   }
  });

 return false;
});


// vm
// vm add
$("#vm_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&vm_add=Add",
  type: "post",
  url: "/virtualmachines",
  success: function(response) {
   $('#vm_add_response').html(response);
   // When the modal hides, refresh the page
   $('#vm_add').on('hide.bs.modal', function (e) {
    window.location.href = "/virtualmachines";
   });
  }
 });

 return false;
});

// vm edit
$("#vm_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#vmtable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vm_edit=Update",
  type: "post",
  url: "/virtualmachines",
  success: function(response) {
   $('#vm_edit_response').html(response);
   $('#vm_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/virtualmachines";
    });
   }
  });

 return false;
});

// vm delete
$("#vm_delete_form").submit(function() {
 var table = $('#vmtable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vm_delete=Yes",
  type: "post",
  url: "/virtualmachines",
  success: function(response) {
   $('#vm_delete_response').html(response);
   $('#vm_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/virtualmachines";
    });
   }
  });

 return false;
});

// vS Switch
// vs add
$("#vs_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&vs_add=Add",
  type: "post",
  url: "/vswitch",
  success: function(response) {
   $('#vs_add_response').html(response);
   // When the modal hides, refresh the page
   $('#vs_add').on('hide.bs.modal', function (e) {
    window.location.href = "/vswitch";
   });
  }
 });

 return false;
});

// vs edit
$("#vs_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#vstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vs_edit=Update",
  type: "post",
  url: "/vswitch",
  success: function(response) {
   $('#vs_edit_response').html(response);
   $('#vs_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/vswitch";
    });
   }
  });

 return false;
});

// vs delete
$("#vs_delete_form").submit(function() {
 var table = $('#vstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vs_delete=Yes",
  type: "post",
  url: "/vswitch",
  success: function(response) {
   $('#vs_delete_response').html(response);
   $('#vs_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/vswitch";
    });
   }
  });

 return false;
});

// vDS Switch
// vds add
$("#vds_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&vds_add=Add",
  type: "post",
  url: "/vdsswitch",
  success: function(response) {
   $('#vds_add_response').html(response);
   // When the modal hides, refresh the page
   $('#vds_add').on('hide.bs.modal', function (e) {
    window.location.href = "/vdsswitch";
   });
  }
 });

 return false;
});

// vds edit
$("#vds_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#vdstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vds_edit=Update",
  type: "post",
  url: "/vdsswitch",
  success: function(response) {
   $('#vds_edit_response').html(response);
   $('#vds_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/vdsswitch";
    });
   }
  });

 return false;
});

// vds delete
$("#vds_delete_form").submit(function() {
 var table = $('#vdstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vds_delete=Yes",
  type: "post",
  url: "/vdsswitch",
  success: function(response) {
   $('#vds_delete_response').html(response);
   $('#vds_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/vdsswitch";
    });
   }
  });

 return false;
});


// vStorage Switch
// vstorage add
$("#vstorage_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&vstorage_add=Add",
  type: "post",
  url: "/vstorage",
  success: function(response) {
   $('#vstorage_add_response').html(response);
   // When the modal hides, refresh the page
   $('#vstorage_add').on('hide.bs.modal', function (e) {
    window.location.href = "/vstorage";
   });
  }
 });

 return false;
});

// vstorage edit
$("#vstorage_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#vstoragetable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vstorage_edit=Update",
  type: "post",
  url: "/vstorage",
  success: function(response) {
   $('#vstorage_edit_response').html(response);
   $('#vstorage_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/vstorage";
    });
   }
  });

 return false;
});

// vstorage delete
$("#vstorage_delete_form").submit(function() {
 var table = $('#vstoragetable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&vstorage_delete=Yes",
  type: "post",
  url: "/vstorage",
  success: function(response) {
   $('#vstorage_delete_response').html(response);
   $('#vstorage_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/vstorage";
    });
   }
  });

 return false;
});


// isos
// iso add
$("#iso_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&iso_add=Add",
  type: "post",
  url: "/isos",
  success: function(response) {
   $('#iso_add_response').html(response);
   // When the modal hides, refresh the page
   $('#iso_add').on('hide.bs.modal', function (e) {
    window.location.href = "/isos";
   });
  }
 });

 return false;
});

// iso edit
$("#iso_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#isostable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&iso_edit=Update",
  type: "post",
  url: "/isos",
  success: function(response) {
   $('#iso_edit_response').html(response);
   $('#iso_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/isos";
    });
   }
  });

 return false;
});

// iso delete
$("#iso_delete_form").submit(function() {
 var table = $('#isostable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&iso_delete=Yes",
  type: "post",
  url: "/isos",
  success: function(response) {
   $('#iso_delete_response').html(response);
   $('#iso_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/isos";
    });
   }
  });

 return false;
});

// iso upload
$(function () {
$('#isodrop').fileupload({
//        dataType: 'json',
	type: 'post',
	url: '/isos',
	replaceFileInput:false,
        add: function (e, data) {
            data.context = $('<button/>').text('Upload').addClass('btn btn-xs')
		.appendTo("#isodropbtn")
                .click(function () {
//                    data.context = $('<p/>').text('Uploading...').replaceAll($(this));
                    data.context = $('<p/>').text('Uploading...').appendTo("#iso_upload_notification");
                    data.submit();
        });
        },
//        done: function (e, data) {
//            $.each(data.result, function (index, file) {
//                $('<p/>').text('Uploaded').appendTo("#iso_upload_response");
//                });
//        },
        progressall: function (e, data) {
            var progress = parseInt(data.loaded / data.total * 100, 10);
            $('.progress-bar').css(
                'width',
                progress + '%'
                );
        },
        success: function(response) {
             $('#iso_upload_response').html(response);
             }
  });

$('#isodrop').bind('fileuploadsubmit', function (e, data) {
       var table = $('#isostable').DataTable();
       var dataid = table.$('input').serialize();
       data.formData = {dataid, iso_upload: 'on'};
});

$('#isodrop').bind('fileuploaddone', function (e, data) {
	$('<p/>').text('Uploading Completed.').replaceAll("#iso_upload_notification");
        $('#iso_upload').on('hide.bs.modal', function (f) {
             window.location.href = "/isos";
        });
});

$('#isodrop').bind('fileuploadfail', function (e, data) {
//        $('<p/>').text('Uploading Failed.').replaceAll("#iso_upload_notification");
        $('<div/>').text('FAILED').addClass('alert alert-danger').replaceAll('#iso_upload_response');
        $('#iso_upload').on('hide.bs.modal', function (f) {
             window.location.href = "/isos";
        });
});

});

// snapshots
// snapshot add
$("#snapshot_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&snapshot_add=Add",
  type: "post",
  url: "/snapshots",
  success: function(response) {
   $('#snapshot_add_response').html(response);
   // When the modal hides, refresh the page
   $('#snapshot_add').on('hide.bs.modal', function (e) {
    window.location.href = "/snapshots";
   });
  }
 });

 return false;
});

// snapshot edit
$("#snapshot_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#snapshotstable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&snapshot_edit=Update",
  type: "post",
  url: "/snapshots",
  success: function(response) {
   $('#snapshot_edit_response').html(response);
   $('#snapshot_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/snapshots";
    });
   }
  });

 return false;
});

// snapshot delete
$("#snapshot_delete_form").submit(function() {
 var table = $('#snapshotstable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&snapshot_delete=Yes",
  type: "post",
  url: "/snapshots",
  success: function(response) {
   $('#snapshot_delete_response').html(response);
   $('#snapshot_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/snapshots";
    });
   }
  });

 return false;
});


// templates
// template add
$("#template_add_form").submit(function() {
 // Send data to posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&template_add=Add",
  type: "post",
  url: "/templates",
  success: function(response) {
   $('#template_add_response').html(response);
   // When the modal hides, refresh the page
   $('#template_add').on('hide.bs.modal', function (e) {
    window.location.href = "/templates";
   });
  }
 });

 return false;
});

// template edit
$("#template_edit_form").submit(function() {
 // Get data from DataTable
 var table = $('#templatestable').DataTable();
 var data = table.$('input').serialize();
 // Send data to the posthandler view.py
 $.ajax({
  data: $(this).serialize() + "&" + data + "&template_edit=Update",
  type: "post",
  url: "/templates",
  success: function(response) {
   $('#template_edit_response').html(response);
   $('#template_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/templates";
    });
   }
  });

 return false;
});

// template delete
$("#template_delete_form").submit(function() {
 var table = $('#templatestable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&template_delete=Yes",
  type: "post",
  url: "/templates",
  success: function(response) {
   $('#template_delete_response').html(response);
   $('#template_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/templates";
    });
   }
  });

 return false;
});

// cobbleriso_import
$("#cobbleriso_import_form").submit(function() {
 var table = $('#cobblerisostable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&cobbleriso_import=Yes",
  type: "post",
  url: "/cobbler",
  success: function(response) {
   $('#cobbleriso_import_response').html(response);
   $('#cobbleriso_import').on('hide.bs.modal', function (e) {
    window.location.href = "/cobbler";
    });
   }
  });

 return false;
});

// cobblerdistro_delete
$("#cobblerdistro_delete_form").submit(function() {
 var table = $('#cobblerdistrostable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&cobblerdistro_delete=Yes",
  type: "post",
  url: "/cobbler",
  success: function(response) {
   $('#cobblerdistro_delete_response').html(response);
   $('#cobblerdistro_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/cobbler";
    });
   }
  });

 return false;
});

// cobblerprofile_delete
$("#cobblerprofile_delete_form").submit(function() {
 var table = $('#cobblerprofilestable').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&cobblerprofile_delete=Yes",
  type: "post",
  url: "/cobbler",
  success: function(response) {
   $('#cobblerprofile_delete_response').html(response);
   $('#cobblerprofile_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/cobbler";
    });
   }
  });

 return false;
});

// build_hextrim_iso
$("#build_hextrim_iso_form").submit(function() {
 $.ajax({
  data: $(this).serialize() + "&" + data + "&build_hextrim_isos_build",
  type: "post",
  url: "/livecd",
  success: function(response) {
    window.location.href = "/livecd";
   }
  });

 return false;
});

// build_hextrim_iso
$("#convert_hextrim_to_pxeboot_form").submit(function() {
 $.ajax({
  data: $(this).serialize() + "&" + data + "&convert_hextrim_to_pxeboot_convert",
  type: "post",
  url: "/livecd",
  success: function(response) {
    window.location.href = "/livecd";
   }
  });

 return false;
});

// system_vm_edit
$("#system_vm_edit_form").submit(function() {
 var table = $('#cobblervmsystems').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&system_vm_edit=Update",
  type: "post",
  url: "/system-vm-profiles",
  success: function(response) {
   $('#system_vm_edit_response').html(response);
   $('#system_vm_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/system-vm-profiles";
    });
   }
  });

 return false;
});


// system_vm_delete
$("#system_vm_delete_form").submit(function() {
 var table = $('#cobblervmsystems').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&system_vm_delete=Yes",
  type: "post",
  url: "/system-vm-profiles",
  success: function(response) {
   $('#system_vm_delete_response').html(response);
   $('#system_vm_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/system-vm-profiles";
    });
   }
  });

 return false;
});

// system_phy_edit
$("#system_phy_edit_form").submit(function() {
 var table = $('#cobblerphysystems').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&system_phy_edit=Update",
  type: "post",
  url: "/system-phy-profiles",
  success: function(response) {
   $('#system_phy_edit_response').html(response);
   $('#system_phy_edit').on('hide.bs.modal', function (e) {
    window.location.href = "/system-phy-profiles";
    });
   }
  });

 return false;
});

// system_phy_delete
$("#system_phy_delete_form").submit(function() {
 var table = $('#cobblerphysystems').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&system_phy_delete=Yes",
  type: "post",
  url: "/system-phy-profiles",
  success: function(response) {
   $('#system_phy_delete_response').html(response);
   $('#system_phy_delete').on('hide.bs.modal', function (e) {
    window.location.href = "/system-phy-profiles";
    });
   }
  });

 return false;
});

$("#deploy_vm_system_form").submit(function() {
 var table = $('#deployvmsystems').DataTable();
 var data = table.$('input').serialize();
 $.ajax({
  data: $(this).serialize() + "&" + data + "&deploy_vm_system=Yes",
  type: "post",
  url: "/deploy-vm-system",
  success: function(response) {
   $('#deploy_vm_system_form_response').html(response);
   $('#deploy_vm_system').on('hide.bs.modal', function (e) {
    window.location.href = "/deploy-vm-system";
    });
   }
  });

 return false;
});


// Function to open a modal by id
function openModal(id) {
        $('#' + id).modal('show');
}


function addOption() {
	$("#names").append("<input type='text' name='name[]' class='form-control'>");
	$("#values").append("<input type='text' name='value[]' class='form-control'>");
}
