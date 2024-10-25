# CI/CD - Continuous Integration and Continuous Delivery

CI/CD is a short for Continuous Integration and Continuous Delivery (or Deployment) and represents a modern approach to agile software development. It encompasses a set of practices and tools aimed at releasing applications more frequently and efficiently, while maintaining high quality and minimizing risks. By embracing CI/CD, organizations can streamline their development processes, enabling faster and more frequent releases while ensuring stringent quality control measures.

Jenkins: Jenkins is a widely used open-source automation server that can be configured to support ML workflows.

GitLab CI/CD: GitLab provides built-in CI/CD capabilities that support ML workflows.

Github Actions: Github Actions provides a flexible and customizable platform to automate your ML pipelines directly from your GitHub repositories.


## Github Action

Action on github that runs automatics tests whetever a push is made in to the main branch. The folder test-mlops has the structure of a github repository with actions.
In this case, it uses pytest, to verify all the cases. See the ["YAML file"](./test-mlops/.github/workflows/test_workflow.yaml)


## Automate Deploy

Whenever a commit occurs in main, the action will be triggered and will run two jobs:

The first will run the automatic tests.
If the first job is successful, the second job will deploy the function to AWS.

The folder automate-deploy has the structure of a github repository with these two jobs. To run it is necessery to add the AWS_REGION, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and AWS_LAMBDA_ROLE_ARN inside github /settings/secrets/actions of your repository