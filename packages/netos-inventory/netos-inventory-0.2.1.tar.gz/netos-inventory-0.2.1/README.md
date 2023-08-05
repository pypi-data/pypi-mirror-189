# netos-inventory

Reconcile device objects with detected values

## Features

The plugin provide following Model:
- ReconDevice (proxy for Device model)

## Installation
The plugin is avialable in tar.gz format in dist folder, can be installed with
```
pip install netos_inventory
```
Enable the plugin in netbox/configuration.py
```
PLUGINS = [ 'netos_inventory' ]
```

Configuration you can specify field mapping which should be used during the reconciliation process. Example config is as follow:
```
PLUGINS_CONFIG = {
    'netos_inventory': {
        "device_recon_fields": {'device_type': 'detected_type',
                                'serial': 'detected_serial_number'}
    }
}
```
Keys in dict `device_recon_fields` are model standard fields and values are custom fields

## Screenshots
Recon Device table view
![Table view](docs/img/table_view.png)

Recon Device reconciliation view
![List view](docs/img/recon_view.png)
