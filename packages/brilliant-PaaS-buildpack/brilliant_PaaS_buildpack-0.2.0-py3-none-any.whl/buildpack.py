import json
class Buildpack:
    def __init__(self, project):
        self.project = project

    def parseScript(self, shonkufile):
        file = open(shonkufile)
        data = json.load(file)
        return data

    def dockerfile(self, language, port=None, entrypoint=None):
        python = f'''FROM python:3.9.5-slim-buster\nWORKDIR /usr/src/app\nRUN echo gunicorn==20.1.0 > requirements.txt\nRUN pip install -r requirements.txt\nCOPY ./requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nCMD gunicorn {entrypoint}:app --bind 0.0.0.0:{port}'''
        html = f'''FROM nginx:alpine\nCOPY . /usr/share/nginx/html\nEXPOSE 80'''
        if language == 'python':
            return python
        if language == 'html':
            return html

    def kube_manifest(self, name, port, image):
        namespace = {
            "apiVersion": "v1",
            "kind": "Namespace",
            "metadata": {
                "name": name,
            "labels": {
                "name": name
                }
            }
        }
        deployment = {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "metadata": {
                "name": name,
                "namespace": name
            },
            "spec": {
                "selector": {
                "matchLabels": {
                    "app": name
                }
                },
                "replicas": 1,
                "template": {
                "metadata": {
                    "labels": {
                    "app": name
                    }
                },
                "spec": {
                    "containers": [
                    {
                        "name": name,
                        "image": image,
                        "imagePullPolicy": "Always",
                        "ports": [
                        {
                            "containerPort": port
                        }
                        ]
                    }
                    ]
                }
                }
            }
        }
        service = {
            "apiVersion": "v1",
            "kind": "Service",
            "metadata": {
                "name": name,
                "namespace": name
            },
            "spec": {
                "ports": [
                {
                    "port": 80,
                    "targetPort": port
                }
                ],
                "selector": {
                "app": name
                }
            }
        }
        ingressroute = {
            "apiVersion": "traefik.containo.us/v1alpha1",
            "kind": "IngressRoute",
            "metadata": {
                "name": name,
                "namespace": name,
                "annotations": {
                    "kubernetes.io/ingress.class": "traefik-internal"
                }
            },
            "spec": {
                "entryPoints": [
                "web",
                "websecure"
                ],
                "routes": [
                {
                    "match": f"Host(`{name}.platform.brilliant.com.bd`)",
                    "kind": "Rule",
                    "services": [
                    {
                        "name": name,
                        "port": 80
                    }
                    ]
                }
                ]
            }
        }
        return namespace, deployment, service, ingressroute

    def save(self, dockerfile, save_location):
        file = open(f"{save_location}/Dockerfile", "w")
        with file as f:
            f.write(dockerfile)

