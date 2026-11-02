# Contributing

Add or update a focused package under `skills/<category>/<name>/`. Follow [authoring guidelines](authoring-guidelines.md), update the root catalog and include behavior cases for significant workflows.

Install validation dependencies with `python3 -m pip install -r requirements-dev.txt`, then run:

```sh
python3 scripts/validate-skills.py
python3 -m unittest discover -s tests
```

Test installation in a temporary repository using the skills CLI and relevant agent targets. Check all package resources survive installation. Actual agent execution should be evaluated separately using the scenario cases; record tools and limitations rather than claiming unperformed tests.

Pull requests should describe changed behavior, validation evidence and relevant limitations. Never include credentials, private topology or production logs.
