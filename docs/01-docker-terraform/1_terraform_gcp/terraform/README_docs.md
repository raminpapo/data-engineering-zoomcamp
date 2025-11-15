# README.md

**Path**: `01-docker-terraform/1_terraform_gcp/terraform/README.md`
**Size**: 514 bytes
**Lines**: 26

## Source Code

```markdown
### Concepts
* [Terraform_overview](../1_terraform_overview.md)

### Execution

```shell
# Refresh service-account's auth-token for this session
gcloud auth application-default login

# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=<your-gcp-project-id>"
```

```shell
# Create new infra
terraform apply -var="project=<your-gcp-project-id>"
```

```shell
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```

```

## Analysis

**Sections (7)**: Concepts, Execution, Refresh service-account's auth-token for this session, Initialize state file (.tfstate), Check changes to new infra plan, Create new infra, Delete infra after your work, to avoid costs on any running services

---
*Generated: 2025-11-15T20:48:44.101502*
