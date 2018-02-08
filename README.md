#vault-gatekeeper-client-example-app

Example app that shows how the [vault-gatekeeper-client module](https://www.github.com/jensendw/vault-gatekeeper-client) is used in a mesos app

## Deployment

The deployment below assumes you're using marathon, although, the relevant pieces should work just fine for ChronosTasks etc..

```json
{
  "id": "/vault-gatekeeper-client-example-app",
  "cmd": null,
  "cpus": 1,
  "mem": 512,
  "disk": 0,
  "instances": 1,
  "acceptedResourceRoles": [
    "*"
  ],
  "container": {
    "type": "DOCKER",
    "volumes": [],
    "docker": {
      "image": "jensendw/vault-gatekeeper-client-example-app",
      "network": "BRIDGE",
      "portMappings": [
        {
          "containerPort": 5000,
          "hostPort": 0,
          "servicePort": 10056,
          "protocol": "tcp",
          "labels": {}
        }
      ],
      "privileged": false,
      "parameters": [],
      "forcePullImage": false
    }
  },
  "env": {
    "GATEKEEPER_ADDR": "https://vault-gatekeeper",
    "VAULT_ADDR": "https://vault:8200",
    "SECRET_PATH": "secret/test"
  },
  "portDefinitions": [
    {
      "port": 10056,
      "protocol": "tcp",
      "name": "default",
      "labels": {}
    }
  ]
}
```
