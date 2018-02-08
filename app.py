from flask import Flask
import os
from vault_gatekeeper_client import VaultGatekeeperClient
import time
app = Flask(__name__)

@app.route("/")
def hello():
    body = """The secrets are: {}
    MESOS_TASK_ID: {}
    GATEKEEPER_ADDR: {}
    VAULT_ADDR: {}
    SECRET_PATH: {}
    """.format(vault_gatekeeper.secrets,
               os.environ['MESOS_TASK_ID'],
               os.environ['GATEKEEPER_ADDR'],
               os.environ['VAULT_ADDR'],
               os.environ['SECRET_PATH'])
    return body

if __name__ == "__main__":
    #give the mesos task a chance to start to vault-gatekeeper-mesos will recognize it
    time.sleep(15)

    vault_gatekeeper = VaultGatekeeperClient(task_id=os.environ['MESOS_TASK_ID'],
                                             gatekeeper_addr=os.environ['GATEKEEPER_ADDR'],
                                             vault_addr=os.environ['VAULT_ADDR'],
                                             secret_path=os.environ['SECRET_PATH'])
    app.run(host='0.0.0.0', debug=True)
