API for Ingenico POS, run with [pyTeliumManager]() library.

### Installation :

**Requirement** : Python 3.5+

Clone repository and install dependency with requirements.txt in [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) :

- `git clone` url of repo

- `python3 -m pip install --user virtualenv`

- `python3 -m venv env`

- `source env/bin/activate`

- `pip install -r requierments.txt`

- `deactivate`

If necessary install gunicorn with aptitude:

- `sudo apt-get install gunicorn3`

Now run app with:

- `gunicorn app:app -b 0.0.0.0:8000`

App access with server ip and port 8000 ! 

Config POS :

- Connect POS with USB 
- Active Caisse support ans USB port in parameter.
- Authorize server to send data in POS. After verified USB port use by POS in your server.

```
# navigate to rules.d directory
cd /etc/udev/rules.d
#create a new rule file
sudo touch my-newrule.rules
# open the file
sudo vim my-newrule.rules
# add the following
KERNEL=="ttyACM0", MODE="0666"
```

### API Endpoint :

| Endpoint | HTTP Method | JSON Body  | Description                 | Return                                                        |
|----------|-------------|------------|-----------------------------|---------------------------------------------------------------|
| `/debit` | `POST`      | `<amount>` | Create new payment request. | Return tuple with True or False and error or success message. |

### Use Endpoint Sample :

Endpoint format is: http://192.168.XXX.XXX/debit.
JSON format is: { "amount": numeric_value }.


